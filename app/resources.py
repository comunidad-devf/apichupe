from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.validation import CleanedDataFormValidation

from app.models import Category
from app.forms import CategoryForm

class CategoryResource(ModelResource):
	class Meta:
		queryset = Category.objects.all()
		authorization = Authorization()
		validation = CleanedDataFormValidation(form_class=CategoryForm)