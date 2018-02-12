from django.conf.urls import url
from . import views

urlpatterns = [
    url (r'^$', views.index, name= 'index'),
    url (r'^ subject/new/$', views.subject_new, name='subject_new'),
    url (r'^ Login/new/$', views.Login_new, name='Login_new'),
    url (r'^ Support/new/$', views.Support_new, name='Support_new'),

]