from django.db import models


class MyModel(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(upload_to='media/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('date_created',)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        return self.name
