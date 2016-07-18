from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from issues import views


urlpatterns = [
    url(r'^$', views.index, name="landing_page"),
    url(r'^issues/$', views.all_issues, name="all_issues"),
    url(r'^issue/(?P<issue_number>[\w-]+)$', views.single_issue, name="issue")
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
