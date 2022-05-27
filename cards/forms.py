from django import forms
from .models import Card

class CardForm(forms.Form):
    card_search = forms.CharField(label="Card Name", max_length=50, required=True)


class CardSearch(forms.Form):
  searched_card = forms.CharField(label="", max_length=50, required=False)
'''class ReviewForm(forms.ModelForm):
  class Meta:
    model = Review
    fields = ['stars', 'review']'''