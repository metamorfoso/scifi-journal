from django.conf.urls import include, url
from subscription import views

urlpatterns = [
    url(r'^subscribe$', views.subscribe, name="subscribe")
]