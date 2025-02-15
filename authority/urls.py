from django.urls import path


app_name='authority'

from authority.views import authority_main
from authority.views import manage_user
from authority.views import manage_features
from authority.views import manage_businessinfo
from authority.views import manage_about
from authority.views import manage_service
from authority.views import manage_blog
from authority.views import manage_project
from authority.views import manage_contact
from authority.views import manage_fact
from authority.views import manage_carousel
from authority.views import manage_logo
from authority.views import manage_sitesettings
from authority.views import manage_brand
from authority.views import manage_product


urlpatterns = [
    path('', authority_main.AdminView.as_view(), name='authority_admin')
]

#Manage User
urlpatterns += [
    path('user-list/', manage_user.UserListView.as_view(), name='user_list'),
    path('login/', manage_user.CustomLoginView.as_view(), name='login'),
    path('logout/',  manage_user.CustomLogoutView.as_view(), name='logout'),
    path('add_admin/', manage_user.AddAdminUserView.as_view(), name='add_admin'),
    path('update_admin/<int:pk>/', manage_user.UpdateAdminUserView.as_view(), name='update_admin'),
    path('reset-password/<int:user_id>/', manage_user.PasswordResetView.as_view(), name='reset_password'),
    path('profile_list/', manage_user.ProfileListView.as_view(), name='profile_list'),
    path('delete_admin/<int:pk>/', manage_user.DeleteUserView.as_view(), name='delete_admin')
]

# Manage Features
urlpatterns += [
    path('feature-list/', manage_features.FeaturesListView.as_view(), name='feature_list'),
    path('feature/add/', manage_features.AddFeatureView.as_view(), name='add_feature'),
    path('feature/update/<int:pk>/', manage_features.UpdateFeatureView.as_view(), name='update_feature'),
    path('feature/delete/<int:pk>/', manage_features.FeatureDeleteView.as_view(), name='delete_feature'),
]

# Manage Feature Icons
urlpatterns += [
    path('feature-icon-list/', manage_features.FeatureIconListView.as_view(), name='feature_icon_list'),
    path('feature-icon/add/', manage_features.AddFeatureIconView.as_view(), name='add_feature_icon'),
    path('feature-icon/update/<int:pk>/', manage_features.UpdateFeatureIconView.as_view(), name='update_feature_icon'),
    path('feature-icon/delete/<int:pk>/', manage_features.FeatureIconDeleteView.as_view(), name='delete_feature_icon'),
]

# Manage Business Info
urlpatterns += [
    path('business-info-list/', manage_businessinfo.BusinessInfoListView.as_view(), name='business_list'),
    path('business-info/add/', manage_businessinfo.AddBusinessInfoView.as_view(), name='add_business_info'),
    path('business-info/update/<int:pk>/', manage_businessinfo.UpdateBusinessInfoView.as_view(), name='update_business_info'),
    path('business-info/delete/<int:pk>/', manage_businessinfo.BusinessInfoDeleteView.as_view(), name='delete_business_info'),
]

# Manage About Us
urlpatterns += [
    path('about-us-list/', manage_about.AboutUsListView.as_view(), name='about_us_list'),
    path('about-us/add/', manage_about.AddAboutUsView.as_view(), name='add_about_us'),
    path('about-us/update/<int:pk>/', manage_about.UpdateAboutUsView.as_view(), name='update_about_us'),
    path('about-us/delete/<int:pk>/', manage_about.AboutUsDeleteView.as_view(), name='delete_about_us'),
]

# Manage About Us Content
urlpatterns += [
    path('about-us-content-list/', manage_about.AboutUsContentListView.as_view(), name='about_us_content_list'),
    path('about-us-content/add/', manage_about.AddAboutUsContentView.as_view(), name='add_about_us_content'),
    path('about-us-content/update/<int:pk>/', manage_about.UpdateAboutUsContentView.as_view(), name='update_about_us_content'),
    path('about-us-content/delete/<int:pk>/', manage_about.AboutUsContentDeleteView.as_view(), name='delete_about_us_content'),
]

# Manage Services
urlpatterns += [
    path('service-list/', manage_service.ServiceListView.as_view(), name='service_list'),
    path('service/add/', manage_service.AddServiceView.as_view(), name='add_service'),
    path('service/update/<int:pk>/', manage_service.UpdateServiceView.as_view(), name='update_service'),
    path('service/delete/<int:pk>/', manage_service.ServiceDeleteView.as_view(), name='delete_service'),
]

# Manage Blogs
urlpatterns += [
    path('blog-list/', manage_blog.BlogListView.as_view(), name='blog_list'),
    path('blog/add/', manage_blog.AddBlogView.as_view(), name='add_blog'),
    path('blog/update/<int:pk>/', manage_blog.UpdateBlogView.as_view(), name='update_blog'),
    path('blog/delete/<int:pk>/', manage_blog.BlogDeleteView.as_view(), name='delete_blog'),
]

