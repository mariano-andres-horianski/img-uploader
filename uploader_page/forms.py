from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({'class': 'img-input'})
        self.fields['image'].label = ""
    class Meta:
        model = Image
        fields = ('image',)