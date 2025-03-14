# Müşteri Destek Temsilcisi Yönlendirme Fonksiyonu
def destek_temsilcisi_yonlendirme(musteri_talepleri, temsilciler, n, m):
    # DP Tablosu: dp[i][j] = i. müşteri talebine kadar ve j. temsilcinin uygunluğu altında en iyi yönlendirme
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Dinamik programlama geçişleri
    for i in range(1, n + 1):  # Müşteri talepleri
        for j in range(1, m + 1):  # Temsilciler
            if temsilciler[j - 1] >= musteri_talepleri[i - 1]:  # Temsilci, talebi karşılayabiliyorsa
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + musteri_talepleri[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]  # Temsilciyi kullanmıyoruz

    # En yüksek talep karşılanma oranı
    en_yuksek_talepler = dp[n][m]

    # Hangi temsilcilerin seçildiğini bulma
    temsilciler_secildi = []
    j = m
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:  # Temsilci seçildiyse
            temsilciler_secildi.append(j - 1)
            j -= 1

    temsilciler_secildi.reverse()
    return en_yuksek_talepler, temsilciler_secildi


# Pazarlama Kampanyası Seçimi Fonksiyonu
def pazarlama_kampanyasi_secimi(butce, maliyet, getiri):
    n = len(maliyet)  # Kampanya sayısı
    dp = [[0] * (butce + 1) for _ in range(n + 1)]  # DP Tablosu

    # Dinamik programlama geçişleri
    for i in range(1, n + 1):  # Kampanyalar
        for j in range(1, butce + 1):  # Bütçe
            if maliyet[i - 1] <= j:  # Eğer kampanyayı seçebiliyorsak
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - maliyet[i - 1]] + getiri[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]  # Kampanyayı seçmiyoruz

    # Sonuç: En yüksek yatırım getirisi
    en_yuksek_getiri = dp[n][butce]

    # Seçilen kampanyaları bulma
    kampanyalar = []
    j = butce
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:  # Kampanya seçilmişse
            kampanyalar.append(i - 1)
            j -= maliyet[i - 1]

    kampanyalar.reverse()  # Seçilen kampanyaları sıralıyoruz
    return en_yuksek_getiri, kampanyalar


# Örnek Veriler
# Müşteri talepleri (Örneğin şehirdeki taleplerin büyüklüğü)
musteri_talepleri = [120, 150, 80, 200, 170]
# Temsilcilerin uygunluk durumu (yani hangi temsilcinin hangi talepleri karşılayabileceği)
temsilciler = [100, 160, 200, 180, 140]

# Müşteri Destek Temsilcisi Yönlendirme
n = len(musteri_talepleri)  # Müşteri talebi sayısı
m = len(temsilciler)  # Temsilci sayısı
en_yuksek_talepler, temsilciler_secildi = destek_temsilcisi_yonlendirme(musteri_talepleri, temsilciler, n, m)
print("En yüksek karşılanabilir talepler:", en_yuksek_talepler)
print("Seçilen Temsilciler:", temsilciler_secildi)


# Pazarlama Kampanyası Seçimi
maliyet = [50, 60, 40, 30]
getiri = [100, 120, 80, 70]
butce = 100
en_yuksek_getiri, kampanyalar = pazarlama_kampanyasi_secimi(butce, maliyet, getiri)
print("En yüksek yatırım getirisi:", en_yuksek_getiri)
print("Seçilen Kampanyalar:", kampanyalar)

