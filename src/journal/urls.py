from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from journal import views


urlpatterns = [
    url(r'^$', views.index, name="landing_page"),
    url(r'^journal/$', views.issue_archive, name="archive"),
    url(r'^issue/(?P<issue_number>[\w-]+)$', views.single_issue, name="issue"),
    url(r'^download_issue/(?P<issue_number>[\w-]+)/(?P<format>[\w\-]+)$',
        views.download_issue,
        name="download_issue"),
    url(r'^current$', views.current, name="current"),
    url(r'^view_story/(?P<slug>[\w\-]+)$', views.view_story, name="view_story")
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
