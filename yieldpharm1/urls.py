from django.conf.urls import url
from yieldpharm1 import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<ydclass_id>[0-9]+)/$',views.ydclass),
    url(r'^(?P<product_id>[0-9]+)/detail$',views.detail),
    url(r'^search/$',views.search),
    url(r'^aboutus/$',views.aboutus),
    url(r'^contactus/$',views.contactus),
    url(r'^products/$',views.products),
    url(r'^lab/$',views.lab),
    url(r'^news/$',views.news),
    url(r'^feedback/$',views.feedback),
    url(r'^en/$',views.indexen),
    url(r'^en/(?P<ydclass_id>[0-9]+)/$', views.ydclassen),
    url(r'^en/(?P<product_id>[0-9]+)/detail$', views.detailen),
    url(r'^en/search/$', views.searchen),
    url(r'^en/aboutus/$',views.aboutusen),
    url(r'^en/contactus/$',views.contactusen),
    url(r'^en/products/$', views.productsen),
    url(r'^en/lab/$', views.laben),
    url(r'^en/news/$', views.newsen),
    url(r'^en/feedback/$', views.feedbacken),

]