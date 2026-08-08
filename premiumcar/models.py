from django.db import models
from django_resized import ResizedImageField

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    title = models.CharField(verbose_name='name', max_length=100)

    def __str__(self):
        return self.title

class Car(models.Model):
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    name = models.CharField(verbose_name='name', max_length=100)
    short_description = models.TextField(verbose_name='short_description', max_length=500)
    description = models.TextField(verbose_name='description', max_length=800)
    image = models.ImageField(verbose_name='Image', upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT)
    year = models.IntegerField(verbose_name='Год выпуска', default=0000)
    probeg = models.IntegerField(verbose_name='Пробег',  null=True, blank=True)
    box = models.CharField(verbose_name='Коробка', max_length=100, null=True, blank=True)
    toplivo = models.CharField(verbose_name='Топливо', max_length=100,  null=True, blank=True)
    motion = models.CharField(verbose_name='Двигатель', max_length=100,  null=True, blank=True)
    color = models.CharField(verbose_name='Цвет', max_length=50, default='no-color')
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2, default=0)

    @property
    def image(self):
        if self.images.first():
            return self.images.first().image
        return None
    
    def __str__(self):
        return self.name


class ImageCar(models.Model):

    class Meta:
        verbose_name_plural = 'изображении товаров'
        verbose_name = 'изображение товара'


    car = models.ForeignKey('premiumcar.Car', on_delete=models.PROTECT, verbose_name='товар', related_name='images')
    image = ResizedImageField('фото', upload_to='car_images/', quality=90, force_format='WEBP')
    
    def __str__(self):
        return f'{self.car.name}'

# Create your models here.
