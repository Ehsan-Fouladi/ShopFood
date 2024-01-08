from django.db import models

# Create your models here.
class ContactModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    phone = models.CharField(max_length=12, verbose_name="تلفن")
    subject = models.TextField(verbose_name="پیام")
    email = models.EmailField(verbose_name="ایمیل")
    
    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = "تماس با ما"

    def __str__(self):
        return self.name

class AboutModel(models.Model):
    body = models.TextField(verbose_name="درباره ما")

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = "درباره ما"

    def __str__(self):
        return self.body[:15]

class OurStory(models.Model):
    title = models.CharField(max_length=50, verbose_name="موضوع")
    body = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="about/", verbose_name="عکس")

    class Meta:
        verbose_name = 'داستان ما'
        verbose_name_plural = "داستان ما"

    def __str__(self):
        return self.title

class OurPartners(models.Model):
    body = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = 'شرکای ما'
        verbose_name_plural = "شرکای ما"

    def __str__(self):
        return self.body[:20]


class OurTeam(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام")
    silence = models.CharField(max_length=70, verbose_name="صمت فرد")
    gmail = models.EmailField(verbose_name="ایمیل")
    your_about = models.TextField(verbose_name="درباره خود")
    work_about = models.TextField(verbose_name="درباره مدرک یا کار های که کردین")
    evidence = models.ImageField(upload_to="team/evidence/", verbose_name="عکس مدرک", null=True, blank=True)
    evidence_two = models.ImageField(upload_to="team/evidence1/", verbose_name="2عکس مدرک", null=True, blank=True)
    evidence_three = models.ImageField(upload_to="team/evidence2/", verbose_name="3عکس مدرک", null=True, blank=True)
    image = models.ImageField(upload_to="about/team/", verbose_name="عکس")
    instagram = models.CharField(max_length=256, verbose_name="لینک اینستاگرام", blank=True, null=True)
    telegram = models.CharField(max_length=256, verbose_name="لینک تلگرام", blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'تیم ما'
        verbose_name_plural = "تیم ما"

    def __str__(self):
        return self.silence