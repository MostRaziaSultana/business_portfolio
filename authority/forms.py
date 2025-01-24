from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth.hashers import make_password
from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ValidationError


# models
from django.contrib.auth.models import User
from home.models import CarouselItem,Fact,AboutUs,AboutUsContent,Service,Feature,\
    FeatureIcon,Project,ContactMessage,Blog,Logo,BusinessInfo,Category,SiteSettings,\
    Brand,ProductCategory,Product

# forms
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','is_staff')


# class AddAdminUserForm(forms.ModelForm):
#     full_name = forms.CharField(max_length=150, required=True, label="Full Name")
#     phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'Password must contain at least 8 characters'}) ,      required=True,
#         label="Password"
#     )
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#     def clean_full_name(self):
#         full_name = self.cleaned_data.get('full_name')
#         if len(full_name.split(' ')) < 2:
#             raise forms.ValidationError("Please enter both first and last names.")
#         return full_name
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         full_name = self.cleaned_data['full_name'].split(' ', 1)
#         user.first_name = full_name[0]
#         user.last_name = full_name[1] if len(full_name) > 1 else ""
#         user.password = make_password(self.cleaned_data['password'])
#         user.is_staff = True
#         user.is_superuser = True
#         if commit:
#             user.save()
#         return user

class AddAdminUserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password must contain at least 8 characters'}),
        required=True,
        label="Password"
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            raise forms.ValidationError('Password must contain at least 8 characters.')

        if password.isdigit():
            raise forms.ValidationError('Password cannot be entirely numeric.')

        common_passwords = ['123456', 'password', 'qwerty', 'letmein', 'admin', 'welcome', 'password123']
        if password.lower() in common_passwords:
            raise forms.ValidationError('Password is too common.')

        username = self.cleaned_data.get('username')
        if username and username.lower() in password.lower():
            raise forms.ValidationError('Password cannot be too similar to the username.')

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user

# class UpdateAdminUserForm(forms.ModelForm):
#     full_name = forms.CharField(max_length=150, required=True, label="Full Name")
#     phone_number = forms.CharField(max_length=15, required=True, label="Phone Number")
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'readonly': True, 'style': 'background-color: #f0f0f0;'}),
#         required=False,
#         label="Password",
#         help_text = "Password cannot be updated through this form."
#     )
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self.instance:
#             full_name = f"{self.instance.first_name} {self.instance.last_name}"
#             self.fields['full_name'].initial = full_name
#             print(f"Debug: Full Name Initial Value: {full_name}")
#
#     def clean_full_name(self):
#         full_name = self.cleaned_data.get('full_name')
#         if len(full_name.split(' ')) < 2:
#             raise forms.ValidationError("Please enter both first and last names.")
#         return full_name
#
#     def clean_phone_number(self):
#         phone_number = self.cleaned_data.get('phone_number')
#         if not phone_number.isdigit() or len(phone_number) < 10:
#             raise forms.ValidationError("Enter a valid phone number with at least 10 digits.")
#         return phone_number
#
#     def clean_password(self):
#         # Prevent password changes via this form
#         return self.instance.password
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         full_name = self.cleaned_data['full_name'].split(' ', 1)
#         user.first_name = full_name[0]
#         user.last_name = full_name[1] if len(full_name) > 1 else ""
#         if commit:
#             user.save()
#         return user
class UpdateAdminUserForm(forms.ModelForm):
    full_name = forms.CharField(
        max_length=150,
        required=False,
        label="Full Name",
        help_text="Enter both first and last name, or leave blank."
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'full_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            # Pre-fill full_name with first_name and last_name
            self.fields['full_name'].initial = f"{self.instance.first_name} {self.instance.last_name}".strip()

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name', '').strip()
        if full_name and len(full_name.split(' ')) < 2:
            raise forms.ValidationError("Please enter both first and last names or leave blank.")
        return full_name

    def save(self, commit=True):
        user = super().save(commit=False)

        user.password = self.instance.password

        full_name = self.cleaned_data.get('full_name', '').strip()
        if full_name:
            full_name_split = full_name.split(' ', 1)
            user.first_name = full_name_split[0]
            user.last_name = full_name_split[1] if len(full_name_split) > 1 else ""
        else:
            user.first_name = ""
            user.last_name = ""

        if commit:
            user.save()
        return user


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, label='New Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:
            raise ValidationError("Passwords do not match.")

        if len(new_password) < 8:
            raise ValidationError("Password must contain at least 8 characters.")

        if new_password.isdigit():
            raise ValidationError("Password cannot be entirely numeric.")

        common_passwords = ['123456', 'password', 'qwerty', 'letmein', 'admin', 'welcome', 'password123']
        if new_password.lower() in common_passwords:
            raise ValidationError("Password is too common.")

        username = self.initial.get('username')
        if username and username.lower() in new_password.lower():
            raise ValidationError("Password cannot be too similar to the username.")

        return cleaned_data

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
        fields = ['title', 'about_image', 'description']

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
        fields = ['title', 'details', 'icon','in_homepage']


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
                  'instagram_link', 'facebook_link', 'youtube_link', 'linkedin_link','messenger_link',
            'twitter_link', 'whatsapp','telegram_link','map_embed_location_link']


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image','in_homepage', 'content']


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        fields = ['gtm_id','keywords', 'description','facebook_domain_verification_id',
                  'google_site_verification_id']
        keywords = forms.CharField(
            widget=forms.Textarea(
                attrs={'placeholder': 'Enter meta keywords separated by commas', 'rows': 4, 'cols': 40,
                       'class': 'form-control'}
            ),
            required=False,
            label="Keywords"
        )

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', 'logo', )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price','image', 'description']


class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['name']