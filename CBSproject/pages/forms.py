from django import forms
from .models import Posting, Comment

class PostingForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ['text'] 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']