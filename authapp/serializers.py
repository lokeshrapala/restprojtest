from rest_framework import serializers
from .models import Product,Review
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pid','pname','pcost','pmfd','pexpdt')

class ReviewSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Review
        fields = ('id', 'title', 'review', 'rating', 'created_by')


