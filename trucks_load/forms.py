from django import forms

from .models import TruckModel

ALL_MODELS = 'Все модели'


class TruckTypeForm(forms.Form):
    type_field = forms.ChoiceField(
        initial=ALL_MODELS,
        label='Отсортировать по модели'
    )

    def __init__(self, *args, **kwargs):
        super(TruckTypeForm, self).__init__(*args, **kwargs)
        trucks_choices = [(ALL_MODELS, ALL_MODELS)]
        for truck in TruckModel.objects.all():
            trucks_choices.append(
                (truck.title, truck.title)
            )
        self.fields['type_field'].choices = trucks_choices