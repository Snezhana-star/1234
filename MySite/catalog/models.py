from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.crypto import get_random_string


def get_name_file(instance, filename):
    return '/'.join([get_random_string(length=5) + '_' + filename])


class Order(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название', blank=False)
    text_order = models.TextField(max_length=1000, blank=False)
    image = models.ImageField(max_length=254, upload_to=get_name_file,
                              null=True, blank=False,
                              validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp'])])
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name
