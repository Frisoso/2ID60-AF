from django import forms

from videokit.forms import VideoField
from .models import Post, Comment

class PostCreateForm(forms.ModelForm):
    video = VideoField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ('video','title','description',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
