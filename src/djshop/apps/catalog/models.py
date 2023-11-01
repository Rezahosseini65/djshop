from django.db import models

from treebeard.mp_tree import MP_Node

# Create your models here.

class Category(MP_Node):
    title = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.CharField(max_length=2048,null=True,blank=True)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
