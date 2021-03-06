from django.db import models


class CategoryManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=55)
    image = models.ImageField(blank=True, null=True, upload_to='categories')

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']
        unique_together = ['name']

    def natural_key(self):
        return self.name

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    image = models.ImageField(blank=True, null=True,
                              upload_to='media/products')
    price = models.FloatField(default=1.99)
    quantity = models.IntegerField(default=1)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name
# Create your models here.
