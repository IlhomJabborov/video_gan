

# GFPGAN Video Enhancer

GFPGAN Video Enhancer - bu video fayllardagi xira joylarni aniqlash va ularni tiniqlashtirish uchun mo'ljallangan dastur. Ushbu dastur GFPGAN (Generative Facial Prior-Generative Adversarial Network) modelidan foydalanadi va foydalanuvchilarga videolarini sifatini oshirish imkoniyatini beradi.

## Talablar

Dastur vositalari va kutubxonalarini o'rnatish uchun quyidagilar talab qilinadi:

- Python 3.10
- **`ffmpeg`** (video fayllarni qayta ishlash uchun)
- Mavjud kutubxonalar ( **requirements.tx** da ko'rsatilgan)

## O'rnatish
**1.Loyihani yuklab oling:**
* GitHub dan loyihani yuklab olish:
  ```
  git clone https://github.com/IlhomJabborov/video_gan.git
  ```
* Loyiha ichiga kirish :
  ```
  cd video_gan
  ```
**2.Talab qilinadigan kutubxonalarni o'rnating:**
```
pip install basicsr

pip install facexlib

pip install -r requirements.txt
```
- Agar siz **python3.10** dan foydalanmayotgan bo'lsangiz shunchaki **python** buyrug'ini ishlating
```
python3.10 setup.py develop
```
```
pip install realesrgan
```
**3.Modelni yuklab olish :**
```
wget https://github.com/TencentARC/GFPGAN/releases/download/v0.2.0/GFPGANCleanv1-NoCE-C2.pth -P experiments/pretrained_models
```
**4.ffmpeg ni o'rnating:**
* Ubuntu uchun:
  ```
  sudo apt update
  sudo apt install ffmpeg
  ```
**! Windows yoki MacOS uchun ffmpeg rasmiy veb-saytidan yuklab oling va o'rnating.** 

## Qo'llanma
1. **Dasturdan foydalanish uchun main.py faylini quyidagi tarzda ishga tushiring:**
  ```
  python3.10 main.py
  ```
2. **[ Video ni Joylang ] yozuvi chiqadi.**
3. **Xira videoni **[ videos ]** fayliga joylang**
4. **[ Video generatsiya boshlansinmi ? ] savoliga [ ha ] deb yozing**
5. **Qayta ishlangan video **[ results_mp4_videos ]** faylida paydo bo'ladi.( .mp4 formatida)**

## Xatoliklar bilan bog'liq muammolar

### Agar siz Xatolik xabarlarini ko'rsangiz, quyidagi qadamlarni bajaring:

* ffmpeg o'rnatilganligini tekshiring.
* Python kutubxonalari to'g'ri o'rnatilganligini va ularning talablariga amal qiling.
* **torchvision.transforms.functional_tensor** bog'liq muammoni quydagicha hal qiling :
```
sed -i 's/torchvision.transforms.functional_tensor import/torchvision.transforms.functional import/' XATOLIK-KO'RSATAYOTGAN-FAYL-PATH
```

**XATOLIK-KO'RSATAYOTGAN-FAYL-PATH ni xatolik ko'rsatayotgan fayl manzili bilan almashtiring.Misol uchun :**
```
sed -i 's/torchvision.transforms.functional_tensor import/torchvision.transforms.functional import/' /usr/local/lib/python3.10/dist-packages/basicsr/data/degradations.py
```

## Mualliflar
### Ilhom Jabborov

### 2024

