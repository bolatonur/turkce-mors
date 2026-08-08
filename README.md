# Türkçe Mors Alfabesi Optimizasyonu

Bu projede, klasik Mors alfabesinin İngilizce harf frekanslarına göre oluşturulmuş yapısı Türkçe için yeniden düzenlenmiştir.

Amaç, Türkçede sık kullanılan harflere daha düşük iletim maliyetine sahip Mors kombinasyonları atayarak daha hızlı bir iletişim yapısı elde etmektir.

## Projede Neler Yapıldı?

- Türkçe ve İngilizce metinlerde harf frekansları çıkarıldı.
- Nokta ve çizgi kombinasyonlarının iletim maliyetleri hesaplandı.
- En düşük maliyetli kombinasyonlar sıralandı.
- Türkçede sık kullanılan harfler düşük maliyetli kombinasyonlarla eşleştirildi.
- Yeni sistem bir Mors karar ağacı haline getirildi.
- Klasik Mors ile oluşturduğumuz sistemin maliyet karşılaştırmaları yapıldı.
- Oluşturulan ağaç GitHub Pages üzerinden kullanılabilir hale getirildi.

## Sonuç

Yapılan testlerde oluşturduğumuz Türkçe Mors sistemi, kullanılan metne göre farklı oranlarda avantaj sağladı.

Türkçe metinlerde ortalama olarak yaklaşık **%9 daha düşük iletim maliyeti** elde edildi. Bazı edebi metinlerde bu oran **%9,93** seviyesine kadar çıktı.

## Yapay Zekâ Kullanımı

Projenin geliştirme sürecinde yapay zekâ araçlarından destek alınmıştır.

Özellikle web arayüzündeki Mors ağacının kodlanması büyük ölçüde yapay zekâ desteğiyle gerçekleştirilmiştir. Projenin amacı, yöntem seçimi, veri analizi, testler ve sonuçların değerlendirilmesi tarafımızca yapılmıştır.

## Proje Dosyaları

Repo içerisinde genel olarak şu dosyalar bulunmaktadır:

- Frekans analizi scriptleri
- Türkçe ve İngilizce frekans çıktıları
- Mors kombinasyonlarının maliyet hesaplamaları
- Optimum harf sıralama scriptleri
- Grafik ve tablolar
- Oluşturulan Mors ağacı
- Web sitesi
- Proje sunumu

## Veri Kaynakları

Frekans analizinde çeşitli Türkçe ve İngilizce edebi eserlerden yararlanılmıştır.

Kullanılan eserlerin tam metinleri telif hakları nedeniyle bu repoya eklenmemiştir. Repo içerisinde yalnızca analiz sonucunda elde edilen frekans verileri, grafikler ve kod çıktıları bulunmaktadır.

Kullanılan eserler ve analiz süreci proje sunumunda gösterilmiştir.

## Web Sitesi

Oluşturduğumuz Türkçe Mors ağacını aşağıdaki GitHub Pages sayfasından deneyebilirsiniz:

https://bolatonur.github.io/turkce-mors/

## Sunum

Projenin yöntemi, kullanılan algoritmalar, frekans analizleri ve test sonuçları sunum içerisinde daha detaylı olarak anlatılmıştır.

[Proje Sunumunu Görüntüle](sunum\Mors_Cozumleme Agacinin_Turkceye_Optimizasyonu.pdf)
