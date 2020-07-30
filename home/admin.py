from django.contrib import admin
from home.models import Contact, Blog


# Register your models here.

# Adding CSS and JS


class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("CSS/main.css",)
        }
        js = ("JS/blog.js",)


admin.site.register(Contact)

admin.site.register(Blog, BlogAdmin)
