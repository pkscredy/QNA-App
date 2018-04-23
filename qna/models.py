from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from qanswer.models import Question

class Ans(models.Model):
	user	=models.ForeignKey(settings.AUTH_USER_MODEL)
	question 	=models.ForeignKey(Question)

	name	=models.CharField(max_length=200)
	contents=models.TextField(help_text='seprate each by comma')
	#excludes=models.TextField(blank=True, null=True, help_text='seprate each by comma')
	public	=models.BooleanField(default=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated	=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# return f"/question/{self.slug}"
		return reverse('qna:detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['-updated','-timestamp']

	def get_contents(self):
		return self.contents.split(",")

	# def get_excludes(self):
	# 	return self.excludes.split(",")