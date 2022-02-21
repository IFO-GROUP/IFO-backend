from modeltranslation.translator import register, TranslationOptions
from .models import AllocationFund, Coin, CoinFeature, CoinField, Project, CoFounder, ShareHolder, NewsCategory, News, TimeLine

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
    
    
@register(Coin)
class CoinranslationOptions(TranslationOptions):
    fields = ('title','desc')
    

@register(CoinField)
class CoinFieldranslationOptions(TranslationOptions):
    fields = ('title','desc')


@register(CoinFeature)
class CoinFeaturetranslationOptions(TranslationOptions):
    fields = ('feature',)


@register(AllocationFund)
class AllocationFundtranslationOptions(TranslationOptions):
    fields = ('title',)
    
    
@register(TimeLine)
class TimeLinetranslationOptions(TranslationOptions):
    fields = ('title','desc')