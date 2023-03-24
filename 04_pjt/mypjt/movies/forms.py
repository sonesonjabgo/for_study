from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    genre = forms.ChoiceField(
        widget=forms.Select,
        choices=[('comedy','comedy'),('horror','horror'),('romance','romance')],
        )
    
    class Meta:
        model = Movie
        fields = '__all__'