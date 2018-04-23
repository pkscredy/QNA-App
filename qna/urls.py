from django.conf.urls import url

from .views import (
	AnsCreateView,
	AnsDetailView,
	AnsListView,
	AnsUpdateView
	)

urlpatterns = [
    url(r'^$', AnsListView.as_view(),name='list'),
    url(r'^create$', AnsCreateView.as_view(),name='create'),
    #url(r'^(?P<pk>\d+)/edit/$', AnsUpdateView.as_view(),name='edit'),
    url(r'^(?P<pk>\d+)/$', AnsUpdateView.as_view(),name='detail'),

]
