from django.db.models import fields
from rest_framework import serializers
from django.conf import settings
from modeltranslation.manager import get_translatable_fields_for_model


from .models import (
        Project,
        CoFounder,
        ShareHolder,
        CareerCategory,
        Career,
        NewsCategory,
        News,
        Image,
        Subscriber
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
        category=CareerCategorySerializer
        model = Career
        fields = "__all__"
        
        
class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = "__all__"
        
        
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        category=NewsCategorySerializer
        model = News
        fields = "__all__"
        
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        news=NewsSerializer
        model = Image
        fields = "__all__"