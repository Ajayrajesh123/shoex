from django.shortcuts import render,redirect
from . models import *
from seller.models import*
# Create your views here.
def Index(request):
    return render(request,'customer/index.html')
def Signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        customer=Customer(name=name,email=email,password=password)
        customer.save()
        return redirect('customer:login')
    return render(request,'customer/signup.html')
def Login(request):
     if request.method=='POST':
        Email=request.POST['email']
        Password=request.POST['password']
        try:
                cust=Customer.objects.get(email=Email,password=Password)
                request.session['customer']=cust.id
                return redirect('customer:customer_dashboard')
        except Customer.DoesNotExist:
               return render(request,'customer/login.html',{'msg':'invalid email or password'})
     return render(request,'customer/login.html')

def  customer_dashboard(request):
    if 'customer' in request.session:
        products=Product.objects.all()
        return render(request,'customer/customer_dashboard.html',{'products':products})
    else:
        return render(request,'customer/index.html')

def cart(request):
  if 'customer' in request.session:

    customer_id = request.session.get('customer')
    cust=Customer.objects.get(id=customer_id)

    cart_items=Cart.objects.filter(customer=cust)
    total_price=sum(item.product.price*item.quantity for item in cart_items)
    total_price_per_item=[]
    grand_total=0
    for item in cart_items:
        item_total=item.product.price*item.quantity
        total_price_per_item.append({'item':item,'total':'item_total'})
        grand_total+=item_total
    return render(request,'customer/cart.html',{'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price})
  else:
      return render(request,'customer/index.html')
def add_to_cart(request,product_id):
   if 'customer' in request.session:
    customer_id = request.session.get('customer')
    cust=Customer.objects.get(id=customer_id)
    if request.method=='POST':
        product=Product.objects.get(id=product_id)
        cart_item,created=Cart.objects.get_or_create(product=product,customer=cust)
        if not created:
            cart_item.quantity+=1
            cart_item.save()
        return redirect('customer:cart')
   else:
        return render(request,'customer/index.html')
    
def remove_from_cart(request,product_id):
  if 'customer' in request.session:
    customer_id = request.session.get('customer')
    cust=Customer.objects.get(id=customer_id)
    product=Product.objects.get(id=product_id)
    cart_item=Cart.objects.get(product=product,customer=cust)
    cart_item.delete()
    return redirect('customer:cart')

def logout(request):
    if 'customer' in request.session:
        del request.session['customer']
        return render(request,'customer/index.html')
    else:
        return render(request,'customer/index.html')
    
def search(request):

    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            products=Product.objects.filter(description__icontains=keyword)
        context={
            'products':products,
        }
    return render(request,'customer/customer_dashboard.html',context)
def all_collection(request):
    products=Product.objects.all()
    return render(request,'customer/all_collection.html',{'products':products})
def payment(request):
    return render(request,'customer/payment.html')
def about(request):
    return render(request,'customer/about.html')
def contact(request):
    return render(request,'customer/contact.html')