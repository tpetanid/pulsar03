from django import forms
from .models import Owner

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'comments']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input rounded-md shadow-sm mt-1 block w-full dark:bg-gray-700 dark:border-gray-400 dark:border-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input rounded-md shadow-sm mt-1 block w-full dark:bg-gray-700 dark:border-gray-400 dark:border-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-input rounded-md shadow-sm mt-1 block w-full dark:bg-gray-700 dark:border-gray-400 dark:border-2'}),
            'phone': forms.TextInput(attrs={'class': 'form-input rounded-md shadow-sm mt-1 block w-full dark:bg-gray-700 dark:border-gray-400 dark:border-2'}),
            'address': forms.Textarea(attrs={'class': 'form-textarea rounded-md shadow-sm mt-1 block w-full dark:bg-gray-700 dark:border-gray-400 dark:border-2', 'rows': 3}),
            'comments': forms.Textarea(attrs={'class': 'form-textarea rounded-md shadow-sm mt-1 block w-full dark:bg-gray-700 dark:border-gray-400 dark:border-2', 'rows': 3}),
        } 