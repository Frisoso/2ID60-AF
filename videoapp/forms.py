from django import forms

from .models import Post
from videokit.forms import VideoField

class PostCreateForm(forms.Form):
    video = VideoField()
    title = forms.CharField()
    description = forms.CharField()
