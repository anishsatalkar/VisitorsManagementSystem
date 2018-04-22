from django.conf.urls import url

from Login import views

# app_name = 'Login'


urlpatterns = [
    url(r'^logout_user/', views.logout_user, name='logout_user'),
    url(r'$', views.login_user, name='login_user'),
]
