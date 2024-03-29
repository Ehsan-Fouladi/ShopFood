# Generated by Django 4.2.8 on 2024-01-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='نام محصول')),
                ('description', models.TextField(verbose_name='توضیح کوتاه درمورد محصول')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='عکس محصول')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'نمایش محصولات',
                'verbose_name_plural': 'نمایش محصولات',
                'ordering': ('-created_at',),
            },
        ),
    ]
