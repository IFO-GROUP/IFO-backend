from rest_framework import viewsets
from rest_framework.decorators import action


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

from api.serializers import (
        AllocationFundSerializer,
        CoinDeadlineSerializer,
        CoinFeatureSerializer,
        CoinFieldSerializer,
        CoinSerializer,
        ProjectSerializer,
        CoFounderSerializer,
        ShareHolderSerializer,
        CareerCategorySerializer,
        CareerSerializer,
        NewsCategorySerializer,
        NewsSerializer,
        SubscriberSerializer,
        TimeLineSerializer
)


class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    http_method_names = ['post', 'options']

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CoFounderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CoFounder.objects.all()
    serializer_class = CoFounderSerializer


class ShareHolderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ShareHolder.objects.all()
    serializer_class = ShareHolderSerializer

class CareerCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CareerCategory.objects.all()
    serializer_class = CareerCategorySerializer


class CareerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer


class NewsCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    
    
class CoinViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    

class CoinFieldViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CoinField.objects.all()
    serializer_class = CoinFieldSerializer


class CoinDeadlineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CoinDeadline.objects.all()
    serializer_class = CoinDeadlineSerializer


class CoinFeatureViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CoinFeature.objects.all()
    serializer_class = CoinFeatureSerializer


class AllocationFundViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AllocationFund.objects.all()
    serializer_class = AllocationFundSerializer


class TimeLineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TimeLine.objects.all()
    serializer_class = TimeLineSerializer



    
    



