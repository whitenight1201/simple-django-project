from django.contrib import admin
from .models import Member


# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        "firstname",
        "lastname",
        "joined_date",
    )
    prepopulated_fields = {"slug": ("firstname", "lastname")}


# include models
admin.site.register(Member, MemberAdmin)
