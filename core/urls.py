from django.urls import include, re_path, path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include('api.urls', namespace='api')),

]

urlpatterns += [re_path(r'^(?!(api|admin|media)).*$', TemplateView.as_view(template_name='index.html'))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }), ]


