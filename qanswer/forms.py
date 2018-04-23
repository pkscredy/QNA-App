from django import forms

from .models import Question
from . validators import validate_category

class QuestionCreateFormN(forms.Form):
	name=forms.CharField()
	location=forms.CharField(required=False)
	category=forms.CharField(required=False)

	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == "Hello":
			raise forms.ValidationError("Not a valida question")
		return name

class QuestionCreateForm(forms.ModelForm):
	#email = forms.EmailField()
	# category = forms.CharField(required=False, validators=[validate_category])
	class Meta:
		model = Question
		fields = [
			'name',
			'location',
			'category',
			'slug',
		]
	def clean_name(self):
		name = self.cleaned_data.get("name")
		if name == "Hello":
			raise forms.ValidationError("Not a valida question")
		return name

	# def clean_email(self):
	# 	email = self.cleaned_data.get("email")
	# 	if ".edu" in email:
	# 		raise forms.ValidationError("not accepting edu email")
	# 	return email