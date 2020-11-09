from django.urls import path
from .views import HomePageView, ContactUsView, BlogView, ProductsView, AboutUsView, NDAView, PrivacyPolicyView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('about/', AboutUsView.as_view(), name='about-us'),
    path('products/', ProductsView.as_view(), name='products'),
    path('nda/', NDAView.as_view(), name='nda'),
    path('privacy/', PrivacyPolicyView.as_view(), name='privacy-policy'),
]
