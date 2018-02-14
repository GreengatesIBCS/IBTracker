from django.conf.urls import url
from . import views

# URL Changes

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^subject/new/$', views.subject_new, name='subject_new'),
    url(r'^subject/all/$', views.subject_all, name='subject_all'),
]