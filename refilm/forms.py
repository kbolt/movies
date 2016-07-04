from django import forms

class MovieEmbed(forms.Form):
	imdbID = forms.CharField()