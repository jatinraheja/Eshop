from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
# Create your views here.
def index(request):
    products = None
    categories = Category.get_all_category()
    if request.GET.get("category"):
        products= Product.get_all_products_by_category_id(request.GET.get("category"))
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request,"index.html",data)

def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        data = {}
        data['first_name'] = first_name
        data['last_name'] = last_name
        data['username'] = username
        data['email']   = email
        data['phone']  = phone
        error_message = None 
        if not first_name:
            error_message = "first name required"
        elif not last_name:
            error_message = "last name required"
        elif not username:
            error_message = "username required"
        elif not email:
            error_message = "email required"
        elif not password1:
            error_message = "Password required"
        elif not password2:
            error_message = "Please confirm your password"
        elif not password1 == password2:
            error_message = "Your password and confirm password does not match"
        elif len(password1) < 8:
            error_message = "The minimum length of password must be 8 characters"
        data['error'] = error_message     
        if error_message:
            return  render(request,'signup.html',data)
        else:
            return redirect("homepage")
    else:
        return render(request,'signup.html')

