from django.conf.urls import url

from Login import views

urlpatterns = [
    url(r'^$', views.login_user ,name='login_user'),
    url(r'^logout_user/', views.logout_user ,name='logout_user'),
]