from django.db import models


class Content(models.Model):
    contentWords = models.TextField()
    contentImage = models.ImageField(null=True, upload_to='rail_pic/images')
