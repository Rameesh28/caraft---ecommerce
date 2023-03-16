# Generated by Django 3.2.16 on 2023-01-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=30)),
                ('pid', models.CharField(max_length=10)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='miniapp/static')),
            ],
        ),
    ]