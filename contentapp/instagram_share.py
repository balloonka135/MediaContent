import os
import urllib
import instaloader
import datetime
from django.conf import settings


def insta_content(url):
    '''
    connects to the instagram post by given URL argument.
    downloads the content post image to the media/ dir.
    returns content post data to create ContentPost instance.
    '''
    L = instaloader.Instaloader()
    shortcode = url.split('/')[-2]
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
    except instaloader.exceptions.InstaloaderException:
        return None
    else:
        title = post.profile
        description = post.caption
        pub_date = post.date
        post_url = post.url

        path = settings.MEDIA_ROOT
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        filename = "_".join([title, suffix]) + '.jpg'

        urllib.request.urlcleanup()
        urllib.request.urlretrieve(post_url, path + filename)

        return [title, description, pub_date, filename]
