from django.urls import path
from .views import HomePageView, AboutPageView, StocksPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('finance/', StocksPageView.as_view(), name='stocks'),
    path('', HomePageView.as_view(), name='home'),
]