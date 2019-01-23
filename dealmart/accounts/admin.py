from django.contrib import admin

from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

admin.site.register(OTP)
admin.site.register(DeliveryAddress)
admin.site.register(User)
admin.site.register(Role)
admin.site.register(PickupAddress)
admin.site.register(SellerDetails)