from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Order,OrderItem



# Create your views here.
def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})

def product_detail(request,product_id):
    product=Product.objects.get(id=product_id)
    return render(request,'product.html',{'product':product})

def add_to_cart(request,product_id):
    cart=request.session.get('cart',{})
    cart[str(id)]=cart.get(str(id),0)+1
    request.session['cart']=cart
    return redirect('cart')


def cart(request):
    cart=request.session.get('cart',{})
    items=[]
    total=0

    for pid,quantity in cart.items():
      product = Product.objects.get(id=pid)
      subtotal = product.price * quantity
      total += subtotal
      items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
    return render(request,'cart.html',{'items':items,'total':total})

@login_required
def checkout(request):
    cart=request.session.get('cart',{})
    if not cart:
        return redirect('home')
    total=0
    order=Order,objects.create(user=request.user, total_price=0)
    for pid, quantity in cart,items():
        product=Product.objects.get(id=id)
        OrderItem.objects.create(order=order,product=product,quantity=quantity)
        total+=product.price*quantity
    order.total_price=total
    order.save()
    request.session['cart']={}
    return render(request,'success.html',{'order':order})

def register(request):
    if request.method=='POST':
        User.object.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
        )
        return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        user=authenticate(
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'Invalid Credentials'})
    return render(request,'login.html')
    

def logout(request):
    logout(request)
    return redirect('home')