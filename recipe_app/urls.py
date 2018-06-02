from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from veg_app import views as veg_views

urlpatterns = [

    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
