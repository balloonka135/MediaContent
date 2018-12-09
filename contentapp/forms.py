from django import forms
from django.conf import settings

from .models import ContentPost


class ContentPostForm(forms.ModelForm):
    '''
    Form for creating content post.
    Fields are autopopulated to the ContentPost model.
    '''

    class Meta:
        model = ContentPost
        fields = ('title', 'description', 'media_content')

    def clean_file(self, form):
        '''
        checks whether the uploaded content meets the required limit.
        '''
        media_file = self.cleaned_data['media_content']
        if media_file:
            if media_file._size > settings.MAX_IMAGE_SIZE:
                raise forms.ValidationError("The file too large ( > 500MB )")
        else:
            raise forms.ValidationError("Couldn't read uploaded file")


class InstagramPhotoForm(forms.Form):
    '''
    Form for filling in Instagram post URL.
    '''
    post_url = forms.CharField(max_length=800)
