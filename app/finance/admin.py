#encoding: utf-8
from django.contrib import admin
from .models import Activity, Order, OrderItem

class OrderItemInline(admin.TabularInline):
	model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('user', 'value', 'created_at')
	fieldsets = (
		(None, {'fields': ()}),
	)
	inlines = [OrderItemInline,]


	def save_model(self, request, obj, form, change):
		if getattr(obj, 'user', None) is None:
			obj.user = request.user
		obj.save()

	

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
	list_display = ('user', 'type', 'value', 'created_at')
	

