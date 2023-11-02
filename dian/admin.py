from django.contrib import admin
from .models import *
# Register your models here.
from .models import ConfirmBooking
from django.contrib import admin

class ConfirmBookingAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(ConfirmBooking,ConfirmBookingAdmin)

admin.site.register(Packages)
admin.site.register(Contact)
# admin.site.register(ConfirmBooking)


admin.site.register(Payment)
