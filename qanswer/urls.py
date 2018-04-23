from django.conf.urls import url

from .views import (
	QuestionListView,
	QuestionDetailView,
	QuestionCreateView,
	QuestionUpdateView 
	)

urlpatterns = [
    url(r'^$', QuestionListView.as_view(),name='list'),
    url(r'^create$', QuestionCreateView.as_view(),name='create'),
    #url(r'^(?P<slug>[\w-]+)/edit/$', QuestionUpdateView.as_view(),name='edit'),
    url(r'^(?P<slug>[\w-]+)/$', QuestionUpdateView.as_view(),name='detail'),
    
]
