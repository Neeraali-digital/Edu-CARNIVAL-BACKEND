from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
import random
import uuid

from .models import (
    City, ProgramDetail, Photo, Video, ExhibitorRegistration, 
    ParticipantRegistration, Inquiry, Stall, StallBooking, 
    WheelPrize, SpinWinner
)
from .serializers import (
    CitySerializer, ProgramDetailSerializer, PhotoSerializer, VideoSerializer,
    ExhibitorRegistrationSerializer, ParticipantRegistrationSerializer, 
    InquirySerializer, StallSerializer, StallBookingSerializer, 
    UserSerializer, WheelPrizeSerializer, SpinWinnerSerializer
)

@extend_schema(tags=['Cities'])
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'slug'

@extend_schema(tags=['Program Details'])
class ProgramDetailViewSet(viewsets.ModelViewSet):
    queryset = ProgramDetail.objects.all()
    serializer_class = ProgramDetailSerializer

@extend_schema(tags=['Gallery'])
class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

@extend_schema(tags=['Gallery'])
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

@extend_schema(tags=['Registrations'])
class ExhibitorRegistrationViewSet(viewsets.ModelViewSet):
    queryset = ExhibitorRegistration.objects.all()
    serializer_class = ExhibitorRegistrationSerializer

@extend_schema(tags=['Registrations'])
class ParticipantRegistrationViewSet(viewsets.ModelViewSet):
    queryset = ParticipantRegistration.objects.all()
    serializer_class = ParticipantRegistrationSerializer

@extend_schema(tags=['Inquiries'])
class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

@extend_schema(tags=['Stalls'])
class StallViewSet(viewsets.ModelViewSet):
    queryset = Stall.objects.all()
    serializer_class = StallSerializer

@extend_schema(tags=['Stalls'])
class StallBookingViewSet(viewsets.ModelViewSet):
    queryset = StallBooking.objects.all()
    serializer_class = StallBookingSerializer

@extend_schema(tags=['Wheel Spinner'])
class WheelPrizeViewSet(viewsets.ModelViewSet):
    queryset = WheelPrize.objects.all()
    serializer_class = WheelPrizeSerializer
    permission_classes = [AllowAny]

@extend_schema(tags=['Wheel Spinner'])
class SpinWinnerViewSet(viewsets.ModelViewSet):
    queryset = SpinWinner.objects.all()
    serializer_class = SpinWinnerSerializer
    permission_classes = [AllowAny]

@extend_schema(tags=['Wheel Spinner'])
@api_view(['POST'])
@permission_classes([AllowAny])
def spin_wheel(request):
    ip = request.META.get('REMOTE_ADDR')
    prizes = WheelPrize.objects.filter(is_active=True, remaining_quantity__gt=0)
    
    if not prizes:
        return Response({'error': 'No prizes available at the moment.'}, status=400)

    weights = [p.weight for p in prizes]
    winner_prize = random.choices(list(prizes), weights=weights, k=1)[0]

    unique_code = f"EC-WIN-{uuid.uuid4().hex[:6].upper()}"
    
    if winner_prize.remaining_quantity > 0:
        winner_prize.remaining_quantity -= 1
        winner_prize.save()

    winner_record = SpinWinner.objects.create(
        prize=winner_prize,
        unique_code=unique_code,
        ip_address=ip
    )

    return Response({
        'prize': winner_prize.name,
        'label': winner_prize.label,
        'code': unique_code,
        'color': winner_prize.color
    })

@extend_schema(tags=['Authentication'])
class CustomLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'is_superuser': user.is_superuser
        })

@extend_schema(tags=['Authentication'])
class AdminRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@extend_schema(tags=['Dashboard'])
@api_view(['GET'])
@permission_classes([AllowAny])
def dashboard_stats(request):
    data = {
        'total_cities': City.objects.count(),
        'exhibitor_regs': ExhibitorRegistration.objects.count(),
        'participant_regs': ParticipantRegistration.objects.count(),
        'inquiries': Inquiry.objects.count(),
        'total_stalls': Stall.objects.count(),
        'total_gallery': Photo.objects.count() + Video.objects.count(),
        'stall_bookings': StallBooking.objects.count(),
        'total_winners': SpinWinner.objects.count(),
        'available_prizes': WheelPrize.objects.filter(is_active=True).count()
    }
    return Response(data)
