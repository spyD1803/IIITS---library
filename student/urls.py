from django.conf.urls import url, include
from . import views


urlpatterns = [
 
    #url(r'^administration/', include('administration.urls')),
    url(r'^$',include('administration.urls') ),
    url(r'^login/$', views.login_user.as_view(), name="login_user"),
    url(r'^logout/$', views.logout_user, name="logout_user"),
    url(r'^teams3/$', views.teams3, name="teams3"),


]