from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('inventory', views.inventory, name='inventory'),
    path('cart', views.cart, name='cart'),
    path('collect_book/<str:pk>', views.collect_book, name='collect_book'),
    path('return_book/<str:pk>', views.return_book, name='return_book'),
    path('checkout', views.check_out, name='checkout'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('make_request/<str:pk>', views.make_request, name='make_request'),
    path('deny/<int:pk>', views.deny, name='deny'),
]
