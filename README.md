# Face_Swap_FaceFusion
🛠️ FaceFusion Kurulum ve Başlatma Süreci (Windows için)
Aşağıdaki adımları takip ederek FaceFusion'u kolayca kurabilir ve kullanmaya başlayabilirsiniz.

### ✅ 1. Gereksinimler
Python 3.10
İndir: https://www.python.org/downloads/release/python-3100/

⚠️ Kurulum sırasında “Add to PATH” kutusunu işaretlemeyi unutmayın.

Git (opsiyonel ama önerilir)

### ✅ 2. Projeyi Klonla
```
cd %USERPROFILE%\Desktop
```
```
git clone https://github.com/facefusion/facefusion.git
```
```
cd facefusion
```

### ✅ 3. Sanal Ortam Oluştur ve Aktifleştir
```
python -m venv venv
```
```
venv\Scripts\activate
```

### ✅ 4. Gerekli Kütüphaneleri Yükle
```
pip install -r requirements.txt
```

### ✅ 5. FFmpeg Kurulumu (Zorunlu)
FaceFusion, video ve görsel işleme için FFmpeg kullanır.

İndir: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip

ZIP dosyasını çıkarın ve C:\ffmpeg\bin dizinine taşıyın

C:\ffmpeg\bin yolunu sistem PATH değişkenine ekleyin

CMD'de test edin:

```
ffmpeg -version
```

### ✅ 6. FaceFusion’u Başlat
```
python facefusion.py run
```
GUI arayüzü tarayıcınızda otomatik olarak açılacaktır:
🔗 http://127.0.0.1:7860

### ✅ 7. Kullanım
Source Image: Yüzünü içeren görüntüyü yükle

Target Image: Yüzün aktarılacağı hedef görüntüyü yükle

Ayarları yap (isteğe bağlı): Face Enhancer (GFPGAN vb.), Device (CUDA/CPU)

Start / Swap butonuna tıkla

Çıktı output/ klasörüne kaydedilir

Kurulum sonrası ilk kullanımda tüm modeller otomatik olarak indirilecektir.

Sorun yaşarsanız: --help parametresi ile komut listesini görüntüleyebilirsiniz.

```
python facefusion.py --help
```
