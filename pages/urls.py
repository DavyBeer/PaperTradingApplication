from django.urls import path
from .views import HomePageView, AboutPageView, StocksPageView, SignUpView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('stocks/', StocksPageView.as_view(), name='stocks'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
]