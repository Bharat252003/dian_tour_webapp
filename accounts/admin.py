from django.contrib import admin

# Register your models here.
{% comment %} from django.contrib import admin {% endcomment %}

admin.site.site_header = "Custom bookstore admin"
admin.site.site_title = "Custom bookstore admin site"
admin.site.index_title = "Custom Bookstore Admin"
