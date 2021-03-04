
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from carts.views import cart_home,cart_update
from search.views import SearchProductListView
from image_data.views import product_list_view,ProductListView,ProductDetailView,product_detail_view,ProductDetailSlugView,login,register,logout
    
urlpatterns=[
        url(r'^admin/', admin.site.urls),
        url(r'^product/(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view(),name='index'),
        url(r'^$',product_list_view,name='product'),
        url(r'^search/',SearchProductListView.as_view(),name='query'),
        url(r'^search/',SearchProductListView.as_view(),name='query'),
        url(r'^cart/', cart_home,name='cart'),
        url(r'^update/', cart_update,name='update'),
        
        url(r'^signup',register,name='register'),
        url(r'^login',login,name='login'),
        url(r'^logout',logout,name='logout'),
    ]
    
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

