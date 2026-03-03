# 📊 Python ile İstatistiksel A/B Testi Analizi
Bu proje, bir e-ticaret platformunda kullanıcı arayüzü değişikliklerinin (UI) satışlar üzerindeki etkisini bilimsel yöntemlerle analiz etmek için geliştirilmiştir.

## 🧐 İş Problemi
Şirketimiz, web sitesindeki "Satın Al" butonunun tasarımını değiştirdi. Elimizde iki grup veri var:
- **Grup A (Kontrol Grubu):** Eski tasarım (1000 ziyaretçi, 50 satış)
- **Grup B (Test Grubu):** Yeni tasarım (1000 ziyaretçi, 75 satış)

**Soru:** Yeni tasarımdaki %2.5'lik artış kalıcı bir başarı mı, yoksa şans eseri mi oluştu?

## 🛠 Uygulanan İstatistiksel Yöntemler
Bu analizde şu adımlar takip edilmiştir:
1. **Betimsel İstatistik:** Her iki grubun dönüşüm oranlarının (Conversion Rate) hesaplanması.
2. **Standart Hata (Standard Error):** Örneklem varyansının ölçülmesi.
3. **Z-Testi:** İki oran arasındaki farkın istatistiksel anlamlılığının (p-value analizi için temel) hesaplanması.
4. **Karar Eşiği:** %95 güven düzeyi için 1.96 kritik değerinin kullanılması.
5. ## 🏆 Final Kararı

Hesaplanan **Z-Skoru: 2.31** (yaklaşık).
Bu değer **1.96'dan büyük** olduğu için boş hipotez reddedilir. %95 güvenle söyleyebiliriz ki yeni tasarım istatistiksel olarak daha başarılıdır ve tüm kullanıcılara yayına alınması önerilir.
