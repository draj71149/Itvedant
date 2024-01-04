from django import forms
from .models import Message,Comment
from django.contrib.auth.models import User

class FeedsForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=['content']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        widgets = {
            'content': forms.Textarea(attrs={'style': 'height: 50px;' }),
        }
class LikeForm(forms.Form):
    class Meta:
        model=Message
        fields=''

class sign_form(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','username','password']