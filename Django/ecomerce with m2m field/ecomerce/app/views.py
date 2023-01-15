from django.shortcuts import render,redirect
from django.views import View
from .models import Product, Customer, Cart, OrderPlaced
from .forms import customerRegistrationForm,CoustomerProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from  django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required # this is for function based view
from django.utils.decorators import method_decorator # this for a class based view


# def home(request):
#  return render(request, 'app/home.html')
class HomeView(View):
    def get(self, request):
        total_item = 0
        topwears = Product.objects.filter(category = 'TW')
        bottomwears = Product.objects.filter(category = 'BW')
        mobile = Product.objects.filter(category = 'M')
        if request.user.is_authenticated:
            total_item = len(Cart.objects.filter(user=request.user))
            # print(total_item)
        return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'mobile':mobile, 'total_item' : total_item})


# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class customerRegistrationView(View):
    def get(self, request):
        form = customerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form' : form})
    # def post(self, request):
    #     form = customerRegistrationForm(request.POST)
    #     if form.is_valid():
    #         messages.success(request, 'Congratulations|Registered sucessfully!!')
    #         form.save()
    #     return render(request, 'app/customerregistration.html', {'form' : form})

    def post(self, request):
        form = customerRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            fname = first_name.capitalize()
            email = form.cleaned_data['email']
            Password1 = form.cleaned_data['password1']
            Password2 = form.cleaned_data['password2']
            User.objects.create_user(username=username, first_name=fname, email=email, password =Password1)
            messages.success(request, 'Congratulations|Registered sucessfully!!')
        return render(request, 'app/customerregistration.html', {'form' : form})


# def profile(request):
#  return render(request, 'app/profile.html')
# @method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class ProfileView(View):
    def get(self, request):
        total_item = 0
        if request.user.is_authenticated:
            total_item = len(Cart.objects.filter(user=request.user))
        form = CoustomerProfileForm()
        return render(request, 'app\profile.html', {'form' : form, 'active' : 'btn btn-primary', 'total_item' : total_item})
    
    def post(self, request):
        total_item = 0
        if request.user.is_authenticated:
            total_item = len(Cart.objects.filter(user=request.user))
        form = CoustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            Customer.bojects.create(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            messages.success(request, "Congratulation !! Your Data Saved Sucessfully")
        return render(request, 'app\profile.html', {'form' : form, 'active' : 'btn btn-primary', 'total_item' : total_item})


def address(request):
    total_item = 0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
    add = Customer.objects.filter(user = request.user)
    return render(request, 'app/address.html', {'add' : add, 'active' : 'btn btn-primary', 'total_item' : total_item})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')
# @method_decorator(login_required(login_url='/accounts/login'), name='dispatch')
class ProductDetailsView(View):
    def get(self, request, pk):
        total_item = 0
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            total_item = len(Cart.objects.filter(user=request.user))
            item_already_in_cart = Cart.objects.filter(product=product ,user=request.user).exists()
            print(item_already_in_cart)
        return render(request, 'app/productdetail.html', {'product':product, 'item_already_in_cart' : item_already_in_cart, 'total_item' : total_item})


def mobile(request, data=None):
    total_item = 0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
    if data == None:
        mobiles = Product.objects.filter(category='M')
    elif data == 'One_plus' or data == 'Apple' or data == 'Samsung' or data == 'Redmi':
        mobiles = Product.objects.filter(category='M').filter(brand=data)
    elif data == 'Below':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__lt=10000)
    elif data == 'Above':
        mobiles = Product.objects.filter(category='M').filter(discounted_price__gt=10000)
    return render(request, 'app/mobile.html', {'mobiles':mobiles, 'total_item' : total_item})


def top_wear(request, data=None):
    total_item = 0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
    # import pdb ; pdb.set_trace()
    if data == None:
        topwear = Product.objects.filter(category='TW')
    elif data == 'Monte_Carlo' or data == 'allen_solly' or data == 'lee' or data == 'US_polo':
        topwear = Product.objects.filter(category='TW').filter(brand=data)
    elif data == 'Below':
        topwear = Product.objects.filter(category='TW').filter(discounted_price__lt=1000)
    elif data == 'Above':
        topwear = Product.objects.filter(category='TW').filter(discounted_price__gt=1000)
    return render(request, 'app/topwear.html', {'topwear':topwear, 'total_item': total_item})


