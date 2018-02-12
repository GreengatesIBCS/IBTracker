
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^chose/$', views.subjects_display,name='subjects_display'),
    url(r'^subject/new/$', views.subject_new,name='subject_new'),
    url(r'^student/detail/(?P<id>\d+)/$', views.student_detail,name='student_detail'),
    url(r'^student/subject/(?P<id>\d+)/$', views.Student_subject,name='student_subject'),
    url (r'^Login/new/$', views.Login_new, name='Login_new'),
    url (r'^Support/new/$', views.Support_new, name='Support_new'),

]