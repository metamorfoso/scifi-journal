from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from issues import views


urlpatterns = [
    url(r'^$', views.index)
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
