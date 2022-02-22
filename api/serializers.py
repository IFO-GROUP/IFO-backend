from django.db.models import fields
from rest_framework import serializers
from django.conf import settings
from modeltranslation.manager import get_translatable_fields_for_model


from .models import (
        AllocationFund,
        Coin,
        CoinDeadline,
        CoinFeature,
        CoinField,
        Project,
        CoFounder,
        ShareHolder,
        CareerCategory,
        Career,
        NewsCategory,
        News,
        Subscriber,
        TimeLine
)

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = "__all__"


class TranslatedModelSerializerMixin(serializers.ModelSerializer):
    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        trans_fields = get_translatable_fields_for_model(self.Meta.model)
        all_fields = []

        requested_langs = []
        if 'request' in self.context:
            lang_param = self.context['request'].query_params.get('lang', None)
            requested_langs = lang_param.split(',') if lang_param else []

        for f in fields:
            if f not in trans_fields:
                all_fields.append(f)
            else:
                for l in settings.LANGUAGES:
                    if not requested_langs or l[0] in requested_langs:
                        all_fields.append("{}_{}".format(f, l[0]))

        return all_fields
    
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        
        
class CoFounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoFounder
        fields = "__all__"
     
        
class ShareHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareHolder
        fields = "__all__"


class CareerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerCategory
        fields = "__all__"
        
        
class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = "__all__"
        
        
class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"
        
        
class NewsSerializer(serializers.ModelSerializer):
    
    category=NewsCategorySerializer()
    class Meta:
        model = News
        fields = "__all__"
        

class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = "__all__"


class CoinFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinField
        fields = "__all__"


class CoinDeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinDeadline
        fields = "__all__"


class CoinFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinFeature
        fields = "__all__"


class AllocationFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllocationFund
        fields = "__all__"
        

class TimeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLine
        fields = "__all__"

        
        
