from django.urls import path
from .views import HomePageView, AboutPageView, StocksPageView, SignUpView, TablePageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('stocks/', StocksPageView.as_view(), name='stocks'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('table/', TablePageView.as_view(), name='table'),
    path('', HomePageView.as_view(), name='home'),
]