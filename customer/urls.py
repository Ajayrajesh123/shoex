from django.urls import path
from.import views
app_name='customer'
urlpatterns=[
    path('',views.Index,name='index'),
    path('login/',views.Login,name='login'),
    path('signup/',views.Signup,name='signup'),
    path('customer_dashboard/',views.customer_dashboard,name='customer_dashboard'),
    path('cart/',views.cart,name='cart'),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('logout/',views.logout,name='logout'),
    path('search/',views.search,name='search'),
    path('all_collection/',views.all_collection,name='all_collection'),
    path('payment/',views.payment,name='payment'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact')

    
]