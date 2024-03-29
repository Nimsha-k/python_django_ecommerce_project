from django.urls import path

from . import views
app_name='ecommerce_app'
urlpatterns=[
    path("",views.allProducts,name="allProducts"),
    path('<slug:c_slug>/', views.allProducts, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='product_category_detail'),

]