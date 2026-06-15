# 🔒 SİBER GÜVENLİK — DETAYLI SINAV NOTLARI

> [!IMPORTANT]
> Bu notlar siber güvenlik ders müfredatındaki kritik konuları genelden özele ele almaktadır. Sınav için kritik noktalar ⭐ ile, her adayı ilgilendiren teknik derinliğe sahip konular 🔥 ile işaretlenmiştir.

---

# BÖLÜM 1: SİBER GÜVENLİK TEMELLERİ VE ŞİFRELEME

## 1.1 Şifreleme Tarihi ⭐

**Giriş:** İletişimin gizliliğini koruma ihtiyacı insanlık tarihi kadar eskidir. Kriptoloji, şifre bilimi anlamına gelir ve iki ana dala ayrılır: Şifre yazımı (Kriptografi) ve şifre çözümü/analizi (Kriptanaliz). Şifreleme tarihi temel olarak klasik ve modern dönem olmak üzere ikiye ayrılır.

### A) Klasik Şifreleme Dönemi
Klasik şifreleme yöntemleri genellikle karakter ikamesi (substitution) veya yer değiştirme (transposition) mantığına dayanır ve kalem-kağıt yardımıyla el yordamıyla gerçekleştirilmiştir.

| Şifreleme Türü | Temel Mantığı | Zayıflıkları |
|----------------|---------------|--------------|
| **Sezar Şifrelemesi** | Alfabedeki her harfi belirlenen bir kaydırma miktarı kadar (örn. 3 karakter sağa) kaydırarak şifreleme yapar. Bir ikame şifrelemesidir. | Yalnızca 25-29 farklı anahtar kombinasyonu (alfabedeki harf sayısı kadar) barındırdığı için deneme-yanılma (brute-force) ile saniyeler içinde çözülür. |
| **Vigenère Şifrelemesi** | Tek bir kaydırma miktarı yerine, tekrarlayan bir anahtar kelime kullanarak çoklu alfabeye göre şifreleme (polyalphabetic substitution) yapar. | Anahtar kelimenin uzunluğu kadar periyotlar halinde frekans analizi yapıldığında (Kasiski testi yardımıyla) kolayca kırılabilir. |
| **Enigma Şifreleme Makinesi** | II. Dünya Savaşı sırasında Almanya tarafından kullanılan, dönen diskler (rotorlar) yardımıyla her harf basımında elektrik devresini ve dolayısıyla alfabeyi değiştiren elektromekanik bir cihazdır. | Alan Turing ve ekibi tarafından tasarlanan "Bombe" makinesiyle, mesajların başındaki standart kalıplar (hava raporu vb.) kullanılarak kırılmıştır. |

> [!TIP]
> **Kritik Kavram (Frekans Analizi):** Her dilde harflerin kullanım sıklığı (frekansı) farklıdır. Örneğin Türkçe'de en sık kullanılan harfler "A", "E" ve "İ"dir. Şifreli metindeki en sık geçen karakterler tespit edilerek dilin harf sıklığıyla eşleştirilir ve şifre çözülür.

### B) Modern Kriptografiye Geçiş
Modern kriptografi, Claude Shannon'ın 1949 yılında yayımladığı "Gizlilik Sistemlerinin Haberleşme Teorisi" makalesiyle matematiksel bir zemine oturmuştur.

- **Tek Kullanımlık Şerit (One-Time Pad - OTP):** Matematiksel olarak asla kırılması mümkün olmayan (perfect secrecy) tek şifreleme yöntemidir. Şifreleme anahtarı, şifrelenecek metinle aynı uzunlukta, tamamen rastgele üretilmiş olmalı ve yalnızca bir kez kullanılmalıdır. İletim sırasında XOR kapısı kullanılır.
- **Zayıflığı:** Anahtarın alıcıya güvenli bir şekilde ulaştırılması (anahtar dağıtım problemi) pratik olarak uygulanmasını zorlaştırır.

---

## 1.2 Asimetrik ve Simetrik Şifreleme 🔥

Modern şifreleme yöntemleri kullanılan anahtar yapısına göre iki ana gruba ayrılır. İkisi arasındaki temel farklar hız, anahtar yönetimi ve güvenlik fonksiyonlarıdır.

```
Simetrik: [Açık Metin] ──(Ortak Gizli Anahtar)──> [Şifreli Metin] ──(Ortak Gizli Anahtar)──> [Açık Metin]
Asimetrik: [Açık Metin] ──(Alıcının Public Anahtarı)──> [Şifreli Metin] ──(Alıcının Private Anahtarı)──> [Açık Metin]
```

### A) Simetrik (Gizli Anahtarlı) Şifreleme
Şifreleme ve deşifreleme işlemleri için aynı gizli anahtarın kullanıldığı yöntemdir.

