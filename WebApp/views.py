from django.shortcuts import render,HttpResponse,redirect
from django.http import FileResponse

# Create your views here.
#two type of views
## function
## class

def home(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def properties(request):
    return render(request,'properties.html')
def property(request):
    return render(request,'property-details.html')
def insert(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact = request.POST.get('contact')
        print(name,contact)
    return render(request,'insert.html')

from .form import Userform
# def insert_form_data(requset):
#     form=UserForm()
#     if requset.method=="POST":
#         form=UserForm(requset.POST)
#         if form.is_valid():
#             name= form.cleaned_data['name']
#             contact=form.cleaned_data['contact']
#             model.name=name
#             model.contact=contact
#             model.save()
#             print(name,contact)
#     return render(requset,'insert_data.html',{'form':form})




def userdata(request,name="Guest"):
    return render(request,'userprofile.html',{'user':name})
def userdata(request,name="Guest"):   ## for single user
    detail=[name,'7982968404','Noida','BTech']  ## for single user
    details=[{'name':'Ankur', 'Contact':'978765444','address':'Delhi'},
             {'name':'Amit', 'Contact':'978765488','address':'Ghaziabad'},
             {'name':'Ankit', 'Contact':'978765466','address':'Pune'}]
    # return render(request,'userprofile.html',{'user_detail':detail})   ## for single user
    return render(request,'userprofile.html',{'user_detail':details})
# from.form import UserForm
# def insert_form_data(request):
#     form=Userform()
#     model=UserModel()
#     if request.method=="POST":
#         form=UserForm(request.POST)
#         if form.is _valid():
#             name=form.cleaned_data['name']
#             contact=form.changed_data['contact']
#             molde.name=name



# from.form import UserModel.............
from.form import userModelform

def insert_form_data(request):
    form=userModelform()

    if request.method=="POST":
        form=userModelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read_model')
    return render(request,'insert_data.html',{'form':form})


# from.models import UserModel
# from django.core.paginator import Paginator

def update_data(request,id):
    user=UserModel.objects.get(id=id)
    form=userModelform(instance=user)
    if request.method=="POST":
        form=userModelform(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('read_model')
    return render(request,'insert_data.html',{'form':form})


# def read_model_data(request):
#     data=UserModel.objects.all()
#     print(data.values())
#     return HttpResponse("Dta Received")

from.models import UserModel
from django.core.paginator import Paginator

def read_model_data(request,page_no=1):
    data=UserModel.objects.all()
    paginator=Paginator(data,10)
    page_obj=paginator.page(page_no)
    return render(request,'read_model_data.html',{'page_obj':page_obj})


def delete_data(request,id):
    user=UserModel.objects.get(id=id)
    user.delete()
    return redirect('read_model')

from .models import product
def products(request):
    products=product.objects.all()
    return render (request,'products.html',{'products':products})

from .form import Productmodelform
def upload_products(request):
    form=Productmodelform()
    if request.method=="POST":
        form=Productmodelform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product')
    return render(request,'upload_products.html',{'form':form})
def download(request,id=None):
    model=product.objects.get(id=id)
    return FileResponse(model.prod_img.open(),as_attachment=True,filename=model.prod_img.name)

def setcookies(request):
    response=HttpResponse("Cookies is Set")
    response.set_cookie('username','ducat123',max_age=30)
    response.set_cookie('password','ducat@123')
    return response

def getcookies(request):
    try:
        user=request.COOKIES.get('username')
        return HttpResponse("Hello"+user)
    except:
        return HttpResponse("User not found")


def setsession(request):
    request.session['sname']= 'ducat'
    request.session['semail']= 'info@ducatindia.com'
    return HttpResponse("session is set")


def getsession(request):
    company_name = request.session['sname']
    company_email = request.session['semail']
    return HttpResponse(company_name+" "+company_email)

    # username=request.COOKIES.get('username')
    # password=request.COOKIES.get('password')
    # return HttpResponse(f"Username is {username} and Password is {password}")
