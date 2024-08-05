from django.contrib import admin

from .models import Departments,Doctors,Booking,Contact

# Register your models here.

admin.site.register(Departments)

admin.site.register(Doctors)


class BookingAdmin(admin.ModelAdmin):
    list_display=('pat_name','p_phone','p_email','doc_name','booking_date','booked_on')


admin.site.register(Booking,BookingAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','message')
    
admin.site.register(Contact,ContactAdmin)