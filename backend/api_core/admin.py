from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from api_core.models import PatientProfile, DoctorProfile


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()


class PatientProfileInline(admin.StackedInline):
    model = PatientProfile
    can_delete = False
    fk_name = 'user'


class DoctorProfileInline(admin.StackedInline):
    model = DoctorProfile
    can_delete = False
    fk_name = 'user'


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    inlines = (PatientProfileInline, DoctorProfileInline)
    fieldsets = UserAdmin.fieldsets + (
        (
            None, {'fields': ('user_type',)}
        ),
    )

    def get_inlines(self, request, obj):
        if hasattr(obj, 'patient_profile'):
            return PatientProfileInline,
        if hasattr(obj, 'doctor_profile'):
            return DoctorProfileInline,
        return tuple()


admin.site.register(get_user_model(), MyUserAdmin)
