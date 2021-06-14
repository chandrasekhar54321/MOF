# Generated by Django 3.2.2 on 2021-05-31 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0010_auto_20210529_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='blog/')),
            ],
        ),
    ]