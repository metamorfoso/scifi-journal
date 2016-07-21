from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from journal import views


urlpatterns = [
    url(r'^$', views.index, name="landing_page"),
    url(r'^journal/$', views.all_issues, name="all_issues"),
    url(r'^issue/(?P<issue_number>[\w-]+)$', views.single_issue, name="issue"),
    url(r'^about/$', views.about, name="about")
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
