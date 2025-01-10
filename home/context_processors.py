from .models import BusinessInfo,Logo

def businessinfo(request):
    return {
        'businessinfo': BusinessInfo.objects.first(),
    }

def logo(request):
    return {
        'logo': Logo.objects.first(),
    }