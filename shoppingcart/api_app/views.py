from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
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
    # Defining Get to retrieve resources
    def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            items = CartItem.objects.all()
            serializer = CartItemSerializer(items, many=True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    # Defining patch allowing us to update records, similar to post but for class-based view
    def patch(self, request, id=None):
        item = CartItem.objects.get(id=id)
        serializer = CartItemSerializer(item, # Instance of cart item
                                        data=request.data, # data received from request
                                        partial=True) # 
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success",
                             "data": serializer.data})
        else:
            return Response({"status": "error", 
                             "data": serializer.data})
    # Defining a Delete method to remove records
    def delete(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

# Create your views here.
