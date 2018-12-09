"""MediaContent URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.urls import include, path, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', RedirectView.as_view(url='/content/', permanent=True)),
    re_path(r'^content/', include('contentapp.urls', namespace='contentapp')),
    re_path(r'^accounts/', include('accounts.urls', namespace='accounts')),
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
