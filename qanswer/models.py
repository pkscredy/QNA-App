from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL

class QuestionQuerySet(models.query.QuerySet):
	def search(self, query): #Question.objects.all()search(query)
		if query:
			return self.filter(
				Q(name__icontains=query)|
				Q(location__icontains=query)|
				Q(category__icontains=query)|
				Q(ans__name__icontains=query)|
				Q(ans__contents__icontains=query)
				).distinct()
			return self

class QuestionManager(models.Manager):
	def get_queryset(self):
		return QuestionQuerySet(self.model, using=self._db)

	def search(self, query): #Question.objects.search()
		return self.get_queryset().search(query)

class Question(models.Model):
	questioner = models.ForeignKey(User)
	name	=models.CharField(max_length=120)
	location=models.CharField(max_length=120, null=True, blank=True)
	category=models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
	timestamp=models.DateTimeField(auto_now_add=True)
	updated	 =models.DateTimeField(auto_now=True)
	slug	 =models.SlugField(null=True, blank=True)
	#my_date_field=models.DateField(auto_now=False, auto_now_add=False)

	objects = QuestionManager()

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		# return f"/question/{self.slug}"
		return reverse('question:detail', kwargs={'slug': self.slug})

	@property
	def title(self):
		return self.name

def q_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.category = instance.category.capitalize()
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
'''
def q_post_save_receiver(sender, instance, created, *args, **kwargs):
	print('saved')
	print(instance.timestamp)
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
		instance.save()
'''
pre_save.connect(q_pre_save_receiver, sender=Question)

#post_save.connect(q_post_save_receiver, sender=Question)