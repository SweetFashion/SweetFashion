from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages

# Carousel Data


def carousel(request):
    carousel = Carousel.newmanager.all()
    return render(request, 'store/carousel.html', {'carousel': carousel, })


# Store Data
def store(request):
    featured = Product.objects.filter(featured=True).order_by('-id')
    subcategory = SubCategory.objects.all()
    carousel = Carousel.objects.all()
    category = Category.objects.all()
    quality = Quality.objects.all()
    brand = Brand.objects.all()
    all_posts = Product.newmanager.all()
    return render(request, 'store/store.html', {
        'posts': all_posts,
        'category': category,
        'quality': quality,
        'brand': brand,
        'carousel': carousel,
        'subcategory': subcategory,
        'featured': featured,
    })


def detail(request, post):
    post = get_object_or_404(Product, slug=post, status='Published')
    compare = bool
    if post.compare.filter(id=request.user.id).exists():
        compare = True
    
    description = Description.objects.filter(post=post)
    related = Product.objects.filter(
        category=post.category).exclude(slug=post.slug)[:8]
    return render(request, 'store/detail.html', {'post': post,
                                                 'related': related,
                                                 'description': description,
                                                 'compare': compare,

                                                 })



# Main
def featured(request):
    featured = Product.objects.filter(featured=True)
    return render(request, 'store/section/featured.html', {'featured': featured})


def quality(request):
    quality= Quality.objects.all()
    return render(request, 'store/section/quality.html', {'quality': quality})


def category(request):
    category = Category.objects.all()
    return render(request, 'store/section/category.html', {'category': category})


def subcategory(request):
    subcategory = SubCategory.objects.all()
    return render(request, 'store/section/subcategory.html', {'subcategory': subcategory})

 
def brand(request):
    brand = Brand.objects.all()
    return render(request, 'store/section/brand.html', {'brand': brand})
 
# List View
def featured_view(request):
    featured_view = Product.objects.filter(featured=True).order_by('-id') 
    return render(request, 'store/views/featured_view.html', {'featured_view': featured_view})

  
def product_view(request):
    product_view = Product.newmanager.all()
    return render(request, 'store/views/product_view.html', {'product_view': product_view})


def category_view(request):
    category_view = Category.newmanager.all()
    return render(request, 'store/views/category_view.html', {'category_view': category_view})


def subcategory_view(request):
    subcategory_view = SubCategory.newmanager.all()
    return render(request, 'store/views/subcategory_view.html', {'subcategory_view': subcategory_view})


def brand_view(request):
    brand_view = Brand.newmanager.all()
    return render(request, 'store/views/brand_view.html', {'brand_view': brand_view})


def quality_view(request):
    quality_view = Quality.newmanager.all()
    return render(request, 'store/views/quality_view.html', {'quality_view': quality_view})

 

 

# List Filter
   
def quality_filter(request, slug):
    quality = Quality.objects.filter(slug=slug).first()
    if (Quality.objects.filter(slug=slug)):
        product = Product.objects.filter(quality__slug=slug)
        quality_name = Quality.objects.filter(slug=slug).first()
        context = {'product': product,
                   'quality_name': quality_name, 'quality': quality, }
        return render(request, "store/filter/quality_filter.html", context)
    else:
        messages.warning(request, "no such quality found")
        return redirect('product')


def brand_filter(request, slug):
    brand = Brand.objects.filter(slug=slug).first()
    if (Brand.objects.filter(slug=slug)):
        product = Product.objects.filter(brand__slug=slug)
        brand_name = Brand.objects.filter(slug=slug).first()
        context = {'product': product, 'brand_name': brand_name,
                   'brand': brand, }
        return render(request, "store/filter/brand_filter.html", context)
    else:
        messages.warning(request, "no such brand found")
        return redirect('product')


def category_filter(request, slug):
    featured = Product.objects.filter(featured=True).order_by('-id').filter(category__slug=slug)[:8]
    subcategory = SubCategory.objects.filter(category__slug=slug).order_by('-id')
    category = Category.objects.filter(slug=slug).first()
    if (Category.objects.filter(slug=slug)):
        product = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {'product': product, 'category_name': category_name,
                   'subcategory': subcategory, 'category': category, 'featured': featured, }
        return render(request, "store/filter/category_filter.html", context)
    else:
        messages.warning(request, "no such category found")
        return redirect('product')



def subcategory_filter(request, slug):
    subcategory = SubCategory.objects.filter(slug=slug).first()
    if (SubCategory.objects.filter(slug=slug)):
        product = Product.objects.filter(subcategory__slug=slug)
        subcategory_name = SubCategory.objects.filter(slug=slug).first()
        context = {'product': product, 'subcategory_name': subcategory_name,
                   'subcategory': subcategory, }
        return render(request, "store/filter/subcategory_filter.html", context)
    else:
        messages.warning(request, "no such subcategory found")
        return redirect('product')
