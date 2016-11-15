from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(
        attrs={'multiple': True, 'required': True, 'webkitdirectory': True, 'mozdirectory': True, 'msdirectory': True,
               'odirectory': True, 'directory': True, "onclick": "uploadFilteredFiles()"}))

    class Meta:
        model = Post
        fields = ('file', )
