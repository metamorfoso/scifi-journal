from django.conf.urls import include, url
from subscription import views

urlpatterns = [
    url(r'^subscribe$', views.subscribe, name="subscribe"),
    url(r'^thanks$', views.confirm, name="confirm"),
    url(r'^unsubscribe', views.unsubscribe, name="unsubscribe")
]