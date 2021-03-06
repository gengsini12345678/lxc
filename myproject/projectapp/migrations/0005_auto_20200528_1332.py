# Generated by Django 2.0.3 on 2020-05-28 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_productadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='客户姓名')),
                ('phone_number', models.CharField(max_length=12)),
                ('sale_price', models.FloatField(verbose_name='销售单价')),
                ('sale_number', models.IntegerField()),
                ('total_money', models.FloatField(verbose_name='合计金额')),
                ('pro_info', models.TextField(verbose_name='备注')),
            ],
        ),
        migrations.AlterField(
            model_name='productadmin',
            name='pro_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='productsale',
            name='product_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectapp.ProductAdmin'),
        ),
    ]
