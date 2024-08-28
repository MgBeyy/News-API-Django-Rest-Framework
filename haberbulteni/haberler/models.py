from django.db import models

# Create your models here.

class Kategori(models.Model):
    adi = models.CharField(max_length=50)
    def __str__(self):
        return self.adi

class Gazeteci(models.Model):
    adi = models.CharField(max_length=50)
    soyadi = models.CharField(max_length=50)
    biyografi = models.TextField()

    def __str__(self):
        return f"{self.adi} {self.soyadi}"

class Yorum(models.Model):
    baslik = models.CharField(max_length=50)
    metin = models.TextField()
    makale = models.ForeignKey("Makale", on_delete=models.CASCADE, related_name="yorumlar")

    def __str__(self):
        return self.baslik


class Makale(models.Model):
    kategori = models.ManyToManyField(Kategori, related_name="makaleler")
    yazar = models.ForeignKey(Gazeteci, on_delete=models.CASCADE, related_name="makaleler")
    baslik = models.CharField(max_length=120)
    aciklama = models.CharField(max_length=200)
    metin = models.TextField()
    sehir = models.CharField(max_length=120)
    yayimlanma_tarihi = models.DateField()
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    gunceleme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baslik