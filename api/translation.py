from modeltranslation.translator import register, TranslationOptions
from .models import AllocationFund, Coin, CoinFeature, CoinField, Partner, Project, CoFounder, ShareHolder, NewsCategory, News, TimeLine

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title','desc','text')
    
    
@register(CoFounder)
class CoFounderTranslationOptions(TranslationOptions):
    fields = ('full_name','desc')
    
    
@register(ShareHolder)
class ShareHolderTranslationOptions(TranslationOptions):
    fields = ('full_name','desc')
    
    
@register(NewsCategory)
class NewsCategoryTranslationOptions(TranslationOptions):
    fields = ('type',)
    

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','desc')
    
    
@register(Coin)
class CoinTranslationOptions(TranslationOptions):
    fields = ('title','desc')
    

@register(CoinField)
class CoinFieldTranslationOptions(TranslationOptions):
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
    

@register(Partner)
class PartnertranslationOptions(TranslationOptions):
    fields = ('title','short_desc','desc')