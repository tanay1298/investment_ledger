# ledger_app/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ledger_view, name='ledger'),
]
