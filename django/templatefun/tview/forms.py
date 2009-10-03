
from django import forms

class CourseForm(forms.Form):
	name = forms.CharField()
	description = forms.CharField()

	def clean_name(self):
		name = self.cleaned_data['name']

		if name.find('INF') == -1:
			raise forms.ValidationError("Course needs to start with INF.")

		return name
