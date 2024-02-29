from django.db import models

# Create your models here.
class quadrilateral(models.Model):
    Name=models.CharField(max_length=100)
    Figure =models.ImageField(upload_to='media/')
    Sides=models.TextField()
    Angles=models.TextField()
    Diagonals=models.TextField()
   

    def __str__(self):
        return self.Name
    

