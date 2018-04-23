from django import forms
from qanswer.models import Question
from .models import Ans

class AnsForm(forms.ModelForm):
	class Meta:
		model = Ans
		fields = [
			'question',
			'name',
			'contents',
			#'excludes',
			'public'
		]

	def __init__(self, user=None, *args, **kwargs):
		print(user)
		#print(kwargs.pop('instance'))
		super(AnsForm, self).__init__(*args,**kwargs)
		self.fields['question'].queryset = Question.objects.filter(questioner=user)#.exclude(ans__isnull=False)