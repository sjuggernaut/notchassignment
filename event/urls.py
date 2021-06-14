from django.urls import path
from .views import EventView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('manage', EventView.as_view(), name='event-manage')
]

urlpatterns = format_suffix_patterns(urlpatterns)
