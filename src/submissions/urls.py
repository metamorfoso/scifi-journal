from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from submissions import views


urlpatterns = [
    url(r'^submissions/$', views.submissions, name="submissions"),
    url(r'^editor_view/$', views.editor_view, name="editor_view")
]
