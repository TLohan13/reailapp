from django.db import models


class Content(models.Model):
    contentWords = models.TextField()
