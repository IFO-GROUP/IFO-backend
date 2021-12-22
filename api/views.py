from rest_framework import viewsets
from rest_framework.decorators import action


from .models import (
        Project,
        CoFounder,
        ShareHolder,
        CareerCategory,
        Career,
        NewsCategory,
        News,
        Image
)

from api.serializers import (
        ProjectSerializer,
        CoFounderSerializer,
        ShareHolderSerializer,
        CareerCategorySerializer,
        CareerSerializer,
        NewsCategorySerializer,
        NewsSerializer,
        ImageSerializer
)


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
    
    
class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


