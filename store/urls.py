from django.conf.urls import url

from store import views

urlpatterns = [
    url(r'^$', views.index, name='store'),
]