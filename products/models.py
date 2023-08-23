from django.db import models


class Product(models.Model):#M from model must be capital
    name=models.CharField(max_length=225)
    description=models.TextField()
    price=models.FloatField()
    photo=models.ImageField(upload_to='photos/%y/%m/%d/')
    is_active=models.BooleanField(default= True)
    publish_date=models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-publish_date']