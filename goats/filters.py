# goats/filters.py
import django_filters
from datetime import date, timedelta
from .models import Goat

class GoatFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        label='Search by Name'
    )    
    IS_AVAILABLE_CHOICES = (
        (True, 'For Sale'),
        (False, 'Not For Sale'),
    )
    is_available = django_filters.ChoiceFilter(
        choices=IS_AVAILABLE_CHOICES,
        empty_label='All Goats',
        label='Availability'
    )
    class Meta:
        model = Goat
        fields = [
            'name',
            'is_available',     
        ]
