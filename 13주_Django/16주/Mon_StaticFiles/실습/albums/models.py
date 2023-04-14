from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Album(models.Model):
    content = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='')
    image_thumbnail = ImageSpecField(source='image',
                                    processors=[ResizeToFill(50, 50)],
                                    format='JPEG',
                                    options={'quality': 60})
album = Album.objects.all()