from django.db import models
from ckeditor.fields import RichTextField
from apps.core.models import PublishableModel

class Member(PublishableModel):
    TYPE_CHOICES = [
        ('executive', 'Executive Committee'),
        ('general', 'General Member'),
        ('coach', 'Coach'),
        ('player', 'Player'),
    ]
    name = models.CharField(max_length=200) # Names are usually universal, but can be translated if needed. Keeping universal for now unless specified.
    member_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    
    role_ne = models.CharField(max_length=100, blank=True)
    role_en = models.CharField(max_length=100, blank=True)
    role_de = models.CharField(max_length=100, blank=True)
    
    bio_ne = models.TextField(blank=True)
    bio_en = models.TextField(blank=True)
    bio_de = models.TextField(blank=True)
    
    image = models.ForeignKey('media.Media', on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(blank=True)
    
    # Player specific
    position_ne = models.CharField(max_length=100, blank=True)
    position_en = models.CharField(max_length=100, blank=True)
    position_de = models.CharField(max_length=100, blank=True)
    
    experience_ne = models.CharField(max_length=100, blank=True)
    experience_en = models.CharField(max_length=100, blank=True)
    experience_de = models.CharField(max_length=100, blank=True)
    
    number = models.CharField(max_length=10, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.member_type})"

class Article(PublishableModel):
    title_ne = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200)
    
    slug = models.SlugField(max_length=200, unique=True)
    
    excerpt_ne = models.TextField()
    excerpt_en = models.TextField()
    excerpt_de = models.TextField()
    
    content_ne = RichTextField()
    content_en = RichTextField()
    content_de = RichTextField()
    
    featured_image = models.ForeignKey('media.Media', on_delete=models.SET_NULL, null=True, blank=True)
    
    category_ne = models.CharField(max_length=100)
    category_en = models.CharField(max_length=100)
    category_de = models.CharField(max_length=100)
    
    is_featured = models.BooleanField(default=False)
    date = models.DateField(null=True) # Added date field as requested in 'News Page' requirement

    def __str__(self):
        return self.title_en

class Notice(PublishableModel):
    title_ne = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200)
    
    content_ne = RichTextField()
    content_en = RichTextField()
    content_de = RichTextField()
    
    category_ne = models.CharField(max_length=100, blank=True)
    category_en = models.CharField(max_length=100, blank=True)
    category_de = models.CharField(max_length=100, blank=True)
    
    date = models.DateField()

    def __str__(self):
        return self.title_en

class Event(PublishableModel):
    title_ne = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200)
    
    description_ne = RichTextField()
    description_en = RichTextField()
    description_de = RichTextField()
    
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=200)
    
    image = models.ForeignKey('media.Media', on_delete=models.SET_NULL, null=True, blank=True)
    
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('past', 'Past'),
        ('cancelled', 'Cancelled'),
    ]
    event_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')

    def __str__(self):
        return self.title_en

class GalleryImage(PublishableModel):
    image = models.ForeignKey('media.Media', on_delete=models.CASCADE)
    
    title_ne = models.CharField(max_length=200, blank=True)
    title_en = models.CharField(max_length=200, blank=True)
    title_de = models.CharField(max_length=200, blank=True)
    
    category_ne = models.CharField(max_length=100)
    category_en = models.CharField(max_length=100)
    category_de = models.CharField(max_length=100)

    def __str__(self):
        return self.title_en or "Gallery Image"
