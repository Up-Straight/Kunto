from django.conf.urls import url
from authentication import views

urlpatterns = [
    url(r'^users/create$', views.UserCreate.as_view()),
]