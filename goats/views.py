from django_filters.views import FilterView
from .models import Goat
from .filters import GoatFilter

class GoatListView(FilterView):
    model = Goat
    template_name = 'goats/goat_list.html'
    context_object_name = 'goats'
    filterset_class = GoatFilter