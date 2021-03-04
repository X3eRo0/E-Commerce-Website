from django.shortcuts import render
from image_data.models import Product
from django.views.generic import ListView
# Create your views here.
class SearchProductListView(ListView):
     template_name='products/list.html'
     def get_context_data(self,*args,**kwargs):
          context=super(SearchProductListView,self).get_context_data(*args,**kwargs)
          context['query']=self.request.GET.get('q')
          return context
     def get_queryset(self,*args,**kwargs):
          request=self.request
          method_dict=request.GET
          print(request.GET)
          query=method_dict.get('q',None)
          print(query)
          if query is not None:
               
               return Product.objects.filter(title__icontains=query)
          return Product.objects.none()
