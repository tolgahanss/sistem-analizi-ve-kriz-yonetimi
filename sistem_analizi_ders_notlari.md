# 📚 SİSTEM ANALİZİ VE TASARIMI — KAPSAMLI SINAV NOTLARI

> [!IMPORTANT]
> Bu notlar 7 PDF'den (Kavram ve Tanımlar, Başlangıç Araştırma/İnceleme, Fizibilite Analizi, Genel Tasarım, Detaylı Planlama/Proje Yönetimi, Gerçekleştirme, Test & Sistem Dönüşümü) çıkarılmıştır. Sınav için kritik konular ⭐ ile, çok sık sorulan konular 🔥 ile işaretlenmiştir.

---

# BÖLÜM 1: KAVRAM VE TANIMLAR ⭐

## 1.1 Sistem Kavramı 🔥

**Tanım:** Belirli bir amaç doğrultusunda girdilere cevap olarak çıktı üreten, aralarında **karşılıklı etkileşim** olan elemanlar topluluğuna **sistem** denir.

### Sistemin Temel Bileşenleri

| Bileşen | Açıklama |
|---------|----------|
| **Girdi** | Sistem tarafından talep edilen/yönlendirilen kaynaklar (veri, hizmet, malzeme, enerji vb.) |
| **Süreç** | Girdilerin çıktılara dönüştürülmesi |
| **Çıktı** | Sistem faaliyetleri sonucunda üretilen ürünler (bilgi, rapor, dokümanlar, malzeme vb.) |
| **Geri Besleme (Feedback)** | Çıktılardan elde edilen bilgilerle sistemi iyileştirme ve yeniden yapılandırma |
| **Alt Sistemler** | Sistem içindeki daha küçük boyuttaki etkileşimli sistemler |
| **Sistem Sınırı** | Sistemi diğerlerinden/çevresinden ayıran alan |
| **Sistem Çevresi** | Sistem tarafından kontrol edilemeyen, sınır dışında kalan her şey |

> [!TIP]
> **Sınav İpucu:** "Sistem sınırı" ve "sistem çevresi" ayrımını bilin. Örneğin bir banka sistemi için müşteri, hükümet, diğer bankalar, borsa → hepsi **sistem çevresi**dir.

### Sistem Hiyerarşisi (Büyükten Küçüğe - Ezberle!) 🔥

```
Süper Sistem > Supra Sistem > Sistem > Alt Sistem
```

---

## 1.2 Sistem Çeşitleri ⭐

| Sistem Türü | Açıklama |
|-------------|----------|
| **Kapalı Sistem** | Çevresiyle etkileşimi olmayan/sınırlı olan sistem |
| **Açık Sistem** | Çevresiyle sürekli etkileşim halinde olan sistem |
| **Teknik Sistem** | Donanım, yazılım gibi teknik bileşenlerden oluşan sistem |
| **Sosyal Sistem** | İnsan ilişkilerine dayalı sistem |
| **Sosyoteknik Sistem** | Hem teknik hem sosyal bileşenleri içeren sistem |

---

## 1.3 Analiz ve Tasarım Tanımları 🔥

- **Analiz**: Bir konuyu temel parçalarına ayırarak, parçaları ve aralarındaki ilişkileri tanımlayarak sonuca gitme yolu. Bir bütünü parçalarına ayırarak **ayrıntılı inceleme**.
- **Tasarım**: Yeni bir nesne/ürün/yazılım/bilgi sistemi için bir **plan oluşturma ve geliştirme** sürecidir.

---

## 1.4 Sistem Analisti ⭐⭐

### Sistem Analisti Kimdir?
- SGYD'deki **kilit isimlerden** biridir
- Başlangıçtan projenin sonuçlandırılmasına kadar görev sürdürür

### Sistem Analistinin 3 Ana Rolü (Ezberle!) 🔥
1. **Danışman**
2. **Destekleyici uzman**
3. **Değişim ajanı**

### Sistem Analistinin Görevleri
- Problemi araştırmak ve anlamak
- Problem çözümünün sağlayacağı faydaları belirlemek
- Çözüme dair ihtiyaçları ortaya koymak
- Alternatif çözümler üretmek
- En iyi çözümü belirlemek
- Seçilen çözümün ayrıntılarını ifade etmek
- Çözümü uygulamak/uygulanmasını sağlamak
- Sonuçların elde edildiğinden emin olmak için **izlemek**

### Analistin Aşamalara Göre Odağı 🔥

| Aşama | Analistin Odağı |
|-------|-----------------|
| **Başlangıç** | Problemlerin, fırsatların ve amaçların tanımlanması |
| **Fizibilite** | Kullanıcıların hangi bilgiye ihtiyacı olduğunu anlama, hedef/veri/yöntem bilgisi |
| **Tasarım** | Eldeki sistemin mantıksal dizaynı, hatasız veri-giriş prosedürü tasarlama |

### Sistem Analistinin Kişisel Özellikleri ⭐
- Dikkatli, Algılama gücü yüksek
- İfade etme yeteneği kuvvetli
- Bilgi yönetimi becerisine sahip
- Çalıştığı firmanın alanına hakim
- İş ortamını iyi analiz edebilen
- Kendini sürekli geliştirebilme isteği
- **İletişim becerisine sahip**
- Öz disiplini yüksek, Sabırlı
- **Analitik düşünebilme** yeteneği
- **Tümevarım ve tümden gelim** bakış açısı
- Tasarım tekniklerine hakim, Ayrıntıcı

---

## 1.5 Kök Neden Analizi - 5 Kez Neden Tekniği 🔥

Semptom (görünen sorun) ile **kök neden** arasındaki farkı anlamak kritiktir.

**Örnek:** Baş ağrısı → Sürekli ağrı kesici → Mide hastalığı → **Kök neden: Hipertansiyon**

### 5 Kez Neden Diye Sor Tekniği ⭐
- Her cevaba tekrar "Neden?" diye sorarak kök nedene ulaşılır
- Semptomları değil, kök nedeni çözmek gerekir

---

## 1.6 Buzdağı Modeli ⭐

| Seviye | Açıklama | Eylem |
|--------|----------|-------|
| **Olaylar** (Görünen) | Dünyayı algıladığımız seviye | Tepkisel eylem |
| **Trendler/Örüntüler** | Benzer ve tekrarlayan olaylar | Proaktif eylem |
| **Sistemin Yapısı** | Fiziksel şeyler, organizasyonlar, politikalar, ritüeller | Dizayn et |
| **Zihinsel Modeller** | Tutumlar, inançlar, ahlak anlayışı, beklentiler, değerler | Dönüştür |

> [!NOTE]
> Buzdağının altına indikçe: **Öğrenme ve dönüşüm düzeyi** artar, **nedensel etki** artar. Üstten alta: Semptom → Kök Neden

---

## 1.7 Sistemleri Grafiksel Olarak Gösterme 🔥🔥

### A) Bağlamsal Veri Akış Diyagramları (Context-level DFD)
- Sisteme giren ve çıkan **verilere** ve verilerin **işlenmesine** odaklanır
- Sistemin **kapsamını** gösterir
- Harici varlıklar sistem kapsamı dışındadır

### B) Varlık-İlişki Modeli (E-R Model) ⭐⭐

Organizasyon sistemi içindeki **varlıklar** ve onların **ilişkilerine** odaklanır.

#### Üç Tür İlişki (Ezberle!)
| İlişki Türü | Açıklama | Örnek |
|-------------|----------|-------|
| **Bire-bir (1:1)** | Her varlık diğerine sadece bir kez bağlı | Ürün ↔ Ürün Paketi |
| **Bire-çok (1:N)** | Bir varlık diğerine birden fazla bağlı | Departman → Çalışanlar |
| **Çoka-çok (M:N)** | Her iki varlık karşılıklı çoklu bağlı | Öğrenci ↔ Ders |

