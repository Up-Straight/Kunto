from django.conf.urls import url

from exercise import views

urlpatterns = [
    url(r'^exercise/create/$', views.ExerciseCreate.as_view(), name='exercise-create'),
    url(r'^exercise/(?P<pk>[0-9]+)/$', views.ExerciseDetails.as_view(), name='exercise-details'),
    url(r'^state/create/$', views.state_create, name='state-create')
]
