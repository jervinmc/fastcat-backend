from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Departure(models.Model):
    timefrom=models.CharField(_('timefrom'),max_length=255,blank=True,null=True)
    timeto=models.CharField(_('timeto'),max_length=255,blank=True,null=True)
    price = models.DecimalField(_('price'),max_digits=20, decimal_places=2,default=0.0)
    package_name=models.CharField(_('package_name'),max_length=255,blank=True,null=True)
    location=models.CharField(_('location'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
