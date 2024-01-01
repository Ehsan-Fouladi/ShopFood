# Generated by Django 4.2.8 on 2023-12-06 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbarpage', '0004_ourteam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='image',
            field=models.ImageField(upload_to='about/team/', verbose_name='عکس'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='instagram',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='لینک اینستاگرام'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='telegram',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='لینک تلگرام'),
        ),
    ]
