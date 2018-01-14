from django import forms

from videokit.forms import VideoField

class PostCreateForm(forms.Form):
    video = VideoField()
    title = forms.CharField()
    description = forms.CharField()
