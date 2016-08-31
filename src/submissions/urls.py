from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from submissions import views


urlpatterns = [
    url(r'^accounts/login/$', auth_views.login),
    url(r'^submissions/$', views.submissions, name="submissions"),
    url(r'^publish/$', views.publish, name="publish")
]
