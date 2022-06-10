from django.db import models


class Pages(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='photos/pages',blank =True)
    url = models.URLField(blank=True)
    
    class Meta:
        verbose_name = 'Pages'
        verbose_name_plural = 'Pages'
    
    def __str__(self):
        return self.title