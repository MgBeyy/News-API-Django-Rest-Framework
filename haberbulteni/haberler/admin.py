from django.contrib import admin
from .models import *

@admin.register(Makale)
class MakaleAdmin(admin.ModelAdmin):
    list_display = ("id","baslik","yazar","aktif")
    list_display_links = ["id","baslik"]
    list_filter = ["yazar"]
    list_editable = ["aktif"]
    search_fields = ["baslik"]

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ["id","adi"]
    list_display_links = ["id","adi"]
    search_fields = ["adi"]

@admin.register(Gazeteci)
class GazeteciAdmin(admin.ModelAdmin):
    list_display = ["id","adi","soyadi"]
    list_display_links = ["id","adi","soyadi"]
    search_fields = ["adi","soyadi"]
