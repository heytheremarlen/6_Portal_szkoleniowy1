from django.conf.urls import url
from . import views

app_name = 'calendar2'
urlpatterns = [

    url(r'^$', views.CalendarView.as_view(), name='calendar2'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
]
