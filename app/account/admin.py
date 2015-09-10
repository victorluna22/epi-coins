#encoding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group
from .models import EpiUser


class EpiUserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(EpiUserCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = EpiUser
        fields = ('full_name', 'email')


class EpiUserChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(EpiUserChangeForm, self).__init__(*args, **kargs)

    class Meta:
        model = EpiUser	
        fields = '__all__'


@admin.register(EpiUser)
class EpiUserAdmin(UserAdmin):
	list_display = ('nome', 'email', 'bank_balance', 'is_active', 'date_joined')
	list_filter = ('is_active', 'date_joined')
	search_fields = ('name', 'email')
	date_hierarchy = 'date_joined'
	form = EpiUserChangeForm
	add_form = EpiUserCreationForm
	readonly_fields = ['bank_balance',]

	fieldsets = (
		(None, {'fields': ('password',)}),
		(_('Personal info'), {'fields': ('full_name', 'email', 'bank_balance')}),
		(_('Atividade no site'), {'fields': ('is_active',)}),
	)
	add_fieldsets = (
		(None, {
		    'classes': ('wide',),
		    'fields': ('email', 'password1', 'password2'),
		}),
	)

	def nome(self, obj):
		return obj.get_full_name()



admin.site.unregister(Site)
admin.site.unregister(Group)