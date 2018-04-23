from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import Question
from .forms import QuestionCreateFormN, QuestionCreateForm



class QuestionListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Question.objects.filter(questioner=self.request.user)


class QuestionDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Question.objects.filter(questioner=self.request.user)



class QuestionCreateView(LoginRequiredMixin,CreateView):
	form_class = QuestionCreateForm
	login_url='/login/'
	template_name = 'form.html'
	#success_url = "/question/"

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.questioner = self.request.user
		#instance.save()
		return super(QuestionCreateView, self).form_valid(form)

	def get_context_data(self, *args, **kwargs):
		context = super(QuestionCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Question'
		return context

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
	form_class = QuestionCreateForm
	login_url='/login/'
	template_name = 'qanswer/detail-update.html'
	#success_url = "/question/"


	def get_context_data(self, *args, **kwargs):
		context = super(QuestionUpdateView, self).get_context_data(*args, **kwargs)
		name = self.get_object().name
		context['title'] = f'update question: {name}'
		return context

	def get_queryset(self):
		return Question.objects.filter(questioner=self.request.user)