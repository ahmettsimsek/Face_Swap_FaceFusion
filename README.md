# Face_Swap_FaceFusion

![Image](https://github.com/user-attachments/assets/c6b4cb0b-2d74-4925-9094-3e1aa30942ea)
![Image](https://github.com/user-attachments/assets/8412933e-f146-4513-a60b-f217875864ca)
![Image](https://github.com/user-attachments/assets/224ed787-fb24-4cc3-9576-334ac72f567d)


🛠️ FaceFusion Kurulum ve Başlatma Süreci (Windows için)
Aşağıdaki adımları takip ederek FaceFusion'u kolayca kurabilir ve kullanmaya başlayabilirsiniz.

### ✅ 1. Gereksinimler
Python 3.10
İndir: https://www.python.org/downloads/release/python-3100/

⚠️ Kurulum sırasında “Add to PATH” kutusunu işaretlemeyi unutmayın.

Git (opsiyonel ama önerilir)

### ✅ 2. Projeyi Klonla
```python
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
---------------------------------------------------------------------------------------------------------------------

(****** result ismini ve job ismini değiştirmeyi unutma(örn: job2)) ve *** png veya jpg tür karıştırma


---Yeni bir job ID kullanarak işlemi tekrar deneyelim (örneğin: job1):

1. Yeni job oluştur
```
python facefusion.py job-create job1
```

2. Yeni step ekle
```
python facefusion.py job-add-step job1 --source inputs/source.png --target inputs/target.png --output-path outputs/result1.png  
```
3. Submit
```
python facefusion.py job-submit job1
```
4. Run
```
python facefusion.py job-run job1
```
------------------------------------------------------------------------------
![Image](https://github.com/user-attachments/assets/99cf3da7-3e92-45ee-b87d-17f59441d703)
------------------------------------------------------------------------------
```
python facefusion.py job-create job2
```
```
python facefusion.py job-add-step job2 --source inputs/source.png --target inputs/target.png --output-path outputs/result2.png
```
```
python facefusion.py job-submit job2
```
```
python facefusion.py job-run job2
```
----------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------
![Image](https://github.com/user-attachments/assets/12aa45ee-a053-4145-b4cf-05f4b88a8888)

