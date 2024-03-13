from django.http import JsonResponse
from django.shortcuts import redirect,render
from system.models import slider,banner_area,Main_Category,Product,Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Min, Sum
from cart.cart import Cart

def BASE(request):
    return render(request, 'base.html')



def HOME(request):
    sliders = slider.objects.all().order_by('-id')[0:3]
    banners = banner_area.objects.all().order_by('-id')[0:3]
    
    main_category = Main_Category.objects.all().order_by('-id')
    product = Product.objects.filter(section__name="Top Deals of the Day")
   

    context = {
        'sliders':sliders,
        'banners':banners,
        'main_category':main_category,
        'product':product,
    }
    return render(request, 'Main/home.html',context)


def PRODUCT_DETAILS(request,slug):
    product = Product.objects.filter(slug = slug)
    if product.exists():
        product = Product.objects.get(slug = slug)
    else:
        return redirect('404')

    context = {
        'product':product,

    }
    return render(request,'product/product_detail.html',context)


def Error404(request):
    return render(request,'errors/404.html')



def MY_ACCOUNT(request):
    return render(request,'account/my-account.html')


def REGISTER(request):
    if request.method == "POST":
      username = request.POST.get('username')
      email = request.POST.get('email')
      password = request.POST.get('password')


      if User.objects.filter(username = username).exists():
          messages.error(request,'Username is already taken')
          return redirect('my_account')
      
      if User.objects.filter(email = email).exists():
          messages.error(request,'Email address already exists')
          return redirect('my_account')

            
      user = User(
          username = username,
          email = email,

          
      )
      user.set_password(password)
      user.save()
      return redirect('my_account')
    
    return render(request,'account/my-account.html')

def LOGIN(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
           messages.error(request, 'Invalid Password or Email')
           return redirect('my_account')
    return render(request,'account/my-account.html')


def ABOUT(request):
    return render(request,'Main/about.html')


def CONTACT(request):
    return render(request,'Main/contact.html')


def PRODUCT(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {
        'category':category,
        'product':product,
    }

    return render(request,'product/product.html',context)


def filter_data(request):
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts = allProducts.filter(Categories__id__in=categories).distinct()

    if len(brands) > 0:
        allProducts = allProducts.filter(Brand__id__in=brands).distinct()


    t = render_to_string('ajax/ajaxproduct.html',{'data':allProducts})

    return JsonResponse({'data': t})
    




@login_required(login_url="/account/my-account")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/my-account")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/account/my-account")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/my-account")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/account/my-account")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/account/my-account")
def cart_detail(request):
    cart = request.session.get('cart')
    packing_cost = sum(i['packing_cost'] for i in cart.values() if i)
    tax = sum(i['tax'] for i in cart.values() if i)
    
    context = {
        'packing_cost':packing_cost,
        'tax':tax,
    }
    return render(request, 'cart/cart.html')


def Checkout(request):
    return render(request,'checkout/checkout.html')



    






