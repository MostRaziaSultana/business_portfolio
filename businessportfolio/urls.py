from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from home.views import *
from authority import urls as authority_urls

urlpatterns = [
    path('admin/', include(authority_urls)),
    path('contact', contact, name='contact'),
    path('company_details/', company_details, name='company_details'),
    path('projects/', projects, name='projects'),
    path('products/', products, name='products'),
    path('blogs/', blogs, name='blogs'),
    path('services/', services, name='services'),
    path('category/<int:id>/', category_products, name='category_products'),
    path('project_details/<int:id>/', project_details, name='project_details'),
    path('product_details/<int:id>/', product_details, name='product_details'),
    path('service/<int:id>/', service_details, name='service_details'),
    path('blog/<int:id>/', blog_details, name='blog_details'),
    path('dashboard/', admin.site.urls),
    path('', home, name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)