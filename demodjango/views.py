from django.http import HttpResponse
from django.shortcuts import render
# form get post crfs
# https redirect , shortcuts redirect

# {{% url 'home' as url}}
# useform a way in django to make inputs forms

def homePage(request):
    # data = {
    #     'list':[
    #     {'name':'abc'},
    #     {'name':'cde'},
    #     {'name':'e'},
    #     {'name':'ff'},
    #     {'name':'g'},
    #     {'name':'hh'},
    # ]}
    data={}
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

def about(request):
    return render(request,'about.html')

def about_us(request):
    return HttpResponse('hi there')

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

    