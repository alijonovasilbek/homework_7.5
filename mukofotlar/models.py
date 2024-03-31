from django.db import models



class Prize(models.Model):
    name = models.CharField(max_length=200, verbose_name="prize name")
    age = models.CharField( max_length=200,verbose_name='age')
    category= models.CharField(max_length=100, verbose_name='category')
    info = models.CharField(max_length=100, verbose_name='info', blank=True,null=True)
    image = models.ImageField(verbose_name='Prize image',upload_to="pri/%Y/%m/%d",blank=True,null=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Prize'
        verbose_name = 'Prize list'
        ordering = ('-id',)

