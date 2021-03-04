from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from django.contrib.auth import authenticate,login,get_user_model
from django.http import Http404
from django.contrib import auth
# Create your views here.
from .models import Product
from .forms import LoginForm,RegisterForm
from django.contrib.auth.models import User
from carts.models import Cart
class ProductListView(ListView):
    queryset=Product.objects.all()
    template_name='products/list.html'
    def get_context_data(self,*args,**kwargs):
        
        context=super(ProductListView,self).get_context_data(*args,**kwargs)
        print(context)
        return context

    def get_queryset(self,*args,**kwargs):
        request=self.request
        pk=self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)
         

def product_list_view(request):
    queryset=Product.objects.all()
    print(queryset)
    context={'object_list': queryset}

    return render(request,'products/list.html',context)

class ProductDetailSlugView(DetailView):
    queryset=Product.objects.all()
    template_name='products/detail.html'
    def get_context_data(self,*args,**kwargs):
        context=super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
        request=self.request
        cart_obj,new_obj=Cart.objects.new_or_get(request)
        context['cart']=cart_obj
        return context
    def get_object(self,*args,**kwargs):
        
        request=self.request
        slug=self.kwargs.get('slug')
        #instance=get_object_or_404((Product,slug=slug,active=True)
        try:
            instance=Product.objects.get(slug=slug)
        except Product.DoesNotExist:
            raise Http404("Not found")
        except Product.MultipleObjectsReturned:
            qs=Product.objects.filter(slug=slug,active=True)
            instance=qs.first()
        return instance
    
            
         
        #return Product.objects.filter(pk=pk)
   
     
class ProductDetailView(DetailView):
    queryset=Product.objects.all()
    template_name='products/detail.html'
    def get_context_data(self,*args,**kwargs):
        context=super(ProductDetailView,self).get_context_data(*args,**kwargs)
        print(context)
        return context

    def get_object(self,*args,**kwargs):
        request=self.request
        pk=self.kwargs.get('pk')
        instance=Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance
        #return Product.objects.filter(pk=pk)
   

def product_detail_view(request,pk=None,*args,**kwargs):
    qs=Product.objects.filter(id=pk)
    if qs.exists() and qs.count()==1:
        instance=qs.first()
    else:
        
        raise Http404("Product does not exist")
    
    instance=get_object_or_404(Product,pk=pk)
    
    context={'object': instance}
    
    
    return render(request,'products/detail.html',context)



def register(request):
     if request.method=='POST':
          print('submitted reg')
          first_name=request.POST['first_name']
          last_name=request.POST['last_name']
          username=request.POST['username']
          email=request.POST['email']
          password=request.POST['password']
          password2=request.POST['password2']
          if password==password2:
               if User.objects.filter(username=username).exists():
                    #message.error(request,'That username is already taken')
                    return redirect('register')
               
               else:
                    if User.objects.filter(email=email).exists():
                         return redirect('register')
                    else:
                         user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                         print(user)
                         user.save()
                         return redirect('login')
                         
     return render(request,'registration/signup.html')


def login(request):
     if request.method=='POST':
          username=request.POST['username']
          password=request.POST['password']

          user=auth.authenticate(username=username,password=password)

          if user is not None:
               auth.login(request,user)
               return redirect('product')
          else:
               return redirect('login')
     
     return render(request,'registration/login.html')

from django.contrib import auth


def logout(request):
    auth.logout(request)
    return render(request,'products/logout.html')
