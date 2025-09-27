from django.db import models
from datetime import date, timedelta

class Goat(models.Model):
    BREED = {
        'F': 'Myotonic/Fainting',
        'M': 'Mixed',
        'N': 'Nigerian',
        'P': 'Pygmy',
        'U': 'Unknown',
    }
    BIRTH_NUMBER = {
        'S': 'Single',
        'W': 'Twin',
        'T': 'Triplet',
        'Q': 'Quad',
        'U': 'Unknown',
    }
    CATEGORY = {
        'BB': 'Breeding Buck',
        'BU': 'Buckling',
        'YB': 'Yearling Buck',
        'MB': 'Market Buck',
        'PB': 'Pet Quality Buck/Buckling',
        'MW': 'Market Wether',
        'PW': 'Pet Quality Wether',
        'BD': 'Breeding Doe',
        'DO': 'Doeling',
        'YD': 'Yearling Doe',
        'MD': 'Market Doe',
        'PD': 'Pet Quality Doe/Doeling',
    }
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    breed = models.CharField(max_length=100, null=True, blank=True, choices=BREED, default='F')
    date_of_birth = models.DateField(null=True, blank=True)
    birth_number = models.CharField(max_length=50, choices=BIRTH_NUMBER, default='S')
    birth_weight = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    category = models.CharField(max_length=50, choices=CATEGORY, default='BD')        
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='goats/', default='goat.jpg')
    is_available = models.BooleanField(default=False)
    is_registered = models.BooleanField(default=False)
    is_disbudded_or_dehorned = models.BooleanField(default=True)
    is_polled = models.BooleanField(default=False)
    registry = models.CharField(max_length=100, null=True, blank=True)
    registry_id = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name

    def age_in_years(self):
        if not self.date_of_birth:
            return None
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or \
           (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day):
            age -= 1
        return age
