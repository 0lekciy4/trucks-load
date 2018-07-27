from django.views import View
from django.shortcuts import render

from django.db.models import F

from .models import Truck
from .forms import TruckTypeForm

from .forms import ALL_MODELS


class TruckListView(View):

    @staticmethod
    def get(request):
        trucks_form = TruckTypeForm()
        trucks_list = Truck.objects.annotate(
            overweight=100 - F('current_weight') * 100 / F('truck_type__carrying')
        )

        return render(
            request,
            'trucks_load/trucks_list.html',
            {
                'trucks_form': trucks_form,
                'trucks_list': trucks_list
            }
        )

    @staticmethod
    def post(request):
        trucks_form = TruckTypeForm(request.POST)
        valid = trucks_form.is_valid()
        all_models = trucks_form.cleaned_data['type_field'] == ALL_MODELS
        if valid and valid is not all_models:
            trucks_list = Truck.objects.filter(
                truck_type__title=trucks_form.cleaned_data['type_field']
            ).extra()
        else:
            trucks_list = Truck.objects.all()
        trucks_list_annotate = trucks_list.annotate(
            overweight=100 - F('current_weight') * 100 / F('truck_type__carrying')
        )
        return render(
            request,
            'trucks_load/trucks_list.html',
            {
                'trucks_form': trucks_form,
                'trucks_list': trucks_list_annotate
            }
        )
