from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.views.defaults import page_not_found


urlpatterns = [
    url(r'^admin$', RedirectView.as_view(url='/admin/', permanent=True)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^404$', page_not_found),
    url(r'^', include("issues.urls"))
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
