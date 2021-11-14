from django.shortcuts import render
from .models import Customer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomerSerializer
from rest_framework import status

class CustomerView(APIView):
    
    def get(self, request):
       customer = Customer.published.all()
       serializer = CustomerSerializer(customer,many=True).data 
       return Response(serializer)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
