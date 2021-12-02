from django.db import models
from django.utils.text import slugify


class Menu(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Menu, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'menu'
        verbose_name_plural = 'menus'

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return str(self.name)
