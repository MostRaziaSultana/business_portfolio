from django.shortcuts import render, redirect
from .models import CarouselItem,Fact,AboutUs,AboutUsContent,Service,Feature,\
    FeatureIcon,Project,ContactMessage,Blog
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
# Create your views here.
def home(request):

    carousel_items = CarouselItem.objects.all()
    facts = Fact.objects.all().order_by('number')
    about_data = AboutUs.objects.first()
    about_content = AboutUsContent.objects.all()
    services = Service.objects.all()
    features = Feature.objects.first()
    feature_icons = FeatureIcon.objects.all()
    blogs = Blog.objects.all()

    return render(request, 'index.html', {
        'carousel_items': carousel_items,
        'facts': facts,
        'about_data': about_data,
        'about_content':about_content,
        'services': services,
        'features': features,
        'feature_icons': feature_icons,
        'projects': projects,
        'blogs': blogs
    })


def contact(request):

    services = Service.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'contact.html', {
        'services': services
    })

def service_details(request, id):
    service = get_object_or_404(Service, id=id)
    services = Service.objects.all()
    return render(request, 'service_details.html', {
        'service': service,
        'services': services
    })

def company_details(request):
    services = Service.objects.all()
    about_us = AboutUs.objects.first()
    return render(request, 'company_details.html', {
        'services': services,
        'about_us': about_us
    })

def project_details(request,id):
    services = Service.objects.all()
    project = get_object_or_404(Project, id=id)
    return render(request, 'project_details.html', {
        'services': services,
        'project': project,
    })


def projects(request):
    projects = Project.objects.all()
    services = Service.objects.all()
    return render(request, 'projects.html', {
        'projects': projects,
        'category_choices': Project.CATEGORY_CHOICES,
        'services': services,
    })


def blog_details(request, id):
    blog_details = get_object_or_404(Blog, id=id)
    blogs = Blog.objects.all()
    services = Service.objects.all()
    return render(request, 'blog_details.html', {
        'blog_details': blog_details,
        'services': services,
        'blogs': blogs
    })