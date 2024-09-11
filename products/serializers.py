from rest_framework import serializers
from .models import Product, Seller

# Seller Serializer
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name', 'photo', 'rating']

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    seller = SellerSerializer()  # Nested seller serializer to include seller details

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'actual_price', 'offer_price', 'product_image', 'warranty_period', 'seller']

    def create(self, validated_data):
        # Extract seller data from the validated data
        seller_data = validated_data.pop('seller')

        # Get or create the seller
        seller, created = Seller.objects.get_or_create(**seller_data)

        # Create the product with the extracted seller
        product = Product.objects.create(seller=seller, **validated_data)

        return product

    def update(self, instance, validated_data):
        # Extract seller data from the validated data
        seller_data = validated_data.pop('seller', None)

        # Update product fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Update or create seller if data is provided
        if seller_data:
            seller, created = Seller.objects.update_or_create(id=instance.seller.id, defaults=seller_data)
            instance.seller = seller

        instance.save()
        return instance
