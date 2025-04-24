 El Hareketleriyle Sembolik Tanıma

Bu proje, **Mediapipe** ve **OpenCV** kullanarak gerçek zamanlı olarak el işaretlerini tanımayı amaçlar.
Kameradan gelen görüntü üzerinde belirli el sembolleri (Bozkurt, Zafer, AKP işareti) algılanarak sınıflandırılır ve ekrana yansıtılır.

 Amaç
- El hareketlerini algılayarak sembol tanıma gerçekleştirmek
- Kamera görüntüsü üzerinden anlık tespit ve görselleştirme yapmak
- Python ile görüntü işleme ve makine görüşü temellerini uygulamak

 Tanınan El İşaretleri
| İşaret Adı       | Açıklama                            

| Zafer İşareti    | İşaret ve orta parmak açık                    
| Bozkurt İşareti  | İşaret ve serçe parmak açık, diğerleri kapalı 
| AKP İşareti      | Tüm parmaklar açık, başparmak sağa açık       

Kullanılan Kütüphaneler
- OpenCV
- MediaPipe
- NumPy

 Kurulum
pip install opencv-python mediapipe numpy

 Kullanım
python el_isareti_tanima.py
