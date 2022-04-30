from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import AllocationFund, Career, CareerCategory, CoFounder, Coin, CoinDeadline, CoinFeature, CoinField, News, NewsCategory, Partner, Project, ShareHolder, Subscriber, TimeLine


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    search_fields = ( 'email',)
    list_display = ('email',)
    
    

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    search_fields = ('title','desc','text','link','created_at')
    list_display = ('title', 'cover_img', 'desc','detail_img','text','link','created_at')
    list_filter = ('title','desc','text','link','created_at')


@admin.register(CoFounder)
class CoFounderAdmin(TranslationAdmin):
    search_fields = ('full_name','desc')
    list_display =  ('full_name','img')
    list_filter =   ('full_name','desc') 



@admin.register(ShareHolder)
class ShareHolderAdmin(TranslationAdmin):
    search_fields = ('full_name','desc')
    list_display =  ('full_name','img','desc')
    list_filter =   ('full_name','desc') 



@admin.register(CareerCategory)
class CareerCategoryAdmin(admin.ModelAdmin):
    search_fields = ('type',)
    list_display =  ('type',)
    list_filter =   ('type',)



@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    search_fields = ('name','email','phone','location')
    list_display =  ('name','email','phone','location','ln_link','comment')
    list_filter =   ('name','email','phone','location')



@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    search_fields = ('type','bg_color')
    list_display =  ('type','bg_color')
    list_filter =   ('type','bg_color')
    
    
@admin.register(News)
class NewsAdmin(TranslationAdmin):
    search_fields = ('title','created_at')
    list_display =  ('title','cover_img','desc','created_at')
    list_filter =   ('title','created_at')
    

@admin.register(Coin)
class CoinAdmin(TranslationAdmin):
    search_fields = ('title','img','desc','ln_link')
    list_display =  ('title','img','desc','ln_link')
    list_filter =  ('title','img','desc','ln_link')
    
    
@admin.register(CoinField)
class CoinFieldAdmin(TranslationAdmin):
    search_fields = ('title','desc')
    list_display = ('title','desc')
    list_filter = ('title','desc')
    
    
@admin.register(CoinDeadline)
class CoinDeadlineAdmin(admin.ModelAdmin):
    search_fields = ('deadline',)
    list_display= ('deadline',)
    list_filter = ('deadline',)
    
    
@admin.register(CoinFeature)
class CoinFeatureAdmin(TranslationAdmin):
    search_fields = ('feature','count')
    list_display= ('feature','count')
    list_filter =('feature','count')
    
    
@admin.register(AllocationFund)
class AllocationFundAdmin(TranslationAdmin):
    search_fields = ('title',)
    list_display= ('title',)
    list_display =  ('title',)
    
    
@admin.register(TimeLine)
class TimeLineAdmin(TranslationAdmin):
    search_fields = ('title','desc','created_at')
    list_display= ('title','desc','created_at')
    list_display = ('title','desc','created_at')


@admin.register(Partner)
class Partnerdmin(TranslationAdmin):
    search_fields = ('title','created_at')
    list_display= ('title','short_desc','created_at')
    list_display = ('title','short_desc','created_at')

