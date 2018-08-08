from django.conf.urls import url
from . import views
app_name='authapp'
urlpatterns = [
url(r'^$',views.input, name='input'),
url(r'^insert$',views.insert,name='insert'),
url(r'^display$',views.display,name='display'),
url(r'^products/(?P<pk>[0-9]+)/$', views.ProductList.as_view()),
#url(r'^products/(?P<pk>[0-9]+)/reviews/$', views.ReviewList.as_view()),
url(r'^products/(?P<product_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/$',
        views.ReviewDetail.as_view()
    ),

]
