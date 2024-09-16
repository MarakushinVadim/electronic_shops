from rest_framework import serializers, permissions
from .models import ShopNode, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ShopNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = ShopNode
        fields = '__all__'
        read_only_fields = ('debt',)

    def create(self, validated_data):
        products_data = validated_data.pop('products')
        shop_node = ShopNode.objects.create(**validated_data)
        for product_data in products_data:
            product, created = Product.objects.get_or_create(**product_data)
            shop_node.products.add(product)
        shop_node.clean()
        shop_node.save()
        return shop_node

    def update(self, instance, validated_data):
        products_data = validated_data.pop('products')
        instance = super().update(instance, validated_data)
        instance.products.clear()
        for product_data in products_data:
            product, created = Product.objects.get_or_create(**product_data)
            instance.products.add(product)
        instance.clean()
        instance.save()
        return instance
