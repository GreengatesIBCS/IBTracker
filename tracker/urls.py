
from django.conf.urls import url
from . import views

#Team1: Support

urlpatterns = [
    url(r'^$', views.index,name='index'),

#Javi: register
    url(r'^subject/new/$', views.subject_new, name='subject_new'),
    url(r'^subject/all/$', views.subject_all, name='subject_all'),

#javi: home page after login
    url(r'^chose/$', views.subject_display,name='subjects_display'),

    url(r'^student/new/$', views.student_new, name='student_new'),
    url(r'^student/detail/(?P<id>\d+)/$', views.student_detail, name='student_detail'),
    url(r'^student/subject/(?P<id>\d+)/$', views.student_subject,name='student_subject'),

    url (r'^support/new/$', views.support_new, name='support_new'),


    url (r'^Resources/new/$', views.Resources, name='resources_new')
]