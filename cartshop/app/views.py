from django.shortcuts import render
from .models import Product,Cart,Customer,OrderPlaced
from django.views import View
from django.contrib import messages
from .forms import UserRegistrationForm

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

def topwear(request,data=None):
    if data == None:
        topwear = Product.objects.filter(category='TW')
    elif data=='amul' or data=='Lee' or data=='dandg':
        topwear = Product.objects.filter(category='TW').filter(brand=data)
    elif data=='above':
        topwear = Product.objects.filter(category='TW').filter(discounted_price__gt=1000)
    elif data=='below':
        topwear = Product.objects.filter(category='TW').filter(discounted_price__lt=1000)
    context = {'topwear':topwear}
    return render(request,'app/topwear.html',context)

def bottomwear(request, data=None):
    if data == None:
        bottomwear = Product.objects.filter(category='BW')
    elif data=='amul' or data=='Lee' or data=='dandg':
        bottomwear = Product.objects.filter(category='BW').filter(brand=data)
    elif data=='above':
        bottomwear = Product.objects.filter(category='BW').filter(discounted_price__gt=1000)
    elif data=='below':
        bottomwear = Product.objects.filter(category='BW').filter(discounted_price__lt=1000)
    context = {'bottomwear':bottomwear}
    return render(request,'app/bottomwear.html',context)

def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self,request):
        fm = UserRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form':fm})
    def post(self,request):
        fm = UserRegistrationForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Your Registration Successfully')
            fm.save()
        return render(request, 'app/customerregistration.html',{'form':fm})


def checkout(request):
 return render(request, 'app/checkout.html')
