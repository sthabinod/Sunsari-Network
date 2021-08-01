from django.contrib import admin
from apps.models import *
from apps.models import About
from django.utils.html import format_html


# Register your models here.

admin.site.site_header = "Sunsari Cable"
admin.site.site_title = "SC"
admin.site.index_title = "Sunsari Cable"


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    # Process of giving permission to store only one object of About class
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

    list_display = ['title', 'description', 'image']


admin.site.register(Service)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'post', 'image']
    list_filter = ['full_name', 'post']
    list_per_page = 4


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', ]
    list_filter = ['title', ]
    list_per_page = 4


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'description']
    list_filter = ['client_name']
    list_per_page = 4


admin.site.register(Blog)


@admin.register(ComapnyInfo)
class CompanyAdmin(admin.ModelAdmin):
    # Process of giving permission to store only one object of Company class
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


admin.site.register(SocialMedia)


@admin.register(Listing)
class DescAdmin(admin.ModelAdmin):
    pass


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['plan_title', 'mbps', 'price']
    list_filter = ['plan_title', 'mbps']
    list_per_page = 4
