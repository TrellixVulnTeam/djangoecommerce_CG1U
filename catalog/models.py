# coding=utf-8

from django.db import models
from django.urls import reverse

class Category(models.Model):

    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name

class Product(models.Model):
        name = models.CharField('Nome', max_length=100)
        slug = models.SlugField('Identificador', max_length=100)
        category = models.ForeignKey('catalog.Category', verbose_name='Categoria', on_delete=models.CASCADE)
        description = models.TextField('Descrição', blank=True)
        price = models.DecimalField('Preço', decimal_places=2, max_digits = 10)


        created = models.DateTimeField('Criado em', auto_now_add=True)
        modified = models.DateTimeField('Modificado em', auto_now=True)

        class Meta:
            verbose_name = 'Produto'
            verbose_name_plural = 'Produtos'
            ordering = ['name']

        def get_absolute_url(self):
            return reverse('catalog:product', kwargs = {'slug':self.slug})

        def __str__(self):
            return self.name
