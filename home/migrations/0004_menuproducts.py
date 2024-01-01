# Generated by Django 4.2.7 on 2023-11-23 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_menufood'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='نام محصول')),
                ('img', models.ImageField(upload_to='image/product', verbose_name='عکس محصول')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'منوی محصولات',
                'verbose_name_plural': 'منوی محصولات ها',
            },
        ),
    ]