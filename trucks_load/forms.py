from django import forms

from .models import TruckModel

ALL_MODELS = 'Все модели'


class TruckTypeForm(forms.Form):
    trucks_titles_list = [(ALL_MODELS, ALL_MODELS)]
    for truck in TruckModel.objects.all():
        trucks_titles_list.append(
            (truck.title, truck.title,)
        )
    type_field = forms.ChoiceField(
        choices=trucks_titles_list,
        initial=ALL_MODELS,
        label='Отсортировать по модели'
    )
