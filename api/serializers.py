from rest_framework import serializers
from .models import City, ProgramDetail, Photo, Video, ExhibitorRegistration, ParticipantRegistration, Inquiry, Stall

class ProgramDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramDetail
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    program_details = ProgramDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = City
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class ExhibitorRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExhibitorRegistration
        fields = '__all__'

class ParticipantRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantRegistration
        fields = '__all__'

class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = '__all__'

class StallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stall
        fields = '__all__'

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_staff=True,
            is_superuser=True
        )
        return user
