from django.conf.urls import url

from Manage import views

app_name = 'Manage'

urlpatterns = [
    url(r'^$', views.show_home, name='manage'),
    url(r'^add_visitor/', views.add_visitor, name='add_visitor'),
    url(r'^view_visitors/', views.view_visitors, name='view_visitors'),
    url(r'^delete_visitor/', views.delete_visitor, name='delete_visitor'),
    url(r'^search_visitor/', views.search_visitor, name='search_visitor'),
    url(r'^edit_visitor/', views.edit_visitor, name='edit_visitor'),
    url(r'^view_profile/', views.view_profile, name='view_profile'),
]
