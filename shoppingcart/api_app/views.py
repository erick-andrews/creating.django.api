from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CartItemSerializer
from .models import CartItem

class CartItemViews(APIView):
    # Create a post request handler
    # Post requests create new records
    def post(self, request):
        # Create serializer using the CartItemSerializer we initialized in serializers.py
        serializer = CartItemSerializer(data=request.data)
        # Checks if request body can be used to create a CartItem
        if serializer.is_valid():
            # Creates new instance of CartItem (the point of post!)
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.data}, status=status.HTTP_400_BAD_REQUEST)
    

# Create your views here.
