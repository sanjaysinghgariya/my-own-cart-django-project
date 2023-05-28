from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json

def index(request):

    allProds = []
    cat_prods = Product.objects.values("category", "product_id")
    cats = {item["category"] for item in cat_prods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n/4) + n//4)
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {"allProds":allProds}
    return render(request, "shop/newhomepage.html", params)
def searchMatch(query, item):
    sample = query.split()
    sample2 = item.desc.lower().split()
    print(sample2)
    print(sample)
    match = 0
    for k in sample:
        for j in sample:
            if k==j:
                match += 1
    print(match)
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower() or query in item.sub_category.lower():
        return True
    elif match >=4 :
        return True
    else:
        return False
def search(request):
    query = request.GET.get("search")
    allProds = []
    cat_prods = Product.objects.values("category", "product_id")
    cats = {item["category"] for item in cat_prods}
    for cat in cats:
        prod_temp = Product.objects.filter(category=cat)
        prod = [item for item in prod_temp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n/4) + n//4)
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {"allProds":allProds, "msg":""}
    if len(allProds) == 0 or len(query) < 4 :
        params = {"msg": "please make sure to enter relevent keywords search query"}
    return render(request, 'shop/search_results.html', params)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        Email = request.POST.get("email", "")
        # name = request.POST.get("name", "")
        Phone_number = request.POST.get("phone", "")
        Desc = request.POST.get("desc", "")
        print(name, Email, Phone_number, Desc)
        contact = Contact(name=name, Email=Email, phone=Phone_number, desc=Desc)
        contact.save()
        thank = True
        return render(request, 'shop/contactpagebackup.html', {"thank":thank})
    return render(request, 'shop/contactpagebackup.html')


def about(request):
    return render(request, 'shop/newaboutus.html')

def tracker(request):
        if request.method=="POST":
                OrderId = request.POST.get("OrderID", "")
                Email = request.POST.get("Email", "")
                print(f"OrderId{OrderId} Email:{Email}")
                try:
                    print("yaha1Pe ruk")

                    order = Orders.objects.filter(Order_id=OrderId, Email=Email)
                    print(order[0].items_jason)

                    if len(order) > 0:
                        print("Hello")
                        update = OrderUpdate.objects.filter(Order_id=OrderId)
                        updates = []

                        for item in update:
                            print(item)
                            updates.append({'text':item.update_desc, "time": item.time_stamp})
                            response = json.dumps({"status":"success", "updates":updates, "itemsJason":order[0].items_jason}, default=str)
                            print("response",response)
                        return HttpResponse(response)
                    else:
                        return HttpResponse('{"status":"No item"}')
                except Exception as e:
                   return HttpResponse('{"status":"success"}')
        return render(request, "shop/tracker.html")

def checkout(request):
    if request.method == "POST":
        items_jason = request.POST.get("itemsJason", "")
        name = request.POST.get("name", "")
        Email = request.POST.get("Email", "")
        phone = request.POST.get("phone", "")
        Address = request.POST.get("Address", "") + request.POST.get("Address2", "")
        city = request.POST.get("city", "")
        State = request.POST.get("State", "")
        zip_code = request.POST.get("zip_code", "")

        order = Orders(items_jason=items_jason, name=name, Email=Email, phone=phone, Address=Address, city=city, State=State, zip_code=zip_code)
        order.save()
        update = OrderUpdate(Order_id=order.Order_id, update_desc="The order has been Placed")
        update.save()
        thank = True
        id = order.Order_id

        return render(request,'shop/checkoutbackup.html', {"thank":thank, 'id':id})
    return render(request, 'shop/checkoutbackup.html')

def prodView(request, my_id):
    product = Product.objects.filter(product_id = my_id)
    print(product)
    return render(request, 'shop/productview.html', {"product":product[0]})

def returns_orders(request):
    return HttpResponse("<h2> the follwing items are your  order please select the order you want to return</h2>")

def grocery(request):
    return HttpResponse("<h1> you are in grocery Store selct your grocery items</h1>")

def product(request):
    my_product = Product.objects.all().values()
    template = loader.get_template('onlyforpractice.html')
    context = {
        'my_product': my_product,
    }
    return HttpResponse(template.render(context, request))
def Basic(request):
    return render(request, 'shop/Basic.html')
def onlyfortesting(request):
    products = Product.objects.all()
    for i in products:
        print(i.id)
