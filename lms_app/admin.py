from django.contrib import admin
from .models import Profile, Book, Catalogue, Blog, Status, Cart, Message, Inventory, Request
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.unregister(Group)
admin.site.register(Catalogue)
admin.site.register(Status)
admin.site.register(Message)
admin.site.register(Blog)
admin.site.register(Request)
admin.site.register(Inventory)

@admin.register(Book)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('name', 'author',)
	ordering = ('name',)
	search_fields = ('name', 'author')

class ProfileInline(admin.StackedInline):
	model=Profile

class UserAdmin(admin.ModelAdmin):
	model=User
	fields=('first_name', 'last_name', 'username', 'email',)
	list_display=('username', 'email',) 
	inlines=[ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)