from django.conf.urls import url, re_path

from . import views

app_name = 'projectapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^register/$', views.register, name='register'),

    url(r'^login/$', views.login_user, name='login_user'),

    url(r'^add_product/$', views.add_product, name='add_product'),

    url(r'^product_list/$', views.product_list, name='product_list'),

    # 产品详情
    url(r'^(?P<id>\d+)/product_info/$', views.product_info, name="product_info"),

    # 修改产品
    url(r'^(?P<proid>\d+)/update_product/$', views.update_product, name="update_product"),

    # 删除产品
    url(r'^(?P<pro_id>\d+)/delete_porduct/$', views.delete_porduct, name="delete_porduct"),

    # 搜索产品
    url(r'^search/$', views.search, name="search"),

    # 添加产品销售
    url(r'^add_product_sale/$', views.add_product_sale, name="add_product_sale"),

    url(r'^sale_list/$', views.sale_list, name="sale_list"),

    url(r'^search_sale/$', views.search_sale, name="search_sale"),

    url(r'^(?P<pro_id>\d+)/delete_sale/$', views.delete_sale, name="delete_sale"),

    # 退出系统
    url(r'^logout/$', views.logout, name="logout"),

    # re_path('^(?P<pro_id>\d+)/update_product/$', views.update_product, name="update_product"),
    # url('^(?P<pro_id>)/update_product/$', views.update_product, name="update_product"),

    # url(r'^(?P<article_id>\d+)/xiuGai_article/$',views.xiugai_article,name="xiuGai_article"),

]