#### Üç Tür Varlık
1. **Temel Varlık** — Kişiler, yerler, şeyler
2. **İlişkisel Varlık** — İki varlığı birleştirmek için kullanılır
3. **Niteliksel Varlık (Öznitelikli)** — Tekrar eden gruplar için kullanılır

#### E-R Diyagramı Oluşturma Adımları
1. Kuruluştaki varlıkları listeleyin
2. Önemli varlıkları seçerek kapsamı daraltın
3. Birincil varlığı belirleyin
4. Sonuçları veri toplama yoluyla doğrulayın

### C) Kullanım Durumu Modellemesi (Use Case - UML) ⭐⭐

- **UML** (Birleşik Modelleme Dili) parçasıdır
- Sistemin **ne yaptığını** açıklar (nasıl çalıştığını değil)

#### Use Case Bileşenleri
| Bileşen | Açıklama |
|---------|----------|
| **Aktör** | Sistem kullanıcısının belirli bir rolü (sistemin dışındadır) |
| **Durum Sembolü** | Kullanım senaryosunun görevini belirten **oval şekil** |
| **Bağlantı Hatları** | Davranışsal ilişkileri diyagramlamak için oklar/çizgiler |

#### İki Tür Aktör 🔥
1. **Birincil Aktör**: Sistemden veri sağlar veya bilgi alır
2. **Yardımcı Aktör**: Sistemin çalışır durumda kalmasına yardım eder (yardım masası, analist, programcı)

#### Her Kullanım Senaryosu 3 Şey Sağlar
1. Bir olayı **başlatan aktör**
2. Kullanım senaryosunu **tetikleyen olay**
3. Eylemleri gerçekleştiren **kullanım senaryosu**

#### 4 Davranışsal İlişki Türü (Çok Önemli!) 🔥🔥

| İlişki | İngilizce | Açıklama | Özellik |
|--------|-----------|----------|---------|
| **İletişim kurar** | Communicates | Aktörü kullanım senaryosuna bağlar | Ok işareti yok |
| **İçerir** | Includes | Birden fazla senaryoda **ortak olan** davranış | **Her zaman** yapılır |
| **Uzatır/Genişletir** | Extends | Temel senaryodan bir varyasyon/istisna | **Bazen** yapılır (opsiyonel) |
| **Genelleştirir** | Generalizes | Hiyerarşik ilişki, biri diğerinden daha genel | Genel → özel |

