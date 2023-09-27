from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
Router = DefaultRouter()
Router.register('product', views.ProductViewSet, basename='product')
Router.register('collection', views.CollectionViewSet)
Router.register('carts', views.CartViewSet)
Router.register('cart_item', views.CartItemViewSet,basename='cart_item')
urlpatterns = [
    path('', include(Router.urls))]
