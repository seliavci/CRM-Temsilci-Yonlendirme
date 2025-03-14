CRM Temsilci Yönlendirme ve Pazarlama Kampanyası Seçimi Projesi

Bu proje, bir CRM (Müşteri İlişkileri Yönetimi) sisteminde iki temel işlevi optimize etmek için dinamik programlama (Dynamic Programming) tekniklerini kullanır:

Müşteri Destek Temsilcisi Yönlendirme
Pazarlama Kampanyası Seçimi


Proje Amacı
Bu projede, CRM sistemindeki müşteri destek temsilcilerinin müşterilere yönlendirilmesi ve bütçe kısıtları altında en yüksek yatırım getirisi (ROI) sağlayacak pazarlama kampanyalarının seçilmesi amaçlanmıştır. 
Her iki işlev de dinamik programlama ilkeleri kullanılarak optimize edilmiştir.


Proje Özeti
Müşteri Destek Temsilcisi Yönlendirme:

Müşteri talepleri ve temsilcilerin uygunluk seviyeleri dikkate alınarak her müşteri için en uygun destek temsilcisi seçilir.
Müşteri talepleri, temsilcilerin yetkinliklerine göre karşılanır ve en verimli yönlendirme yapılır.

Pazarlama Kampanyası Seçimi:
Verilen bütçe kısıtlamaları altında, her kampanyanın maliyeti ve beklenen getirisi değerlendirilerek, maksimum ROI sağlayan pazarlama kampanyaları seçilir.


Dinamik Programlama Kullanımı
Dinamik Programlama (DP), optimize edilecek problemlerde alt problemlerin çözümünü birbirine bağlayarak, daha büyük bir problemi çözme yaklaşımını benimser.
Bu projede, her iki işlevde de karar verme süreci dinamik programlama ile çözülmüştür.

Temsilci Yönlendirme: Müşteri taleplerini ve temsilcilerin uygunluklarını dikkate alarak en uygun temsilcinin atanması.

Pazarlama Kampanyası Seçimi: Bütçe kısıtları ve beklenen ROI'yi dikkate alarak en verimli pazarlama kampanyalarının seçilmesi.


Kullanılan Yöntemler
Dinamik Programlama (Dynamic Programming): Projede her iki işlevin optimizasyonunda da dinamik programlama teknikleri kullanılmıştır.

Python Programlama Dili: Python dilinde yazılmıştır, bu sayede hem okunabilir hem de verimli bir çözüm sağlanmıştır.


Nasıl Çalışır?
Müşteri Destek Temsilcisi Yönlendirme
Sistemdeki her müşteri ve temsilci için bir dizi parametre tanımlanır (müşteri talepleri, temsilcinin yetkinliği vs.).
Dinamik programlama algoritması, her müşteri için en uygun temsilciyi seçer.

Pazarlama Kampanyası Seçimi
Bütçe, kampanyaların maliyeti ve beklenen getirisini göz önünde bulundurularak en uygun kampanyalar seçilir.
Bu işlem dinamik programlama kullanılarak en yüksek ROI'yi sağlayacak şekilde yapılır.


Proje Yapısı
crm_temsilci_yonlendirme.py: Temsilci yönlendirme algoritmasını içeren Python dosyası.

pazarlama_kampanyasi_seçimi.py: Pazarlama kampanyası seçim algoritmasını içeren Python dosyası.

main.py: Ana dosya, her iki algoritmanın da test edilmesini ve sonuçların ekrana yazdırılmasını sağlar.


Dinamik Programlama ve Avantajları
Dinamik programlama, özellikle optimize edilecek problemlerde alt problemlerin çözümünü birbirine bağlayarak çözümler sağlar. Bu proje, temsilci yönlendirme ve pazarlama kampanyası seçimi gibi optimizasyon problemleri için dinamik programlamanın ne kadar etkili olduğunu göstermektedir.

Avantajları:
Karmaşık ve büyük ölçekli problemlerin çözülmesini sağlar.
Çoğu durumda, çözümün zaman karmaşıklığını azaltır.
Verimli ve doğru sonuçlar üretir.


Lisans
Bu proje, MIT Lisansı ile lisanslanmıştır.





