> [!CAUTION]
> **Sınav Klasiği:** Include vs Extend farkı çok sık sorulur!
> - **Include** = Her zaman yapılan ortak işlem (ör: ATM'de Para çek → **include** → Kimlik doğrulama)
> - **Extend** = Bazen yapılan ek işlem (ör: Satın alma → **extend** → İndirim kuponu kullanma)

---

# BÖLÜM 2: BAŞLANGIÇ ARAŞTIRMA VE İNCELEME ⭐

## 2.1 İlk Aşamanın Önemi 🔥

- SGYD'nin **ilk aşamasıdır**
- Analist **sorunları, fırsatları ve hedefleri** doğru tanımlar
- Projenin geri kalanının başarısı için **kritik önem** taşır
- Yanlış sorunu çözmek için zaman kaybı önlenir

## 2.2 İlk Aşamada Ne Yapılır?

- Analist **işletmeyi dikkatlice inceler**
- Kullanıcılarla birlikte **problemleri tespit eder**
- **Fırsatlar** değerlendirilir (rekabet avantajı kazanma)
- **Hedefler** belirlenir

### Başlangıç Araştırmalarında Kimler Bulunur?
1. **Kullanıcılar**
2. **Analistler**
3. Yeni sistemi talep eden **yöneticiler**

### Bu Aşamadaki Faaliyetler
1. Kullanıcı ve yöneticilerle **görüşme**
2. Elde edilen bilgilerin **özetlenmesi**
3. Projenin **kapsamının tespiti**
4. Sonuçların **belgelenmesi**

### Çıktı
- **Problem tanımı** içeren ve hedefleri özetleyen bir **fizibilite raporu**
- Yönetim bu rapora göre devam/iptal kararı verir

---

## 2.3 Sistem Gereksinimlerini Tanımlama ⭐

- Sistemin sağlaması gereken **yeteneklerdir**
- Hedef: **Müşterinin ihtiyaçlarını** belirlemek
- Temel prensip: Analistler ile kullanıcılar arasında **etkili ve iyi iletişim**

### Gereksinimlerin Yazılması Kuralları 🔥

**Gereksinim söz dizimi yapısı:**

| Bileşen | Açıklama |
|---------|----------|
| **Kullanıcı** | Sistemden fayda sağlayacak kişi/nesne |
| **Eylem** | Gelecek zaman veya geniş zaman kipinde ("-cak", "-r") |
| **Nesne** | Ortaya çıkacak sonuç ürün, bilgi, fayda |
| **Niteleyici** | Ölçümlenebilir belirleyici değer aralığı |

### Gereksinim Yazma Kuralları
- Kısa tutulmalı (paragraf boyutunda yazılmamalı)
- Gramer ve noktalama kurallarına uyulmalı
- Terim kullanılmamalı (kullanılırsa veri sözlüğünde açıklanmalı)
- Hem kullanıcı hem geliştirici gözüyle tekrar okunmalı
- Tasarım ve geliştirme yapılacak kadar **açık** olmalı
- Her gereksinim **tek başına test edilebilir** olmalı
- "Ve", "veya", "ki" bağlaçlarıyla **birbirine bağlanmamalı**
- **Tutarlı** olmalı, kapsamın dışına çıkmamalı
- **Tekrar eden** gereksinimler olmamalı

---

## 2.4 Gereksinim Analiz Teknikleri 🔥

| Teknik | Detay |
|--------|-------|
| **Yüz yüze görüşme** | Birincil teknik |
| **Anketler** | En fazla kullanılan veri toplama aracı |
| **Soru listeleri** | Yapılandırılmış sorular |
| **Formların analizi** | Mevcut formların incelenmesi |
| **Video kamera** | Gözlem kaydı |
| **Senaryolar** | İş senaryoları |
| **Story board** | Görsel hikaye anlatımı |
| **Ağaç yapıları** | Hiyerarşik yapılandırma |
| **Prototip oluşturma** | Deneme modeli |
| **Doğrudan gözlem** | Yerinde izleme |

### Görüşme Formları Sırası (Önemli!)
1. **Müşteri Gereksinimleri** Formu
2. **Sistem Gereksinimleri** Formu
3. **Yazılım Gereksinimleri** Formu

### Başlangıç Araştırmalarının Çıktısı
- Problemin tanımı ve amaçların özetlenmesini içeren **fizibilite raporu**
- Yönetim bu raporla devam kararı verir

---

# BÖLÜM 3: FİZİBİLİTE ANALİZİ ⭐⭐

## 3.1 Fizibilite Nedir? 🔥

**Sözlük anlamı:** Herhangi bir girişimin işletme ve ekonomi yönlerinden durumunu önceden tespit etme (TDK).

**Basit ifade:** *"Attığın taş ürküttüğün kurbağaya değiyor mu?"*

### Fizibilite Analizi Neyi Araştırır?
- Yapılabilirlik
- Karlılık
- Gerçekleştirme maliyeti
- Süreklilik olasılığı
- Avantaj ve dezavantajlar

### Fizibilite Analizi 4 Aşaması (Ezberle!) ⭐
1. **Veri Toplama**
2. **Veri Analizi**
3. **Karar Verme**
4. **Kapsamlı Rapor Hazırlama** (detaylı dokümantasyon)

---

## 3.2 Fizibilite Analizinde Gerçekleştirilen Etkinlikler 🔥

| Etkinlik | Açıklama |
|----------|----------|
| **Mevcut Sistemin Analizi** | Var olan sistemin kullanıcıları, yazılım/donanımları, kuralları, ilişkileri, uygulama metotları incelenir |
| **Mevcut Sistemin Sorunlarını Belirleme** | Gecikmeler, çakışmalar, yetersizlik, verimsizlik gibi sorunlar |
| **Geliştirilecek Sistemin Hedeflerini Belirleme** | Hangi sorunlara çözüm getireceği, hangi kullanıcılara uygun olduğu |
| **Sınırlılıkları Belirleme** | Sistemin ve çalışmanın sınırlayıcı etkenleri |

---

## 3.3 Problem Tanımı ⭐

### Problem Tanımı Bileşenleri
1. **Problem tanımı** — 1-2 paragrafta problemin ifade edilmesi
2. **Sorunlar** — Problemin bağımsız ana parçaları
3. **Hedefler** — Sorunlarla nokta nokta eşleşen hedefler
4. **Gereksinimler** — Çözüm için gerekenler
5. **Kısıtlamalar** — Bütçe, zaman vb. sınırlamalar

> [!NOTE]
> **Sorunlar = mevcut durum**, **Hedefler = istenen durum**. Hedefler çok özel veya genel ifadeyle belirtilebilir.

### Problem Tanımında Sorulacak İş Soruları
- Organizasyonun amaçları nelerdir?
- Kar amaçlı mı, kar amacı gütmeyen mi?
- Büyüme/genişleme planı var mı?
- Teknolojiyle ilgili tutum (kültür) nedir?
- BT bütçesi nedir?
- Personel uzmanlığa sahip mi?

---

## 3.4 Fizibilite Analizinde Sorulacak Sorular

1. Sisteme/projeye gerçekten **ihtiyaç var mı**?
2. Gerçekleştirme için **nelere ihtiyaç** var?
3. **Ne kadar süre** gerekli?
4. Tahmini **bütçe** nedir?
5. **Alternatif yollar** var mı?
6. Alternatiflerin **avantaj/dezavantajları** nelerdir?

---

## 3.5 Veri Toplama Yöntemleri (Detaylı) 🔥🔥

### A) Yazılı-Basılı Belge İncelemesi ⭐
- E-posta mesajları, notlar, prosedür kılavuzları, politika el kitapları, web sayfaları incelenir
- Metaforlar aranır (ör: "Biz büyük mutlu bir aileyiz" → aile metaforu)
- İçeridekiler vs dışarıdakiler zihniyeti var mı?
- Mizah duygusu anlaşılmaya çalışılır
- **Dikkat:** Basılı kılavuzlar nadiren güncel tutulur!

### B) Yüz Yüze Görüşme (Mülakat) ⭐⭐

**Amaç:** Araştırma sorusu hakkında bilgi toplamaktır.

#### Görüşme Türleri (4 Tür - Ezberle!) 🔥

| Tür | Kontrol Düzeyi | Açıklama |
|-----|---------------|----------|
| **Biçimsel olmayan** | Yok | Araştırmacının ortamdaki kişilerle karşılıklı konuşmaları |
| **Yapılandırılmamış** | Çok az | Sorular önceden belirlenmez, katılımcının cevabına göre şekillenir |
| **Yarı-yapılandırılmış** | Orta | Önceden belirlenmiş soru/konu başlıkları rehberlik eder |
| **Yapılandırılmış** | Yüksek | Tüm katılımcılara aynı sorular, aynı sırada, aynı biçimde |

#### Görüşmenin Aşamaları
1. **Hazırlık** — Görüşme türü, kimlerle görüşülmesi
2. **Düzenleme** — Uygun ortam
3. **Görüşmenin yönetimi** — Güven, iletişim
4. **Kapanış**
5. **Değerlendirme**

#### Açık Uçlu vs Kapalı Uçlu Sorular 🔥

| | Açık Uçlu | Kapalı Uçlu |
|---|-----------|-------------|
| **Tanım** | İstediği gibi cevap vermesine imkan tanır | Seçenek sunar, belli kalıpta cevap |
| **Avantaj** | Ayrıntılı bilgi, önceden bahsedilmemiş süreçler ortaya çıkabilir | Karşılaştırmaya imkan, konu dağılmaz |
| **Dezavantaj** | Konu dağılabilir, kontrol kaybedilebilir | Zengin içerik oluşturulmaz, samimi cevaplar alınamayabilir |

### C) Anket ⭐

- En fazla kullanılan veri toplama aracı
- **Avantaj:** Çok fazla insana uygulanması kolay, uzaktaki kişilerden bilgi toplanır
- **Dezavantaj:** Ayrıntılı/samimi bilgi elde edilemez

#### Ankette Soru Türleri
1. **Açık uçlu sorular**
2. **Liste sıralama**
3. **İki seçenekli sorular** (Evet/Hayır)
4. **Çok seçenekli sorular**
5. **Ölçeklendirme soruları** (Likert ölçeği: Çok Kötü → Çok İyi)

### D) Gözlem ⭐

**Tanım:** Nesneleri, olayları ve durumları sistematik biçimde izleyerek betimleme.

#### İki Tür Gözlem
1. **Katılımcı gözlem** — Araştırmacı ortamın içine girer, yaşama katılır
2. **Doğrudan gözlem** — Dışarıdan izler, ortamın doğal üyesi değildir

#### Gözlemin Aşamaları
1. Araştırma sorusu ve amaçların belirlenmesi
2. Gözlenecek kişilerin belirlenmesi
3. Gözlenecek kişilere ulaşılması
4. Uygun gözlem biçimiyle veri toplama
5. Veri analizi
6. Raporlaştırma

### E) Karar Vericinin Davranışını Gözlemlemek
- Fiziksel çevre ve etkileşimleri gözlemleme
- Gerçekte ne yapıldığını anlama (belgelerden farklı olabilir)
- Karar vericiler arası ilişkileri görme

### F) İş Yeri ve Ofis Düzeni İncelenmesi

| İncelenen Unsur | Ne Aranır? |
|-----------------|------------|
| **Ofis yeri** | Köşe ofis kimde? Önemli konumlar karar vericilere dağılmış mı? |
| **Masa yerleşimi** | İletişimi teşvik ediyor mu? Otorite gösteriyor mu? |
| **Ofis malzemeleri** | Karar verici bilgileri kişisel mi saklıyor? |
| **Teknoloji kullanımı** | PC, akıllı telefon, tablet kullanımı var mı? |
| **Dış bilgi kaynakları** | Ticaret dergileri, web gibi harici kaynaklardan bilgi alıyor mu? |
| **Giyim** | Takım elbise = otorite göstergesi |

---

## 3.6 Örnekleme ⭐

### Temel Kavramlar (Ezberle!)

| Kavram | Simge | Açıklama |
|--------|-------|----------|
| **Evren** | N | Araştırma bulgularının genellendiği büyük grup |
| **Örneklem** | n | Evreni temsil eden daha küçük küme |
| **Öge** | — | Örnekleme girme ihtimali olan her bir analiz birimi |
| **Denek** | — | Örnekleme dahil edilen her bir öge |
| **Örnekleme** | — | Evrenden örneklem seçim işlemi |
| **Örneklem Oranı** | n/N | Örneklem büyüklüğü / Evren büyüklüğü |
| **Parametre** | — | Evreni betimlemek için kullanılan değerler |
| **Örneklem İstatistiği** | — | Örneklemi betimlemek için kullanılan değerler |

### Genel Evren vs Araştırma Evreni
- **Genel (ideal) evren:** Tanımlaması kolay ama ulaşılması güç (ör: 10.000 çalışan)
- **Araştırma (çalışma) evreni:** Ulaşılması ve genelleme yapılması daha kolay (ör: Üretim departmanındaki çalışanlar)

### Örneklem Büyüklüğü Hesaplama 🔥

**3 Temel Parametre:**
1. **Güven düzeyi (t):** Genellikle %95 (z=1.96) veya %99 (z=2.58)
2. **Kabul edilebilir sapma toleransı (d):** %5'e kadar kabul edilir
3. **Evren için tahmin edilen standart sapma (s):** Pilot araştırma veya önceki çalışmalardan elde edilir

**Formül:**
```
n₀ = (t² × s²) / d²
n = n₀ / (1 + n₀/N)
```

**Örnek:** N=6000 hemşire, %95 güven (t=1.96), s=0.5, d=0.05
- n₀ = (1.96² × 0.5²) / 0.05² = (3.8416 × 0.25) / 0.0025 = 384.16
- n = 384.16 / (1 + 384.16/6000) = 384.16 / 1.064 ≈ **361 kişi**

---

# BÖLÜM 4: GENEL TASARIM ⭐

## 4.1 SGYD Nedir? (Sistem Geliştirme Yaşam Döngüsü) 🔥

SGYD, analist ve kullanıcıların birlikte sürdürdükleri **sistematik ve aşamalı faaliyetler dizisi**dir.

### SGYD Aşamaları (Sırasıyla Ezberle!)

| # | Aşama | Çıktı | Amaç |
|---|-------|-------|------|
| 1 | **Başlangıç Araştırma-İnceleme** | İhtiyaçlar listesi | Problemi ortaya koymak |
| 2 | **Fizibilite Çalışması** | Fizibilite raporu | Projenin kapsamı ve olabilirliğini belirlemek |
| 3 | **Genel Tasarım** | Maliyet ve üst düzey tasarım | Sistemin NASIL gerçekleştirileceğini belirlemek |
| 4 | **Ayrıntılı Tasarım** | Özellikleri ve ayrıntılı tasarım | Alt sistemlerin tanımlanması |
| 5 | **Gerçekleştirme** | Çalışan sistem ve dokümantasyon | Program yazma, yükleme ve sınama |
| 6 | **Test Kullanımı** | Çalışmaya hazır sistem | Sistemin test edilmesi, hataların giderilmesi |
| 7 | **Uygulama ve Değerlendirme** | Eğitilmiş kullanıcılar | Uygulamaya başlama, eğitim, değerlendirme |

> [!TIP]
> **Sınav İpucu:** "Fizibilite = NE?, Genel Tasarım = NASIL?" ayrımını kesinlikle bilin. Bu çok klasik bir sınav sorusudur.

### Genel Tasarım vs. Ayrıntılı Tasarım Farkı 🔥

| Özellik | Genel Tasarım | Ayrıntılı Tasarım |
|---------|---------------|-------------------|
| **Odak** | Genel seviyede çerçeve/mantık | Her program için ayrıntılı mantık |
| **Detay** | Üst düzey | Alt sistem ve modül düzeyi |
| **İçerik** | Kullanılacak ortam belirlenir, raporlar/ekranlar için ihtiyaçlar ortaya konulur | Rapor, ekran, dosya tasarım ve düzeni tamamlanır |
| **Rolü** | Ayrıntılı tasarım için **yol haritası** | Gerçekleştirme için hazırlık |

---

## 4.2 SGYD Modelleri (Yapılandırılmış Tasarım) 🔥🔥

### A) Geleneksel / Şelale (Waterfall) ⭐

```
Planlama → Analiz → Tasarım → Uygulama → Sistem
```

- Aşamalar **sıra ile** adım adım gerçekleştirilir
- **Bir aşama tamamlanmadan diğerine geçilmez**
- En geleneksel model

### B) Paralel Geliştirme (Parallel Development)

```
Planlama → Analiz → [Tasarım Alt Proje 1] → [Uygulama 1]
                   → [Tasarım Alt Proje 2] → [Uygulama 2] → Sistem
                   → [Tasarım Alt Proje 3] → [Uygulama 3]
```

- Tasarım aşamasından itibaren **birkaç parçaya ayrılır**
- Parçalar **birbirine paralel** şekilde ilerler

### C) Fazlandırılmış Geliştirme (Phased Development - RAD)

```
Planlama → Analiz → Tasarım → Uygulama → Sistem V1
                  → Analiz → Tasarım → Uygulama → Sistem V2
                           → Analiz → Tasarım → Uygulama → Sistem V3
```

- Analiz aşamasından itibaren **belirli fazlar** için devam ettirilir
- Her faz için tüm aşamalar sırayla gerçekleştirilir
- **Bir fazın sonucu, bir sonraki faz için veri sağlar**

### D) Sistem Prototipi Oluşturma (Prototyping - RAD)

- Önce sistemin bir **prototipi** oluşturulur
- Prototip üzerinde **iyileştirmeler** yapılarak devam edilir

### E) Tasarım Prototipi (Throw-away Prototyping)

```
Planlama → Analiz → Tasarım Prototipi → Analiz → Tasarım → Uygulama → Sistem
```

- Prototip sadece tasarım amacıyla kullanılır ve **atılır** (throw-away)

> [!CAUTION]
> **Sınav Klasiği:** Şelale, Paralel, Fazlandırılmış, Prototip modellerini karşılaştıran sorular sıklıkla çıkar. Her modelin akış şemasını çizebilecek kadar bilin!

---

## 4.3 Ne Zaman Hangi Yöntem? 🔥

### SGYD (Şelale) Ne Zaman Kullanılır?
- Mevcut sistemler SGYD ile geliştirilmiş ve belgelenmiştir
- **Her adımı belgelemek** önemlidir
- Üst düzey yönetim SGYD'yi tercih ediyor
- Tam SGYD için **yeterli kaynak ve zaman** vardır
- Yeni sistemlerin nasıl çalıştığına dair **iletişim** önemlidir

### Çevik (Agile) Ne Zaman Kullanılır?
- Çevik yöntemlere **aşinalık** var
- **Dinamik çevre** nedeniyle hızlı geliştirme gerekli
- Kurtarma faaliyeti gerekli (sistem başarısız)
- Müşteri **adım adım ve sürekli artan iyileştirmelerden** memnun
- Yöneticiler çevik ilkelerine katılıyor

### Nesne Tabanlı (OO) Ne Zaman Kullanılır?
- Problemler **değişik sınıflardan** kaynaklanıyor
- Firma **UML** (Unified Modelling Language) kullanıyor
- Sistemler **kademeli** yapılanmış
- **Yazılım yeniden kullanımı** mümkün
- Önce **zor sorunlara** odaklanmak mümkün

---

## 4.4 Çevik (Agile) Sistem Analizi ve Tasarımı ⭐

### Çevik Değerler (4 Tane - Ezberle!)
1. **İletişim**
2. **Basitlik**
3. **Geri bildirim**
4. **Cesaret**

### Çevik Prensipler (Önemli Olanlar)
- ✅ Çalışan yazılımı teslim ederek müşteriyi memnun edin
- ✅ Geliştirme aşamasında bile değişimi kabul edin
- ✅ Çalışan yazılımı aşamalı ve sık sık geliştirin
- ✅ Müşterileri ve analistleri her gün birlikte çalıştırın
- ✅ Motive olmuş bireylere güvenin
- ✅ Yüz yüze iletişimi teşvik edin
- ✅ Basitliği benimseyin
- ✅ Kendi kendini organize eden ekipleri destekleyin

### Dört Çevik Kaynak Kontrol Değişkeni 🔥
1. **Zaman**
2. **Maliyet**
3. **Kalite**
4. **Odak**

### Juran ve Pareto Analizi ⭐
- **Pareto İlkesi (80/20 Kuralı):** Bir sorunun **%80'i**, nedenlerin **%20'sinden** kaynaklanır
- "Az sayıda önemli, çok sayıda önemsiz"
- Juran: "Yaşamsal azınlık ve yararlı çoklar"

### Çevik Temel Uygulamalar
- Küçük ve öncelikli sürümler üretmek
- **40 saatlik haftalık çalışma** (daha fazlası değil!)
- Müşterinin yanında işletme/yönetim uzmanı temsilci bulundurmak
- Kodlama gruplarını sık sık değiştirmek

### Çevik Proje Geliştirme Süreci
```
Keşif/Araştırma → Planlama → İlk Sürüm Denemeleri → Üretim → Bakım
```

---

## 4.5 Nesne Tabanlı (OO) Sistem Analizi

- **Dinamik iş ortamlarında** hızla değişen sistemler için alternatif yaklaşım
- Analiz, sistemin **küçük bir bölümünde** yapılır → ardından tasarım ve uygulama
- **Karmaşık bilgi sistemlerinin** sürekli bakım/uyarlama/yeniden tasarıma tabi tutulduğu durumlarda işe yarar
- Sistemin **nesnelerini** ele alır ve tek tek inceler
- Döngü tekrar eder: analiz → tasarım → uygulama → tekrar

---

# BÖLÜM 5: DETAYLI PLANLAMA VE PROJE YÖNETİMİ ⭐

## 5.1 Problem Tanımı 🔥

Problem tanımı şu bileşenlerden oluşur:

| Bileşen | Açıklama |
|---------|----------|
| **Problemin İfadesi** | Sorunu/fırsatı belirten 1-2 paragraf |
| **Sorunlar** | Sorunla ilgili bağımsız parçalar |
| **Hedefler** | Sorunlarla tek tek eşleşen hedefler |
| **Gereksinimler** | Olası çözümler ve kısıtlamalar |

### Kullanıcılardan Problem Tespit Yolları (7 Yol)
1. Farklı kişiler tarafından **tekrarlanan konu/tema**
2. Aynı **metaforları** kullanarak iletişim kurma
3. Giriş-gelişme-sonuç içeren **hikaye** anlatma
4. Bir konu üzerinde **uzun uzun** konuşma
5. Doğrudan **"Büyük bir sorun var"** deme
6. **Vücut dili** ve vurgulu konuşma
7. İlk bahsettikleri şey olabilir

> [!NOTE]
> Hedefler belirtildikten sonra **göreceli önemleri** belirlenmelidir. Yetersiz fon varsa **kritik hedefler** önce tamamlanır. **Kullanıcılar**, kritik hedefleri belirleyen en iyi kişilerdir.

---

## 5.2 Proje Seçimi

Bir projenin seçilmesi için kriterler:
- ✅ **Yönetimden destek** olması
- ✅ Uygun **zamanlama**
- ✅ **Organizasyonel hedeflere** ulaşmayı iyileştirme
- ✅ Mevcut kaynaklar açısından **pratik** olması
- ✅ Diğer yatırımlarla karşılaştırıldığında **değerli** olması

### Organizasyonel Hedefler
- Kurumsal karların iyileştirilmesi
- Rekabet stratejisinin desteklenmesi
- Satıcılar/ortaklarla işbirliğinin geliştirilmesi
- Dahili operasyon ve karar desteğinin iyileştirilmesi
- Müşteri hizmetlerinin iyileştirilmesi
- Çalışan moralinin arttırılması

---

## 5.3 Fizibilitenin Belirlenmesi 🔥🔥

### Üç Temel Fizibilite Türü (Mutlaka Ezberle!)

| Fizibilite Türü | Soru | İçerik |
|-----------------|------|--------|
| **Teknik Fizibilite** | Teknoloji uygun mu? | Mevcut sisteme ekleme yapılabilir mi? İhtiyaçları karşılayacak teknoloji mevcut mu? |
| **Ekonomik Fizibilite** | Yatırım değerli mi? | Analist maliyeti, personel maliyeti, eğitim maliyeti, donanım maliyeti, yazılım maliyeti |
| **Operasyonel Fizibilite** | Çalışacak mı? Kullanılacak mı? | Sistem kurulduktan sonra çalıştıracak insan kaynağı var mı? Kullanıcılar istemiyor mu? |

> [!WARNING]
> **Dikkat:** Yeni sistem istemeyen kullanıcılar, sistemin operasyonel olarak uygulanabilir hale gelmesini **engelleyebilir**!

---

## 5.4 İş Kırılım Yapısı (WBS - Work Breakdown Structure) ⭐

### WBS Nedir?
- Projenin **daha küçük görevlere/faaliyetlere** bölünmesidir
- Bu görevler birlikte İş Kırılım Yapısını oluşturur

### WBS Özellikleri
- Her görev **somut bir sonuç/teslim edilebilir** içerir
- Her görev **tek bir kişi/gruba** atanabilir
- Her görevin **sorumlu bir kişisi** vardır

### WBS Geliştirme Yaklaşımları
- **Ayrıştırma**: Büyük fikirlerden → yönetilebilir faaliyetlere
- **Ürün odaklı**: Web sitesi oluşturmak → parçalara bölünür
- **Süreç odaklı**: Her aşamanın önemini vurgular

---

## 5.5 Zaman Tahmin Teknikleri

1. **Deneyime güvenmek**
2. **Analojileri kullanma**
3. **Üç nokta tahmini** (Formül!) ⭐
4. **Fonksiyon noktalarını tanımlama**
5. **Zaman tahmin yazılımı kullanma**

### Üç Nokta Tahmini Formülü 🔥🔥

```
Ağırlıklı Ortalama = (a + 4m + b) / 6
```

- **a** = En iyi durum tahmini (iyimser)
- **m** = En olası zaman tahmini
- **b** = En kötü durum tahmini (kötümser)

**Örnek:** Bir yazılım modülü:
- En iyi: 8 gün, En olası: 10 gün, En kötü: 30 gün
- Tahmin = (8 + 4×10 + 30) / 6 = (8 + 40 + 30) / 6 = **78/6 = 13 gün**

---

## 5.6 Proje Planlama Araçları 🔥

### Gantt Grafikleri
- **Basit** ve anlaşılır
- Son kullanıcı iletişimine uygun
- **Ölçeğe göre** çizilmiş
- Paralel faaliyetlerin planlanmasında kullanılır

### PERT Diyagramları (Program Evaluation and Review Technique)
- Faaliyetler **paralel** olarak yapılabildiğinde kullanışlı
- **Kritik yol** kolayca belirlenebilir
- **Gevşek zaman** (slack time) kolayca hesaplanır

### PERT Diyagramının Avantajları ⭐
1. Öncelik sırasının kolay belirlenmesi
2. **Kritik yolun** ve kritik faaliyetlerin kolay tanımlanması
3. **Gevşek zamanın** kolay belirlenmesi

---

## 5.7 Maliyet Tahmin Yaklaşımları 🔥

| Yaklaşım | Diğer Adı | Açıklama |
|----------|-----------|----------|
| **Yukarıdan Aşağıya** | Top-Down | Benzer projelere dayalı tahmin. Deneyim çok önemli. |
| **Aşağıdan Yukarıya** | Bottom-Up | Her ekip üyesi kendi faaliyetinin maliyetini tahmin eder. Uzun sürer. |
| **Parametrik Modelleme** | — | Faktör/parametre bazlı tahmin (ör: kod satırı başına 75$). COCOMO II gibi yazılımlar kullanılır. |

---

## 5.8 Proje Riski ve Balık Kılçığı Diyagramı ⭐

### Proje Başarısızlıklarını Önleme
- Eğitim
- Deneyim
- Diğer projelerin neden başarısız olduğunu öğrenmek

### Balık Kılçığı Diyagramı (Ishikawa Diyagramı)
- Diğer adları: **Neden-sonuç diyagramı**, **Ishikawa diyagramı**
- Meydana gelebilecek tüm olası sorunları **sistematik olarak** listeler
- Takvim kaymalarını analiz etmek için kullanılır

---

## 5.9 Kazanılmış Değer Yönetimi (EVM) ⭐

Projedeki ilerlemeyi/aksaklıkları belirlemek için kullanılır.

### 4 Temel Ölçek (Ezberle!)

| Kısaltma | Tam Adı | Açıklama |
|----------|---------|----------|
| **BAC** | Budget at Completion | Projenin **toplam bütçesi** |
| **PV** | Planned Value | Tamamlanacak işin **planlanan değeri** |
| **AC** | Actual Cost | İşin tamamlanması için **katlanılan toplam maliyet** |
| **EV** | Earned Value | Şu ana kadar gerçekleştirilen işin **değer tahmini** |

---

## 5.10 Ekip Yönetimi

### Ekip Oluşturma Değerleri
- Ekip çalışmasının ortak değeri
- İyi iş ahlakı, Dürüstlük, Yeterlilik
- Uzmanlığa dayalı liderlik
- Motivasyon, Heyecan, Güven

### İki Tür Ekip Lideri 🔥
1. **Görev Lideri**: Üyeleri görevleri tamamlamaya yönlendirir
2. **Sosyo-duygusal Lider**: Sosyal ilişkilerle ilgilenir

---

## 5.11 Proje Şartları Dokümanı (Charter) ⭐

Proje charter'ının cevapladığı sorular:
- Kullanıcı projeden ne bekliyor?
- Projenin **kapsamı** nedir?
- Hangi **analiz yöntemleri** kullanılacak?
- **Anahtar katılımcılar** kimlerdir?
- Proje **çıktıları** nelerdir?
- Sistemi kim/nasıl **değerlendirecek**?
- Tahmini proje **zaman çizelgesi** nedir?
- Kullanıcıları kim **eğitecek**?
- Sistemin **bakımını** kim sürdürecek?

---

## 5.12 Sistem Önerisi (Proposal) Bileşenleri

1. Ön yazı
2. Projenin başlık sayfası
3. İçindekiler
4. **Yönetici Özeti**
5. Sistem çalışmasının ana hatları
6. Ayrıntılı sonuçlar
7. Sistem alternatifleri
8. Analistlerin tavsiyeleri
9. Özet
10. Ekler

---

# BÖLÜM 6: GERÇEKLEŞTİRME ⭐

## 6.1 Kodlama (Coding) 🔥

### Kodlama Nedir?
- Tasarım aşamasında fiziksel olarak tanımlanan yazılımın (diyagramlar/pseudocode), **makine tarafından okunabilecek** bir program haline getirilmesidir.

### Kodlama Girdileri ve Çıktıları

| Girdi | Çıktı |
|-------|-------|
| İş akış şemaları | Üretilen yazılım |
| Veritabanı tasarımı | Kodun dokümantasyonu |
| Arayüz - Ekran görüntüleri | |
| Ağ Şemaları | |

### Kodlama Aşamasında Analistin Görevleri ⭐
1. Programcılar arasında **eşgüdüm** sağlar
2. Arayüz, veritabanı ve ağ şemaları hakkında **bilgilendirir**
3. Değişken isimleri, kod açıklamaları gibi konularda **eğitim toplantıları** yapar
4. Programlama dili seçiminde **yazılım mühendisliği uygunluğu** dikkate alınır

---

## 6.2 Programlama Dili Seçimi 🔥

### Dikkat Edilecek Konular
1. **Genel uygulama alanı**
2. Algoritma, bilgi işlem ve veri yapısı açılarından **karmaşıklık derecesi**
3. Yazılımın kullanılacağı **ortam**
4. **Uygulama koşulları**
5. Personelin **bilgi düzeyi**

### Dil Seçimini Sınırlayan Faktörler
- Kuruluşun belirli bir dile **yatırım yapmış** olması
- Programcıların bir dilde **tecrübe** sahibi olması
- Müşterinin belirli bir dili **ön koşul** olarak ileri sürmesi
- Sahip olunan derleyici, VTYS, işletim sistemi kısıtlamaları

---

## 6.3 Kodlama Kalitesi ⭐

### Kaliteyi Oluşturan Faktörler
- **Açıklama Satırları** (Comments)
- **Okunabilirlik**
- **Kod yazım düzeni** (boşluk ve girinti kullanımı)
- Bakım/Test/Hata Ayıklama maliyetlerinin **düşüklüğü**
- **Taşınabilirlik** (Portability)
- **Karmaşıklığın azaltılması**
- Düşük kaynak tüketimi (**CPU, RAM**)
- Kuvvetli **girdi geçerliliği** (Validation) ve **hata yakalama** (Error Handling)

### Kaliteyi Arttıran Faktörler
1. **Yeniden Düzenleme** (Refactoring)
2. **Kod Denetimi** / Yazılımın Gözden Geçirilmesi
3. **Kodun Dokümantasyonu**

---

## 6.4 Sınama / Test (Testing) 🔥

**Tanım:** Programdaki hataları bulmak amacı ile yapılan işlemlerdir.

**Amaç:** Yazılımın fonksiyonel, performans, dayanıklılık ve yapısal açılardan yeterliliğini denetlemek.

### Ünite / Birim Testi (Unit Test) ⭐
- Yazılım tasarımının **en küçük birimi olan modül** üzerinde uygulanır
- **Saydam kutu** (white box) testi olarak uygulanır
- Çok sayıda modül üzerinde **paralel** olarak yürütülür
- Modülün **arabirimi, veri yapısı, kontrol yapıları, hata arama yolları ve sınırları** sınanır

---

## 6.5 Yükleme / Dönüşüm (Installation/Conversion) 🔥🔥

**Tanım:** Yeni sistemin eski sistemin yerini alması ve eski sistemin tamamen ortadan kalkması sürecine **dönüşüm** denir.

> [!WARNING]
> Dönüşüm süreci **yazılım süreci kadar önemlidir**! Canlı verilerin dönüşümü, yedekleme ve güvenlik çok iyi planlanmalıdır.

### 5 Dönüşüm Stratejisi (Mutlaka Ezberle ve Karşılaştır!) 🔥🔥🔥

#### 1. Doğrudan Geçiş (Direct Changeover)

| Avantajlar | Dezavantajlar |
|-----------|---------------|
| ✅ Hızlı Geçiş | ❌ Kapsamlı test ihtiyacı |
| ✅ Maliyet etkinliği | ❌ **Yüksek riskli** yaklaşım |
| | ❌ Kullanıcı memnuniyetsizliği |
| | ❌ Sonuç karşılaştırma zorluğu |

#### 2. Paralel Dönüşüm (Parallel Conversion)

| Avantajlar | Dezavantajlar |
|-----------|---------------|
| ✅ Eş zamanlı çalışma (iş sürekliliği) | ❌ **İş yükünün iki katına çıkması** |
| ✅ Veri karşılaştırma imkanı | |

#### 3. Kademeli / Aşamalı Dönüşüm (Gradual/Phased)

| Avantajlar | Dezavantajlar |
|-----------|---------------|
| ✅ Paralel + doğrudan'ın en iyi özelliklerini birleştirir | ❌ Uygulama süresini uzatabilir |
| ✅ İşlem hacmi giderek artar | ❌ Karmaşıklık |
| ✅ Kullanıcılar yavaş yavaş dahil olur | |
| ✅ **Çevik metodolojilere uygun** | |

#### 4. Modüler Prototip Dönüşümü

| Avantajlar | Dezavantajlar |
|-----------|---------------|
| ✅ Her modül ayrı test edilir ve kullanıma sunulur | ❌ Yönetim zorlukları |
| ✅ Kapsamlı modül testleri | ❌ **Bütünleştirme zorluğu** |
| ✅ Kullanıcılar modüllere aşina olur | |
| ✅ **Nesneye yönelik metodolojilere uygun** | |

#### 5. Dağıtılmış Dönüşüm (Distributed Conversion)

| Avantajlar | Dezavantajlar |
|-----------|---------------|
| ✅ Sorunlar tespit edilip kontrol altına alınabilir | ❌ Her sitenin kendine has özellikleri vardır |

> [!IMPORTANT]
> **Kritik Sınav Notu:** Kademeli dönüşüm → **Çevik** metodolojilere uygun. Modüler prototip → **Nesneye yönelik** metodolojilere uygun. Bu eşleştirme sık sorulan bir detaydır!

---

## 6.6 Dokümantasyon (Documentation) ⭐

### İki Tür Dokümantasyon

| Tür | İçerik |
|-----|--------|
| **İç Dokümantasyon** | Gereksinim raporu, iş akış diyagramları, veritabanı şemaları, detaylı tasarım raporu, ağ şemaları |
| **Dış Dokümantasyon** | Çevrimiçi yardım, Kullanıcı kılavuzu, Sıkça sorulan sorular (FAQ) |

- Dokümantasyonun büyük kısmı **analist tarafından** hazırlanır
- Aslında dokümantasyon yazılım bittikten sonra değil, **tüm aşamalarda** yapılır

---

## 6.7 Eğitim ve Destek 🔥

### Eğitim
- **"Sistemi kullanacak herkes"** eğitime alınmalıdır
- Eğitim süresi/derinliği: görev, kullanma derecesi ve bilgi düzeyine göre değişir
- Modüller ve ekranlar **kullanıcı görevlerine göre** gruplanmalı
- Kullanıcılar düzeylerine göre **ayrı ayrı** eğitim almalı

### Eğitim Çeşitleri
1. Kurum içi Uzman
2. Geleneksel eğitim
3. E-öğrenme/Uzaktan Eğitim
4. **Karma Öğrenme** (Geleneksel + E-Öğrenme)
5. Yazılım Yardım Bileşeni
6. Dış Kaynak

### Eğitim Materyalleri
- Görüntülü/Sesli Materyal
- Sunum
- Basılı Doküman/Kitap
- Ekran Görüntüleri (ScreenCast)

### Destek (Support)
- **Yardım Masası** (Help Desk): Kullanıcıların ilk arayacağı yer
- Otomatik destek: Sesli cevap sistemleri, dahili e-posta, grup destek sistemi
- Satıcı firma desteği

### Destek Personelinin Özellikleri
- İyi iletişim kurabilmeli
- Problemleri dinleyebilmeli
- Olası çözümler üretebilmeli
- Teknolojiye ve yeni sisteme hakim olmalı

---

# BÖLÜM 7: TEST, UYGULAMA VE DEĞERLENDİRME ⭐⭐

## 7.1 Test Kullanımının Amacı
1. Sistem **tasarlandığı gibi çalışıyor** mu?
2. Sistem **kullanıcı ihtiyaçlarını karşılıyor** mu?

---

## 7.2 Test Süreci (4 Aşama - Sırasıyla!) 🔥

1. **Test verileriyle program testi**
2. **Test verileriyle bağlantı/dize testi**
3. **Test verileriyle tam sistem testi**
4. **Canlı verilerle tam sistem testi**

### 1. Test Verileriyle Program Testi
- Analist: danışman ve koordinatör
- **Masa Kontrolü**: Programcılar programdaki her adımı **kağıt üzerinde** takip eder
- **Test Verisi Oluşturma**: Geçerli ve geçersiz veriler, minimum/maksimum değerler test edilir

### 2. Test Verileriyle Bağlantı Testi (Dize Testi / String Test)
- Birbirine **bağımlı programların** birlikte çalışıp çalışmadığı test edilir
- Önce **tipik test verileri**, ardından **varyasyonlar ve geçersiz veriler** işlenir

### 3. Test Verileriyle Tam Sistem Testi
- Operatör dokümantasyonu yeterli mi?
- Prosedür kılavuzları anlaşılır mı?
- İş akışları doğru çalışıyor mu?
- Çıktı doğru mu? Kullanıcılar anlıyor mu?
- **Kalite standartları** yeniden onaylanır

### 4. Canlı Verilerle Tam Sistem Testi
- Mevcut sistem aracılığıyla **daha önce işlenmiş gerçek veriler** kullanılır
- Kullanıcı-sistem etkileşimi **gözlemlenir**
- Üretim öncesi gerçek sorunlar ele alınır
- Kılavuzlar da test edilir

---

## 7.3 Test Stratejileri (10 Tür) 🔥🔥

| # | Test Türü | Amaç | Yaklaşım |
|---|-----------|------|----------|
| 1 | **Birim Testi** | Bireysel modüllerin doğruluğu | Kodlama aşamasında geliştiriciler yapar |
| 2 | **Entegrasyon Testi** | Modüller arası etkileşim | Artımlı veya Big Bang entegrasyon |
| 3 | **Sistem Testi** | Tüm sistemin gereksinimlere uygunluğu | **Kara kutu testi** ile |
| 4 | **Kabul Testi (UAT)** | Kullanıcı/iş gereksinimlerini karşılama | Gerçek kullanıcılar test eder |
| 5 | **Gerileme/Regresyon Testi** | Değişikliklerin mevcut işlevi bozmaması | **Otomatik test** yaygın |
| 6 | **Performans/Verim Testi** | Yanıt verebilirlik, ölçeklenebilirlik | Yük testi, stres testi |
| 7 | **Güvenlik Testi** | Güvenlik açıkları/riskleri | Sızma testi, güvenlik açığı taraması |
| 8 | **Kullanılabilirlik Testi** | Kullanım kolaylığı, UX | Kullanıcı geri bildirimi, anketler |
| 9 | **Uyumluluk Testi** | Farklı ortam/cihaz/yapılandırma | Çeşitli platformlarda test |
| 10 | **Sürdürülebilirlik/Güvenilirlik** | Bakım kolaylığı, güvenilirlik | Sağlamlık, hata kurtarma testleri |

---

## 7.4 Test Seviyeleri (Detaylı) 🔥🔥

| Test Seviyesi | Açıklama | Kim Yapar? |
|--------------|----------|------------|
| **İskeleleme (Scaffolding)** | Sistemi test etmek için özel üretilmiş yazılımlar. Sistem simüle edilir. | Geliştiriciler |
| **Birim Testi (Unit)** | Tek bir program/modül/bileşen test edilir. Diğerleriyle ilişki göz ardı edilir. | Geliştiriciler |
| **Entegrasyon Testi** | 2+ modülün birlikte çalışması test edilir. | Geliştiriciler |
| **Fonksiyon Testi** | Entegrasyon testi yapılmış sistemlerin testi. Simüle/test verisiyle yapılır. | Analist + Geliştirici |
| **Sistem Testi** | Tüm sistem test edilir. Test datası + gerçek kullanıcı datası kullanılır. | Analist + Kullanıcı |
| **Kullanıcı Kabul Testi (UAT)** | Kullanıcının kendi yerinde, kendi verileriyle yapılan test. | **Kullanıcı** |
| **Regresyon Testi** | Eski test verileriyle yeni sistemin kullanılabilirliği test edilir. | Otomatik araçlar |
| **Sistem Performans Testi** | Aşırı yüklenme durumundaki davranış ölçülür. | Geliştiriciler |
| **Toparlama Testi (Recovery)** | Güç, veritabanı, sistem çalışmama durumu test edilir. | Geliştiriciler |
| **Denetleme Testi (Audit)** | Sistemin hatasız olduğunun belirlenmesi. Kalite güvence fonksiyonu. | **Bağımsız teknik uzmanlar** |
| **Donanım Testi** | Temel fonksiyonlar, yanma süresi (burn-in), stres testi | Donanım uzmanları |

### Prosedür Testi (3 Aşama)
1. **Taslak prosedür testi**: Teknik personel kullanılır
2. **Kontrollü kullanıcı testi**: Seçilmiş kullanıcılar yapar, iyileştirme önerileri dikkate alınır
3. **Canlı testler**: Gerçek kullanıcılar ve gerçek veriler kullanılır

---

## 7.5 Güvenlik Testleri 🔥🔥

### Güvenlik Kaygıları (3 Tür) ⭐

| Tür | Açıklama |
|-----|----------|
| **Fiziksel Güvenlik** | Bilgisayar tesisi, ekipman ve yazılımın fiziksel yollarla güvenliği |
| **Mantıksal Güvenlik** | Yazılımın kendisindeki mantıksal kontroller |
| **Davranışsal Güvenlik** | Donanım/yazılımın kötüye kullanımını önleyen prosedürler |

### Güvenlik Testi Neden Yapılır?
- Gizli bilgilerin başkalarının eline geçmemesi
- Hizmetin engellenmemesi
- Yetkilendirme hiyerarşisinin aşılmaması
- Prestij ve güvenilirlik kaybının önlenmesi
- Bilgi kayıpları ve maddi zararların önlenmesi
- Hukuki sorunların tespit edilmesi

### İki Tür Güvenlik Testi 🔥🔥🔥

#### Black Box Testing (Siyah Kutu Testi)
- Yazılımın **iç bileşenleri hesaba katılmadan**, sadece **girdi ve çıktılar** değerlendirilir
- Dışarıdan bir **saldırgan gözüyle** izlenir
- Test uzmanı kodun iç yapısını **bilmez**
- Ne kadar bilgi açığa çıkarılabilir → **bulgu**

#### White Box Testing (Beyaz Kutu Testi)
- Yazılım **içerden** bir yazılımcı/yönetici gibi incelenir
- Test uzmanı **çalışır haldeki koda** bakarak güvenlik gereksinimlerini denetler
- Sadece kod güvenliği değil, **tüm bilişim sistemi** gözden geçirilir

> [!TIP]
> **Sınav İpucu:** Black Box = Dışarıdan bakılır, iç yapı bilinmez. White Box = İçerden bakılır, kod görülür. Bu ayrımı kesinlikle bilin!

### Bulgu Nedir? ⭐
- Bir saldırganın verilmesi **planlanmayan** bir bilgiyi ifşa etmesini sağlayacak her tespit
- Veya verilmesi **planlanan** bir bilginin ifşa edilmesinin **engellenmesini** sağlayacak her tespit

**Bulgu Örnekleri:**
- Şifrelerin açığa çıkabilmesi
- Hesap kilitleme (5 hatalı girişle) → **Hizmet Engelleme bulgusu**
- JavaScript/HTML enjeksiyonu (filtreleme eksikliği)
- Cookie bilgisi çalınması

### XSS/HTML Enjeksiyon Riskleri
- Kullanıcı sahte ekranlarla kandırılabilir
- Oturum çerez bilgisi çalınabilir → yetkisiz işlem
- Sayfa engellenebilir
- Yeni saldırı senaryoları üretilebilir

---

## 7.6 E-ticaret Güvenlik Hususları

### Güvenlik Araçları
- Virüs koruma yazılımı
- E-posta filtreleme, URL filtreleme
- Güvenlik duvarları, ağ geçitleri, VPN
- İzinsiz giriş tespit ürünleri
- Güvenlik açığı yönetimi
- **SSL** (kimlik doğrulama), **Şifreleme teknolojileri**
- **PKI** (Public Key Infrastructure) - Dijital sertifika

### E-ticaret Gizlilik Kuralları
- Kurumsal gizlilik politikasıyla başlayın
- Yalnızca **işlemi tamamlamak için gereken bilgileri** isteyin
- Kişisel bilgi doldurmayı **isteğe bağlı** yapın
- Anonim bilgi edinmeye olanak tanıyan kaynaklar kullanın
- **Etik olun**

---

# 📝 SINAV HAZIRLIK: PRATİK SORULAR

## Çoktan Seçmeli Sorular

**S1:** Fizibilite çalışması hangi soruyu cevaplar?
- a) NASIL?
- b) **NE? ✅**
- c) NE ZAMAN?
- d) KİM?

