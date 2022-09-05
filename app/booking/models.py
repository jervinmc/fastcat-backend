from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from django.utils import timezone
# Create your models here.

def nameFile(instance, filename):
    """
    Custom function for naming image before saving.
    """
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return 'uploads/{filename}'.format(filename=filename)


class Booking(models.Model):
    departure_package=models.CharField(_('departure_package'),max_length=255,blank=True,null=True)
    return_package=models.CharField(_('return_package'),max_length=255,blank=True,null=True)
    departure_price=models.CharField(_('departure_price'),max_length=255,blank=True,null=True)
    return_price = models.DecimalField(_('return_price'),max_digits=20, decimal_places=2,default=0.0)
    departure_time=models.CharField(_('departure_time'),max_length=255,blank=True,null=True)
    return_time=models.CharField(_('return_time'),max_length=255,blank=True,null=True)
    return_time=models.CharField(_('return_time'),max_length=255,blank=True,null=True)
    date_from=models.DateTimeField(_('date_from'), null=False,blank=False,default=timezone.now)
    date_to=models.DateTimeField(_('date_to'), null=False,blank=False,default=timezone.now)
    departure_from=models.CharField(_('departure_from'),max_length=255,blank=True,null=True)
    departure_to=models.CharField(_('departure_to'),max_length=255,blank=True,null=True)
    firstname=models.CharField(_('location_to'),max_length=255,blank=True,null=True)
    lastname=models.CharField(_('location_to'),max_length=255,blank=True,null=True)
    email=models.CharField(_('email'),max_length=255,blank=True,null=True)
    mobile_number=models.CharField(_('mobile_number'),max_length=255,blank=True,null=True)
    province=models.CharField(_('province'),max_length=255,blank=True,null=True)
    city=models.CharField(_('city'),max_length=255,blank=True,null=True)
    ticket_type=models.CharField(_('ticket_type'),max_length=255,blank=True,null=True)
    status=models.CharField(_('status'),max_length=255,blank=True,null=True)
    barangay=models.CharField(_('barangay'),max_length=255,blank=True,null=True)
    user_id=models.CharField(_('user_id'),max_length=255,blank=True,null=True)
    class Meta:
        ordering = ["-id"]
