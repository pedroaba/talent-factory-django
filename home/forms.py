from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT NAME'
            }
        )
    )

    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'E-MAIL'
            }
        )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'PHONE'
            }
        )
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-2 placeholder:text-sm w-full h-36',
                'placeholder': 'INPUT YOUR MESSAGE'
            }
        )
    )
