from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name',)

class AdventureForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    answer = forms.CharField(max_length=20)
    room = forms.CharField(max_length=20)
    current_player = forms.CharField(max_length=200)

	