'''url for learning_logs'''
from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.index, name = 'index'),
	url(r'^topics/$', views.topics, name = 'topics'),
# page with information about particular theme
url (r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
#page for new theme
url(r'^new_topic/$', views.new_topic, name='new_topic'),
]
