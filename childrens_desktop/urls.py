
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.load_user_manager_page, name='load_user_manager_page'),
	url(r'^sign_up/$', views.add_new_user_manager, name='add_new_user_manager'),
	url(r'^user/new/$', views.add_new_user, name='add_new_user'),
	url(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
	url(r'^(?P<name>\w+)/new/$', views.add_new_app, name='add_new_app'),
	url(r'^(?P<name>\w+)/(?P<pk>\d+)/$', views.app_detail, name='app_detail'),
	url(r'^(?P<name>\w+)/(?P<pk>\d+)/$', views.remove_app, name='remove_app'),
	# url(r'^book/(?P<pk>\d+)/add_name/$', views.add_new_name, name='add_new_name'),
]