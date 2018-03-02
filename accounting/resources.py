from import_export import resources
from .models import Accounting, Person

class PersonResource(resources.ModelResource):
    class Meta:
        model = Accounting

class PersonResource(resources.ModelResource):
    class Meta:
        model = Person
