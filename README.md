PostSpammer

Bu proje, belirttiğiniz bir web sayfasındaki formu otomatik olarak gönderme işlemini gerçekleştiren bir Python betiğidir. Kullanıcı, formdaki her alan için rastgele veriler oluşturulmasını sağlar ve ardından formu belirtilen sayıda gönderir.
Özellikler

    Web sayfasındaki formu analiz eder ve gerekli alanları (input alanları) bulur.
    number ve text türündeki alanlara rastgele veri gönderir.
    Kullanıcı, kaç kez form göndermek istediğini belirleyebilir.
    Her gönderimden sonra durum kodu ve gönderilen veriler hakkında bilgi alabilirsiniz.

Gereksinimler

    Python 3.6+ (Python 3.12 gibi yeni sürümlerle uyumludur)
    requests kütüphanesi
    beautifulsoup4 kütüphanesi

Gerekli Paketlerin Yüklenmesi

Gerekli Python kütüphanelerini yüklemek için aşağıdaki adımları takip edebilirsiniz.

    requirements.txt Dosyasını Kullanarak Yükleme:

    Proje klasöründe requirements.txt dosyasını sağ tıklayarak terminal veya komut istemcisine şunu yazın:

pip3 install -r requirements.txt

Bu komut, projenin ihtiyaç duyduğu tüm kütüphaneleri otomatik olarak yükler.

Alternatif Yöntem: Manüel Yükleme:

Alternatif olarak, gerekli kütüphaneleri tek tek de yükleyebilirsiniz:

    pip3 install requests
    pip3 install beautifulsoup4

Kullanım

    Scripti Çalıştırın: Python dosyasını çalıştırın:

    python3 main.py

    URL Girin: Web sayfasının formunu göndereceğiniz URL'yi girin.

    Kaç Kez Form Göndereceğinizi Seçin: Kullanıcıdan, formu kaç kez göndermek istediği sorulacaktır. Sayıyı girdikten sonra işlemi başlatabilirsiniz.!

    Sonuçları Kontrol Edin: Her form gönderildikten sonra, gönderilen veriler ve HTTP durum kodu yazdırılır.

Script Detayları

    generate_random_number(): Bu fonksiyon, sayı türündeki form alanları için rastgele bir sayı üretir.
    generate_random_text(): Bu fonksiyon, metin türündeki form alanları için rastgele bir metin üretir.
    prepare_form_data(): Bu fonksiyon, form verilerini hazırlayarak rastgele verilerle doldurur.
    get_number_of_requests(): Kullanıcıdan kaç kere form göndereceğini alır.
    requests.post(): Web sayfasına POST isteği gönderir.

Örnek Çıktı

Her gönderim sonrası şu gibi çıktılar alabilirsiniz:

1. Form gönderildi! Durum kodu: 200
Gönderilen veriler: {'username': 'A1B2C3D4E5', 'email': 'random_email@example.com'}
2. Form gönderildi! Durum kodu: 200
Gönderilen veriler: {'username': 'F6G7H8I9J0', 'email': 'random_email2@example.com'}

Sorunlar

Eğer form gönderimi sırasında bir hata alırsanız, aşağıdaki gibi bir hata mesajı alabilirsiniz:

Hata varr!: ConnectionError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

Bu durumda internet bağlantınızı kontrol edin veya formun URL’sini doğru girdiğinizden emin olun.
