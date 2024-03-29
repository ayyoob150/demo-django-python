from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from service.models import Product
from django.core.paginator import Paginator
from service.serializers import ProductSerializer
# form get post crfs
# https redirect , shortcuts redirect

# {{% url 'home' as url}}
# useform a way in django to make inputs forms

def homePage(request):
    searchKey=''
    dataInserted = ''
    productData = Product.objects.all()
    paginator = Paginator(productData,3)
    pageNumber= request.GET.get('page')
    dataOnPage= paginator.get_page(pageNumber)
    lastPage= dataOnPage.paginator.num_pages
    if request.method == 'GET':
        searchKey = request.GET.get('searchProduct')
        if searchKey != None :
            dataOnPage = Product.objects.filter(name__icontains=searchKey)
    # for a in productData:
    #     print(a.name)
    
    # data = {
    #     'list':[
    #     {'name':'abc'},
    #     {'name':'cde'},
    #     {'name':'e'},
    #     {'name':'ff'},
    #     {'name':'g'},
    #     {'name':'hh'},
    # ]}
    
    if request.method == 'POST':
        name = request.POST.get('pName')
        price = request.POST.get('price')
        description = request.POST.get('description')
        insertInProduct = Product(name=name,price=price,description=description)
        insertInProduct.save()
        dataInserted = 'Data Inserted'
    data={'product':dataOnPage,
          'searchKey':searchKey,
          'lastPage':lastPage,
          'totalPageList':[n+1 for n in range(lastPage)],
          'dataInserted':dataInserted
          }    
    try:
        
        if request.method == "POST":
            n1=request.POST.get("name")
            n2=request.POST['pass']
            # n2=request.POST.get("pass")
            data={'name':n1,'pass':n2}
            print("ghii",data)
            
    except:
        pass
    return render(request,'index.html',data)

def about(request,id):
    productDetail = Product.objects.get(id=id)
    return render(request,'about.html',{'productDetail':productDetail})

def about_us(request):
    pro = Product.objects.all()
    return JsonResponse({'pro':pro},safe=False)

def calculator(request):
    c=''
    try:
        if request.method == "POST" :
            num1 = eval(request.POST.get('num1'))
            num2 = eval(request.POST.get('num2'))
            opr = request.POST.get('operator')
            if opr == '+':
                c=num1+num2
            elif opr == '-':
                c=num1-num2
            elif opr == '*':
                c=num1*num2
            elif opr == '/':
                c=num1/num2
    except:
        c='invalid inputs'
    return render(request,'calculator.html',{'op':c})

def delete(request,id):
    delPro=Product.objects.get(id=id)
    delPro.delete()
    return redirect('home')

def product(request):
    product = Product.objects.all()
    proSerializer = ProductSerializer(product,many=True)
    return JsonResponse(proSerializer.data, safe=False)
    
    