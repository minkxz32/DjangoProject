from django import forms
from .models import Pet
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name', 'species', 'breed', 'age', 'description',
            'available', 'photo', 'color', 'size', 'health_status',
            'posted_date', 'adoption_fee'
        ]
        widgets = {
            'available': forms.CheckboxInput(attrs={'class': 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded'}),
            'posted_date': forms.DateInput(attrs={'type': 'date', 'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}),
            'adoption_fee': forms.NumberInput(attrs={'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'}),
            'size': forms.Select(attrs={
                    'style': ' background-color: rgb(17 24 39);'  # Set text color to black and background to red
                }),
            'health_status': forms.Select(attrs={
                'style': ' background-color: rgb(17 24 39);'  # Set text color to black and background to red
            }),
    }

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)
        
        # Apply floating label styling only to non-checkbox fields
        field_classes = 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'

        if 'instance' not in kwargs:
            self.fields['posted_date'].initial = timezone.now().date()  # Set default to today
        for field_name, field in self.fields.items():
            # Apply field classes to all fields except 'available' and 'posted_date'
            if field_name not in ['available', 'posted_date']:
                field.widget.attrs.update({
                    'class': field_classes,
                    'placeholder': ' ',
                })

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer',
            'placeholder': ' ',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        
        # Update each field widget with the same floating label styling
        field_classes = 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': field_classes,
                'placeholder': ' ',
            })

class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'placeholder': 'Username'
        }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
            'class': 'bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500',
            'placeholder': 'Username'
        }))
