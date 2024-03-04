from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField

def user_directory_path(instance, filename):
    return 'static/products{0}/{1}'.format(instance.id, filename)

# Carousel Data


class Carousel(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='Published')

    options = (
        ('Draft', 'draft'),
        ('Published', 'published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    link = models.CharField(max_length=250, null=True, blank=False)
    thumbnail = models.ImageField(upload_to=user_directory_path, blank=False)
    publish = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='carousel_posts')
    status = models.CharField(max_length=10, choices=options, default='draft')
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


# Carousel Data End
class Category(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='Published')
    options = (
        ('Draft', 'draft'),
        ('Published', 'published'),
    )
    thumbnail = models.ImageField(upload_to=user_directory_path)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager
    status = models.CharField(max_length=10, choices=options, default='draft')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='Published')
    options = (
        ('Draft', 'draft'),
        ('Published', 'published'),
    )
    category = models.ForeignKey(
        Category, max_length=250, on_delete=models.PROTECT, default=1)
    thumbnail = models.ImageField(upload_to=user_directory_path)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager
    status = models.CharField(max_length=10, choices=options, default='draft')

    def __str__(self):
        return self.name


class Quality(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='Published')
    options = (
        ('Draft', 'draft'),
        ('Published', 'published'),
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager
    status = models.CharField(max_length=10, choices=options, default='draft')

    def __str__(self):
        return self.name


class Brand(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='Published')
    options = (
        ('Draft', 'draft'),
        ('Published', 'published'),
    )
    thumbnail = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager
    status = models.CharField(max_length=10, choices=options, default='draft')

    def __str__(self):
        return self.name


class Product(models.Model):
    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='Published')
    options = (
        ('Draft', 'draft'),
        ('Published', 'published'),
    )
    category = models.ForeignKey(
        Category, max_length=250, on_delete=models.PROTECT, default=1, blank=False)
    brand = models.ForeignKey(Brand, max_length=250,
                              on_delete=models.PROTECT, default=1, blank=False)
    quality = models.ForeignKey(
        Quality, max_length=250, on_delete=models.PROTECT, default=1, blank=False)
    subcategory = models.ForeignKey(
        SubCategory, related_name='variants', on_delete=models.CASCADE, blank=False, null=True)

    # Product data and Detail
    title = models.CharField(max_length=500, unique=True)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    sku = models.CharField(max_length=500, unique=True, null=True)

    # Images Data
    thumbnail = models.ImageField(upload_to=user_directory_path, blank=False)
    image1 = models.ImageField(upload_to=user_directory_path, blank=False)
    image2 = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True)
    image3 = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True)
    image4 = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True)
    image5 = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True)
    
    video = models.FileField(
        upload_to=user_directory_path, null=True, blank=True)

    # Product details Section data

    sale = models.BooleanField(default=False)
    # Publish data
    publish = models.DateTimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='product_posts')
    created_at = models.DateTimeField(auto_now_add=True)

    # status log
    bestoffer = models.BooleanField(default=False)
    on_stock = models.BooleanField(default=False)

    status = models.CharField(max_length=10, choices=options, default='draft')

    featured = models.BooleanField(default=False)
    compare = models.ManyToManyField(
        User, related_name='compare', default=None, blank=True)

    objects = models.Manager()  # default manager
    newmanager = NewManager()  # custom manager

    def get_absolute_url(self):
        return reverse('product:detail', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Description(models.Model):
    post = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE, related_name='product_description')
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
