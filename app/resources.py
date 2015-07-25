from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.validation import CleanedDataFormValidation

from app.models import Category, Drink
from app.forms import CategoryForm, DrinkForm

class CategoryResource(ModelResource):
	class Meta:
		queryset = Category.objects.all()
		authorization = Authorization()
		validation = CleanedDataFormValidation(form_class=CategoryForm)


class DrinkResource(ModelResource):
	class Meta:
		queryset = Drink.objects.all()
		authorization = Authorization()
		validation = CleanedDataFormValidation(form_class=DrinkForm)