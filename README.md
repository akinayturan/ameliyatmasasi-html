# Beta Biomedikal — statik site

PHP, WordPress, MySQL ve Node.js sunucusu gerektirmeyen HTML/CSS/JavaScript site. Hazırlanan dosyalar `modern-site/` klasöründedir. Mevcut canlı siteye dağıtım yapılmadı.

## Yerel önizleme

```sh
python3 -m http.server 8080 --bind 127.0.0.1 --directory modern-site
```

Tarayıcıda http://127.0.0.1:8080 adresini açın. Kökten başlayan bağlantılar kullanıldığı için HTML dosyasını çift tıklayarak açmayın.

## Düzenleme ve yeniden üretim

- Sayfa şablonları ve gezinme: `scripts/build.py`
- Tasarım: `modern-site/assets/style.css`
- Menü, filtreler ve görsel büyütme: `modern-site/assets/app.js`
- Yedekten çıkarılan yayımlanmış WordPress içerikleri: `data/content.json`

```sh
python3 scripts/build.py
python3 scripts/validate.py
node --check modern-site/assets/app.js
```

Depoda yalnızca yayımlanmış sayfa içeriklerini içeren `data/content.json` bulunur; SQL ve sunucu yedekleri gönderilmez. Normal düzenleme ve üretim için yedek gerekmez.

Betikler Python standart kütüphanesiyle çalışır; paket kurulumu gerekmez. `extract_content.py`, `private/database/` içindeki SQL yedeğini okur; veritabanı sunucusu çalıştırmaz ve SQL komutlarını yürütmez. `build.py`, kurtarılan içerikleri ve dosyaları kullanır. CSS/JavaScript dosyalarını değiştirmez.

## Yayınlama

Yalnızca `modern-site/` **içeriği** alan adının web köküne yüklenmelidir. Hazır `ameliyatmasasi-static.zip` paketi aynı içeriği barındırır. Dosyalar alan adının kökünde çalışacak şekilde hazırlanmıştır. `backup_*`, `private/` ve SQL dosyalarını web köküne yüklemeyin.

Canlı geçiş sırasında önce mevcut WordPress web kökünün ayrı bir kopyasını alın; eski WordPress `.htaccess` dosyasını bu çıktının `.htaccess` dosyasıyla değiştirin. Apache üzerinde `DirectoryIndex` ve `ErrorDocument` kuralları dahildir. Nginx kullanılıyorsa `index index.html` ve `error_page 404 /404.html` sunucu yapılandırmasında tanımlanmalıdır. Yerel Python sunucusu Apache `.htaccess` kurallarını uygulamaz. WordPress dosyalarını yeni statik siteyle karışık bırakmak yerine ayrı web kökü kullanın; bu çalışma canlı dosyaları değiştirmedi.

## Taşıma kapsamı

- Ana sayfa, hakkımızda, ürünler, referanslar, basından ve iletişim.
- 7 ürün grubu; orijinal ürün metinleri, görseller ve teknik özellikler.
- 24 referans kaydı; kaynaktaki tekrarlar korunmuştur.
- 3 ürün broşürü, 2 basın PDF'i ve dergi reklamı.
- Eski `/about-us/`, `/urunlerimiz/`, `/faq/`, `/full-width/`, `/contact/`, `/homepage-2/`, `/archives/` ve `/sitemap/` adresleri.
- Eski ürün çapa adresleri ve `/wp-content/uploads/2018/10/` medya adresleri.
- Canonical, sayfa açıklamaları, Open Graph, sitemap.xml, robots.txt ve 404 sayfası.

## Bilinen farklar

- İletişim sayfasında form yerine açık bir e-posta iletişim metni ve tıklanabilir `bbmedikal@yahoo.com` adresi bulunur. E-posta bağlantısı ziyaretçinin e-posta uygulamasını açar. Telefon bağlantısı da kullanılabilir.
- Eski `/images/Ote2005.pdf` bağlantısının dosyası yedekte bulunamadı. Canlı sitedeki aynı adres ve eski www adresi de 30 Ekim 2026 tarihinde HTTP 404 döndürdü. Bu kırık bağlantı kaldırıldı; kurtarılan üç broşür kullanılabilir.
- Güncelliği doğrulanmamış eski “10 yıl” ifadesi ana sayfada kullanılmadı. Firma tanıtımında süre belirtilmedi. Eski sertifika görseli, güncel geçerlilik iddiası oluşturacak şekilde tasarıma eklenmedi; arşiv medya klasöründe korundu.
- Teknik değerler ve iletişim bilgileri sağlanan yedekten aktarılmıştır; yeni ürün veya güncel sertifika bilgisi eklenmemiştir.
- PHP tema/eklenti dosyaları, kullanıcı hesapları, veritabanı, özel sunucu dosyaları ve örnek tema görselleri yayın çıktısına taşınmadı. Orijinal yedeğe dokunulmadı.

## GitHub Pages

`main` dalına push yapıldığında `.github/workflows/pages.yml` bağlantıları ve JavaScript sözdizimini kontrol eder, ardından yalnızca `modern-site/` klasörünü GitHub Pages'e yayımlar. SQL, yedekler, üretim kaynakları ve README yayın paketine girmez. GitHub Actions yayını için özel alan adı ayrıca deponun **Settings → Pages** ayarında `ameliyatmasasi.com` olarak tanımlanır; `CNAME` dosyası tek başına bu ayarın yerini tutmaz.

DNS kayıtları:

| Tür | Ad | Değer |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | akinayturan.github.io |

TTL: Auto veya 300 saniye. Cloudflare kullanılıyorsa ilk kurulumda web kayıtları **DNS only** (gri bulut) olmalıdır. Aynı `@` ve `www` adlarındaki eski web hedeflerini değiştirin; eski sunucuya giden AAAA kayıtları varsa kaldırın veya GitHub'ın IPv6 değerleriyle güncelleyin. MX, SPF, DKIM ve diğer e-posta kayıtlarını koruyun. DNS doğrulaması ve sertifika oluşumu tamamlandığında Pages ayarından **Enforce HTTPS** açılabilir. DNS değişikliği bu commit tarafından yapılmaz.

Kaynak: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
