from django.db import models

# Create your models here.

from datetime import datetime


class UserTable(models.Model):
    '''
    用户数据模型
    '''
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    userpass = models.CharField(max_length=100)
    realname = models.CharField(max_length=50, default='请完善')


class ProductAdmin(models.Model):
    '''
    产品管理模块
    '''
    id = models.AutoField(primary_key=True)
    # 产品名称
    pro_name = models.CharField(max_length=50)
    # 产品代码
    pro_code = models.IntegerField()
    # 产品类别
    pro_type = models.CharField(max_length=100)
    # 单价
    pro_price = models.FloatField(verbose_name='商品价格')
    # 库位
    pro_kuwei = models.IntegerField()
    # 备注
    pro_intro = models.TextField(verbose_name='产品备注')
    # 所属用户
    user = models.ForeignKey(UserTable, on_delete=models.CASCADE)


class ProductSale(models.Model):
    '''
    产品销售
    '''
    id = models.AutoField(primary_key=True)
    # 客户姓名
    name = models.CharField(max_length=50,verbose_name='客户姓名')
    # 客户手机
    phone_number = models.CharField(max_length=12)
    # 销售单价
    sale_price = models.FloatField(verbose_name='销售单价')
    # 销售数量
    sale_number =  models.IntegerField()
    # 合计金额
    total_money = models.FloatField(verbose_name='合计金额')
    # 备注
    pro_info = models.TextField(verbose_name='备注')
    # 和产品管理模块关联
    product_admin = models.ForeignKey(ProductAdmin, on_delete=models.CASCADE)


