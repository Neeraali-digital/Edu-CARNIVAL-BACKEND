from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='cities/')
    date = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_current_expo = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.is_current_expo:
            # Set all other cities' is_current_expo to False
            City.objects.filter(is_current_expo=True).exclude(pk=self.pk).update(is_current_expo=False)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Cities"
        ordering = ['start_date']

class ProgramDetail(models.Model):
    city = models.ForeignKey(City, related_name='program_details', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    time = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.city.name} - {self.title}"

class Photo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/photos/')
    year = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Photo {self.id}"

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField() # Youtube/Vimeo link
    thumbnail = models.ImageField(upload_to='gallery/videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ExhibitorRegistration(models.Model):
    full_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.company_name})"

class ParticipantRegistration(models.Model):
    full_name = models.CharField(max_length=200)
    school_college = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    interests = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Inquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} - {self.subject}"

class Stall(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='stalls', null=True, blank=True)
    image = models.ImageField(upload_to='stalls/', blank=True, null=True)

    def __str__(self):
        return self.title

class StallBooking(models.Model):
    stall = models.ForeignKey(Stall, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    slot_id = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking: {self.name} - {self.stall.title}"
