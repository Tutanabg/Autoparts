from django.contrib import admin
from .models import User, Body, Doors, AVDevices, Cameras, Windows, Payment
 
# Register your models here.
admin.site.register(User) 
admin.site.register(Body) 
admin.site.register(Doors) 
admin.site.register(AVDevices) 
admin.site.register(Cameras) 
admin.site.register(Windows) 
admin.site.register(Payment) 
