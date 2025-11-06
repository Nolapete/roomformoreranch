import django_filters

from .models import Goat


class GoatFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains", label="Name")
    IS_AVAILABLE_CHOICES = (
        (None, "All Goats"),
        (True, "For Sale"),
        (False, "Not For Sale"),
    )
    is_available = django_filters.ChoiceFilter(
        choices=IS_AVAILABLE_CHOICES,
        empty_label=None,  # Explicitly set to None for better control
        label="Availability",
    )

    class Meta:
        model = Goat
        fields = [
            "name",
            "is_available",
        ]
