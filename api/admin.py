from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Career, CareerCategory, CoFounder, Image, News, NewsCategory, Project, ShareHolder

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    
    
@admin.register(Project)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('title','desc','text','link','created_at')
    list_display = ('title', 'cover_img', 'desc','detail_img','text','link','created_at')
    list_filter = ('title','desc','text','link','created_at')


@admin.register(CoFounder)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('full_name','desc')
    list_display =  ('full_name','img','desc')
    list_filter =   ('full_name','desc') 



@admin.register(ShareHolder)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('full_name','desc')
    list_display =  ('full_name','img','desc')
    list_filter =   ('full_name','desc') 



@admin.register(CareerCategory)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('type',)
    list_display =  ('type',)
    list_filter =   ('type',)



@admin.register(Career)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name','email','phone','location')
    list_display =  ('name','email','phone','location','ln_link','comment')
    list_filter =   ('name','email','phone','location')



@admin.register(NewsCategory)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('type',)
    list_display =  ('type',)
    list_filter =   ('type',)
    
    
@admin.register(News)
class ContactAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    search_fields = ('title','type','created_at')
    list_display =  ('title','cover_img','desc','type','created_at')
    list_filter =   ('title','type','created_at')