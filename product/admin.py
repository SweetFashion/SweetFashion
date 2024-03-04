from django.contrib import admin
from . import models
from embed_video.admin import AdminVideoMixin
# multi data from backend.- Viewing
from .models import Product, Description, Category, SubCategory, Carousel


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


class DescriptionAdmin(admin.StackedInline):
    model = Description


@admin.register(Product)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [DescriptionAdmin]
    list_display = ('sku', 'brand', 'quality', 'on_stock', 'sale', 'bestoffer', 'category', 'subcategory', 'id', 'featured', 'status',
                    'title', 'author', 'publish')
    list_editable = ('status', 'featured', 'on_stock', 'sale', 'bestoffer',)
    prepopulated_fields = {
        "slug": ("title",),
    }
    search_fields = ['sku', 'category__name',
                     'on_stock', 'brand__name', 'title', 'id',]


@admin.register(Carousel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    prepopulated_fields = {
        "slug": ("title",),
    }
    
    
@admin.register(Category)  # done
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'status')
    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(SubCategory)  # done
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status')
    prepopulated_fields = {
        "slug": ("name",),
    }
    search_fields = ['name', 'category' 'status']


@admin.register(models.Quality)  # done
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(models.Brand)  # done
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    prepopulated_fields = {
        "slug": ("name",),
    }
