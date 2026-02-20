from django.contrib import admin
from .models import City, ProgramDetail, Photo, Video, ExhibitorRegistration, ParticipantRegistration, Inquiry, Stall, StallBooking, WheelPrize, SpinWinner

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'date', 'location')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(ProgramDetail)
class ProgramDetailAdmin(admin.ModelAdmin):
    list_display = ('city', 'title', 'time')
    list_filter = ('city',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_url', 'created_at')

@admin.register(ExhibitorRegistration)
class ExhibitorRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'company_name', 'email', 'phone_number', 'created_at')
    search_fields = ('full_name', 'company_name', 'email')

@admin.register(ParticipantRegistration)
class ParticipantRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'school_college', 'email', 'phone_number', 'prize_code', 'created_at')
    search_fields = ('full_name', 'school_college', 'email', 'prize_code')

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')

@admin.register(Stall)
class StallAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

@admin.register(StallBooking)
class StallBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'stall', 'city', 'created_at')

@admin.register(WheelPrize)
class WheelPrizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'label', 'remaining_quantity', 'total_quantity', 'weight', 'is_active')
    list_editable = ('remaining_quantity', 'weight', 'is_active')

@admin.register(SpinWinner)
class SpinWinnerAdmin(admin.ModelAdmin):
    list_display = ('unique_code', 'prize', 'is_claimed', 'created_at')
    list_filter = ('is_claimed', 'prize')
    search_fields = ('unique_code', 'ip_address')
