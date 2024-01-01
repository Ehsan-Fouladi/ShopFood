# Generated by Django 4.2.7 on 2023-11-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='نام محصول')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('img', models.ImageField(upload_to='image/food', verbose_name='عکس محصول')),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'محصولات جدید',
                'verbose_name_plural': 'محصولات جدید',
            },
        ),
    ]
