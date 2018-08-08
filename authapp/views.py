from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product,Review
from django.http import HttpResponse
from .serializers import ProductSerializer,ReviewSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly
def input(request):
    return render(request,'input.html')
def insert(request):
    pid1=int(request.GET['t1'])
    pname1=request.GET['t2']
    pcost1=float(request.GET['t3'])
    pmfd1=request.GET['t4']
    pexpd1=request.GET['t5']
    f=Product(pid=pid1,pname=pname1,pcost=pcost1,pmfd=pmfd1,pexpdt=pexpd1)
    f.save()
    return render(request,'links.html')
def display(request):
    recs=Product.objects.all()
    return render(request,'display.html',{'records':recs})

class ProductList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_url_kwarg = 'review_id'

    def get_queryset(self):
        review = self.kwargs['review_id']
        return Review.objects.filter(id=review)

#http --json POST http://127.0.0.1:8000/authapp/products/ pid="1003" pname="iphoneX" pcost="99999" pmfd="2018-02-16" pexpdt="2019-02-16" Authorization:"Token bd383ffbe95479ca017a0305e29500e7c9cb71fa"
#http --json DELETE http://127.0.0.1:8000/authapp/products/1003/ Authorization:"Token bd383ffbe95479ca017a0305e29500e7c9cb71fa"







