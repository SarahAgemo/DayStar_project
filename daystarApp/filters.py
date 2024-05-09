import django_filters
from.models import *

class SitterFilter(django_filters.FilterSet):
    class Meta:
        model = Sitterform
        fields = ['name']