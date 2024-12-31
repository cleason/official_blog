from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'content']
        widgets = {
            'name': forms.TextInput(attrs={
            'class': 'w-full rounded border-gray-300 py-6 px-6',
            'placeholder': 'Votre nom'
            }),
            'content': forms.Textarea(attrs={
            'class': 'w-full rounded border-gray-300 py-2 px-4',
            'placeholder': 'Votre message',
            'rows': 10
            }),
        }

