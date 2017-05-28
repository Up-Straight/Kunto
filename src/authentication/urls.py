from django.conf.urls import url
from authentication import views

urlpatterns = [
    url(r'^users/create$', views.UserCreate.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserGet.as_view()),
    url(r'^getuser/$', views.current_user)
]