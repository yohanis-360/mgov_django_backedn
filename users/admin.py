from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django import forms
from .models import Developer

User = get_user_model()

# Custom User Admin Form
class CustomUserAdminForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_developer')

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user




class CustomUserAdmin(BaseUserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_developer')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('email',)
    readonly_fields = ('password',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(id__in=Developer.objects.values('user_id'))

class DeveloperAdminForm(forms.ModelForm):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField()

    class Meta:
        model = Developer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['email'].initial = self.instance.user.email
            self.fields['username'].initial = self.instance.user.username
            self.fields['password'].initial = self.instance.user.password

    def save(self, commit=True):
        developer = super().save(commit=False)
        user = developer.user
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            developer.save()
        return developer

class DeveloperAdmin(admin.ModelAdmin):
    form = DeveloperAdminForm
    list_display = ('user', 'organization_name', 'status', 'organization_address', 'city', 'woreda', 'zone', 'sub_city', 'business_registration_number')
    search_fields = ('organization_name', 'organization_address', 'city', 'woreda', 'zone', 'sub_city', 'business_registration_number')
    ordering = ('organization_name',)
    actions = ['approve_developers', 'reject_developers']

    def approve_developers(self, request, queryset):
        queryset.update(status='approved')
    approve_developers.short_description = "Approve selected developers"

    def reject_developers(self, request, queryset):
        queryset.update(status='rejected')
    reject_developers.short_description = "Reject selected developers"

admin.site.register(User, CustomUserAdmin)
admin.site.register(Developer, DeveloperAdmin)
