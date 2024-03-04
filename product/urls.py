from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    
    # Carousel Data
    path('', views.store, name="store"),
    path('carousel/', views.carousel, name="carousel"),
    path('<slug:post>/', views.detail, name="detail"), 
       
    # Main
    
    path('category/', views.category, name="category"),
    path('brand/', views.brand, name="brand"),
    path('qualitys/', views.quality, name="quality"),
    path('subcategory/', views.subcategory, name="subcategory"),
    path('featured/', views.featured, name="featured"),
    # View
    path('products', views.product_view, name="product_view"),
    path('features', views.featured_view, name="featured_view"),
    path('categories', views.category_view, name="category_view"),
    path('subcategories', views.subcategory_view, name="subcategory_view"),
    path('brands', views.brand_view, name="brand_view"),
    path('qualities', views.quality_view, name="quality_view"),
  
    # Filter
     
    
    path('brand/<str:slug>', views.brand_filter, name="brand_filter"),
    path('category/<str:slug>', views.category_filter, name="category_filter"),
    path('subcategory/<str:slug>', views.subcategory_filter, name="subcategory_filter"),
    path('quality/<str:slug>', views.quality_filter, name="quality_filter"),
    
]
