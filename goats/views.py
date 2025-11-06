from django_filters.views import FilterView

from .filters import GoatFilter
from .models import Goat


class GoatListView(FilterView):
    model = Goat
    template_name = "goats/goat_list.html"
    context_object_name = "goats"
    filterset_class = GoatFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        filter_title = ""
        # Access the raw value from request.GET, as cleaned_data handles None
        is_available_value_raw = self.request.GET.get("is_available")

        if is_available_value_raw is not None:
            # Check if the raw value is an empty string,
            # which indicates the 'All Goats' option
            if is_available_value_raw == "":
                # The title should remain "Goats" when 'All Goats' is selected
                pass
            else:
                # Get the choices from the filter class
                choices = dict(self.filterset.filters["is_available"].extra["choices"])

                # Convert the raw value string to a boolean to match filter choices
                if is_available_value_raw == "True":
                    is_available_bool = True
                elif is_available_value_raw == "False":
                    is_available_bool = False
                else:
                    is_available_bool = None  # Should not happen with your choices

                selected_label = choices.get(is_available_bool)
                if selected_label and selected_label != "All Goats":
                    filter_title = selected_label

        context["filter_title"] = filter_title

        return context
