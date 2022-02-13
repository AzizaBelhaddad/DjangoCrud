from django.forms import ModelForm
from django import forms
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # fields = "__all__" 
        exclude = ["state", "deleted"]
        widgets = {
            "title": forms.TextInput(attrs={ "class": "form-control" }),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={ "class": "form-control"}), 
            "tag": forms.SelectMultiple(attrs={ "class": "form-control"})
        }

