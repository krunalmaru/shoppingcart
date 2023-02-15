from django.shortcuts import render
from .models import Product,Cart,Customer,OrderPlaced
from django.views import View
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwear = Product.objects.filter(category= 'TW')
        bottomwear = Product.objects.filter(category= 'BW')
        mobile = Product.objects.filter(category= 'M')
        laptop = Product.objects.filter(category= 'L')
        context = {'topwear':topwear,'bottomwear':bottomwear,'mobile':mobile,'laptop':laptop}
        return render(request, 'app/home.html',context)

class ProductDetailView(View):
    def get(self,request, pk):
        productdetail = Product.objects.get(pk=pk)
        context = {'productdetail':productdetail}
        return render(request,'app/productdetail.html',context)

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data==None:
        mobile = Product.objects.filter(category='M')
    elif data=='vivo' or data=='samsung' or data=='mi':
        mobile = Product.objects.filter(category='M').filter(brand=data)
    elif data=='above':
        mobile = Product.objects.filter(category='M').filter(discounted_price__gt=20000) 
    elif data=='below':
        mobile = Product.objects.filter(category='M').filter(discounted_price__lt=20000) 
    return render(request, 'app/mobile.html',{'mobile':mobile})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
