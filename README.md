# Music-Tags-Editor 🎵

Kişisel müzik arşivinizi organize etmek için geliştirilmiş, dosya isimlerini analiz ederek MP3 ve diğer ses dosyalarının metadata (ID3) etiketlerini otomatik olarak düzenleyen Python aracı.

## 🎯 Projenin Amacı

Windows dosya özellikleriyle tek tek uğraşmak yerine; klasördeki müzikleri tarayıp dosya isminde geçen anahtar kelimelere (örn: "slowed", "speed up", "çat") göre otomatik albüm ve sanatçı ataması yapar. Bu proje, manuel etiketleme sürecini otomatize ederek müzik kütüphanenizi saniyeler içinde düzenler.

## ✨ Özellikler

* **Geniş Format Desteği:** .mp3, .wav, .flac, .ogg, .m4a, .wma, .ape, .wv formatlarını destekler.

* **Akıllı Albümleme:** Dosya isminde geçen özel kelimelere göre şarkıyı ilgili albüme atar.

    * *Örnek:*
    
    * "slowed" → Speed Electro albümü
    
    * "çat" → Çat albümü

* **Otomatik Başlıklandırma:** Dosya ismini temizleyerek şarkı başlığı (Title) olarak işler.

* **Toplu İşlem:** Tek çalıştırmada klasördeki yüzlerce dosyayı analiz eder ve günceller.

## 🛠️ Kurulum

Gerekli kütüphaneyi yüklemek için terminalde şu komutu çalıştırın:

```bash
pip install mutagen
```

## ⚙️ Yapılandırma (Önemli)

Programı çalıştırmadan önce main.py dosyasında bazı değişiklikler yapmalısınız.

### Klasör yolunu düzenleyin

```python
KLASOR_YOLU = r"C:\Users\KullaniciAdiniz\Music\Arsivim"
```

### Varsayılan albüm ve sanatçı ayarları

```python
VARSAYILAN_ALBUM = "Favori Listem"
VARSAYILAN_ALBUM_SANATCISI = "Çeşitli Sanatçılar"
```

## 💻 Kullanım

Programı çalıştırmak için:

```bash
python main.py
```

Program klasörü tarar, etiketleri günceller ve kaç dosyanın işlem gördüğünü raporlar.

## 📚 Kullanılan Teknolojiler

* Python 3
* Mutagen
* OS & Path

## 📄 Lisans

Bu proje MIT Lisansı ile dağıtılmaktadır.
