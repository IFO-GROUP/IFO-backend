from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as api_views

from . import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'cofounders', views.CoFounderViewSet)
router.register(r'shareholders', views.ShareHolderViewSet)
router.register(r'careercategories', views.CareerCategoryViewSet)
router.register(r'careers', views.CareerViewSet)
router.register(r'newscategories', views.NewsCategoryViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'images', views.ImageViewSet)
router.register(r'subscribers', views.SubscriberViewSet)


app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
    path('api-token-auth/', api_views.obtain_auth_token)
]
