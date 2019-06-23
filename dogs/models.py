from django.db import models


class Dog(models.Model):
    breed = models.CharField(
        max_length=100,
        verbose_name='Порода',
    )
    display_image = models.ImageField(
        upload_to='dogs',
        verbose_name='Фото',
    )

    def __str__(self):
        return self.breed

    class Meta:
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
