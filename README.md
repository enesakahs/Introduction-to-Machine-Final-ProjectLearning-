# Introduction-to-Machine-Final-ProjectLearning-
mushroom classification

**Proje Adı: Mantar Sınıflandırma: Zehirli mi, Yenilebilir mi?**

**Açıklama**: Bu proje, Kaggle.com'dan alınan "Mantar Sınıflandırma" veri kümesi kullanılarak mantarların zehirli veya yenilebilir olup olmadığını tahmin etmeyi amaçlamaktadır. 23 tür gilled mantarın hipotetik örneklerinin tanımlarını içeren bu veri kümesinde, her bir tür yenilebilir veya zehirli olarak belirtilmiştir. Mantarlarla ilgili edibilitenin belirlenmesi genellikle basit bir kurala dayanmaz, bu nedenle makine öğrenimi modellerini kullanarak bu sınıflandırma problemi çözülmeye çalışılacaktır.

**Kullanılan Modeller**: Bu sınıflandırma problemi için, farklı makine öğrenimi modelleri kullanılmıştır. Bu modeller şunlardır:


_*Lojistik Regresyon
*Ridge Sınıflandırıcısı
*Karar Ağacı
*Naive Bayes
*Yapay Sinir Ağı (MLP)
*Random Forest_

**Veri Ön İşleme**: Veri kümesi 8124 mantar örneğinden oluşmaktadır ve her bir örnek 22 özelliğe sahiptir. "cap-shape", "cap-color", "ring-number" ve "ring-type" özellikleri kullanılarak veri özellikler ve etiketlere ayrılmıştır. Etiketler, "edible" ve "poisonous" olarak kodlanmıştır ve özellikler de label encoding yöntemiyle sayısal değerlere dönüştürülmüştür.

**Model Eğitimi ve Değerlendirme**: Veri kümesi eğitim ve test kümelerine bölünmüş ve farklı modeller üzerinde eğitim gerçekleştirilmiştir. Sonuçlar, her bir model için doğruluk, kesinlik, hatırlama ve F1 puanlarını içeren sınıflandırma raporları aracılığıyla değerlendirilmiştir. Ayrıca, karşılaştırmalı bir analiz için Random Forest modeli de eklenmiştir.

**Sonuçlar**: Projenin sonuçları, farklı modellerin performanslarını değerlendiren sınıflandırma raporları ve karmaşıklık matrisleri ile görselleştirilmiştir. Bu sayede, hangi modelin mantar sınıflandırma görevinde en iyi performansı sergilediği belirlenmiştir.

**Sonuç**: Proje, makine öğrenimi modelleri kullanarak mantarların zehirli veya yenilebilir olup olmadığını tahmin etme görevini başarıyla tamamlamıştır. Karar ağacı modelinin diğer modellere göre daha iyi performans gösterdiği saptanmıştır. Bu çalışma, mantarların türünü belirlemek için hızlı ve etkili bir yöntem sunarak, gıda güvenliği ve doğal yaşam açısından önemli bir uygulama alanına sahip olabilir.
