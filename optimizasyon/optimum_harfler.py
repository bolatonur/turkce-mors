import csv

# Bu kodla mors kodlarını oluşturup bir CSV dosyasına yazdırıyoruz. Nokta ve çizgi karakterlerini kullanarak tüm kombinasyonları oluşturuyoruz ve her kombinasyonun uzunluğunu hesaplayarak dosyaya yazıyoruz. Sonrasında dosyayı okuyup, uzunluklarına göre sıralıyoruz ve tekrar dosyaya yazıyoruz.

nokta = 1
cizgi = 3
bosluk = 1

dosya_adi = r'mors.csv'
karakterler = [nokta, cizgi]

isim = {nokta: '.', cizgi: '_'}

with open(dosya_adi, mode='w', newline='') as f:
    writer = csv.writer(f)

    for i in karakterler:
        uz_i = i
        writer.writerow([isim[i], uz_i])
        
        for j in karakterler:
            uz_j = uz_i + j + bosluk
            writer.writerow([isim[i], isim[j], uz_j])
            
            for k in karakterler:
                uz_k = uz_j + k + bosluk
                writer.writerow([isim[i], isim[j], isim[k], uz_k])
                
                for l in karakterler:
                    uz_l = uz_k + l + bosluk
                    writer.writerow([isim[i], isim[j], isim[k], isim[l], uz_l])
                    
                    for m in karakterler:
                        uz_m = uz_l + m + bosluk
                        writer.writerow([isim[i], isim[j], isim[k], isim[l], isim[m], uz_m])

with open(dosya_adi, 'r') as f:
    reader = csv.reader(f)
    data = list(reader)


sirali_data = sorted(data, key=lambda satir: (float(satir[-1]), len(satir)))

with open(dosya_adi, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sirali_data)