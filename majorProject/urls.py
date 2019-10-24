from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^field/', views.storesField, name='storeField')
]
urlpatterns += staticfiles_urlpatterns()