from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm

def index(request):
	'''Home page Learning logs'''
	return render (request, 'learning_logs/index.html')

def topics(request):
	'''list of themes'''
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}

	return render (request, 'learning_logs/topics.html', context)

def topic (request, topic_id):
	'''render one theme and all his entries'''
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render (request, 'learning_logs/topic.html', context)

def new_topic(request):
	'''define a new theme'''
	if request.method != 'POST':
		#date is not send; create empty form
		form = TopicForm ()
	else:
		#POST date is send, computate next
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))
		
	context = {'form': form}
	return render (request, 'learning_logs/new_topic.html', context)

