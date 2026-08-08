import PyPDF2
import os
import collections
import re

#Bu kodla girilen klasördeki tüm PDF dosyalarını okuyup, içindeki harflerin frekansını sayıyoruz ve sonuçları bir txt dosyasına kaydediyoruz. Kullanıcıdan klasör yolunu alıyoruz ve Türkçe veya İngilizce dil seçimi yapmasını istiyoruz. Seçime göre ilgili frekans dosyasına verileri yazıyoruz.


def update_frequency_file(file_path, new_counts):
    """
    Mevcut txt dosyasını okur, verileri günceller ve tekrar yazar.
    """
    current_data = collections.Counter()
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    try:
                        char, count_part = line.split(':')
                        char = char.strip()
                        count = int(re.search(r'\d+', count_part).group())
                        current_data[char] = count
                    except:
                        continue

    current_data.update(new_counts)

    with open(file_path, 'w', encoding='utf-8') as f:
        for char in sorted(current_data.keys()):
            f.write(f"{char}: {current_data[char]} adet\n")

def process_pdf(pdf_path, lang_file):
    """
    Tek bir PDF dosyasını okur ve harfleri sayar.
    """
    valid_chars_pattern = re.compile(r'[a-zA-ZçğıöşüÇĞİÖŞÜ]')
    char_counts = collections.Counter()
    
    try:
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    found_chars = valid_chars_pattern.findall(text.lower())
                    char_counts.update(found_chars)
        
        update_frequency_file(lang_file, char_counts)
        return True
    except Exception as e:
        print(f"Hata oluştu ({os.path.basename(pdf_path)}): {e}")
        return False

def process_folder(folder_path, lang_file):
    """
    Klasördeki tüm PDF'leri bulur ve sırayla işler.
    """
    # Klasördeki .pdf uzantılı dosyaları bul
    files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    
    if not files:
        print("\nHata: Klasörde PDF dosyası bulunamadı.")
        return

    print(f"\n{len(files)} adet PDF dosyası bulundu. İşlem başlıyor...")
    
    for index, file_name in enumerate(files, 1):
        full_path = os.path.join(folder_path, file_name)
        print(f"[{index}/{len(files)}] İşleniyor: {file_name}")
        process_pdf(full_path, lang_file)
    
    print(f"\nİşlem başarıyla tamamlandı. Veriler '{lang_file}' dosyasına kaydedildi.")

if __name__ == "__main__":
    print("\n--- Toplu PDF Karakter Frekans Sayıcı ---")
    raw_path = input("PDF'lerin bulunduğu KLASÖR yolunu girin: ").strip()
    
    # macOS/Linux terminal kaçış karakterlerini ve tırnakları temizleme
    clean_path = raw_path.replace('\\ ', ' ').replace("'", "").replace('"', '')
    
    # Eğer yolun sonunda hala kaçış karakteri varsa temizle
    clean_path = os.path.abspath(clean_path)

    if not os.path.isdir(clean_path):
        print(f"\nHata: '{clean_path}' geçerli bir klasör yolu değil!")
        print("Lütfen yolu kontrol edin veya klasörü terminale sürükleyip bırakın.")
    else:
        print("\nDil Seçimi:")
        print("1 - Türkçe (turkce_frekans.txt)")
        print("2 - İngilizce (ingilizce_frekans.txt)")
        secim = input("Seçiminiz (1/2): ").strip()

        if secim == "1":
            process_folder(clean_path, "turkce_frekans.txt")
        elif secim == "2":
            process_folder(clean_path, "ingilizce_frekans.txt")
        else:
            print("Geçersiz seçim. Program sonlandırıldı.")