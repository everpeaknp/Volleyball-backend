from django.db import models
from apps.core.models import TimeStampedModel

class Media(TimeStampedModel):
    file = models.FileField(upload_to='uploads/%Y/%m/')
    title = models.CharField(max_length=200)
    
    alt_text_ne = models.CharField(max_length=200, blank=True)
    alt_text_en = models.CharField(max_length=200, blank=True)
    alt_text_de = models.CharField(max_length=200, blank=True)
    
    file_type = models.CharField(max_length=20, choices=[
        ('image', 'Image'),
        ('video', 'Video'),
        ('document', 'Document'),
    ])
    size = models.PositiveIntegerField()
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.file:
            self.size = self.file.size
            if not self.title:
                self.title = self.file.name
        super().save(*args, **kwargs)
