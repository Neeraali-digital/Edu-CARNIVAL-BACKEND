from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CityViewSet, ProgramDetailViewSet, PhotoViewSet, VideoViewSet,
    ExhibitorRegistrationViewSet, ParticipantRegistrationViewSet, InquiryViewSet, StallViewSet,
    StallBookingViewSet
)

router = DefaultRouter()
router.register(r'cities', CityViewSet)
router.register(r'program-details', ProgramDetailViewSet)
router.register(r'photos', PhotoViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'registrations/exhibitor', ExhibitorRegistrationViewSet)
router.register(r'registrations/participant', ParticipantRegistrationViewSet)
router.register(r'inquiries', InquiryViewSet)
router.register(r'stalls', StallViewSet)
router.register(r'stall-bookings', StallBookingViewSet)

from .views import CustomLoginView, AdminRegistrationView, dashboard_stats

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', CustomLoginView.as_view(), name='api_login'),
    path('auth/register/', AdminRegistrationView.as_view(), name='api_register'),
    path('dashboard-stats/', dashboard_stats, name='dashboard_stats'),
]
