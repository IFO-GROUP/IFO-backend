from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as api_views

from . import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'partners', views.PartnerViewSet)
router.register(r'cofounders', views.CoFounderViewSet)
router.register(r'shareholders', views.ShareHolderViewSet)
router.register(r'careercategories', views.CareerCategoryViewSet)
router.register(r'careers', views.CareerViewSet)
router.register(r'newscategories', views.NewsCategoryViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'subscribers', views.SubscriberViewSet)
router.register(r'coins', views.CoinViewSet)
router.register(r'coinfields', views.CoinFieldViewSet)
router.register(r'coindeadlines', views.CoinDeadlineViewSet)
router.register(r'coinfeatures', views.CoinFeatureViewSet)
router.register(r'allocationfunds', views.AllocationFundViewSet)
router.register(r'timelines', views.TimeLineViewSet)

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
    path('api-token-auth/', api_views.obtain_auth_token)
]
