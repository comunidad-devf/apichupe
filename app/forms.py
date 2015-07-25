from django import forms

from app.models import Category, Drink

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']


class DrinkForm(forms.ModelForm):
	class Meta:
		model = Drink
		fields = '__all__'