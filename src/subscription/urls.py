from django.conf.urls import include, url
from subscription import views

urlpatterns = [
    url(r'^subscribe$', views.subscribe, name="subscribe"),
    url(r'^thanks$', views.confirm, name="confirm"),
]