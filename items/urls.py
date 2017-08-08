from django.conf.urls import url
from items import views

urlpatterns = [
    url(r'^$', views.item),
    url(r'^add/', views.add_item),
    url(r'^delete/(?P<pk>\d+)/', views.delete_item),
    url(r'^update/(?P<pk>\d+)/', views.update_item)
]
