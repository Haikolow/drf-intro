from django.contrib import admin

# Register your models here.
from .models import Sensor, Measurement

@admin.register(Sensor)
class SenorAdmin(admin.ModelAdmin):
    pass

@admin.register(Measurement)
class Measurement(admin.ModelAdmin):
    pass