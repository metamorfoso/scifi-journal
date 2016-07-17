from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from issues import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^issue/(?P<issue_number>[\w-]+)$', views.issue, name="issue")
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