- **Özellikleri:** Çok hızlı çalışır, düşük işlemci gücü gerektirir. Büyük verileri şifrelemek için idealdir.
- **Anahtar Yönetim Problemi:** Güvenli olmayan bir hat üzerinden bu gizli anahtarın alıcıya nasıl ulaştırılacağı en büyük sorundur. Cihaz sayısı arttıkça gereken anahtar sayısı üstel olarak artar: $N(N-1)/2$ adet anahtar gerekir.
- **Önemli Algoritmalar:**
  1. **DES (Data Encryption Standard):** 56-bitlik kısa anahtar boyutu nedeniyle günümüzde güvensiz kabul edilir.
  2. **3DES (Triple DES):** DES algoritmasının veriyi üç kez şifrelemesi esasına dayanır, yavaştır.
  3. **AES (Advanced Encryption Standard):** Günümüz standardıdır. 128, 192 ve 256 bit anahtar boyutlarını destekler. Oldukça güvenli ve performanslıdır.
  4. **RC4 (Rivest Cipher 4):** Akış şifrelemesidir (stream cipher). Eski WEP protokollerinde kullanılmış olup artık güvensiz kabul edilir.

### B) Asimetrik (Açık Anahtarlı) Şifreleme
Matematiksel olarak birbiriyle ilişkili iki farklı anahtar çiftinin (Açık Anahtar - Public Key ve Gizli Anahtar - Private Key) kullanıldığı yöntemdir.

