from django import forms

from .models import Article


class ArticleCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'slug', 'thumbnail']


class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'slug', 'thumbnail']