def bottom_wear(request, data=None):
    total_item = 0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
    if data == None:
        bottomwear = Product.objects.filter(category='BW')
    elif data == 'Monte_Carlo' or data == 'Van_Heusen' or data == 'lee' or data == 'Pepe_Jeans':
        bottomwear = Product.objects.filter(category='BW').filter(brand=data)
    elif data == 'Below':
        bottomwear = Product.objects.filter(category='BW').filter(discounted_price__lt=900)
    elif data == 'Above':
        bottomwear = Product.objects.filter(category='BW').filter(discounted_price__gt=900)
    return render(request, 'app/bottomwear.html', {'bottomwear':bottomwear, 'total_item' : total_item})


@login_required(login_url='/accounts/login')
def buy_now(request):
 return render(request, 'app/buynow.html')


@login_required(login_url='/accounts/login')
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id') # we take prod_id from productdetails.html page while choosing any for addimg to cart
    product = Product.objects.get(id=product_id)
     
    if Cart.objects.filter(user = user).exists():
           temp = Cart.objects.filter(user = user)
           import pdb;pdb.set_trace()
           nm = Cart(user=user)
           nm.product.set([product])
    else:
        c =Cart.objects.create(user=user) 
        c.product.set([product]) # here we set a
    return redirect('/cart')

@login_required(login_url='/accounts/login')
def show_cart(request):
    total_item = 0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
        user = request.user
        cart = Cart.objects.filter(user=user) # cart of particular user so we get objects from cart of particular user
        # print(cart)#this will give objects of Cart model in the form of query set
        # for i in cart:
        #     for x in i.product.values():
        #         print(x)
            
        # import pdb;pdb.set_trace()
        amount = 0.0
        shipping_charges = 70.0
        total_amount = 0.0
        # import pdb;pdb.set_trace()
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        # product_details = Product.objects.all() 
        # print(product_details)
        # print("line")
        # for pd in product_details:
        #     print(pd)
        # print(cart_product)# this will give objects of Cart in the form of list
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity ) * (p.product.values('discounted_price')).get().get("discounted_price")
                # import pdb;pdb.set_trace()
                amount += tempamount
                total_amount = amount+shipping_charges
            return render(request, 'app/addtocart.html', {'carts' : cart, 'total_amount': total_amount, 'amount' : amount, 'total_item' : total_item})
        else:
            return render(request, 'app\emptycart.html')

# @login_required(login_url='/accounts/login')
def plus_cart(request):
    if request.method == "GET":
        # import pdb;pdb.set_trace()
        prod_id = request.GET['prod_id'] # we take prod_id from productdetails.html page while choosing any for addimg to cart
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1 
        c.save()
        amount = 0.0
        shipping_charges = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity ) * (p.product.values('discounted_price')).get().get("discounted_price")
            amount += tempamount
            total_amount = amount+shipping_charges

        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : total_amount
        }
        return JsonResponse(data)

# @login_required(login_url='/accounts/login')
def minus_cart(request):
    if request.method == "GET":
        # import pdb;pdb.set_trace()
        prod_id = request.GET['prod_id'] # We Get prod_id From A productdetail.html page
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_charges = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity ) * (p.product.values('discounted_price')).get().get("discounted_price")
            amount += tempamount
            total_amount = amount+shipping_charges

        data = {
            'quantity' : c.quantity,
            'amount' : amount,
            'totalamount' : total_amount
        }
        return JsonResponse(data)

# @login_required(login_url='/accounts/login')
def remove_cart(request):
    if request.method == "GET":
        # import pdb;pdb.set_trace()
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_charges = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity ) * (p.product.values('discounted_price')).get().get("discounted_price")
            amount += tempamount
            total_amount = amount+shipping_charges

        data = {
            'amount' : amount,
            'totalamount' : total_amount
        }
        return JsonResponse(data)



