from django.contrib import admin
from django.urls import path
from trucks_load.views import TruckListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TruckListView.as_view())
]
