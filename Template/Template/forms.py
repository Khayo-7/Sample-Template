from django import forms

class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=255, label="Search Here! (Use Code or Name)")
    