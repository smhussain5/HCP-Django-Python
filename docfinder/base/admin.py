from django.contrib import admin

from .models import Physician, Specialty

# Register your models here.

admin.site.register(Physician)
admin.site.register(Specialty)
