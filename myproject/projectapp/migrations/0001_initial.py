# Generated by Django 2.0.3 on 2020-05-26 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('userpass', models.CharField(max_length=50)),
                ('realname', models.CharField(default='请完善', max_length=50)),
            ],
        ),
    ]
