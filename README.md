# Knn

KNN (K Nearest Neighbor) algoritması yapay zekâda girdileri elimizdeki kategorilerden hangisine benzediğini tahmin etmek için kullanılan sınıflandırma algoritmalarından biridir. Girdinin hangi sınıfa ait olduğu girdiye benzeyen K tane verinin seçilmesi ile tahmin edilir.

Python dilinde iris veriseti kullanılarak yaptığım bir uygulamadır.

# Eksikleri
- Sadece iris.xlsx ile denenmiştir.

# Çalışma mantığı
Training, Test ve Result adında excel formatında çıktılar vermektedir.

iris veri setinin 5 satırından 4 tanesini Training dizisine, 1 tanesini Test dizisine atmaktadır. 
Bu durum config_sets fonksiyonunda değiştirilebilir.

iris veriseti iki diziye bölünmektedir. Bu iki diziye verilerin kendileri değil indis değerleri eklenmektedir.

# Kurulum
```
pip3 install -r requirements
```
