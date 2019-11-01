from django import forms
from django.forms import ModelForm

from news.models import Article


class ArticleUrlForm(forms.Form):
    article_url = forms.URLField(max_length=255)


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        exclude = ['author']
        widgets = {
            'publish_date': forms.DateTimeInput(attrs={
                            'type': 'date',
                        })
        }

