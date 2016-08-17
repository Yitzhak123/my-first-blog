
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.book_list, name='book_list'),
	url(r'^book/(?P<pk>\d+)/$', views.book_detail, name='book_detail'),
	url(r'^book/new/$', views.add_new_book, name='add_new_book'),
	url(r'^book/(?P<pk>\d+)/add_name/$', views.add_new_name, name='add_new_name'),
]