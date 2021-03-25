from django.views import View
from django.shortcuts import render,redirect
from store.models import Product

class ProductDetails(View):
    def get(self,request):
        product_id = request.GET['product_id']
        product = Product.get_product_by_id(product_id)
        return render(request,'product_details.html',{'product':product})

