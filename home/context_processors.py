from .models import BusinessInfo,Logo,ContactMessage,Service,Blog,Project,SiteSettings,ProductCategory

def businessinfo(request):
    return {
        'businessinfo': BusinessInfo.objects.first(),
    }

def logo(request):
    return {
        'logo': Logo.objects.first(),
    }

def product_categories(request):
    return {
        'product_categories': ProductCategory.objects.all(),
    }

def site_settings(request):
    return {
        'site_settings': SiteSettings.objects.first(),
    }

def last_messages(request):
    latest_messages = ContactMessage.objects.order_by("-created_at")[:10]
    total_services_count = Service.objects.count()
    total_blog_count = Blog.objects.count()
    total_messages_count = ContactMessage.objects.count()
    total_projects_count = Project.objects.count()

    return {
        'latest_messages': latest_messages,
        'total_services': total_services_count,
        'total_blogs': total_blog_count,
        'total_messages': total_messages_count,
        'total_projects': total_projects_count,
    }