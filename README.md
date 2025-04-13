# Face_Swap_FaceFusion

## Komut istemcisi üzerinden job ID kullanarak:
![Image](https://github.com/user-attachments/assets/02c91744-864e-4252-8729-a5514305e3a5)
![Image](https://github.com/user-attachments/assets/9625a045-a5c8-4f57-8a34-a5fe113e05ee)
----------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------
## GUI arayüzü :
![Image](https://github.com/user-attachments/assets/971b2e9d-eba3-46dd-ba33-1ca95c9f1bdc)
----------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------
## ✅✅✅✅✅ GUI arayüzü ile:✅✅✅✅✅

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
```python
git clone https://github.com/facefusion/facefusion.git
```
```python
cd facefusion
```

### ✅ 3. Sanal Ortam Oluştur ve Aktifleştir
```python
python -m venv venv
```
```python
venv\Scripts\activate
```

### ✅ 4. Gerekli Kütüphaneleri Yükle
```python
pip install -r requirements.txt
```

### ✅ 5. FFmpeg Kurulumu (Zorunlu)
FaceFusion, video ve görsel işleme için FFmpeg kullanır.

İndir: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip

ZIP dosyasını çıkarın ve C:\ffmpeg\bin dizinine taşıyın

C:\ffmpeg\bin yolunu sistem PATH değişkenine ekleyin

CMD'de test edin:

```python
ffmpeg -version
```

### ✅ 6. FaceFusion’u Başlat
```python
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

```python
python facefusion.py --help
```
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
## ✅✅✅✅✅ Komut istemcisi üzerinden job ID kullanarak:✅✅✅✅✅

(****** result ismini ve job ismini değiştirmeyi unutma(örn: job2)) ve *** png veya jpg tür karıştırma


---Yeni bir job ID kullanarak işlemi tekrar deneyelim (örneğin: job1):

1. Yeni job oluştur
```python
python facefusion.py job-create job1
```

2. Yeni step ekle
```python
python facefusion.py job-add-step job1 --source inputs/source.png --target inputs/target.png --output-path outputs/result1.png  
```
3. Submit
```python
python facefusion.py job-submit job1
```
4. Run
```python
python facefusion.py job-run job1
```
------------------------------------------------------------------------------
![Image](https://github.com/user-attachments/assets/99cf3da7-3e92-45ee-b87d-17f59441d703)
------------------------------------------------------------------------------
```python
python facefusion.py job-create job2
```
```python
python facefusion.py job-add-step job2 --source inputs/source.png --target inputs/target.png --output-path outputs/result2.png
```
```python
python facefusion.py job-submit job2
```
```python
python facefusion.py job-run job2
```

