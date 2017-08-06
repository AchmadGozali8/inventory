from django.conf.urls import url
from items import views

urlpatterns = [
    url(r'^$', views.item),
    url(r'^add/', views.add_item),
]
