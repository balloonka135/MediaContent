import os
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify



User = get_user_model()


class ContentPost(models.Model):
    user = models.ForeignKey(User, related_name="photos", on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=False)
    media_content = models.FileField(upload_to='content/%Y/%m/%d', blank=False, unique=True, verbose_name='Media file')

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ContentPost, self).save(*args, **kwargs)

    def check_file_extension(self):
        file_extension = os.path.splitext(self.media_content.name)[1]
        file_extension = file_extension.lower()

        img_extensions = ['.jpg', '.jpeg', '.png', '.tiff', '.gif']
        video_extensions = ['.avi', '.mp4', '.mov', '.mkv']
        if file_extension in img_extensions:
            return 'image'
        elif file_extension in video_extensions:
            return 'video'
        else:
            return None
