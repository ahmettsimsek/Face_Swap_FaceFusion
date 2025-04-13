import os
import random
from datetime import datetime
from deepface import DeepFace


# 1. Kaynak görsel
source_image = "inputs/source.png"

# 2. Cinsiyet tespiti
print("🔎 Yüz analizi yapılıyor...")
result = DeepFace.analyze(img_path=source_image, actions=["gender"])
gender_prediction = result[0]['gender']
gender = "female" if gender_prediction['Woman'] > gender_prediction['Man'] else "male"
print("👤 Tespit edilen cinsiyet:", gender)

# 3. Temaya göre hedef seç
theme_dir = f"inputs/themes/{gender}"
target_candidates = [f for f in os.listdir(theme_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

if not target_candidates:
    raise Exception(f"{theme_dir} klasöründe kullanılabilir target görseli yok!")

target_image = random.choice(target_candidates)
target_path = os.path.join(theme_dir, target_image)
print("🎯 Seçilen tema hedefi:", target_path)

# 4. Benzersiz job ID üret
job_id = f"job_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

# 5. Job oluştur
os.system(f"python facefusion.py job-create {job_id}")

# 6. Step ekle
output_file = f"outputs/output_image_{job_id}.jpeg"
os.system(
    f"python facefusion.py job-add-step {job_id} "
    f"--source {source_image} "
    f"--target {target_path} "
    f"--output-path {output_file} "
    f"--output-image-quality 100 "
    f"--output-image-resolution 2048x2048 "
    f"--face-enhancer-model codeformer "
    f"--face-enhancer-blend 100 "
)

# 7. Submit ve çalıştır
os.system(f"python facefusion.py job-submit {job_id}")
os.system(f"python facefusion.py job-run {job_id}")

# 8. Çıktıyı aç
print("✅ İşlem tamamlandı, çıktı açılıyor...")
os.system(f"start {output_file}")
