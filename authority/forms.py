from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.hashers import make_password
from ckeditor.widgets import CKEditorWidget


# models
from django.contrib.auth.models import User
from home.models import CarouselItem,Fact,AboutUs,AboutUsContent,Service,Feature,\
    FeatureIcon,Project,ContactMessage,Blog,Logo,BusinessInfo,Category

# forms
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','is_staff')


class AddAdminUserForm(forms.ModelForm):
    full_name = forms.CharField(max_length=150, required=True, label="Full Name")
    phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password must contain at least 8 characters'}) ,      required=True,
        label="Password"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        if len(full_name.split(' ')) < 2:
            raise forms.ValidationError("Please enter both first and last names.")
        return full_name

    def save(self, commit=True):
        user = super().save(commit=False)
        full_name = self.cleaned_data['full_name'].split(' ', 1)
        user.first_name = full_name[0]
        user.last_name = full_name[1] if len(full_name) > 1 else ""
        user.password = make_password(self.cleaned_data['password'])
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user

class LogoForm(forms.ModelForm):
    class Meta:
        model = Logo
        fields = ['header_logo', 'footer_logo','favicon']


class CarouselItemForm(forms.ModelForm):
    class Meta:
        model = CarouselItem
        fields = ['title', 'description', 'image']


class FactForm(forms.ModelForm):
    class Meta:
        model = Fact
        fields = ['icon', 'number', 'title', 'description']



class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = ['title', 'about_image', 'brief_details', 'content']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class AboutUsContentForm(forms.ModelForm):
    class Meta:
        model = AboutUsContent
        fields = ['icon', 'number', 'title']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'brief_details', 'content', 'icon']


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['title', 'description', 'image']


class FeatureIconForm(forms.ModelForm):
    class Meta:
        model = FeatureIcon
        fields = ['title', 'highlighted_word', 'icon']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'subtitle', 'category', 'content', 'image']


class BusinessInfoForm(forms.ModelForm):
    class Meta:
        model = BusinessInfo
        fields = ['site_name', 'address', 'phone', 'email', 'copyright_year',
                  'instagram_link', 'facebook_link', 'youtube_link', 'linkedin_link', 'map_embed_location_link']


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'content']