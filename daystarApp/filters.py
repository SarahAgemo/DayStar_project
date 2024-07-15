import django_filters
from .models import *
from .models import Baby

class SitterFilter(django_filters.FilterSet):
    sitters_name = django_filters.CharFilter(field_name = 'name', lookup_expr='icontains')


    class Meta:
        model = Sitterform
        fields = ['name']

class BabyFilter(django_filters.FilterSet):
    babys_name = django_filters.CharFilter(field_name = 'baby_name', lookup_expr='icontains')

    class Meta:
        model = Baby
        fields = ['baby_name']

    