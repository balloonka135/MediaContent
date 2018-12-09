from django import forms
from django.conf import settings

from .models import ContentPost


class ContentPostForm(forms.ModelForm):

    class Meta:
        model = ContentPost
        fields = ('title', 'description', 'media_content')

    def clean_file(self, form):
        media_file = self.cleaned_data['media_content']
        if media_file:
            if media_file._size > settings.MAX_IMAGE_SIZE:
                raise forms.ValidationError("The file too large ( > 500MB )")
        else:
            raise forms.ValidationError("Couldn't read uploaded file")


class InstagramPhotoForm(forms.Form):
    post_url = forms.CharField(max_length=800)
