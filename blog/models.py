from django.db import models
from accounts.models import User
from jalali_date import date2jalali
from django.utils.html import format_html

class Category(models.Model):
    blog = models.CharField(max_length=20, verbose_name="نام")
    date = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ["-date"]
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.blog

class BlogModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users", verbose_name="نام کاربر")
    title = models.CharField(max_length=50, verbose_name="عنوان")
    image = models.ImageField(upload_to="blog/", verbose_name="تصویر", blank=True, null=True)
    description = models.TextField(verbose_name="متن")
    slug = models.SlugField(max_length=250, verbose_name="عنوان")
    category = models.ManyToManyField(Category, related_name="blogs", verbose_name="دسته بندی")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "وبلاگ"
        verbose_name_plural = "وبلاگ ها"

    def get_jalail_date(self):
        return date2jalali(self.created_at).strftime("%y/%m/%d")

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" height="50px" width="60px">')
        return format_html(f'<span style="color:red">این مقاله عکس ندارد</span>')
    show_image.short_description = "تصویر مقاله"

    def __str__(self):
        return self.title
