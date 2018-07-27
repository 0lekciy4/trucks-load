from django.contrib import admin

# Register your models here.
from trucks_load import models as trucks_load_models

admin.site.register(trucks_load_models.TruckModel)
admin.site.register(trucks_load_models.Truck)
