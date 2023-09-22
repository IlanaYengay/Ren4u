from django import forms
from .models import Callback, Car, CarMake

from django.contrib.auth.models import User


class CallbackForm(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': "Name "
        }
    ))
    phone = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': "Phone"
               }
    ))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': "Email"
               }
    ))
    message = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': "Message"
               }
    ))

    class Meta:
        model = Callback
        fields = ['name', 'phone', 'email', 'message']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'color', 'price', 'image')

# Определяем форму для поиска автомобилей
class CarSearchForm(forms.Form):
    make = forms.ModelChoiceField(queryset=CarMark.objects.all(), required=False, widget=forms.Select,
                                  empty_label="Выберите марку")
    model = forms.ChoiceField(choices=[("", "Все")] + list(set([(car.model, car.model) for car in Car.objects.all()])), required=False)
    color = forms.ChoiceField(choices=[("", "Все")] + list(set([(car.color, car.color) for car in Car.objects.all()])), required=False)
    year = forms.ChoiceField(choices=[("", "Все")] + [(i, i) for i in range(2023, 1980, -1)], required=False)
    price_from = forms.IntegerField(required=False)
    price_to = forms.IntegerField(required=False)