**S2:** Genel tasarım aşaması hangi soruyu cevaplar?
- a) NE?
- b) **NASIL? ✅**
- c) NEREDE?
- d) NE KADAR?

**S3:** Pareto İlkesine göre bir sorunun %80'i, nedenlerin yüzde kaçından kaynaklanır?
- a) %80
- b) %50
- c) **%20 ✅**
- d) %10

**S4:** Üç nokta tahmini formülü nedir?
- a) (a + b + m) / 3
- b) **(a + 4m + b) / 6 ✅**
- c) (a + 2m + b) / 4
- d) (a + m + b) / 3

**S5:** Hangisi çevik değerlerden biri DEĞİLDİR?
- a) İletişim
- b) Basitlik
- c) Geri bildirim
- d) **Hız ✅** (Doğrusu: Cesaret)

**S6:** Hangisi fizibilite türlerinden biri DEĞİLDİR?
- a) Teknik fizibilite
- b) Ekonomik fizibilite
- c) Operasyonel fizibilite
- d) **Sosyal fizibilite ✅**

**S7:** Doğrudan geçişin en büyük dezavantajı nedir?
- a) Yavaş geçiş
- b) **Yüksek riskli yaklaşım ✅**
- c) İş yükünün artması
- d) Maliyet

**S8:** Paralel dönüşümün en büyük dezavantajı nedir?
- a) Riskli
- b) Yavaş
- c) **İş yükünün iki katına çıkması ✅**
- d) Karmaşıklık

