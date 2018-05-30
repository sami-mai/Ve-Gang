from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from thirdauth import views as tauth_views

urlpatterns = [

    url(r'^$', tauth_views.account, name='account'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
