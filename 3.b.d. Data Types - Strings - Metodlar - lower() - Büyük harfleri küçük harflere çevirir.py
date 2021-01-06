# lower()
# kod içerisine yazılan haflerin küçültmeye yarar:
print("BU HARFLERİ BÜYÜK YAZIYORUM AMA KÜÇÜK OLSUN İSTİYORUM.".lower())
bu harfleri̇ büyük yaziyorum ama küçük olsun i̇sti̇yorum.
# Bunu da parça parça kullanabilirim:
print("BURAYA KADAR YAZILANLAR KÜÇÜK OLSUN,".lower(),"BURASI BÜYÜK KALSIN.")
buraya kadar yazilanlar küçük olsun, BURASI BÜYÜK KALSIN.
# Hem lower()'ı hem upper()'ı aynı kod içinde kullanabilirim:
print("upper".upper(),"LOWER".lower())
UPPER lower
# Bu metod bir değişkene de atanabilir:
isim = "GÖKAY"
print(isim.lower())
gökay
# HATIRLATMA: Değişkene atasam da değişkeni kalıcı olarak değiştirmez. Daha son-
# ra ben değişkeni yazdırmak istediğimde ilk haliyle aynen yazdırır:
print(isim)
GÖKAY
# Ama yeni bir değişkene metodla beraber atarsak değişkeni yeni haliyle yazar:
yeni_isim = isim.lower()
print(yeni_isim)
gökay
