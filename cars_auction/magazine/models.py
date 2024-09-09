from django.db import models

# Create your models here.
class Car(models.Model):

    class AutoClassification(models.TextChoices):
        SEDAN = ('Sedan', 'Sedan')
        HATCHBACK = ('Hatchback', 'Hatchback')
        BUISNESS = ('Business', 'Business')
        MINIVAN = ('Minivan', 'Minivan')
        CROSSOVER = ('Crossover', 'Crossover')
        SPORT = ('Sports', 'Sports')

    name = models.CharField(max_length=100)
    car_brand = models.OneToOneField('CarBrand', on_delete=models.DO_NOTHING, blank=True, null=True)
    year = models.DateField(null=True)
    classification = models.CharField(choices=AutoClassification)
    description = models.TextField()
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id}) {self.name}"