# Manage Contact Messages
urlpatterns += [
    path('contact-message-list/', manage_contact.ContactMessageListView.as_view(), name='contact_message_list'),
    path('contact-message/detail/<int:pk>/', manage_contact.ContactMessageDetailView.as_view(), name='contact_message_detail'),
    path('contact-message/delete/<int:pk>/', manage_contact.ContactMessageDeleteView.as_view(), name='delete_contact_message'),
]

# Manage Projects
urlpatterns += [
    path('project-list/', manage_project.ProjectListView.as_view(), name='project_list'),
    path('project/add/', manage_project.AddProjectView.as_view(), name='add_project'),
    path('project/update/<int:pk>/', manage_project.UpdateProjectView.as_view(), name='update_project'),
    path('project/delete/<int:pk>/', manage_project.ProjectDeleteView.as_view(), name='delete_project'),

    # Category management
    path('category-list/', manage_project.CategoryListView.as_view(), name='category_list'),
    path('category/add/', manage_project.AddCategoryView.as_view(), name='add_category'),
    path('category/update/<int:pk>/', manage_project.UpdateCategoryView.as_view(), name='update_category'),
    path('category/delete/<int:pk>/', manage_project.CategoryDeleteView.as_view(), name='delete_category'),
]

# Manage Facts
urlpatterns += [
    path('fact-list/', manage_fact.FactListView.as_view(), name='fact_list'),
    path('fact/add/', manage_fact.AddFactView.as_view(), name='add_fact'),
    path('fact/update/<int:pk>/', manage_fact.UpdateFactView.as_view(), name='update_fact'),
    path('fact/delete/<int:pk>/', manage_fact.FactDeleteView.as_view(), name='delete_fact'),
]

# Manage Carousel Items
urlpatterns += [
    path('carousel-item-list/', manage_carousel.CarouselItemListView.as_view(), name='carousel_item_list'),
    path('carousel-item/add/', manage_carousel.AddCarouselItemView.as_view(), name='add_carousel_item'),
    path('carousel-item/update/<int:pk>/', manage_carousel.UpdateCarouselItemView.as_view(), name='update_carousel_item'),
    path('carousel-item/delete/<int:pk>/', manage_carousel.CarouselItemDeleteView.as_view(), name='delete_carousel_item'),
]

# Manage Logos
urlpatterns += [
    path('logo-list/', manage_logo.LogoListView.as_view(), name='logo_list'),
    path('logo/add/', manage_logo.AddLogoView.as_view(), name='add_logo'),
    path('logo/update/<int:pk>/', manage_logo.UpdateLogoView.as_view(), name='update_logo'),
    path('logo/delete/<int:pk>/', manage_logo.LogoDeleteView.as_view(), name='delete_logo'),
]


# Manage Site Settings
urlpatterns += [
    path('site-settings/', manage_sitesettings.SiteSettingsListView.as_view(), name='site_settings'),
    path('site-settings/add/', manage_sitesettings.AddSiteSettingView.as_view(), name='add_site_setting'),
    path('site-settings/<int:pk>/update/', manage_sitesettings.UpdateSiteSettingView.as_view(), name='update_site_setting'),
    path('site-settings/<int:pk>/delete/', manage_sitesettings.SiteSettingDeleteView.as_view(), name='delete_site_setting'),
]

# Manage Brand
urlpatterns +=[
    path('brand-list/', manage_brand.BrandListView.as_view(), name='brand_list'),
    path('update-brand/<int:pk>/', manage_brand.UpdateBrandView.as_view(), name='update_brand'),
    path('add-brand/', manage_brand.AddBrandView.as_view(), name='add_brand'),
    path('delete_brand/<int:pk>/', manage_brand.BrandDeleteView.as_view(), name='delete_brand'),
]

# Manage ProductCategory
urlpatterns += [
    path('product-category-list/', manage_product.ProductCategoryListView.as_view(), name='product_category_list'),
    path('update-product-category/<int:pk>/', manage_product.UpdateProductCategoryView.as_view(), name='update_product_category'),
    path('add-product-category/', manage_product.AddProductCategoryView.as_view(), name='add_product_category'),
    path('delete-product-category/<int:pk>/', manage_product.DeleteProductCategoryView.as_view(), name='delete_product_category'),
]

# Manage Product
urlpatterns += [
    path('product-list/', manage_product.ProductListView.as_view(), name='product_list'),
    path('update-product/<int:pk>/', manage_product.UpdateProductView.as_view(), name='update_product'),
    path('add-product/', manage_product.AddProductView.as_view(), name='add_product'),
    path('delete-product/<int:pk>/', manage_product.DeleteProductView.as_view(), name='delete_product'),
]




