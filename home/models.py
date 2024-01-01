from django.db import models
# Create your models here.

class SocialNetworks(models.Model):
    telegram = models.CharField(max_length=100, blank=True, null=True, verbose_name="تلگرام")
    instagram = models.CharField(max_length=100, blank=True, null=True, verbose_name="اینستاگرام")

    class Meta:
        verbose_name = "شبکه های اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"

    def __str__(self):
        return f"instagram {self.instagram}  telegram {self.telegram}"

class Banner(models.Model):
    subject = models.CharField(max_length=70, verbose_name="نام")
    title = models.CharField(max_length=70, verbose_name="نام دوم")
    Description = models.TextField(verbose_name="توضیحات")
    img = models.ImageField(upload_to="image/background" ,verbose_name="عکس")
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "بنر"
        verbose_name_plural = "بنر ها"

    def __str__(self):
        return self.title

class MenuFood(models.Model):
    title = models.CharField(max_length=40 ,verbose_name="نام محصول")
    price = models.IntegerField(verbose_name="قیمت")
    img = models.ImageField(upload_to="image/food" ,verbose_name="عکس محصول")
    create = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "محصولات جدید"
        verbose_name_plural = "محصولات جدید"

    def __str__(self):
        return self.title

class MenuProducts(models.Model):
    title = models.CharField(max_length=40, verbose_name="نام محصول")
    img = models.ImageField(upload_to="image/product", verbose_name="عکس محصول")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "منوی محصولات"
        verbose_name_plural = "منوی محصولات ها"

    def __str__(self):
        return self.title

class SpecialOffer(models.Model):
    title = models.CharField(max_length=30, verbose_name="نام")
    price = models.IntegerField(verbose_name="قیمت")
    discount = models.IntegerField(verbose_name="قیمت تخفیف")
    Description = models.TextField(verbose_name="توضیحات")

    class Meta:
        verbose_name = "پیشنهاد ویژه"
        verbose_name_plural = "پیشنهاد ویژه"
    
    def __str__(self):
        return self.title