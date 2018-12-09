from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .models import ContentPost
from .forms import ContentPostForm, InstagramPhotoForm
from .instagram_share import insta_content


def index(request):
    """
    View function for home page of site.
    """
    posts = ContentPost.objects.order_by('-pub_date')
    return render(request, 'contentapp/index.html', {
        'posts': posts
    })


def detail_content(request, id, slug):
    """
    View function for detail post page.
    """
    try:
        post = get_object_or_404(ContentPost, id=id, slug=slug)
    except ConnectionResetError:
        pass
    return render(request, 'contentapp/post_detail.html', {
        'post': post
    })


@login_required
def edit_content(request, id, slug):
    """
    View function for editing post page.
    """
    post = get_object_or_404(ContentPost, id=id, slug=slug)
    if request.method == 'POST':
        form = ContentPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(reverse('contentapp:index'))
    else:
        form = ContentPostForm(instance=post)
    return render(request, 'contentapp/post_edit.html', {
        'form': form,
        'post': post
    })


@login_required
def delete_content(request, id):
    """
    View function to process post deletion.
    """
    post = get_object_or_404(ContentPost, id=id)
    post.delete()
    return redirect(reverse('contentapp:index'))


@login_required
def upload_content(request):
    """
    View function for uploading content.
    """
    if request.method == 'POST':
        form = ContentPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect(reverse('contentapp:index'))
    else:
        form = ContentPostForm()
    return render(request, 'contentapp/post_upload.html', {
        'form': form
    })


@login_required
def share_insta_content(request):
    """
    View function for sharing insta-content by url.
    """
    if request.method == 'POST':
        form = InstagramPhotoForm(request.POST)
        if form.is_valid():
            result = insta_content(form.cleaned_data['post_url'])
            if not result:
               return render(request, 'contentapp/error.html')
            else:
                title, description, pub_date, content = result
                post = ContentPost(user=request.user, title=title, description=description, pub_date=pub_date, media_content=content)
                post.save()
                return redirect(reverse('contentapp:index'))
    else:
        form = InstagramPhotoForm()
    return render(request, 'contentapp/share_content.html', {'form': form})
