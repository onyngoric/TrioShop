from django import forms
from django.forms import ClearableFileInput
from front.models import *

class AdForm(forms.ModelForm):
    class Meta:
        model=Ad
        fields="__all__"
        labels = {
            "title":"Title:",
            "category":"Category:",
            "condition":"Condition (Optional):",
            "description":"Description:",
            "delivery":"PickUp (Optional):",
            "location":"Select Your Location:",
            "price":"Price($) of Item:",
            "payment":"Select payment method:",
        }
        widgets = {
          'description': forms.Textarea(attrs={'class': 'decribeit'}),
          'media': forms.FileInput(attrs={'class': 'pics'}),
          'category': forms.Select(attrs={'class':'inbox'}),
          'condition': forms.Select(attrs={'class':'inbox'}),
          'delivery': forms.Select(attrs={'class':'inbox'}),
          'title': forms.TextInput(attrs={'class':'inbox'}),
          'location': forms.Select(attrs={'class':'inbox'}),
          'price': forms.TextInput(attrs={'class':'inbox'}),
          'payment': forms.Select(attrs={'class':'inbox'}),
        }
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(AdForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['condition'].required = False
        self.fields['delivery'].required = False
        self.fields['price'].required = False
        self.fields['payment'].required = False
        
class AdImageForm(forms.ModelForm):
  class Meta:
    model = AdImages
    fields =['media']
    widgets = {
          'media': ClearableFileInput(attrs={'allow_multiple_selected': True}),
      }