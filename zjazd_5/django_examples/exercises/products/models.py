from django.db import models

# Create your models here.
from django.db import models

#tu tworzymy tabele w bazie danych
# Create your models here.

class Product(models.Model):
    nazwa = models.CharField(max_length=15, ) #nazwa operacji w mojej aplikacji maths
    opis = models.CharField(max_length=100, )
    cena = models.IntegerField()
    status = models.BooleanField() #default jest false, można ustawić defualt=True

    def __str__(self):
        return f"""Product: {self.nazwa}
            Opis: {self.opis}
            Cena: {self.cena}
            Status : {self.status}
            """