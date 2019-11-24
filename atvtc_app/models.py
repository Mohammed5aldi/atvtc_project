from django.db import models





class table(models.Model):
    name = models.CharField(max_length=40)
    ter1 = models.CharField(max_length=20)
    ter2 = models.CharField(max_length=30)
    ter3 = models.CharField(max_length=30)
    ter4 = models.CharField(max_length=30)
    ter5 = models.CharField(max_length=30)
    ter6 = models.CharField(max_length=30)
    

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('detail', args=[str(self.id)])

# Create your models here.
