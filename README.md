# bidirectional-associative-memory
 A python implementation of a BAM
1.slayt
Çift Yönlü ilişkisel Bellek (BAM), Yapay Sinir Ağlarında denetimli bir ogrenme modelidir.Denetimli öğrenme kanita dayalı tahminler oluşturur.Bilinen bir girdi verisini alır ve yeni veriler için tahminler oluşturur. Bu hetero-ilişkisel bellektir, bir giriş modeli için potansiyel olarak farklı boyutta başka bir model döndürür.İnsan beynine çok benzer. Insan hafızası zorunlu olarak çağrışımsaldır. Kayıp bir hafızayı kurtarmak için yuzlerin isimlerle, sinav sorularında cevaplarla, vb. ilişkilendirmeleri gibi bir zihinsel cağrışimlar zincirini kullanır.

(BAM), ilk olarak 1980lerin başında Bart Kosko tarafından önerilen, otomatik ilişkisel Tek Yönlü Hopfield ağının ve çağrışımlanı öğrenen YSAların bilinen birkaç dezavantajınin üstesinden gelmeye çalışan özel bir türde tekrarlayan sinir ağıdır (RNN).

Girdi olarak bir nöron kümesinin bir modeli ve başka bir nöron kümesinin ilişkili, ancak farkli bir çikti modelini üretir.

2.slayt
Verilerin çağnışımları, BAM'in belleğinden geri çagrılmadan önce yalnızca bir kez eşzamanlı olarak saklanır Normalde BAM, mevcut YSA'ları geride bırakarak, çağnışımları geri çağınırken önemli ölçüde daha iyi performans sağlar. Ayrıca BAM kullanmak, mevcut YSA'lara kıyasla bilinen bitsel XOR problemini mukemmel bir şekilde çözer, bu da ikili (bipolar) biçimde kodlanmış verilerin hafızasında saklanmasını mümkün kılar.

BAM neden gereklidir? Böyle bir ağ modelini tanıtmanin temel amacı, hetero-ilişkisel model çiftlerini depolamaktır.

Bu, eksik bir model verilen bir kalıbı

almak için kullanılır.

Tek yönlü Hopfield ağından farklı olarak BAM, girişlerine veya çıkışlarına atanan veri ilişkilerini çift yönlü olarak geri çağirma yeteneğine sahiptir. Ayrica, eksik veya bozuk ginş venleri için bile doğru ilişkilendirmelerin alınmasını sağlar

3.slayt
BAM Mimarisi: BAM, A kümesinden n-boyutlu X vektörünün bir girdisini kabul ettiğinde, model B kümesinden m boyutlu Y vektörünü geri çağınır. Benzer şekilde, Y girdi olarak ele alındığinda, BAM, Xi geri çağınır.

4.slayt 
Bam modeli
Bam modelini oluşturmak için üç ana adım vardır.
Learning
Testing
Retrieval

5.slayt
Set A: giriş modelleri
Set B: karşılık gelen hedef modelleri

Adım 1: Burada M'nin değeri (örüntü çifti sayısı) 4'tür.

Adım 2: Girdi ve çıktı katmanındaki nöronlari atayın. Burada giriş katmanındaki nöronlar 6 ve çıkış katmanı 3'tür

Adım 3: Şimdi Ağırlık Matrisini (W) hesaplayın:

6.slayt


Adım 3: Şimdi Ağırlk Matrisini (W) hesaplayin:



Adım 4: BAM modeli öğrenme algoritmasını test edin-giriş kalıpları için BAM, karşılık gelen hedef kalıpları çıktı olarak döndürür. Ve hedef kalıpların her biri için BAM, karşılık gelen girdi kalıplarını döndürür.

7.slayt
Burada, girdi modellerinin her biri için BAM modeli doğru hedef kalıpları verecek ve hedef kaliplar için model ayrıca karşılık gelen girdi kalıplarını verecektir.

Bu, bellekteki veya model ağdaki çift yönlü ilişkiyi ifade eder.
Giriş değerlerini (A Grubu) üzerinde test etme:

Hedef paternler Üzerinde test etme (Set B)
