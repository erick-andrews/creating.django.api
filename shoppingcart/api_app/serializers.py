from rest_framework import serializers
from .models import CartItem

# Creating CartItemSerializer to convert json data to models as object instances
class ClassItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    # Setting default to 1, but not required.
    # In models, required. But incoming, 1 is reasonable assumption.
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ("__all__")