**S9:** Kademeli dönüşüm hangi metodolojiye uygundur?
- a) Şelale
- b) **Çevik ✅**
- c) Nesne tabanlı
- d) Paralel

**S10:** Black Box Testing'de test uzmanı neyi bilmez?
- a) Girdi verilerini
- b) Çıktı verilerini
- c) **Yazılımın iç kod yapısını ✅**
- d) Kullanıcı gereksinimlerini

**S11:** EVM'de BAC ne anlama gelir?
- a) Planlanan değer
- b) Gerçek maliyet
- c) Kazanılmış değer
- d) **Tamamlandığındaki bütçe ✅**

**S12:** İş kırılım yapısının diğer adı nedir?
- a) Gantt Chart
- b) PERT Diyagramı
- c) **WBS (Work Breakdown Structure) ✅**
- d) Balık Kılçığı Diyagramı

**S13:** Birim testi hangi test türüne girer?
- a) Black Box
- b) **Saydam/White Box ✅**
- c) Gri kutu
- d) Fonksiyon testi

**S14:** Modüler prototip dönüşümü hangi metodolojiye uygundur?
- a) Çevik
- b) **Nesneye yönelik ✅**
- c) Şelale
- d) Fazlandırılmış

**S15:** Balık kılçığı diyagramının diğer adları nelerdir?
- a) **Neden-sonuç diyagramı ve Ishikawa diyagramı ✅**
- b) PERT diyagramı ve Gantt şeması
- c) Pareto diyagramı ve WBS
- d) UML diyagramı ve akış şeması

