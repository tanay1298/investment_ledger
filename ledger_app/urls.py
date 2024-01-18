from django.urls import path
from . import views

urlpatterns = [
    path('', views.ledger_view, name='ledger'),
]
