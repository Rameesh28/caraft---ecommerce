# Generated by Django 3.2.16 on 2023-01-30 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0004_delete_cartmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartname', models.CharField(max_length=30)),
                ('pid', models.CharField(max_length=10)),
                ('cid', models.CharField(max_length=6)),
                ('cartprice', models.IntegerField()),
                ('cartdescription', models.CharField(max_length=100)),
                ('cartimage', models.ImageField(upload_to='miniapp/static')),
            ],
        ),
    ]
