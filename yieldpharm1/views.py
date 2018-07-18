from django.shortcuts import render
from yieldpharm1.models import Category,Product
from django.db.models import F,Q

# Create your views here.


def index(request):
    category_list=Category.objects.all()
    # print(category_list)
    return render(request,'yieldpharm1/index.html',{'category_list':category_list})

def ydclass(request,ydclass_id):
    category_list = Category.objects.all()
    product_list=Product.objects.filter(category_id=ydclass_id)
    return render(request,'yieldpharm1/ydclass.html',{'product_list':product_list,'category_list':category_list})

def detail(request,product_id):
    category_list = Category.objects.all()
    product=Product.objects.get(pk=product_id)
    # print(category_list)
    return render(request,'yieldpharm1/detail.html',{'product':product,'category_list':category_list})

def search(request):
    category_list = Category.objects.all()
    search_text=request.POST.get('search_text')
    product_list=Product.objects.filter(Q(name__icontains=search_text)|Q(cas_no__icontains=search_text))
    # print(search_text,product_list)
    return render(request,'yieldpharm1/search.html',{'product_list':product_list,'category_list':category_list})

def aboutus(request):
    category_list = Category.objects.all()
    return render(request, 'yieldpharm1/aboutus.html', {'category_list': category_list})

def contactus(request):
    category_list = Category.objects.all()
    return render(request, 'yieldpharm1/contactus.html', {'category_list': category_list})

def products(request):
    category_list = Category.objects.all()
    product_list = Product.objects.all()
    return render(request, 'yieldpharm1/products.html', {'product_list': product_list, 'category_list': category_list})

def lab(request):
    category_list = Category.objects.all()
    return render(request, 'yieldpharm1/lab.html', {'category_list': category_list})

def news(request):
    category_list = Category.objects.all()
    return render(request, 'yieldpharm1/news.html', {'category_list': category_list})

def feedback(request):
    category_list = Category.objects.all()
    return render(request, 'yieldpharm1/feedback.html', {'category_list': category_list})

def indexen(request):
    category_list = Category.objects.all()
    # print(category_list)
    return render(request, 'yieldpharm1/en/index.html', {'category_list': category_list})

def aboutusen(request):
    category_list = Category.objects.all()
    return render(request, 'yieldpharm1/en/aboutus.html', {'category_list': category_list})

def contactusen(request):
    category_list = Category.objects.all()
    return render(request, 'yieldpharm1/en/contactus.html', {'category_list': category_list})

def productsen(request):
    category_list = Category.objects.all()
    product_list = Product.objects.all()
    return render(request, 'yieldpharm1/en/products.html', {'product_list': product_list, 'category_list': category_list})

def laben(request):
    category_list = Category.objects.all()
    return render(request, 'yieldpharm1/en/lab.html', {'category_list': category_list})

def newsen(request):
    category_list = Category.objects.all()
    return render(request, 'yieldpharm1/en/news.html', {'category_list': category_list})

def feedbacken(request):
    category_list = Category.objects.all()
    return render(request, 'yieldpharm1/en/feedback.html', {'category_list': category_list})

def ydclassen(request,ydclass_id):
    category_list = Category.objects.all()
    product_list = Product.objects.filter(category_id=ydclass_id)
    return render(request, 'yieldpharm1/en/ydclass.html', {'product_list': product_list, 'category_list': category_list})

def detailen(request,product_id):
    category_list = Category.objects.all()
    product = Product.objects.get(pk=product_id)
    # print(category_list)
    return render(request, 'yieldpharm1/en/detail.html', {'product': product, 'category_list': category_list})

def searchen(request):
    category_list = Category.objects.all()
    search_text=request.POST.get('search_text')
    product_list=Product.objects.filter(Q(name__icontains=search_text)|Q(cas_no__icontains=search_text))
    # print(search_text,product_list)
    return render(request,'yieldpharm1/en/search.html',{'product_list':product_list,'category_list':category_list})

