# myapp/api.py
from tastypie.resources import ModelResource
from app.models import Avaluo


class AvaluoResource(ModelResource):
    class Meta:
        queryset = Avaluo.objects.all()
        resource_name = 'avaluo'