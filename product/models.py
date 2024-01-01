from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=50, verbose_name="نام محصول")
    description = models.TextField(verbose_name="توضیح کوتاه درمورد محصول")
    image = models.ImageField(upload_to='gallery/', verbose_name="عکس محصول")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "نمایش محصولات"
        verbose_name_plural = "نمایش محصولات"

    def __str__(self):
        return self.title