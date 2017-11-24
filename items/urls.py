from django.conf.urls import url
from items import views

urlpatterns = [
    url(r'^$', views.item, name="list"),
    url(r'^add/', views.add_item, name="add"),
    url(r'^delete/(?P<pk>\d+)/', views.delete_item, name="delete"),
    url(r'^update/(?P<pk>\d+)/', views.update_item, name="update")
]
