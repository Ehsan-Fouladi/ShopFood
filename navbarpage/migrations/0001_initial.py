# Generated by Django 4.2.8 on 2024-01-02 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='درباره ما')),
            ],
            options={
                'verbose_name': 'درباره ما',
                'verbose_name_plural': 'درباره ما',
            },
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('phone', models.CharField(max_length=12, verbose_name='تلفن')),
                ('subject', models.TextField(verbose_name='پیام')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
            ],
            options={
                'verbose_name': 'تماس با ما',
                'verbose_name_plural': 'تماس با ما',
            },
        ),
        migrations.CreateModel(
            name='OurPartners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'شرکای ما',
                'verbose_name_plural': 'شرکای ما',
            },
        ),
        migrations.CreateModel(
            name='OurStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='موضوع')),
                ('body', models.TextField(verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='about/', verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'داستان ما',
                'verbose_name_plural': 'داستان ما',
            },
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام')),
                ('silence', models.CharField(max_length=70, verbose_name='صمت فرد')),
                ('image', models.ImageField(upload_to='about/team/', verbose_name='عکس')),
                ('instagram', models.CharField(blank=True, max_length=256, null=True, verbose_name='لینک اینستاگرام')),
                ('telegram', models.CharField(blank=True, max_length=256, null=True, verbose_name='لینک تلگرام')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'تیم ما',
                'verbose_name_plural': 'تیم ما',
            },
        ),
    ]