def checkout(request):
    # import pdb;pdb.set_trace()
    total_item = 0
    user = request.user
    add = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    # for prod_detail in cart_items:
    #     prod = prod_detail.product.values()
    #     print(prod)
    # # import pdb;pdb.set_trace()    
    amount = 0.0
    shipping_charges = 70.0
    totalamount = 0.0
    if request.user.is_authenticated:
        total_item = len(Cart.objects.filter(user=request.user))
    cart_product = [p for p in cart_items if p.user == user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity ) * (p.product.values('discounted_price')).get().get("discounted_price")
            amount += tempamount
        totalamount = amount+shipping_charges         
        return render(request, 'app/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_items' : cart_items, 'total_item' : total_item})
    else:
        return HttpResponse("Please add some item to the cart hit back button")


@login_required(login_url='/accounts/login')
def payment_done(requset):
    user = requset.user
    custid = requset.GET.get('custid') # to get "custid" (from-"checkout.html") from GET request from webpage id get from selected radio button
    customer = Customer.objects.get(id=custid)  ## we get a particular user on the basis of custid for ordered placed
    cart = Cart.objects.filter(user=user) # then we filter the current user who is login the products which he/she carted in the we get those product
    # for cart_product in cart.product.ob
    cart_product_tosave = []
    cart_product_todelete = []
    for i in cart: # We applied loop here because if user is stored multiple items in carts then we get all elements
        crt = OrderPlaced(user=user, customer=customer, quantity=i.quantity) # saving data in model
        for x in i.product.all():
            cart_product_tosave.append(x.id)
        # crt.save()
        # crt.product.set([p_id])
        cart_product_todelete.append(i)
        # i.delete() # delete saved product from cart model
    # import pdb;pdb.set_trace()
    crt.save()
    crt.product.set(cart_product_tosave)
    for j in cart_product_todelete:
        j.delete()
    # for x in cart_product_tosave:
    #     print(x.id)
    #     crt.product.set([x])
    # import pdb;pdb.set_trace()
    return redirect("orders")

# def payment_done(requset):
#     user = requset.user
#     custid = requset.GET.get('custid') # to get "custid" (from-"checkout.html") from GET request from webpage id get from selected radio button
#     customer = Customer.objects.filter(id=custid)  ## we get a particular user on the basis of custid for ordered placed
#     cart = Cart.objects.filter(user=user) # then we filter the current user who is login the products which he/she carted in the we get those product
#     import pdb;pdb.set_trace()
#     # for c in customer:
#     #     print(c.name)
#     for (c,c1) in zip(cart,customer): # We applied loop here because if user is stored multiple items in carts then we get all elements
#         import pdb;pdb.set_trace()  
#         OrderPlaced.objects.create(user=user, customer=c1.name, product=c.product, quantity=c.quantity) # saving data in model
#         c.delete() # delete saved product from cart model
#     return redirect("orders")


@login_required(login_url='/accounts/login')
def orders(request):
    prod_last_prize = []
    total_item = 0
    order_placed = OrderPlaced.objects.filter(user=request.user)
    for x in order_placed:
        prod_quan = x.quantity
        for i in x.product.values():
            k=i['discounted_price']
            last_cost = prod_quan*k
            prod_last_prize.append(last_cost)
    # import pdb;pdb.set_trace()
    # if request.user.is_authenticated:
    #     total_item = len(Cart.objects.filter(user=request.user))
    # last_cost = prod_last_prize
    return render(request, 'app/orders.html', {'order_placed' : order_placed, 'last_cost' : prod_last_prize})
    # mylist = zip(order_placed, prod_last_prize)
    # for i,j in mylist:
    #     print(i,j)
    #     # import pdb;pdb.set_trace()
    # context = {
    #     'mylist' : mylist,
    # }
    # return render(request, 'app/orders.html', context)
    # import pdb;pdb.set_trace()

    # id = OrderPlaced.obj
    # ects.values_list('product')
    # # print(id)
    # for i in id:
    #     dp= Product.objects.get(id=i[0])
    #     fp = dp.discounted_price
    #     print(fp)