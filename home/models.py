from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
# Create your models here.


class Logo(models.Model):
    header_logo = models.ImageField(upload_to='logos/header/', blank=True, null=True)
    footer_logo  = models.ImageField(upload_to='logos/footer/', blank=True, null=True)
    favicon = models.ImageField(upload_to='logos/favicon/', blank=True, null=True)

    def __str__(self):
        return f"Header: {self.header_logo } | Footer: {self.footer_logo }"

class CarouselItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images/')
    def __str__(self):
        return self.title

class Fact(models.Model):
    icon = models.ImageField(upload_to='fact_icons/')
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    about_image = models.ImageField(upload_to='about_images/', null=True, blank=True)
    description  = RichTextField()

    def __str__(self):
        return self.title

class AboutUsContent(models.Model):
    icon = models.ImageField(upload_to='about_icons/', null=True, blank=True)
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Service(models.Model):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    title = models.CharField(max_length=255)
    details = RichTextField()
    icon = models.ImageField(upload_to='service_icons/', null=True, blank=True)
    in_homepage = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)


    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='features/')

    def __str__(self):
        return self.title

class FeatureIcon(models.Model):
    title = models.CharField(max_length=255)
    highlighted_word = models.CharField(max_length=255, blank=True, null=True)
    icon = models.ImageField(upload_to='icons/')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    content = RichTextField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title

def validate_year(value):
    current_year = date.today().year
    if value > current_year:
        raise ValidationError(f"The year {value} cannot be in the future.")
class BusinessInfo(models.Model):
    site_name = models.CharField(max_length=255, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    copyright_year = models.PositiveIntegerField(default=date.today().year, null=True, blank=True,
                                                 validators=[validate_year],
                                                 help_text="Year for copyright (cannot be in the future).")
    instagram_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    messenger_link = models.URLField(blank=True, null=True, verbose_name="Messenger Link")
    twitter_link = models.URLField(blank=True, null=True, verbose_name="Twitter Link")
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    telegram_link = models.URLField(blank=True, null=True, verbose_name="Telegram Link")
    map_embed_location_link = models.TextField(default="")

    def __str__(self):
        return "Business Info"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Blog(models.Model):
    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs/')
    content = RichTextField()
    in_homepage =  models.CharField(max_length=3,choices=YES_NO_CHOICES,null=True)

    def __str__(self):
        return self.title

class SiteSettings(models.Model):
    gtm_id = models.CharField(max_length=20, blank=True, null=True,
                              help_text="Google Tag Manager ID (e.g., GTM-XXXXXX)")
    keywords = models.TextField(blank=True,null=True,help_text="Meta keywords for SEO, separated by commas.")
    description = models.TextField(blank=True,null=True,help_text="Meta description for SEO.")
    facebook_domain_verification_id = models.CharField(max_length=255,blank=True,null=True,
                                                       help_text="Facebook domain verification ID.")
    google_site_verification_id = models.CharField(max_length=255,blank=True,null=True,
                                                   help_text="Google site verification ID.")

    def __str__(self):
        return self.site_name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='brand_logos/')

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, related_name='products', on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='product_images/', default='product_images/default_product.jpg')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = RichTextField()

    def __str__(self):
        return self.name
