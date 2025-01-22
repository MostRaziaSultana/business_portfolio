from django.contrib import admin
from .models import CarouselItem,Fact,AboutUsContent,AboutUs,Service,Feature,\
    FeatureIcon,BusinessInfo,Logo,Project,ContactMessage,Blog,Category,SiteSettings,Brand,ProductCategory,Product
# Register your models here.
admin.site.register(CarouselItem)
admin.site.register(Fact)
admin.site.register(AboutUs)
admin.site.register(AboutUsContent)
admin.site.register(Service)
admin.site.register(Feature)
admin.site.register(FeatureIcon)
admin.site.register(BusinessInfo)
admin.site.register(Logo)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ContactMessage)
admin.site.register(Blog)
admin.site.register(SiteSettings)
admin.site.register(Brand)
admin.site.register(ProductCategory)
admin.site.register(Product)
