from django.contrib import admin
from .models import Profile, Book, Catalogue, Status, Cart, Message
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.unregister(Group)
admin.site.register(Catalogue)
admin.site.register(Status)
admin.site.register(Message)

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