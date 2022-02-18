from modeltranslation.translator import register, TranslationOptions
from .models import Project, CoFounder, ShareHolder, NewsCategory, News

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title','desc','text')
    
    
@register(CoFounder)
class CoFounderranslationOptions(TranslationOptions):
    fields = ('full_name','desc')
    
    
@register(ShareHolder)
class ShareHolderranslationOptions(TranslationOptions):
    fields = ('full_name','desc')
    
    
@register(NewsCategory)
class NewsCategoryranslationOptions(TranslationOptions):
    fields = ('type',)
    

@register(News)
class NewsranslationOptions(TranslationOptions):
    fields = ('title','desc')


    
