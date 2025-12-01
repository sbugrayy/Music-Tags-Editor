# Music-Tags-Editor 🎵

[🇬🇧 English](#english) | [🇹🇷 Türkçe](#-türkçe)

---

## 🇬🇧 English

A Python tool developed to organize your personal music archive by automatically editing metadata (ID3) tags of MP3 and other audio files by analyzing file names.

### 🎯 Project Purpose

Instead of manually dealing with Windows file properties one by one; it scans music files in a folder and automatically assigns albums and artists based on keywords found in file names (e.g., "slowed", "speed up", "çat"). This project automates the manual tagging process, organizing your music library in seconds.

### ✨ Features

* **Wide Format Support:** Supports .mp3, .wav, .flac, .ogg, .m4a, .wma, .ape, .wv formats.

* **Smart Album Assignment:** Assigns songs to relevant albums based on special keywords found in file names.

    * *Example:*
    
    * "slowed" → Speed Electro album
    
    * "çat" → Çat album

* **Automatic Titling:** Cleans the file name and processes it as the song title (Title).

* **Batch Processing:** Analyzes and updates hundreds of files in a folder with a single run.

* **Customizable:** You can customize keywords and album names according to your needs.

### 🛠️ Installation

To install the required library, run the following command in the terminal:

```bash
pip install mutagen
```

### ⚙️ Configuration (Important)

You need to make some changes in the `main.py` file before running the program.

#### Edit the folder path

```python
klasor_yolu = r"C:\Users\YourUsername\Music\Archive"
```

#### Default album and artist settings

```python
varsayilan_album = "Electro"
varsayilan_album_sanaticisi = "Subnine"
varsayilan_katkida_bulunan_sanaticilar = "Subnine"
```

#### Special album settings

The program searches for specific keywords in file names and assigns songs to special albums. You can customize these settings according to your needs:

##### Speed/Slowed Album

For songs with "slowed" or "speed up" keywords in the file name:

```python
ozel_album_speed = "Speed Electro"
ozel_album_speed_sanaticisi = "Subnine"
ozel_katkida_bulunan_sanaticilar_speed = "Subnine"
```

##### Çat Album

For songs with "çat" keyword in the file name:

```python
ozel_album_cat = "Çat"
ozel_album_cat_sanaticisi = "Subnine"
ozel_katkida_bulunan_sanaticilar_cat = "Subnine"
```

#### Adding Your Own Custom Keywords

To add your own custom keywords, you can edit the control block in the `etiketleri_guncelle` function. For example, if you want to add a new album for the "remix" keyword:

1. First, define the variables:

```python
ozel_album_remix = "Remix Collection"
ozel_album_remix_sanaticisi = "Artist Name"
ozel_katkida_bulunan_sanaticilar_remix = "Artist Name"
```

2. Then add it to the if-elif block in the `etiketleri_guncelle` function:

```python
elif "remix" in yeni_baslik.lower():
    print(f"  'remix' found in '{yeni_baslik}'. Assigning to '{ozel_album_remix}' album.")
    current_album = ozel_album_remix
    current_album_artist = ozel_album_remix_sanaticisi
    current_contributing_artists = ozel_katkida_bulunan_sanaticilar_remix
```

**Note:** The order of checks is important. The first matching condition is used, so it may be better to check more specific keywords first.

### 💻 Usage

To run the program:

```bash
python main.py
```

The program scans the folder, updates tags, and reports how many files were processed.

### 📚 Technologies Used

* Python 3
* Mutagen
* OS & Path

### 📄 License

This project is distributed under the MIT License.

---

## 🇹🇷 Türkçe

Kişisel müzik arşivinizi organize etmek için geliştirilmiş, dosya isimlerini analiz ederek MP3 ve diğer ses dosyalarının metadata (ID3) etiketlerini otomatik olarak düzenleyen Python aracı.

### 🎯 Projenin Amacı

Windows dosya özellikleriyle tek tek uğraşmak yerine; klasördeki müzikleri tarayıp dosya isminde geçen anahtar kelimelere (örn: "slowed", "speed up", "çat") göre otomatik albüm ve sanatçı ataması yapar. Bu proje, manuel etiketleme sürecini otomatize ederek müzik kütüphanenizi saniyeler içinde düzenler.

### ✨ Özellikler

* **Geniş Format Desteği:** .mp3, .wav, .flac, .ogg, .m4a, .wma, .ape, .wv formatlarını destekler.

* **Akıllı Albümleme:** Dosya isminde geçen özel kelimelere göre şarkıyı ilgili albüme atar.

    * *Örnek:*
    
    * "slowed" → Speed Electro albümü
    
    * "çat" → Çat albümü

* **Otomatik Başlıklandırma:** Dosya ismini temizleyerek şarkı başlığı (Title) olarak işler.

* **Toplu İşlem:** Tek çalıştırmada klasördeki yüzlerce dosyayı analiz eder ve günceller.

* **Özelleştirilebilir:** Anahtar kelimeleri ve albüm isimlerini kendi ihtiyaçlarınıza göre düzenleyebilirsiniz.

### 🛠️ Kurulum

Gerekli kütüphaneyi yüklemek için terminalde şu komutu çalıştırın:

```bash
pip install mutagen
```

### ⚙️ Yapılandırma (Önemli)

Programı çalıştırmadan önce `main.py` dosyasında bazı değişiklikler yapmalısınız.

#### Klasör yolunu düzenleyin

```python
klasor_yolu = r"C:\Users\KullaniciAdiniz\Music\Arsivim"
```

#### Varsayılan albüm ve sanatçı ayarları

```python
varsayilan_album = "Electro"
varsayilan_album_sanaticisi = "Subnine"
varsayilan_katkida_bulunan_sanaticilar = "Subnine"
```

#### Özel albüm ayarları

Program, dosya isimlerinde belirli anahtar kelimeleri arayarak şarkıları özel albümlere atar. Bu ayarları kendi ihtiyaçlarınıza göre özelleştirebilirsiniz:

##### Speed/Slowed Albümü

Dosya isminde "slowed" veya "speed up" kelimeleri geçen şarkılar için:

```python
ozel_album_speed = "Speed Electro"
ozel_album_speed_sanaticisi = "Subnine"
ozel_katkida_bulunan_sanaticilar_speed = "Subnine"
```

##### Çat Albümü

Dosya isminde "çat" kelimesi geçen şarkılar için:

```python
ozel_album_cat = "Çat"
ozel_album_cat_sanaticisi = "Subnine"
ozel_katkida_bulunan_sanaticilar_cat = "Subnine"
```

#### Kendi Özel Kelimelerinizi Eklemek

Kendi özel kelimelerinizi eklemek için `etiketleri_guncelle` fonksiyonundaki kontrol bloğunu düzenleyebilirsiniz. Örneğin, "remix" kelimesi için yeni bir albüm eklemek istiyorsanız:

1. Önce değişkenleri tanımlayın:

```python
ozel_album_remix = "Remix Koleksiyonu"
ozel_album_remix_sanaticisi = "Sanatçı Adı"
ozel_katkida_bulunan_sanaticilar_remix = "Sanatçı Adı"
```

2. Sonra `etiketleri_guncelle` fonksiyonundaki if-elif bloğuna ekleyin:

```python
elif "remix" in yeni_baslik.lower():
    print(f"  '{yeni_baslik}' başlığında 'remix' bulundu. '{ozel_album_remix}' albümüne atanıyor.")
    current_album = ozel_album_remix
    current_album_artist = ozel_album_remix_sanaticisi
    current_contributing_artists = ozel_katkida_bulunan_sanaticilar_remix
```

**Not:** Kontrol sırası önemlidir. İlk eşleşen koşul kullanılır, bu yüzden daha spesifik kelimeleri önce kontrol etmek daha iyi olabilir.

### 💻 Kullanım

Programı çalıştırmak için:

```bash
python main.py
```

Program klasörü tarar, etiketleri günceller ve kaç dosyanın işlem gördüğünü raporlar.

### 📚 Kullanılan Teknolojiler

* Python 3
* Mutagen
* OS & Path

### 📄 Lisans

Bu proje MIT Lisansı ile dağıtılmaktadır.
