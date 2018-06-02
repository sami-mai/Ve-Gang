from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from accounts_app import views as account_views

urlpatterns = [

    url(r'^$', account_views.dashboard, name='dashboard'),
    url(r'^account/', account_views.edit_profile, name='edit_profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
