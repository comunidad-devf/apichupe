from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from app.models import Category


class CategoryResource(ModelResource):
	class Meta:
		queryset = Category.objects.all()
		authorization = Authorization()