from rest_framework import serializers
from .models import * 
from decimal import Decimal
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields=['id','title','products_count']
    products_count=serializers.IntegerField(read_only=True)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','unit_price','inventory','price_with_tax','collection','slug','description']
    price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    def calculate_tax(self,product:Product):
        return product.unit_price*Decimal(1.1)
class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','unit_price']
class CartItemSerializer(serializers.ModelSerializer):
    product=SimpleProductSerializer()
    total_price=serializers.SerializerMethodField()
    def get_total_price(self,cartitem:CartItem):
        return cartitem.quantity*cartitem.product.unit_price
    class Meta:
        model=CartItem
        fields=['id','product','quantity','total_price']
class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True,read_only=True)
    id=serializers.UUIDField(read_only=True) 
    total_price=serializers.SerializerMethodField()
    def get_total_price(self,cart):
        return sum([item.quantity*item.product.unit_price for item in cart.items.all()])
    class Meta:
        model=Cart
        fields=['id','items','total_price']



    
    
