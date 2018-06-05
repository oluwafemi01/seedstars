from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
	
    url(r'^list/$', views.employees, name='employees'),
	url(r'^logout/$', views.signout, name='logoutPage'),
	url(r'^add/$', views.createuser, name='createuser'),
	url(r'^$', views.homepage, name='indexPage'),
]


if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)