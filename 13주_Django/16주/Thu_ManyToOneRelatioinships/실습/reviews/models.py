from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = ProcessedImageField(blank = True,
                                upload_to='image/',
                                processors=[ResizeToFill(300, 300)],
                                format='JPEG',
                                options={'quality': 60})
    movie = models.CharField(max_length=30)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)




