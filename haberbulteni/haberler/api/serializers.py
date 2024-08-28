from rest_framework import serializers
from haberler.models import *

from datetime import date, datetime
from django.utils.timesince import timesince

class YorumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yorum
        fields = "__all__"


class MakaleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    # yazar = serializers.StringRelatedField()
    # yazar = GazeteciSerializer()
    yorumlar = YorumSerializer(read_only=True, many=True)
    class Meta:
        model = Makale
        fields = "__all__"
        read_only_fields = ['id', 'yaratilma_tarihi', 'gunceleme_tarihi']

    def get_time_since_pub(self, obj):
        now = datetime.now()
        pub_date = obj.yayimlanma_tarihi
        if obj.aktif == True:
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return "Pasif makale"

    def validate_yayimlanma_tarihi(self, tarih):
        if tarih > date.today():
            raise serializers.ValidationError("Gecersiz yayimlanma tarihi")
        return tarih

class GazeteciSerializer(serializers.ModelSerializer):

    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay',
    )
    class Meta:
        model = Gazeteci
        fields = "__all__"


class KategoriSerializer(serializers.ModelSerializer):
    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detay',
    )
    class Meta:
        model = Kategori
        fields = "__all__"










# class MakaleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     yazar = serializers.CharField()
#     baslik = serializers.CharField()
#     aciklama = serializers.CharField()
#     metin = serializers.CharField()
#     sehir = serializers.CharField()
#     yayimlanma_tarihi = serializers.DateField()
#     aktif = serializers.BooleanField()
#     yaratilma_tarihi = serializers.DateTimeField(read_only=True)
#     gunceleme_tarihi = serializers.DateTimeField(read_only=True)

#     def create(self, validated_data):
#         print(validated_data)
#         return Makale.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.yazar = validated_data.get('yazar', instance.yazar)
#         instance.baslik = validated_data.get('baslik', instance.baslik)
#         instance.aciklama = validated_data.get('aciklama', instance.aciklama)
#         instance.metin = validated_data.get('metin', instance.metin)
#         instance.sehir = validated_data.get('sehir', instance.sehir)
#         instance.yayimlanma_tarihi = validated_data.get('yayimlanma_tarihi', instance.yayimlanma_tarihi)
#         instance.aktif = validated_data.get('aktif', instance.aktif)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['baslik'] == data['aciklama']:
#             raise serializers.ValidationError("Başlık ile acıklama aynı olamaz")
#         return data

#     def validate_baslik(self, value):
#         if len(value) < 4:
#             raise serializers.ValidationError(f"En az 4 karakter olmalıdır. Girilen karakter sayısı {len(value)}")
#         return value