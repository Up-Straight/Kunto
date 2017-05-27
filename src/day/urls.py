from django.conf.urls import url

from day import views

urlpatterns = [
    url(r'^day/create/$', views.DayCreate.as_view(), name='day-create'),
    url(r'^day/(?P<id>[0-9]+)/$', views.DayDetails.as_view(), name='day-details')
]
