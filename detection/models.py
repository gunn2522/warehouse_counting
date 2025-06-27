from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)

class FlowLog(models.Model):
    ACTIONS = (('IN', 'Inflow'), ('OUT', 'Outflow'))
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    action = models.CharField(max_length=3, choices=ACTIONS)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
