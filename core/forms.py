from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostSearchForm(forms.Form):
    q = forms.CharField()


class ContactForm(forms.Form):
    name = forms.CharField(max_length =50)
    email = forms.EmailField(max_length=150)
    message = forms.CharField(widget = forms.Textarea, max_length= 2000)