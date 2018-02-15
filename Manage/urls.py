from django.conf.urls import url

from Manage import views

urlpatterns = [
    url(r'^$', views.show_home ,name='manage'),
    url(r'^add_visitor/', views.add_visitor ,name='add_visitor'),
    url(r'^view_visitors/', views.view_visitors ,name='view_visitors'),
]