- **Özellikleri:** Açık anahtar herkesle paylaşılabilir, gizli anahtar ise sadece sahibinde kalır. Anahtar dağıtım problemi yoktur. Gizlilik yanında kimlik doğrulama ve inkâr edememe (non-repudiation) özelliklerini sağlar.
- **Zayıflığı:** Simetrik şifrelemeye göre çok yavaştır (yaklaşık 1000 kat daha yavaş). Matematiksel olarak büyük asal sayıların çarpımına veya eliptik eğriler üzerindeki logaritma problemlerine dayanır.
- **Önemli Algoritmalar:**
  1. **RSA:** İki büyük asal sayının çarpımının çarpanlarına ayrılmasının zorluğuna dayanır. Günümüzde en az 2048-bit anahtar boyutu önerilir.
  2. **Diffie-Hellman:** Güvensiz bir hat üzerinden iki tarafın ortak bir gizli anahtar üretmesini sağlayan anahtar değişim protokolüdür. Şifreleme yapmaz, ortak anahtar üretir.
  3. **ECC (Elliptic Curve Cryptography):** Eliptik eğri matematiğine dayanır. Çok daha küçük anahtar boyutlarıyla (örneğin 256-bit ECC, 3072-bit RSA'e eşdeğerdir) aynı güvenlik seviyesini sunarak mobil ve IoT cihazlar için yüksek performans sağlar.

### Karşılaştırma Tablosu

| Özellik | Simetrik Şifreleme | Asimetrik Şifreleme |
|---------|---------------------|----------------------|
| **Anahtar Sayısı** | Taraf başına 1 ortak gizli anahtar | Taraf başına 2 anahtar (Public + Private) |
| **Hız** | Çok Hızlı | Yavaş |
| **Kullanım Amacı** | Büyük dosyaların/verilerin şifrelenmesi | Anahtar değişimi, Dijital İmza, Kimlik Doğrulama |
| **Ölçeklenebilirlik** | Zor (Kullanıcı sayısı arttıkça anahtar sayısı patlar) | Kolay (Her kullanıcının sadece kendi anahtar çifti vardır) |

> [!CAUTION]
> **Hibrit Şifreleme (Hybrid Encryption):** Gerçek dünyadaki uygulamaların (HTTPS, SSH, TLS) neredeyse tamamı hibrit yöntem kullanır. İletişim başında **Asimetrik şifreleme** ile taraflar arasında güvenli bir tek seferlik "oturum anahtarı" (session key) paylaşılır. Ardından asıl veri aktarımı bu anahtar kullanılarak **Simetrik şifreleme** ile gerçekleştirilir.

---

# BÖLÜM 2: AĞ VE SİSTEM GÜVENLİĞİ

## 2.1 Firewall ve VPN Teknolojileri ⭐

**Açıklama:** Ağ güvenliğinin temel yapı taşları, iç ağı dış dünyadan korumak (Firewall) ve güvensiz ağlar üzerinden güvenli tüneller oluşturmaktır (VPN).

### A) Güvenlik Duvarı (Firewall) Gelişimi
Güvenlik duvarları, önceden tanımlanmış kurallara göre gelen ve giden ağ trafiğini izleyen ve engelleyen ağ güvenlik sistemleridir.

1. **Paket Filtreleme Güvenlik Duvarları (Stateless - Durumsuz):**
   - Paketlerin yalnızca kaynak IP, hedef IP, kaynak port ve hedef port bilgilerine (OSI 3. ve 4. Katman) bakar.
   - Paketin geçmişiyle veya önceki paketlerle olan ilişkisiyle ilgilenmez. Hızlıdır ancak gelişmiş saldırılara karşı yetersizdir.
2. **Durumsal Denetim Güvenlik Duvarları (Stateful Inspection):**
   - Aktif bağlantıların durumunu bir "durum tablosunda" (state table) tutar.
   - Dışarıdan gelen bir paketin, içeriden başlatılmış meşru bir oturuma ait olup olmadığını kontrol eder. İçeriden başlatılmamış paketleri otomatik engeller.
3. **Uygulama Katmanı Güvenlik Duvarları (Proxy Firewall):**
   - Trafiği uygulama seviyesinde (OSI 7. Katman - HTTP, FTP vb.) keser ve inceler. En güvenli ancak en yavaş çalışan yöntemdir.
4. **Yeni Nesil Güvenlik Duvarları (NGFW - Next-Generation Firewall):**
   - Klasik stateful kurallarına ek olarak; Derin Paket İnceleme (DPI), Uygulama Farkındalığı (Application Awareness), Saldırı Önleme Sistemi (IPS) entegrasyonu ve Tehdit İstihbaratı gibi özellikleri tek bir platformda birleştirir.

### B) VPN (Virtual Private Network - Sanal Özel Ağ)
VPN, güvensiz bir ortak ağ (genellikle İnternet) üzerinden iki cihaz veya ağ arasında şifreli tüneller oluşturarak güvenli veri aktarımı sağlar.

```
[Merkez Ofis] <==== Şifreli Tünel (IPsec/SSL) ====> [Şube / Uzak Çalışan]
```

- **Tünelleme Protokolleri:**
  - **IPsec (Internet Protocol Security):** Ağ katmanında çalışır. Genellikle şubeler arası (Site-to-Site) VPN bağlantılarında kullanılır. İki ana modu vardır:
    * *Taşıma Modu (Transport Mode):* Sadece veri kısmını (payload) şifreler, IP başlığı şifrelenmez.
    * *Tünel Modu (Tunnel Mode):* Paketin tamamını şifreler ve yeni bir IP başlığı ekler. En güvenli moddur.
  - **SSL/TLS VPN:** Uygulama katmanında çalışır. Genellikle kullanıcıların tarayıcı veya hafif istemciler üzerinden şirket içine bağlanması (Remote Access / Client-to-Site) için tercih edilir. Port 443'ü kullandığı için firewall engellerine takılmaz.
  - **WireGuard:** Son yıllarda popülerleşen, IPsec ve OpenVPN'e göre çok daha az kod satırıyla yazılmış, yüksek performanslı ve modern kriptografi kullanan yeni nesil VPN protokolüdür.

---

## 2.2 Nüfuz Tespit ve Önleme Sistemleri (IDS/IPS) 🔥

**Tanım:** Ağ veya sistemler üzerindeki şüpheli aktiviteleri ve güvenlik ihlallerini tespit etmek ve gerekirse müdahale etmek amacıyla kullanılan yazılım veya donanım sistemleridir.

### A) IDS vs IPS Farkı
- **IDS (Intrusion Detection System - Saldırı Tespit Sistemi):** Pasif bir sistemdir. Trafiği izler, analiz eder ve bir tehdit algıladığında ağ yöneticisine alarm üretir. Trafik akışını doğrudan kesmez.
- **IPS (Intrusion Prevention System - Saldırı Önleme Sistemi):** Aktif bir sistemdir. Ağ trafiğinin geçiş hattı üzerinde (inline) konumlandırılır. Bir saldırı tespit ettiğinde paketi düşürür (drop) ve bağlantıyı anında sonlandırır.

### B) Konumlandırma Modelleri
- **NIDS / NIPS (Network-based):** Tüm ağ segmentindeki trafiği analiz etmek amacıyla kritik ağ anahtarlarının (switch) ayna portlarına (SPAN) veya hat arasına kurulur. Tüm ağı izler.
- **HIDS / HIPS (Host-based):** Doğrudan kritik sunuculara (örn: veritabanı veya web sunucusu) kurulur. Sistem loglarını, dosya bütünlüğünü (FIM) ve çalışan süreçleri izler. Ağ trafiğini analiz etmez.

### C) Algılama Yöntemleri
1. **İmza Tabanlı Algılama (Signature-based):** Bilinen saldırıların dijital izleri (imzaları) veritabanında saklanır. Gelen trafik bu imzalarla karşılaştırılır.
   - *Avantajı:* Bilinen saldırıları sıfıra yakın hata ile yakalar.
   - *Dezavantajı:* Sıfırıncı gün (zero-day) saldırılarını ve henüz tanımlanmamış yeni virüsleri yakalayamaz.
2. **Anomali Tabanlı Algılama (Anomaly-based / Davranışsal):** Sistemin veya ağın "normal" çalışma düzeni (baseline) öğrenilir. Bu normalin dışındaki sapmalar saldırı olarak kabul edilir.
   - *Avantajı:* Sıfırıncı gün saldırılarını yakalayabilir.
   - *Dezavantajı:* Çok sayıda **False Positive** (Yanlış Alarm - Temiz bir işlemi saldırı sanma) üretir.

> [!WARNING]
> **Kritik Metrikler:**
> - **False Positive (Yanlış Pozitif):** Zararsız bir ağ paketinin sistem tarafından saldırı olarak algılanmasıdır. İş kesintisine yol açabilir.
> - **False Negative (Yanlış Negatif):** Gerçek bir saldırının sistem tarafından fark edilmeyip gözden kaçırılmasıdır. En tehlikeli durumdur.

---

## 2.3 Yerel Ağ (LAN) Güvenliği ⭐

**Açıklama:** Güvenlik dış kapıdan değil, en içeriden, yani yerel ağ switch katmanından başlar. Saldırganların fiziksel olarak binaya sızıp bir ethernet kablosu takması durumunda yapılacak korumaları içerir.

### A) Switch Port Güvenliği (Port Security)
Ağ anahtarındaki (Switch) fiziksel portlara hangi cihazların bağlanabileceğini kontrol etme yöntemidir.

- **MAC Adresi Limitleme:** Bir porta maksimum bağlanabilecek benzersiz cihaz (MAC adresi) sayısı belirlenir (genellikle 1).
- **Sticky MAC:** Portun bağlanan ilk cihazın MAC adresini otomatik öğrenip konfigürasyona kaydetmesini sağlar.
- **İhlal Eylemleri (Violation Modes):** Yabancı bir MAC adresi takıldığında switch'in vereceği tepki:
  1. *Protect:* Yabancı cihazın paketlerini sessizce engeller, log üretmez.
  2. *Restrict:* Yabancı cihazı engeller, SNMP logu ve hata mesajı üretir.
  3. *Shutdown:* Portu tamamen kapatır (`err-disable` moduna alır). Yönetici elle açana kadar port çalışmaz. En güvenli yöntemdir.

### B) 802.1X ve NAC (Network Access Control)
Ağa kablolu veya kablosuz olarak bağlanan cihazların kimlik doğrulamasından geçirilmesini zorunlu kılan protokoldür. Cihaz geçerli kullanıcı adı/şifre veya sertifika sunana kadar ağa erişimi engellenir.
- **Bileşenleri:** İstemci (Supplicant), Ağ Anahtarı/AP (Authenticator) ve Kimlik Doğrulama Sunucusu (Authentication Server - RADIUS/TACACS+).

### C) Switch Katmanı Saldırı Önleme Yöntemleri

| Saldırı Türü | Açıklama | Önleme Yöntemi |
|--------------|----------|----------------|
| **DHCP Spoofing** | Saldırgan ağda sahte bir DHCP sunucusu kurarak kullanıcılara kendi IP'sini varsayılan ağ geçidi (gateway) olarak dağıtır ve trafiği dinler (MitM). | **DHCP Snooping:** Switch portları "güvenilir" (trusted) ve "güvenilmez" (untrusted) olarak ayrılır. DHCP teklif paketleri (DHCPOFFER) sadece güvenilir portlardan kabul edilir. |
| **ARP Spoofing** | Saldırgan, hedef bilgisayarlara sahte ARP mesajları göndererek gateway'in MAC adresinin kendi MAC adresi olduğunu söyler. Trafik saldırganın üzerinden geçer. | **Dynamic ARP Inspection (DAI):** DHCP Snooping tablosunu kullanarak gelen ARP paketlerinin IP-MAC eşleşmesini doğrular. Geçersiz eşleşmeleri engeller. |
| **IP Spoofing** | Saldırgan, paketin kaynak IP adresini ağdaki yetkili başka bir cihazın IP'si gibi göstererek sızmaya çalışır. | **IP Source Guard:** DHCP Snooping tablosuna dayanarak porttan gelen paketlerin kaynak IP ve MAC adreslerini doğrular, sahteleri engeller. |
| **VLAN Hopping** | Saldırgan, switch arasındaki trunk bağlantı protokollerini (DTP) manipüle ederek yetkisi olmayan diğer VLAN'lara geçiş yapar. | Kullanılmayan switch portlarının kapatılması, default VLAN 1'den çıkarılması ve otomatik trunking protokollerinin (DTP) devre dışı bırakılması gerekir. |

---

# BÖLÜM 3: KURUMSAL GÜVENLİK VE YÖNETİM

## 3.1 SIEM, DLP ve MDM Çözümleri 🔥

**Giriş:** Kurumsal siber güvenlik yönetiminde merkezi izleme (SIEM), veri güvenliği (DLP) ve uç cihaz yönetimi (MDM) üç temel sac ayağını oluşturur.

### A) SIEM (Security Information and Event Management)
SIEM, tüm ağ cihazlarından, sunuculardan ve uygulamalardan gelen logları (günlük kayıtlarını) tek bir merkezde toplayıp analiz eden sistemdir.

- **SIEM Çalışma Aşamaları:**
  1. *Log Toplama (Collection):* Sistemlerden ham loglar çekilir.
  2. *Normalizasyon (Normalization):* Farklı formatlardaki loglar (IIS logu, Firewall logu vb.) ortak bir dile çevrilir.
  3. *Korelasyon (Correlation):* **SIEM'in kalbidir.** Farklı sistemlerden gelen olaylar arasında ilişkiler kurularak anlamlı kurallar işletilir.
     - *Örnek Korelasyon:* "Aynı kullanıcı 5 saniye içinde 5 kez yanlış şifre girdi (Active Directory logu) VE hemen ardından VPN ile başarılı giriş yaptı (Firewall logu) -> Brute Force / Yetkisiz Erişim Alarımı Üret!"
  4. *Alarm Üretimi ve Bildirim:* Şüpheli durumlar için güvenlik ekibine (SOC) uyarı gönderilir.

### B) DLP (Data Loss Prevention - Veri Sızıntısı Önleme)
DLP, kurumun hassas ve gizli verilerinin (müşteri bilgileri, kaynak kodlar, finansal tablolar vb.) yetkisiz kişilerin eline geçmesini ve kurum dışına sızdırılmasını engelleyen teknolojidir.

- **DLP'de Veri Sınıflandırma Durumları:**
  - **İletimdeki Veri (Data in Motion):** Ağ üzerinden e-posta, web transferi veya anlık mesajlaşma ile aktarılan veriler. Ağ DLP (Network DLP) ile korunur.
  - **Depolanan Veri (Data at Rest):** Veritabanlarında, dosya sunucularında veya hard disklerde duran veriler. Keşif araçlarıyla taranarak şifrelenir veya taşınır.
  - **Kullanımdaki Veri (Data in Use):** Kullanıcının bilgisayarında aktif olarak açtığı, kopyaladığı, USB'ye yazdırdığı veya yazıcıdan bastığı veri. Endpoint DLP ile kontrol edilir.

### C) MDM (Mobile Device Management - Mobil Cihaz Yönetimi)
Kurum çalışanlarının akıllı telefon ve tablet gibi mobil cihazlarının merkezi olarak yönetilmesi ve güvenliğinin sağlanması sürecidir.

- **Temel Fonksiyonlar:**
  - *Uzaktan Silme (Remote Wipe):* Cihaz kaybolduğunda içindeki kurumsal veriler uzaktan tamamen silinir.
  - *Kapsülleme (Containerization):* Cihazda kişisel alan ile kurumsal alan (şirket postası, belgeleri) birbirinden tamamen ayrılır. Kişisel alandaki bir uygulama kurumsal veriyi kopyalayamaz.
  - *Politika Dayatma:* Şifre zorunluluğu, kamera kullanımının engellenmesi, root/jailbreak tespiti gibi güvenlik kuralları zorunlu kılınır.

---

## 3.2 ISO 27001 Bilgi Güvenliği Yönetim Sistemi ⭐

**Tanım:** ISO 27001, kurumların bilgi güvenliği risklerini yönetmek amacıyla kuracakları "Bilgi Güvenliği Yönetim Sistemi" (BGYS / ISMS) standartlarını belirleyen tek uluslararası denetlenebilir standarttır.

### A) BGYS Yapısı ve Temel Maddeler (4 - 10)
ISO 27001 standardı iki ana bölümden oluşur. İlk kısım BGYS'nin yönetimsel çerçevesini çizen zorunlu standart maddeleridir (4-10 arası maddeler):
- *Madde 4:* Kuruluşun Bağlamı (iç ve dış hususlar)
- *Madde 5:* Liderlik (üst yönetimin taahhüdü ve bilgi güvenliği politikası)
- *Madde 6:* Planlama (risk değerlendirme ve risk işleme süreçleri)
- *Madde 7:* Destek (kaynaklar, yetkinlik, farkındalık, iletişim)
- *Madde 8:* İşletim (planlanan risk değerlendirmelerinin yürütülmesi)
- *Madde 9:* Performans Değerlendirme (iç tetkik, yönetimin gözden geçirmesi)
- *Madde 10:* İyileştirme (uygunsuzluklar ve düzeltici faaliyetler)

### B) ISO 27001 Ek-A (Annex A) Kontrolleri
Standardın ikinci kısmı olan Ek-A, kurumun uygulayabileceği teknik, fiziksel ve organizasyonel güvenlik kontrollerinin listesini içerir. Risk analizine göre bu kontrollerden hangilerinin uygulanacağı seçilir ve **Uygulanabilirlik Bildirgesi (SoA - Statement of Applicability)** dokümanında gerekçeleriyle listelenir.

### C) Risk Yönetimi ve PUKÖ Döngüsü
- **Risk Değerlendirme:** Bilgi varlıkları üzerindeki tehditler ve açıklıklar analiz edilerek risk seviyesi (Olasılık x Etki) hesaplanır.
- **Risk İşleme Seçenekleri:** Risk tespit edildikten sonra 4 yoldan biri seçilir:
  1. *Azaltma (Mitigation):* Güvenlik önlemleri alarak riski düşürmek (örn: firewall kurmak).
  2. *Devretme (Transfer):* Riski başkasına yüklemek (örn: siber sigorta yaptırmak, outsourcing).
  3. *Kaçınma (Avoidance):* Riski doğuran faaliyeti sonlandırmak (örn: tehlikeli bir servisi kapatmak).
  4. *Kabul Etme (Acceptance):* Riskin getireceği maliyet düşükse, riski olduğu gibi kabul etmek.
- **PUKÖ (PDCA) Döngüsü:** Sürekli iyileştirme için sistem her zaman döner:
  ```
  Planla (Plan) -> Uygula (Do) -> Kontrol Et (Check) -> Önlem Al (Act)
  ```

---

## 3.3 Biyometrik Şifreleme ve Kimlik Doğrulama

**Açıklama:** Kullanıcının fiziksel veya davranışsal özelliklerini analiz ederek kimlik doğrulama gerçekleştiren gelişmiş güvenlik sistemleridir.

### A) Biyometri Türleri
Biyometrik özellikler statik ve dinamik olmak üzere ikiye ayrılır:

1. **Fizyolojik Biyometri (Değişmeyen Fiziksel Özellikler):**
   - *Parmak İzi:* En yaygın ve ucuz yöntemdir.
   - *İris Tanıma:* Gözün iris tabakasındaki rastgele desenleri tarar. Doğruluk oranı en yüksek yöntemlerden biridir.
   - *Retina Tarama:* Gözün arkasındaki kılcal damar yapısını inceler. Güvenlidir ancak kullanıcı için rahatsız edicidir.
   - *Yüz Tanıma:* Yüzdeki kemik yapısı ve referans noktaları arasındaki mesafeleri ölçer.
2. **Davranışsal Biyometri (Kullanıcının Alışkanlıkları):**
   - *Ses Tanıma:* Konuşma sırasındaki frekans ve ton değişimlerini analiz eder (ortam gürültüsünden etkilenir).
   - *Tuş Vuruş Dinamiği (Keystroke Dynamics):* Kullanıcının klavyede tuşlara basma hızı, tuşlar arası geçiş süreleri.
   - *Yürüyüş (Gait) Analizi:* Bireyin kendine has adım atma ve yürüme stilinin tespiti.

### B) Performans Metrikleri ve Hata Oranları
Biyometrik sistemlerin başarısı şu üç temel metrikle ölçülür:

- **FAR (False Acceptance Rate - Yanlış Kabul Oranı):** Sistemde kayıtlı olmayan yabancı birinin sistem tarafından yanlışlıkla yetkili kullanıcı olarak kabul edilmesi oranıdır. Güvenlik açığı yaratır.
- **FRR (False Rejection Rate - Yanlış Reddetme Oranı):** Gerçek sistem sahibinin sistem tarafından tanınmayıp reddedilmesi oranıdır. Kullanıcı konforunu bozar.
- **EER (Equal Error Rate - Eşit Hata Oranı):** FAR ve FRR oranlarının eşitlendiği hassasiyet noktasıdır. **EER değeri ne kadar küçükse, biyometrik sistem o kadar başarılı ve kalitelidir.**

---

## 3.4 Yıkımdan Korunma ve İş Sürekliliği 🔥

**Açıklama:** Doğal afetler (deprem, yangın vb.) veya büyük siber saldırılar (fidye yazılımı vb.) sonucunda şirketin bilgi sistemlerinin çökmesi durumunda işin devam etmesini sağlama sürecidir.

### A) RPO ve RTO Metrikleri (Mutlaka Ezberle!)
Bir felaket anında veri kurtarma hedeflerini belirleyen en kritik iki parametredir.

```
Felaket Anı
   │ <────────── RPO ──────────│────────── RTO ──────────> │
Son Başarılı Yedek          Olay Anı                   Sistemlerin Açılması
(Kabul Edilebilir Veri Kaybı)                        (Kabul Edilebilir Kesinti Süresi)
```

- **RPO (Recovery Point Objective - Kurtarma Noktası Hedefi):** Felaket anında kurumun kabul edebileceği **maksimum veri kaybı süresidir**. Örneğin RPO = 4 saat ise, felaket anında en fazla son 4 saatlik verinin kaybına tahammül edilebilir. Bu değer yedekleme sıklığını belirler.
- **RTO (Recovery Time Objective - Kurtarma Süresi Hedefi):** Felaket sonrasında sistemlerin yeniden çalışır hale gelmesi için kabul edilebilir **maksimum kesinti süresidir**. Örneğin RTO = 2 saat ise, sistemler en geç 2 saat içinde tekrar ayağa kaldırılmalıdır.

### B) Veri Yedekleme Yöntemleri
1. **Tam Yedekleme (Full Backup):** Seçilen tüm verilerin tamamı yedeklenir. Kurtarması en hızlı, yedeklemesi en uzun süren ve en çok disk alanı kaplayan yöntemdir.
2. **Fark Yedeklemesi (Differential Backup):** En son yapılan **Tam Yedeklemeden** sonra değişen tüm veriler yedeklenir. Kurtarmak için son Tam yedek ve son Fark yedeği yeterlidir.
3. **Artımlı Yedekleme (Incremental Backup):** En son yapılan **herhangi bir yedekten (tam veya artımlı)** sonra değişen veriler yedeklenir. En az disk alanını kaplar ancak kurtarmak için tüm artımlı yedeklerin sırayla yüklenmesi gerektiğinden kurtarma süresi uzundur.

### C) Olağanüstü Durum Kurtarma Merkezleri (DRC)

| Merkez Türü | Özellikleri | Kurtarma Süresi | Maliyet |
|-------------|-------------|-----------------|---------|
| **Sıcak Merkez (Hot Site)** | Asıl merkezin birebir kopyasıdır. Sunucular çalışır vaziyettedir ve veriler anlık (senkron) olarak senkronize edilir. | Dakikalar / Saniyeler | En Yüksek |
| **Ilık Merkez (Warm Site)** | Altyapı ve bağlantılar hazırdır ancak sunucular pasiftir. Felaket anında son yedekler yüklenerek sistemler açılır. | Saatler / Günler | Orta |
| **Soğuk Merkez (Cold Site)** | Sadece fiziksel alan ve elektrik/iklimlendirme mevcuttur. Donanım ve yazılım kurulu değildir. | Günler / Haftalar | En Düşük |

---

# BÖLÜM 4: GELECEĞİN KRİPTOGRAFİSİ

## 4.1 Kuantum Şifreleme ve Post-Kuantum Dönemi ⭐

**Giriş:** Kuantum mekaniği prensiplerine (süperpozisyon ve dolanıklık) dayanan kuantum bilgisayarları, günümüzün geleneksel şifreleme yöntemleri için çok büyük bir tehdit oluşturmaktadır.

### A) Kuantum Bilgisayarlarının Mevcut Şifrelemelere Tehdidi
Kuantum bilgisayarları, paralel işlem güçleri sayesinde klasik bilgisayarların milyarlarca yılda çözemeyeceği matematiksel problemleri dakikalar içinde çözebilir.

1. **Shor Algoritması (Asimetrik Şifrelemenin Sonu):**
   - Shor algoritması çalıştıran güçlü bir kuantum bilgisayarı; asal sayı çarpanlarına ayırma (RSA) ve ayrık logaritma (Diffie-Hellman, ECC) problemlerini anında çözer.
   - Bu durum, günümüzde kullanılan HTTPS, SSL/TLS, bankacılık şifreleri ve blokzincir altyapılarının **tamamen kırılması** anlamına gelir.
2. **Grover Algoritması (Simetrik Şifrelemenin Zayıflaması):**
   - Grover algoritması, simetrik şifreleme anahtarlarını deneme-yanılma (brute force) süresini karekök oranında ($O(\sqrt{N})$) kısaltır.
   - Örneğin 128-bitlik AES anahtarının güvenlik seviyesini 64-bit seviyesine düşürür. Bu tehdide karşı korunmak için **AES-256** kullanılmalıdır (AES-256'nın kuantum korumalı gücü 128-bit düzeyinde kalacaktır ki bu hala kırılamazdır).

### B) Kuantum Anahtar Dağıtımı (QKD) ve BB84 Protokolü
Kuantum mekaniğini kullanarak iki taraf arasında kesinlikle dinlenemeyen bir gizli anahtar paylaşma yöntemidir.

- **Fiziksel İlke (Heisenberg Belirsizlik İlkesi):** Kuantum durumundaki bir fotonun ölçülmesi veya kopyalanması onun durumunu değiştirir. Saldırgan (Eve) hattı dinlemeye çalıştığında fotonların yapısını bozacağı için dinleme yapıldığı anında tespit edilir ve o anahtar iptal edilir.
- **BB84 Protokolü:** İlk QKD protokolüdür. Fotonların farklı polarizasyon filtreleri (yatay/dikey ve çapraz) kullanılarak gönderilmesi esasına dayanır.

### C) Post-Kuantum Kriptografi (PQC)
Kuantum bilgisayarlarının çözemeyeceği kadar karmaşık yeni matematiksel problemlere dayanan ve mevcut klasik bilgisayarlarda/ağlarda çalışabilen şifreleme algoritmalarıdır. NIST (Amerikan Standartlar Enstitüsü) tarafından Kyber, Dilithium gibi kafes tabanlı (lattice-based) algoritmalar yeni standartlar olarak seçilmektedir.

---

# BÖLÜM 5: GENEL ÖZET

## 5.1 Siber Güvenlik Genel Özet ve Kritik Notlar 🔥

1. ✅ **Şifreleme Tarihi:** Klasik şifrelemeler harf ikamesine dayanır, frekans analiziyle çözülür. Tek Kullanımlık Şerit (One-Time Pad) mükemmel gizlilik sağlayan tek kırılamaz yöntemdir.
2. ✅ **Simetrik vs Asimetrik:** Simetrik hızlıdır ve tek gizli anahtar kullanır (AES). Asimetrik yavaştır, çift anahtar kullanır (RSA, ECC), anahtar dağıtım problemini çözer. Gerçek hayatta ikisi bir arada (Hibrit) kullanılır.
3. ✅ **Güvenlik Duvarı (Firewall):** Stateless sadece paket başlığına bakar, Stateful durum tablosunu kontrol eder, NGFW ise uygulama katmanını derinlemesine denetler (DPI).
4. ✅ **VPN Protokolleri:** IPsec ağ katmanında çalışır (Site-to-Site için tünel modu), SSL/TLS uygulama katmanında çalışır (Remote Access için port 443).
5. ✅ **IDS vs IPS:** IDS pasiftir alarm üretir (ayna portta çalışır), IPS aktiftir saldırıyı anında keser (hat üzerinde inline konumlandırılır).
6. ✅ **Algılama Yöntemleri:** İmza tabanlı bilinen tehditleri yakalar, Anomali tabanlı bilinmeyen sıfırıncı gün saldırılarını yakalar ama çok sayıda False Positive (yanlış alarm) üretir.
7. ✅ **LAN Güvenliği:** Port Security ihlalinde port kapatılır (Shutdown). DHCP Snooping sahte DHCP sunucuları engeller, DAI ise ARP spoofing / MitM saldırılarını önler.
8. ✅ **SIEM:** Logları toplar, normalize eder ve en önemlisi **korelasyon** kuralları işleterek alarmlar üretir.
9. ✅ **DLP:** Hassas verinin sızmasını önler. Verinin 3 durumu vardır: İletimde (Motion), Depolanan (Rest) ve Kullanımda (Use).
10. ✅ **MDM:** Kurumsal cihaz güvenliğini sağlar. Cihaz kaybolduğunda uzaktan tamamen silinir (Remote Wipe) ve kurumsal veriler kapsüllenir (Containerization).
11. ✅ **ISO 27001:** BGYS standardıdır. PUKÖ (Planla-Uygula-Kontrol Et-Önlem Al) döngüsüyle sürekli iyileşmeyi hedefler. Kontroller Uygulanabilirlik Bildirgesinde (SoA) belgelenir.
12. ✅ **Biyometrik Başarı:** FAR (Yanlış Kabul) ve FRR (Yanlış Red) oranlarının eşitlendiği EER (Equal Error Rate) değeri ne kadar küçükse, sistem o kadar kalitelidir.
13. ✅ **Felaket Kurtarma:** RPO kabul edilebilir maksimum veri kaybı süresidir (yedekleme sıklığını belirler), RTO ise sistemlerin açılması için geçen maksimum kesinti süresidir.
14. ✅ **Kuantum Tehdidi:** Shor algoritması mevcut asimetrik şifrelemeyi (RSA, ECC) tamamen işlevsiz kılar. Grover algoritmasına karşı simetrik şifreleme anahtarları (AES-256) büyütülmelidir.
15. ✅ **LAN Güvenliği Altın Kuralı:** Kullanılmayan switch portları `shutdown` konumuna getirilmeli ve default VLAN 1 dışındaki pasif bir VLAN'a atanmalıdır.
