from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    class Meta(object):
        db_table = 'post'

    name = models.CharField(
        'Name', blank=True, null=True, max_length=14, db_index=True
    )
    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', auto_now_add=True
    )
    image = CloudinaryField('image', blank=True, default=None,  null=True)
    like_count = models.IntegerField(default='0', blank=True)
    updated_at = models.DateTimeField(
        'Updated DateTime', auto_now=True
    )
