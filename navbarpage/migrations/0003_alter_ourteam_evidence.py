# Generated by Django 4.2.8 on 2024-01-08 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navbarpage', '0002_ourteam_evidence_ourteam_gmail_ourteam_work_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='evidence',
            field=models.ImageField(upload_to='team/evidence/', verbose_name='عکس مدرک'),
        ),
    ]
