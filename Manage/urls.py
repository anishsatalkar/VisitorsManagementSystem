from django.conf.urls import url

from Manage import views

app_name = 'Manage'

urlpatterns = [
    url(r'^$', views.show_home ,name='manage'),
    url(r'^add_visitor/', views.add_visitor ,name='add_visitor'),
    url(r'^view_visitors/', views.view_visitors ,name='view_visitors'),
    url(r'^delete_visitor/',views.delete_visitor,name='delete_visitor'),
    url(r'^(?P<pk>\d+)/visitor_edit/',views.visitor_edit,name='visitor_edit'),
]