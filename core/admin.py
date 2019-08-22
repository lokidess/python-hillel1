from django.contrib import admin
from core.models import Post, Tag, Category, MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
#
#
# class TestModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'test_field', 'test_integer')
#     # list_editable = ('test_field', )
#
#
# admin.site.register(TestModel, TestModelAdmin)


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'avatar', 'phone')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(MyUser, MyUserAdmin)
