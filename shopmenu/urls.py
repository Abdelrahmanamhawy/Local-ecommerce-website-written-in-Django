from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/?$', views.login, name='login'),
    url(r'^logout/?$', views.logout, name='logout'),
    url(r'^home/?$',views.home, name='home'),
    url(r'^signup/?$', views.signup, name='signup'),
    url(r'^details/?$',views.details,name='details'),
    url(r'^addproductitem/?$',views.addproductitem,name='addproductitem'),
    url(r'^addProduct/?$',views.addProduct,name='addProduct'),
    url(r'^shops/(?P<shopname>[a-zA-Z0-9\s]+)/?$',views.shopview,name='shopview'),
    # url(r'^search/?$',views.search,name='search'),
     url(r'^savedetails/?$',views.editDetails,name='editDetails'),
    # url(r'^cart/?$',views.cart,name='cart'),
    # url(r'^history/?$',views.history,name='history'),
    # url(r'^addtocart/?$',views.saveToCart,name='saveToCart'),

    # url(r'^resthistory/?$',views.restaurantOrderHistory,name='resthistory'),
    # url(r'^delivered/?$',views.delivered,name='delivered'),

    # url(r'^removefooditem/?$',views.removefooditem,name='removefooditem'),
    #
    # # url(r'^makepaymenet/?$'.views.makepaymenet,name='makepaymenet'),

    # url(r'^about/?$',views.about,name='about'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
