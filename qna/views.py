from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView

from .forms import AnsForm
from .models import Ans

class HomeView(View):
	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return render(request, "home.html", {})

		user = request.user
		is_following_user_ids = [x.user.id for x in user.is_following.all()]
		qs = Ans.objects.filter(user__id__in=is_following_user_ids, public=True).order_by("-updated")[:20]
		return render(request, "qna/home-feed.html", {'object_list':qs})

class AnsListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return Ans.objects.filter(user=self.request.user)

class AnsDetailView(LoginRequiredMixin, DetailView):
	def get_queryset(self):
		return Ans.objects.filter(user=self.request.user)

class AnsCreateView(LoginRequiredMixin, CreateView):
	template_name = 'form.html'
	form_class = AnsForm

	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = self.request.user
		return super(AnsCreateView, self).form_valid(form)

	def get_form_kwargs(self):
		kwargs = super(AnsCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		#kwargs['instance'] = Ans.objects.filter(user=self.request.user).first()
		return kwargs

	def get_queryset(self):
		return Ans.objects.filter(user=self.request.user)


	def get_context_data(self, *args, **kwargs):
		context = super(AnsCreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'create ans'
		return context

class AnsUpdateView(LoginRequiredMixin, UpdateView):
	template_name = 'qna/detail-update.html'
	form_class = AnsForm
	def get_queryset(self):
		return Ans.objects.filter(user=self.request.user)

	def get_context_data(self, *args, **kwargs):
		context = super(AnsUpdateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'update ans'
		return context
	def get_form_kwargs(self):
		kwargs = super(AnsUpdateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		#kwargs['instance'] = Ans.objects.filter(user=self.request.user).first()
		return kwargs