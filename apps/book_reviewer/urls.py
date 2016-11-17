from django.conf.urls import url
from . import views          
  
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^editor$', views.show_editor, name='editor'),
  url(r'^add_book$', views.add_book_and_review, name='add_book'),
  url(r'^show_book/(?P<id>\d+)$', views.show_book, name='show_book'),
  url(r'^add_review/(?P<id>\d+)$', views.add_review, name='add_review'),
  url(r'^destroy/(?P<review_id>\d+)/(?P<book_id>\d+)$', views.destroy, name='destroy'),
  url(r'^show_user/(?P<id>\d+)$', views.show_user, name='show_user'),
  url(r'^logout$', views.logout, name='logout'),
]
