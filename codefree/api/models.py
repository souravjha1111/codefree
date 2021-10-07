from django.db import models
from django.db.models.fields import CharField
from django.core.validators import MinValueValidator, MaxValueValidator

class irisModel(models.Model):
    sepal_length  = models.DecimalField(validators=[MinValueValidator(0)], decimal_places = 3, max_digits = 10)
    sepal_width  = models.DecimalField(validators=[MinValueValidator(0)], decimal_places = 3, max_digits = 10)
    petal_length  = models.DecimalField(validators=[MinValueValidator(0)], decimal_places = 3, max_digits = 10)
    petal_width  = models.DecimalField(validators=[MinValueValidator(0)], decimal_places = 3, max_digits = 10)
    choices = choices = [
        ('Iris-Setosa', 'Iris-Setosa'),
        ('Iris-Versicolour', 'Iris-Versicolour'),
        ('Iris-Versicolour', 'Iris-Virginica')
        ]
    category = models.CharField(
        max_length=50,
        choices=choices,
        default='Iris-Setosa',
    )
