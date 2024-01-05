from django.urls import path
from .views import HTMLView

urlpatterns = [
    path('', HTMLView.as_view(), name='html_converter')
]