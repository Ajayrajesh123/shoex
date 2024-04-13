from django.urls import path
from . import views
app_name='seller'
urlpatterns=[
    path('',views.Home,name='home'),
    path('seller_login/',views.seller_login,name='seller_login'),
    path('seller_dashboard/',views.seller_dashboard,name='seller_dashboard'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('views_products/',views.views_products,name='views_products'),
    path('delete_product/<int:product_id>',views.delete_product,name='delete_product'),
    path('product_updates/<int:product_id>',views.product_updates,name='product_updates')
]