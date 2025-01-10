from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
# Create your models here.


class Logo(models.Model):
    header_logo = models.ImageField(upload_to='logos/header/', blank=True, null=True)
    footer_logo  = models.ImageField(upload_to='logos/footer/', blank=True, null=True)

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
    brief_details = models.TextField(null=True)
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
    title = models.CharField(max_length=255)
    brief_details = RichTextField(null=True)
    description = RichTextField()
    icon = models.ImageField(upload_to='service_icons/', null=True, blank=True)

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

def validate_year(value):
    current_year = date.today().year
    if value > current_year:
        raise ValidationError(f"The year {value} cannot be in the future.")


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('first', 'Completed Project'),
        ('second', 'Ongoing Project'),
    ]
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = RichTextField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title


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

    def __str__(self):
        return "Business Info"