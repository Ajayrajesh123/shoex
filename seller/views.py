from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse

def Home(request):
    return render(request,'seller/home.html')
def seller_login(request):

    if request.method=='POST':
       
        Email=request.POST['email']
        Password=request.POST['password']
        
        if SellerRegestration.objects.filter(email=Email,password=Password).exists():
            return redirect('seller:seller_dashboard')
        else:
            return render(request,'seller/seller_login.html',{'msg':'Invalid email or Password'})
    return render(request,'seller/seller_login.html')
def seller_dashboard(request):
    return render(request,'seller/seller_dashboard.html')
def addproduct(request):
    categories=Category.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.FILES['image']
        category=request.POST.get('category')
        cat=Category.objects.get(id=category)
        product=Product(product_name=name,description=description,price=price,image=image,category_name=cat)
        product.save()
    return render(request,'seller/addproduct.html',{'categories':categories})
def views_products(request):
    products=Product.objects.all()
    return render(request,'seller/views_products.html',{'products':products})
def  delete_product(request,product_id):
    Product.objects.get(id=product_id).delete()
    return redirect('seller:views_products')
def  product_updates(request,product_id):
    categories=Category.objects.all()
    product=Product.objects.get(id=product_id)
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        image=request.FILES['image']
        category=request.POST.get('category')
        cat=Category.objects.get(id=category)
        
        product.product_name=name
        product.description=description
        product.price=price
        product.image=image
        product.category_name=cat
        product.save()
        return redirect('seller:view_products')
    return render(request,'seller/product_update.html',{'categories':categories,
                                              'product':product})
