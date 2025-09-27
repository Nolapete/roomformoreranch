from django.urls import path
from .views import GoatListView

urlpatterns = [
    path('', GoatListView.as_view(), name='goat_list'),
]