---

## Klasik/Açık Uçlu Soru Örnekleri

**S1:** SGYD aşamalarını sırasıyla yazınız ve her birinin amacını kısaca açıklayınız.

**S2:** Şelale, Paralel Geliştirme ve Fazlandırılmış Geliştirme modellerini karşılaştırınız. Her birinin avantaj ve dezavantajlarını belirtiniz.

**S3:** 5 dönüşüm stratejisini karşılaştırarak avantaj ve dezavantajlarını açıklayınız.

**S4:** Teknik, Ekonomik ve Operasyonel Fizibiliteyi açıklayınız. Her biri için birer örnek veriniz.

**S5:** Black Box ve White Box testing arasındaki farkları açıklayınız.

**S6:** EVM'nin 4 temel ölçeğini açıklayınız.

**S7:** Çevik değerleri ve prensiplerini sıralayınız.

**S8:** Proje şartları dokümanının (charter) cevapladığı soruları yazınız.

---

> [!TIP]
> ## 🎯 SINAV STRATEJİSİ
> 1. **Önce tabloları ezberleyin** — Dönüşüm stratejileri, fizibilite türleri, test seviyeleri
> 2. **Formülleri bilin** — Üç nokta tahmini formülü: (a + 4m + b) / 6
> 3. **Karşılaştırma yapabilin** — Şelale vs Çevik vs OO, Black Box vs White Box
> 4. **Anahtar kelimeleri bilin** — WBS, PERT, Gantt, EVM, BAC, PV, AC, EV, UAT
> 5. **Eşleştirmeleri ezberleyin** — Kademeli→Çevik, Modüler→OO, Fizibilite=NE, Genel Tasarım=NASIL
