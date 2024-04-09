from django import forms

from cars.models import Car


class CarsForms(forms.ModelForm):
    FUEL_TYPE_CHOICES = (
        ('GASOLINE', 'GASOLINE'),
        ('ALCOHOL', 'ALCOHOL'),
        ('DIESEL', 'DIESEL')
    )

    CAR_TYPE_CHOICES = (
        ('AUTOMATIC', 'AUTOMATIC'),
        ('MANUAL', 'MANUAL'),
    )

    brand = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE BRAND'
            }
        )
    )

    model = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE MODEL'
            }
        )
    )

    version = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE VERSION'
            }
        )
    )

    car_year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE YEAR'
            }
        )
    )

    color = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE COLOR'
            }
        )
    )

    kilometers = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE KILOMETERS'
            }
        )
    )

    motor_detail = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE MOTOR DETAIL'
            }
        )
    )

    fuel = forms.ChoiceField(
        choices=FUEL_TYPE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 font-semibold font-roboto '
                         'text-app-blue-300 py-1.5 text-sm',
                'placeholder': 'INPUT THE MOTOR DETAIL'
            }
        )
    )

    car_type = forms.ChoiceField(
        choices=CAR_TYPE_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 font-semibold font-roboto '
                         'text-app-blue-300 py-1.5 text-sm',
                'placeholder': 'INPUT THE CAR TYPE'
            }
        )
    )

    price = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE PRICE'
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-2 placeholder:text-sm w-full h-36',
                'placeholder': 'DESCRIBE THE MAIN INFORMATION ABOUT THE CAR'
            }
        )
    )

    photo_car = forms.ImageField()

    class Meta:
        model = Car
        fields = '__all__'
        exclude = ('car_id',)
