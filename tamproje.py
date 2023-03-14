import tkinter as tk
from tkinter import messagebox
from tkinter import*

pencereI=tk.Tk()
pencereI.geometry("500x500")
pencereI.title("Osmanlı Devleti")

la=tk.Label(pencereI, text="HOŞGELDİNİZ", font="Arial 25 bold", bg="red", fg="black").pack()

def padisah():

    pencere = tk.Tk()
    pencere.geometry("900x900")
    pencere.title("Osmanlı Padişahları")

    def osmangazi():
        pencereosman = tk.Tk()
        pencereosman.geometry("900x600")
        pencereosman.title("OSMAN GAZİ 1299-1326")

        baslikosmangazi = tk.Label(pencereosman, text="OSMAN GAZİ 1299-1326", font="Arial 25 bold", bg="black",
                                   fg="red")
        baslikosmangazi.pack()

        metinosmangazi = tk.Label(pencereosman, text="""        1299 yılında uç beyi olmaktan çıkıp Söğüt ve Domaniç'te Osmanlı Beyliği'ni kurmuştur.
        Sonrasında bağımsızlığını ilan etmiştir. 
        Tarihçi Halil İnalcık'a göre Osmanlı Devleti bağımsızlığını 1302'de Koyunhisar 
        Muharebesi'nden sonra kazanmıştır.
        Moğol istilalarından kaçan bazı Türkmen topluluklarının beyliğine 
        sığınması ile siyasi ve askerî gücü artmıştır. 
        Çöküş döneminde bulunan Doğu Roma İmparatorluğu'ndaki karışıklıkların da 
        etkisiyle kısa sürede Anadolu ve Doğu Roma'nın hâkimi durumuna gelmiştir.
        Öldüğü zaman beylik, Eskişehir ile Bursa arasındaki topraklarda hüküm sürüyor 
        ve Doğu Roma İmparatorluğu'na ait İznik ve Bursa'yı abluka altında tutuyordu.""", justify="left",
                                  font="Arial 13")
        metinosmangazi.pack()

        yazisıra = tk.Label(pencereosman, text="I. Padişah", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencereosman.mainloop()

    def orhangazi():
        pencereorhan = tk.Tk()
        pencereorhan.geometry("900x600")
        pencereorhan.title("ORHAN GAZİ 1326-1359")

        baslikorhangazi = tk.Label(pencereorhan, text="ORHAN GAZİ 1326-1359", font="Arial 25 bold", bg="black",
                                   fg="red")
        baslikorhangazi.pack()

        metinorhangazi = tk.Label(pencereorhan, text="""        Osmanlı Beyliği'nin kurucusu Osman Gazi ve Malhun Hatun'un oğludur.
        Sarışın, uzun boylu ve mavi gözlü, halk tarafından çok sevilen, 
        ulemaya saygılı, merhametli bir hükümdar olarak tanımlanır.
        Sık sık halkın arasına karıştığı, ve dertlerini dinlediği söylenir.
        Babası Osman Gazi'nin vefatı üzerine 1326'da bey olmuştur.
        Orhan Bey'e Şücaeddin, "İhtiyareddin" ve "Seyfeddin" unvanları verilmiştir. 
        Ölüm tarihini 1359, 1360, 1361 ve 1362 gösteren kaynaklar da vardır.

           "Sultan" unvanını kullanan ilk Osmanlı padişahının I. Murad olduğu kabul edilmektedir;
        lakin bazı kaynaklar Orhan Bey'i "sultan" unvanını kullanan ilk Osman padişahı olarak kabul etmektedir.
        Hatta, onun adına darb edilen sikkede "Sultan-ı Azam Orhan Bey" yazılmaktadır; 
        ve üstelik, Orhan Bey'e ait olan bir tuğra'da "Sultan Orhan" yazılmaktadır.
        Hatta İbn-i Batuta, Osman Gazi'yi "ilk sultan" olarak adlandırmaktadır.""", justify="left", font="Arial 13")
        metinorhangazi.pack()

        yazisıra = tk.Label(pencereorhan, text="II. Padişah", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencereorhan.mainloop()

    def Imurad():
        pencere1murad = tk.Tk()
        pencere1murad.geometry("900x600")
        pencere1murad.title("I. MURAD 1359-1389")

        baslik1murad = tk.Label(pencere1murad, text="I. MURAD 1359-1389", font="Arial 25 bold", bg="black", fg="red")
        baslik1murad.pack()

        metin1murad = tk.Label(pencere1murad, text="""        I. Murad, Murad-ı Hüdavendigâr veya Gazi Hünkar, 
        Osmanlı Devleti’nin üçüncü padişahı. 
        Babası Orhan Gazi, annesi Nilüfer Hatun'dur. 
        Babası Orhan Gazi döneminde 95.000 km² olan devlet toprakları onun döneminde yaklaşık 500.000 km² kadar genişlemiştir.

           "Hükümdar", "bey" anlamına gelen hüdavendigâr unvanı verilmiştir.
        Tuğrası Sultan Murad bin Orhan olarak istiflenmiştir.
        Bazı kitabelerde Melikû'l-Âdil İl Gazi es-Sultan Giyâsû'd-Dünya ve'd-Din şanı ile anılmıştır. 
        Adına kesilmiş olan gümüş ve bakır sikkelerde ve bazı diğer kitabelerde Murad bin Orhan el-Melik,
        el-Adil, es Sultanü'l Gaalib ad ve unvanları kullanılmıştır. 
        Bazı kaynaklara göre, bu Osmanlıların İlhanlılara olan bağımlılığının sona erdiğini göstermektedir.
        Böylece Sultan unvanı ilk kez I. Murad zamanında kullanılmıştır.
        Batı kaynaklarında Amourad I olarak anılmaktadır.

           Şehzadeliği döneminde Edirne'yi fethederek Balkanlara geçmiştir
        ve Balkanlarda fetihler yapmaya başlayarak Osmanlı Devleti'nin sınırlarını genişletmiştir.
        40'ın üzerinde savaşı yönettiği ve hiç yenilmediği çeşitli kaynaklarda söylenmektedir.
        I. Kosova Savaşı'ndan sonra savaş alanını gezerken bir Sırp askeri olan Milos Obilic tarafından hançerlenerek öldürüldü.""",
                               justify="left", font="Arial 13")
        metin1murad.pack()

        yazisıra = tk.Label(pencere1murad, text="III. Padişah", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencere1murad.mainloop()

    def yildirim():
        pencereyildirim = tk.Tk()
        pencereyildirim.geometry("900x600")
        pencereyildirim.title("I. Bayezid (Yıldırım Bayezid) 1389–1402")

        baslikyildirim = tk.Label(pencereyildirim, text="I. Bayezid (Yıldırım Bayezid) 1389–1402", font="Arial 25 bold",
                                  bg="black", fg="red")
        baslikyildirim.pack()

        metinyildirim = tk.Label(pencereyildirim, text="""        Babası Sultan I. Murad, annesi Rum[3] asıllı olan Gülçiçek Hatun'du.
        Adı babaannesinin babası Türkmenlerin Ede-Balı diye andığı Ebâ Yezîd'in adından gelir. 
        Küçük yaştan itibaren zamanın seçkin âlimlerinden genel İslam eğitimi ve
        değerli kumandanlardan askerlik, sevk ve idare dersleri aldı. 
        Osmanlı tarihlerinde kendisinden ilk olarak söz edilmesi,
        1381'de Germiyanoğulları Beyi Süleyman Şah'ın kızı Devlet Sultan/Hatun'la evlenişi nedeniyledir. 
        Bu evlilik babası I. Murat'ın Germiyan topraklarının neredeyse tamamını
        "gelin çeyizi" olarak sınırlarına katmak politikasının sonucuydu.
        1381 yılında evlenişinin takip eden yıllarda devlet idaresinde yetişmesi 
        için Sultanönü, Eskişehir ve sonra Germiyan ili Kütahya sancakları
        beyliğine atandı. Sancaklarının askeriyle Anadolu ve
        Rumeli yakalarında savaşlarda babasının safında yer aldı. 
        1385'te kardeşi Şehzade Savcı Bey'in, Bizans veliahdı Andronikos 
        Paleologos ile birlikte hareket ederek ayaklanmasının bastırılışı ve 
        Şehzade Savcı'nın gözlerine mil çekilmesi sonucu öldürülmesi olayları ile de 
        Osmanlı tarihlerinde bahsi geçmektedir. 1389'da Sırpların çoğunluğunu 
        oluşturduğu Haçlı ordusu ile yapılan Birinci Kosova Muharebesi'ne katıldı. 
        Osmanlı ordusunun sağ kanadının komutanlığını yaptı; 
        savaşta büyük kahramanlık gösterdi ve savaşın Osmanlılar 
        tarafından kazanılmasında komutası altında bulunan Osmanlı sağ 
        kanadının Sırplara bir karşı taarruz ile Sırp ordusunu çökertmesi çok 
        önemli katkı sağladı. Babası Sultan Murad, bu savaş sonunda bir Sırp soylusu olan 
        Milos Obilic tarafından öldürülünce, devlet ileri gelenlerinin müşterek kararı ile Osmanlı tahtına geçti.""",
                                 justify="left", font="Arial 13")
        metinyildirim.pack()

        yazisıra = tk.Label(pencereyildirim, text="IV. Padişah", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencereyildirim.mainloop()

    def fetret():
        pencerefetret = tk.Tk()
        pencerefetret.geometry("900x600")
        pencerefetret.title("FETRET DÖNEMİ 1402-1413")

        baslikfetret = tk.Label(pencerefetret, text="FETRET DÖNEMİ 1402-1413", font="Arial 25 bold", bg="black",
                                fg="red")
        baslikfetret.pack()

        metinfetret = tk.Label(pencerefetret, text="""        Fetret Devri, Bunalım Devri veya Fasıla-i Saltanat, 
        Osmanlı hükümdarı Yıldırım Bayezid'in hayattaki beş oğlundan dördü arasındaki 
        taht kavgaları nedeniyle 1402'den 1413'e kadar süren kargaşa dönemidir. 
        Bu süreç Yıldırım Bayezid'in 1402'deki Ankara Savaşı'nda, 
        Timur İmparatorluğu'nun kurucusu Timur'a yenilip esir düşmesi sonucu ortaya çıktı. 
        Fetret Devri'nde birbirleriyle taht mücadelesine giren Yıldırım Bayezid'in oğulları Emir Süleyman, 
        İsa Çelebi, Musa Çelebi ve Çelebi Mehmed'dir. Dağılan Osmanlı birliği, 
        1413 yılında, I. Mehmed (Çelebi Mehmet) tarafından yeniden sağlandı. 
        Bu gelişmeye bağlı olarak Çelebi Mehmet için "DEVLETİN İKİNCİ KURUCUSU" tabiri kullanılmaktadır""",
                               justify="left",
                               font="Arial 13")
        metinfetret.pack()

        yazisıra = tk.Label(pencerefetret, text="DURAKLAMA DÖNEMİ", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencerefetret.mainloop()

    def Imehmet():
        pencere1mehmed = tk.Tk()
        pencere1mehmed.geometry("900x600")
        pencere1mehmed.title("I. MEHMED 1413 – 1421")

        baslik1mehmet = tk.Label(pencere1mehmed, text="I. MEHMED 1413-1421", font="Arial 25 bold", bg="black", fg="red")
        baslik1mehmet.pack()

        metin1mehmed = tk.Label(pencere1mehmed, text="""        1413'ten sonra tek padişah olarak hüküm sürdü.
        Sultan Mehmet Çelebi, Fetret Devrini bitiren ve Osmanlı devletini tekrar eski 
        gücüne kavuşturan kişi olduğundan Osmanlı Devleti'nin ikinci kurucusu olarak da anılmaktadır.

          Tek padişah olarak Sultan Mehmet Çelebi önce, 
        Musa Çelebi tarafından etrafına büyük duvarlar inşa ettirilmiş olan, Edirne Sarayı'nda kaldı. 
        Burada kendini kutlamaya gelen yabancı elçileri kabul etti ve 
        devletin üst kademelerine kendi görüşüne uygun atamalarda bulundu. 
        Şeyh Bedreddin şeyhülislamlıktan atılıp ailesiyle İznik'e sürüldü ve 
        yerine Sünni ulemanın seçtiği bir kişi getirildi. Mihaloğlu Mehmet Bey de Anadolu'ya 
        sürgüne gönderildi. Musa Çelebi tarafından Bizans'tan alınan Selânik ve 
        Konstantinopolis yakınlarındaki bölgeler tekrar Bizans'a geri verildi.

          Sonra Anadolu seferine çıktı. Önce yangın ve kuşatmadan kurtulmuş olan 
        devletin birinci başkenti Bursa'ya uğradı. Sonra Ege sahillerine yürüdü. Ayaklanan 
        İzmiroğlu Cüneyd Bey'i sindirerek Ayasoluk (şimdi Selçuk) kalesini aldı. 
        İzmir kalesini orada bulunan Senjan şövalyeleriyle yaptığı görüşmeler 
        sonunda Osmanlı devletine kattı.
        """, justify="left", font="Arial 13")
        metin1mehmed.pack()

        yazisıra = tk.Label(pencere1mehmed, text="V. Padişah", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencere1mehmed.mainloop()

    def IImurad():
        pencere2murad = tk.Tk()
        pencere2murad.geometry("900x600")
        pencere2murad.title("II. Murad 1421–1451")

        baslik2murad = tk.Label(pencere2murad, text="II. Murad 1421–1451", font="Arial 25 bold", bg="black", fg="red")
        baslik2murad.pack()

        metin2murad = tk.Label(pencere2murad, text="""        II. Murad; bazı kaynaklara göre 1402'de, bazılarına 
        göre ise 1404'te[2] Amasya'da dünyaya geldi. İlk çocukluk yılları Amasya'da geçti. 1410'da 
        babasıyla Bursa'ya gelerek orada saray eğitimi aldı. 1415'te lalası 
        Yörgüç Paşa gözetimi altında merkezi Amasya'da bulunan ve devletin doğu sınırında 
        olması dolayısıyla büyük stratejik önemi olan Rum ve Danışmendiye eyaleti valisi olarak 
        görevlendirildi. Tahta çıkıncaya kadar 6 yıl bu görevi yaptı. 
        Amasya aynı zamanda çok önemli bir Anadolu kültür merkeziydi ve bu merkezde bilim ve 
        din alimleri, şairler ve mutasavvıflarla meclisler tertip edip şehrin kültür hayatına 
        destek sağlayıp katıldı. 1416'da bölgesi askeri başında Börklüce Mustafa'nın İzmir ve Saruhan tarafında çıkardığı 
        ayaklanmaların bastırılmasında görev aldı. 1418'de sonraki lalası Hamza Bey ile Çandaroğullarından Samsun'u aldı.

        Babası I. Mehmed Edirne'de bir av kazası sonunda ağır yaralanınca ölüm yatağında devletin idaresinin biran evvel 
        oğlu Murat'a devrini vasiyet etti. Murat, Amasya'dan tahta geçme töreni yapılacak Bursa'ya 
        gelinceye kadar devlet adamları babasının ölümünü sakladılar. Murat 25 Haziran 1421'de Bursa'da 
        gelip culûs ve biat törenleri yapılıp devletin ileri gelenleri ve yeniçerilerin desteğiyle 17 yaşındayken tahta çıktı.

        Sultan II. Murad, soyunun Kayı boyuna mensubiyetini göstermek için, sikkelerine, 
        Kayı boyuna ait iki ok ve bir yaydan müteşekkil damgayı koydurmuştur. 
        Sonraki padişahların bastırdıkları sikkelerde görülmeyen Kayı damgası, I. Süleyman’a 
        kadar çeşitli eşya ve silâhlar üzerine konulmasına devam edilmiştir.""", justify="left", font="Arial 13")
        metin2murad.pack()

        yazisıra = tk.Label(pencere2murad, text="VI. Padişah", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencere2murad.mainloop()

    def fatih():
        pencerefatih = tk.Tk()
        pencerefatih.geometry("900x800")
        pencerefatih.title("FATİH SULTAN MEHMED 1451–1481")

        baslikfatih = tk.Label(pencerefatih, text="FATİH SULTAN MEHMED 1451–1481", font="Arial 25 bold", bg="black",
                               fg="red")
        baslikfatih.pack()

        metinosmangazi = tk.Label(pencerefatih, text="""        Fatih Sultan Mehmed, 29 Mart 1432’de, Edirne’de doğdu. 
        Babası Sultan İkinci Murad, annesi Humâ Hatun’dur. Fatih Sultan Mehmed, uzun boylu, dolgun 
        yanaklı, kıvrık burunlu, adaleli ve kuvvetli bir yapıya sahipti. Devrinin en 
        büyük âlimlerinden çok iyi eğitim görmüştü; yedi yabancı dil bildiği söylenir. 
        Âlim, şâir ve sanatkârları sık sık toplar ve onlarla sohbet etmekten çok hoşlanırdı. İlginç ve 
        bilinmedik konular hakkında makaleler yazdırır ve bunları incelerdi. Hocalığını da yapmış 
        olan Akşemseddin, Fatih Sultan Mehmed’in en çok değer verdigi âlimlerden biridir. 
        Fatih Sultan Mehmed, gayet soğukkanlı ve cesurdu. Eşsiz bir komutan ve idareciydi. 
        Yapacağı işlerle ilgili olarak en yakınlarına bile hiçbir şey söylemezdi.

           Fatih Sultan Mehmed, okumayı çok severdi. Farsça ve Arapça’ya 
        çevrilmiş olan felsefî eserler okurdu. 1466 yılında Batlamyos Haritası’nı yeniden 
        tercüme ettirip, haritadaki adları Arap harfleriyle yazdırdı. Bilimsel sorunlarda, 
        hangi din ve mezhebe mensup olursa olsun bilginleri korur onlara eserler yazdırırdı. Bilime büyük önem veren 
        Fatih Sultan Mehmed, yabancı ülkelerdeki büyük bilginleri İstanbul’a getirtti. Nitekim astronomi 
        bilgini Ali Kuşçu, kendi döneminde İstanbul’a geldi. Ünlü ressam Bellini’yi de İstanbul’a 
        davet ederek kendi resmini yaptırdı.

           Fatih Sultan Mehmed, 1481 yılına kadar hükümdarlık yaptı ve bizzat yirmi beş sefere katıldı. 
        Azim ve irade sahibiydi. Temkinli ve verdiği kararları kesinlikle uygulayan bir 
        kişiliği vardı. Devlet yönetiminde oldukça sertti. Savaşlarda çok cesur olur, 
        bozgunu önlemek için ileri atılarak askerleri savaşa teşvik ederdi.

           20 yaşında Osmanlı padişahı olan Sultan İkinci Mehmed, İstanbul’u fethedip 1100 yıllık Doğu Roma 
        İmparatorluğu’nu ortadan kaldırarak ‘Fatih’ unvanını aldı. Hz. Muhammed’in 
        Hadis-i Şerifinde müjdelediği İstanbul’un fethini gerçekleştiren büyük komutan olmayı da 
        başaran Fatih Sultan Mehmed, yüksek yeteneği ve dehasıyla dost ve düşmanlarına gücünü kabul 
        ettirmiş bir Türk hükümdarıydı. Ortaçağ’ı kapatıp, Yeniçağ’ı açan cihan hükümdarı Fatih Sultan Mehmed, 
        nikris hastalığından dolayı 3 Mayıs 1481 günü, Maltepe’de vefat etti ve Fatih Camii’nin yanındaki 
        Fatih Türbesi’ne defnedildi. O’nun Roma’yı fethedeceği düşüncesiyle zehirlendiği de kaynaklarda yer almaktadır..""",
                                  justify="left", font="Arial 13")
        metinosmangazi.pack()

        yazisıra = tk.Label(pencerefatih, text="VII. Padişah", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencerefatih.mainloop()

    def IIBayezid():
        pencereosman = tk.Tk()
        pencereosman.geometry("900x600")
        pencereosman.title("II. BAYEZİD 1481-1512")

        baslikosmangazi = tk.Label(pencereosman, text="II. BAYEZİD 1481-1512", font="Arial 25 bold", bg="black",
                                   fg="red")
        baslikosmangazi.pack()

        metinosmangazi = tk.Label(pencereosman, text="""        Sultan İkinci Bayezid, 3 Aralık 1448’de, Dimetoka’da doğdu. 
        Babası Fatih Sultan Mehmed, annesi Mükrime Hatun adında bir Türk kızıdır.
        Cesur ve atılgandı. Aynı zamanda çok hâlim-selim, dindar, hoşgörülü bir padişahtı. 
        Babası Fatih Sultan Mehmed ilme ilgi duyduğu için, oğlu Şehzade Bayezid’e 
        iyi bir eğitim verdi. Ona devrin en meşhur âlimlerinden ders okutturdu, bütün İslâm 
        ilimlerini en iyi şekilde öğrenmesini sağladı.

           Sultan İkinci Bayezid, yedi yaşında iken, Hadim Ali Paşa nezaretinde 
        Amasya valiliğine tayin edildi. Amasya, Selçuklular devrinden beri 
        önemli bir ilim ve kültür merkeziydi. Padişah olacak şehzadelerin yetişmesi için, 
        bu vilayette bütün imkânlar vardı.
    """, justify="left", font="Arial 16")
        metinosmangazi.pack()

        yazisıra = tk.Label(pencereosman, text="VIII. Padişah", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencereosman.mainloop()

    def yavuz():
        pencereosman = tk.Tk()
        pencereosman.geometry("900x600")
        pencereosman.title("I. SELİM (YAVUZ SULTAN SELİM) 1512 – 1520")

        baslikosmangazi = tk.Label(pencereosman, text="I. SELİM (YAVUZ SULTAN SELİM) 1512 – 1520", font="Arial 25 bold",
                                   bg="black", fg="red")
        baslikosmangazi.pack()

        metinosmangazi = tk.Label(pencereosman, text="""        Yavuz Sultan Selim, 10 Ekim 1470’de doğdu. 
        Babası Sultan İkinci Bayezid, annesi Gülbahar Hatun’dur. 
        Gülbahar Hatun, Dulkadiroğulları Beyliği’ndendir.
            Babası Sultan İkinci Bayezid, padişah olduktan sonra, askeri sevk 
        ve devlet idareciliğini öğrenmesi için, Şehzade Selim’i Trabzon Sancağına 
        vali olarak tayin etti. Valiliği sırasında Trabzon halkını rahat bırakmayan 
        Gürcüler üzerine üç sefer yaptı. En önemlisi olan Kütayis Seferinde Kars, 
        Erzurum ve Artvin illeri ile birçok yeri fethederek Osmanlı topraklarına kattı (1508). 
        Buralarda yaşayan Gürcülerin hepsi Müslüman oldular.""", justify="left", font="Arial 15")
        metinosmangazi.pack()

        yazisıra = tk.Label(pencereosman, text="IX. Padişah", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencereosman.mainloop()

    def sulo():
        pencereosman = tk.Tk()
        pencereosman.geometry("1100x600")
        pencereosman.title("I. SÜLEYMAN (KANUNİ SULTAN SÜLEYMAN) 1520 – 1566")

        baslikosmangazi = tk.Label(pencereosman, text="I. SÜLEYMAN (KANUNİ SULTAN SÜLEYMAN) 1520 – 1566",
                                   font="Arial 25 bold", bg="black", fg="red")
        baslikosmangazi.pack()

        metinosmangazi = tk.Label(pencereosman, text="""        Kanûnî Sultan Süleyman, 27 Nisan 1495 doğdu. 
        Babası Yavuz Sultan Selim, annesi Hafsa Hatun’dur.   Kanûnî Sultan Süleyman devri, Türk 
        hakimiyetinin doruk noktasına ulaştığı bir devir olmuştur. Babası Yavuz Sultan Selim, 
        onu küçük yaşlardan itibaren çok titiz bir şekilde yetiştirmeye başladı. Benzeri görülmemiş bir 
        terbiye ve tahsil gördü. İlk eğitimini annesinden ve ninesi Gülbahar Hatun’dan 
        (Yavuz Sultan Selim’in annesi) aldı. Sigetvar kuşatmasını idare ederken, 7 Eylül 1566 
        yılında yetmiş bir yaşında vefat etti. Kanûnî Sultan Süleyman, tahta çıktığı sırada Osmanlı Devleti dünyanın 
        en zengin ve en güçlü devleti konumundaydı. Babasının ölümü ve kendisinin padişah olması, “Arslan öldü, 
        yerine kuzu geçti” diye düşünen Avrupalıları sevindiriyordu. 
        Ancak Avrupalılar, çok geçmeden hayal kırıklığına uğradılar""", justify="left", font="Arial 15")
        metinosmangazi.pack()

        yazisıra = tk.Label(pencereosman, text="X. Padişah", font="Arial 25 bold", bg="yellow", fg="black")
        yazisıra.pack()

        pencereosman.mainloop()

    yazianaekranyapan = tk.Label(pencere, text="OSMANLI PADİŞAHLARI", bg="black", fg="white", font="Arial 43 bold")
    yazianaekranyapan.pack()

    yazipadisahsec = tk.Label(pencere, text="Aşağıdan hakkında bilgi almak istediğiniz padişahı seçiniz", bg="red",
                              fg="white", font="Arial 23 bold")
    yazipadisahsec.pack()

    butonOsmangazi = tk.Button(pencere, text="Osman Gazi 1299-1326", font="Arial 15 bold", bg="yellow", fg="black",
                               width="50", command=osmangazi)
    butonOsmangazi.pack()

    butonOrhangazi = tk.Button(pencere, text="Orhan Gazi 1326-1359", font="Arial 15 bold", bg="black", fg="white",
                               width="50", command=orhangazi)
    butonOrhangazi.pack()

    butonIMurad = tk.Button(pencere, text="I. Murad 1359-1389", font="Arial 15 bold", bg="yellow", fg="black",
                            width="50", command=Imurad)
    butonIMurad.pack()

    butonYildirimBayezid = tk.Button(pencere, text="I. Bayezid (Yıldırım Bayezid) 1389-1402", font="Arial 15 bold",
                                     bg="black", fg="white", width="50", command=yildirim)
    butonYildirimBayezid.pack()

    butonFetret = tk.Button(pencere, text="Fetret (Duraklama) Dönemi 1402-1413", font="Arial 15 bold", bg="yellow",
                            fg="black", width="50", command=fetret)
    butonFetret.pack()

    butonIMehmed = tk.Button(pencere, text="I. (Çelebi) Mehmed 1413-1421", font="Arial 15 bold", bg="black", fg="white",
                             width="50", command=Imehmet)
    butonIMehmed.pack()

    butonIIMurad = tk.Button(pencere, text="II. Murad 1421-1451", font="Arial 15 bold", bg="yellow", fg="black",
                             width="50", command=IImurad)
    butonIIMurad.pack()

    butonIIMehmed = tk.Button(pencere, text="FATİH SULTAN MEHMED (II.Mehmed) 1451-1481", font="Arial 20 bold",
                              bg="black", fg="white", width="50", command=fatih)
    butonIIMehmed.pack()

    butonIIBayezid = tk.Button(pencere, text="II.Bayezid 1481-1512", font="Arial 15 bold", bg="yellow", fg="black",
                               width="50", command=IIBayezid)
    butonIIBayezid.pack()

    butonyavuz = tk.Button(pencere, text="I. Selim (Yavuz Sultan Selim) 1512-1520", font="Arial 15 bold", bg="black",
                           fg="white", width="50", command=yavuz)
    butonyavuz.pack()

    butonkanuni = tk.Button(pencere, text="I. Süleyman (Kanunî Sultan Süleyman) 1520-1566", font="Arial 15 bold",
                            bg="yellow", fg="black", width="50", command=sulo)
    butonkanuni.pack()

    def a():
        messagebox.showinfo("Yapanlar-Emeği Geçenler", """-Pamir Açar
    -Eymen Ocak
    """)

    butyapan = tk.Button(pencere, text="Yapanlar - Emeği Geçenler", font="Arial 18 bold", command=a).pack()

    pencere.mainloop()
    
def savas():
    


    pencere = Tk()
    pencere.geometry("800x700")
    pencere.title("Osmanlı Dönemi Savaşları")



    label1=Label(pencere)
    label1.config(text="OSMANLI SAVAŞLARI", fg="yellow", bg="black",font="Vertana 40")
    label1.pack()

    label150=Label(pencere)
    label150.config(text="Aşağıdan Hakkında Bigi Almak İstediğiniz Padişaha Tıklayınız", fg="white", bg="red", font="Arial 20")
    label150.pack()
    def koyun():
        pencerekoyun = Tk()
        pencerekoyun.geometry("700x500")
        pencerekoyun.title("Koyunhisar Savaşı 1302")

        label=Label(pencerekoyun)
        label.config(text="Koyunhisar Savaşı",bg="black",fg="yellow",font=("Vertana",35))
        label.pack()
        label300=Label(pencerekoyun)
        label300.config(text="""
    Savaş Tarihi: 1302
    Savaşın Tarafları :Osmanlı X Bizans İmparatorluğu 
    Padişah: Osman Gazi
    Savaşın Sebepleri: Osmanlının fetih folitikası
    Savaşın Sonuçları: Osmanlı ordusu kazanmıştır
                     : Bizans İmparatorluğunun zayıfladığı iyice ortaya çıkmıştır""", font="Arial 15",justify="left")
        label300.pack()
        mainloop()

    koyunbuton=Button(pencere)
    koyunbuton.config(text="Koyunhisar Savaşı (1302)", command=koyun ,font="Arial 15",bg="orange",fg="black")
    koyunbuton.pack(fill="both")


    def maltepe():
        penceremaltepe = Tk()
        penceremaltepe.geometry("700x500")
        penceremaltepe.title("Maltepe Savaşı (1329)")
        label2=Label(penceremaltepe)
        label2.config(text="Maltepe Savaşı", bg="black", fg="yellow", font=("Vertana",35))
        label2.pack()
        label301=Label(penceremaltepe)
        label301.config(text="""   Savaşın tarihi : 1329
        Savaşın tarafları : Osmanlı X Bizans imparatorluğu
        Padişah : Orhan Gazi
        Savaşın sebepleri : Osmanlının Kocaeli yarımadasındaki fetihleri 
                      : Bizansın Osmanlının sınırlarının genişlemesinmden rahatsız olması
        Savaşın sonuçları :  Osmanlı kazandı
                      :  Bizans ın Anadoluda toprağı kalmadı""", font="Arial 15", justify="left")
        label301.pack()
        mainloop()

    maltepebuton=Button(pencere)
    maltepebuton.config(text="  Maltepe Savaşı (1329)   ", command=maltepe ,font="Arial 15", bg="blue", fg="white")
    maltepebuton.pack(fill="both")

    def sazlıdere():
        penceresazlı = Tk()
        penceresazlı.geometry("1170x500")
        penceresazlı.title("Sazlıdere Savaşı (1361)")
        label3=Label(penceresazlı)
        label3.config(text="Sazlıdere Savaşı", bg="black", fg="yellow", font=("Vertana",35))
        label3.pack()
        label45=Label(penceresazlı)
        label45.config(text="""Savaşın Tarihi: 1361
    Savaşın Tarafları: Osmanlı X Bizans
    Hangi padişah dönemi: 1. Murat
    Savaşın Sebepleri: Osmanlı Devleti’nin Rumeli’de gerçekleştireceği fetihlerle bölgeyi Türkleştirmek istemesi.
    	         :Murad’ın 1359 yılında Rumeli’ye geçmesiyle Edirne’nin Osmanlı Devleti tarafından ana hedef olarak belirlenmesi.
    	         :Bizans İmparatorluğu ve Bulgar kuvvetlerinin Osmanlı Devleti’nin Balkanlar’daki ilerleyişini durdurmak istemeleri.

    Savaşın Sonuçları: Edirne, Osmanlı Devleti tarafından fethedilmiştir ve şehir devletin yeni başkenti olmuştur.
    	         :Balkanlardaki önemli bir yer olan Edirne’nin fethedilmesiyle Rumeli fetihlerinin önü açılmıştır.
    	         :Gerçekleşecek fetihler için Edirne önemli bir askeri üs olarak kullanılmıştır.
    	         :Bizans İmparatorluğu’nun Balkanlar ve Avrupa ile olan bağlantısı kesilmiş ve Bizans Devleti İstanbul’a sıkıştırılmıştır.""",font="Arial 15", justify="left")
        label45.pack()
        mainloop()



    sazlıbuton=Button(pencere)
    sazlıbuton.config(text="  Sazlıdere Savaşı (1361) ",command=sazlıdere ,font="Arial 15", bg="orange",fg="black")
    sazlıbuton.pack(fill="both")


    def k1osova():
        pencerek1osova = Tk()
        pencerek1osova.geometry("700x500")
        pencerek1osova.title("Ⅰ. Kosova Savaşı (1389)")
        label4=Label(pencerek1osova)
        label4.config(text="Ⅰ. Kosova Savaşı ", bg="black", fg="yellow", font=("Vertana",35))
        label4.pack()
        label90=Label(pencerek1osova)
        label90.config(text="""Savaşın Tarihi:1389
    Savaşın Tarafları: OSMANLI X HAÇLILAR
    Hangi padişah dönemi: 1.Murad
    Savaşın Sebepleri: Türkleri Balkanlardan atmak
    Savaşın Sonuçları: Sırplar vergiye bağlandı.
                     :1.Murad savaş alanında öldü ,yerine 1.Bayezid geçti.""", font="Arial 15", justify="left")
        label90.pack()
        mainloop()



    kos1buton=Button(pencere)
    kos1buton.config(text="Ⅰ. Kosova Savaşı (1389) ",command=k1osova ,font="Arial 15", bg="blue",fg="white")
    kos1buton.pack(fill="both")


    def nigbolu():
        pencerenigbolu = Tk()
        pencerenigbolu.geometry("700x500")
        pencerenigbolu.title("Niğbolu Savaşı (1396)")
        label5=Label(pencerenigbolu)
        label5.config(text="Niğbolu Savaşı ", bg="black", fg="yellow", font=("Vertana",35))
        label5.pack()
        label91=Label(pencerenigbolu)
        label91.config(text="""Savaşın Tarihi:1396
    Savaşın Tarafları: Osmanlı X Haçlılar
    Hangi padişah dönemi: 1.Bayezid
    Savaşın Sebepleri: Türkleri balkanlardan atmak
                     :Papa nın kışkırtması
                     :Yıldırım Bayezid in İstanbul u kuşatması.
    Savaşın Sonuçları: Bulgaristan tamamen Osmanlı topraklarına katıldı.
                     :Abbasi Halifesi Bayezid e Sultan I İklim İ Rum unvanını verdi""", font="Arial 15", justify="left")
        label91.pack()

        mainloop()


    nigbuton=Button(pencere)
    nigbuton.config(text="   Niğbolu Savaşı (1396)   ",command=nigbolu ,font="Arial 15", bg="orange",fg="black")
    nigbuton.pack(fill="both")



    def ankara():
        pencereankara = Tk()
        pencereankara.geometry("700x500")
        pencereankara.title("Ankara Savaşı (1402)")
        label5=Label(pencereankara)
        label5.config(text="Ankara Savaşı ", bg="black", fg="yellow", font=("Vertana",35))
        label5.pack()
        label75=Label(pencereankara)
        label75.config(text="""Savaşın Tarihi: 1402 
    Savaşın Tarafları: Osmanlı X  Timurlular
    Hangi padişah dönemi: 1.Bayezid
    Savaşın Sebepleri: Timur ve Bayezid in dünya hakimi olma düşüncesi
                     :Her iki hükümdarın da birbirini kışkırtması
    Savaşın Sonuçları: Anadolu da Türk siyasi birliği bozuldu.
                     :Fetret devri yaşandı.
                     :Bizans ın siyasi ömrü uzadı.""", font="Arial 15", justify="left")
        label75.pack()
        mainloop()



    ankbuton=Button(pencere)
    ankbuton.config(text="   Ankara Savaşı (1402)   ",command=ankara ,font="Arial 15", bg="blue",fg="white")
    ankbuton.pack(fill="both")



    def venedik():
        pencerevenedik = Tk()
        pencerevenedik.geometry("1000x500")
        pencerevenedik.title("Venediklilerle Deniz Savaşı (1416)")
        label6=Label(pencerevenedik)
        label6.config(text="Venediklilerle Deniz Savaşı", bg="black", fg="yellow", font=("Vertana",35))
        label6.pack()
        label78=Label(pencerevenedik)
        label78.config(text="""Savaşın Tarihi: 1416
    Savaşın Tarafları: Venedikliler 
    Hangi padişah dönemi: 1.Mehmet
    Savaşın Sebepleri: Venediklilerin Ege de düşmanca tavırlar sergilemesi
    Savaşın Sonuçları: Osmanlı kaybetmiş ve Osmanlı kadırgaları Venediklilerin eline geçmiştir""", font="Arial 15", justify="left")
        label78.pack()
        mainloop()



    vndkbuton=Button(pencere)
    vndkbuton.config(text="Venediklilerle Deniz Savaşı(1416)",command=venedik ,font="Arial 15", bg="orange",fg="black")
    vndkbuton.pack(fill="both")


    def varna():
        pencerevarna = Tk()
        pencerevarna.geometry("900x500")
        pencerevarna.title("Varna Savaşı (1444)")
        label7=Label(pencerevarna)
        label7.config(text="Varna Savaşı  ", bg="black", fg="yellow", font=("Vertana",35))
        label7.pack()
        label98=Label(pencerevarna)
        label98.config(text="""Savaşın Tarihi: 1444
    Savaşın Tarafları: Osmanlı X Haçlılar
    Hangi padişah dönemi: 2.Murad
    Savaşın Sebepleri: Osmanlı tahtında 12 yaşında bir padişah bulunması ( 2. Mehmet )
    Savaşın Sonuçları: Yunanistan ve Bulgaristan doğrudan Osmanlı devletine bağlandı.
                     :Osmanlıların Balkanlardaki egemenliği pekişti.""", font="Arial 15", justify="left")
        label98.pack()
        mainloop()



    vrnbuton=Button(pencere)
    vrnbuton.config(text="    Varna Savaşı (1444)    ",command=varna ,font="Arial 15", bg="blue",fg="white")
    vrnbuton.pack(fill="both")

    def k2os():
        pencere2kos = Tk()
        pencere2kos.geometry("700x500")
        pencere2kos.title("Kosova Savaşı (1448)")
        label8=Label(pencere2kos)
        label8.config(text="Kosova Savaşı", bg="black", fg="yellow", font=("Vertana",35))
        label8.pack()
        label23=Label(pencere2kos)
        label23.config(text="""Savaşın Tarihi: 1448
    Savaşın Tarafları: Osmanlı X Haçlılar
    Hangi padişah dönemi: 2.Murad
    Savaşın Sebepleri: Türk ilerleyişini durdurmak ve Balkanlardan atmak
                     :Varna savaşının intikamı
                     :Papa nın kışkırtması
    Savaşın Sonuçları: Balkanlarda Türk hakimiyeti kesinleşti.
                     :Savaşı kazanan Osmanlı büyük ganimet elde etti.
                     :İsatanbul un alınması kolaylaştı.""", font="Arial 15", justify="left")
        label23.pack()
        mainloop()



    kos2buton=Button(pencere)
    kos2buton.config(text="II. Kosova Savaşı (1448)",command=k2os ,font="Arial 15", bg="orange",fg="black")
    kos2buton.pack(fill="both")





    def cem():
        pencerecem = Tk()
        pencerecem.geometry("700x500")
        pencerecem.title("Cem Sultan İsyanı (1481)")
        label9=Label(pencerecem)
        label9.config(text="Cem Sultan İsyanı  ", bg="black", fg="yellow", font=("Vertana",35))
        label9.pack()
        label87=Label(pencerecem)
        label87.config(text="""Savaşın Tarihi: 1481
    Savaşın Tarafları: 2.Bayezid X Cem sultan
    Hangi padişah dönemi: -
    Savaşın Sebepleri: Cem Sultan ın 2.Bayezid in tahta çıkışına isyan etmesi
    Savaşın Sonuçları: 2.Bayezid savaşı kazanmıştır.
                     :Cem Sultan Avrupa ya sığınmıştır""", font="Arial 15", justify="left")
        label87.pack()
        mainloop()




    cembuton=Button(pencere)
    cembuton.config(text="Cem Sultan İsyani (1481) ",command=cem ,font="Arial 15", bg="blue",fg="white")
    cembuton.pack(fill="both")



    def cald():
        pencerecald = Tk()
        pencerecald.geometry("900x500")
        pencerecald.title("Çaldıran Savaşı  (1514)")
        label10=Label(pencerecald)
        label10.config(text="Çaldıran Savaşı  ", bg="black", fg="yellow", font=("Vertana",35))
        label10.pack()
        label67=Label(pencerecald)
        label67.config(text="""Savaşın Tarihi: 1514
    Savaşın Tarafları: Osmanlı X Safeviler
    Hangi padişah dönemi: Yavuz Sultan Selim
    Savaşın Sebepleri: Şah İsmail in Anadolu da Şiiliği yayması ve sürekli isyan çıkarması
    Savaşın Sonuçları: 1.Selim Yavuz lakabıyla anılmaya başlandı.
                     :Anadolu daki Şii sorunu geçici olarak çözüldü.""", font="Arial 15", justify="left")
        label67.pack()
        mainloop()




    caldbuton=Button(pencere)
    caldbuton.config(text="Çaldıran Savaşı (1514) ",command=cald ,font="Arial 15", bg="orange",fg="black")
    caldbuton.pack(fill="both")


    def mer():
        penceremer = Tk()
        penceremer.geometry("900x500")
        penceremer.title("Mercidabık Savaşı (1516)")
        label11=Label(penceremer)
        label11.config(text="Mercidabık Savaşı  ", bg="black", fg="yellow", font=("Vertana",35))
        label11.pack()
        label95=Label(penceremer)
        label95.config(text="""Savaşın Tarihi: 1516
    Savaşın Tarafları: Osmanlı X Memlük devleti
    Hangi padişah dönemi: Yavuz Sultan Selim
    Savaşın Sebepleri: Hem Osmanlı Hem de Memlüklerin İslam dünyasında hakimiyeti almak istemeleri
                     :Memlüklerin Osmanlılara karşı Safeviler ile ittifak kurması.
    Savaşın Sonuçları: Osmanlı ordusunun mutlak zaferi
                     :Osmanlı Mısır ı fethetmek için ilk adımı tamamladı.""", font="Arial 15", justify="left")
        label95.pack()
        mainloop()




    merbuton=Button(pencere)
    merbuton.config(text="Mercidabık Savaşı (1516) ",command=mer ,font="Arial 15", bg="blue",fg="white")
    merbuton.pack(fill="both")


    def rid():
        pencererid = Tk()
        pencererid.geometry("700x500")
        pencererid.title("Ridaniye Savaşı  (1517)")
        label12=Label(pencererid)
        label12.config(text="Ridaniye Savaşı  ", bg="black", fg="yellow", font=("Vertana",35))
        label12.pack()
        label69=Label(pencererid)
        label69.config(text="""Savaşın Tarihi: 1517
    Savaşın Tarafları: Osmanlı X Memlükler
    Hangi padişah dönemi: Yavuz Sultan Selim
    Savaşın Sebepleri: Selim in Mısır ı ele geçirmek istemesi
                     :Türk İslam Dünyasının lideri olmak istemesi
    Savaşın Sonuçları: Mısır Osmanlı Hakimiyetine girdi.
                     :Memlükler yıkıldı.
                     :Halifelik Osmanlıya geçti.
                     :Baharat yolu Osmanlı kontrolüne girdi 
                     :Kutsal emanetler İstanbula getirildi.""", font="Arial 15", justify="left")
        label69.pack()
        mainloop()




    ridbuton=Button(pencere)
    ridbuton.config(text="Ridaniye Savaşı (1517) ",command=rid ,font="Arial 15", bg="orange",fg="black")
    ridbuton.pack(fill="both")

    def s():
        a=messagebox.showinfo("Yapanlar Emeği Geçenler ", """-Zafer Ayaz Şen 
    -Alp Çavuşoğlu""")

    Button(pencere, text="Yapanlar & Emeği Geçenler ", command=s , font="Arial 15").pack()
    buton=Button(pencere)


    mainloop()
l=tk.Label(pencereI, text="""

""").pack()
butpadisah=tk.Button(pencereI, text="Padişahlar Hakkında", font="Arial 27 bold", fg="black", bg="yellow", command=padisah).pack()
l=tk.Label(pencereI, text="""

""").pack()
butsafas=tk.Button(pencereI, text="Savaşlar Hakkında", font="Arial 27 bold", fg="black", bg="yellow", command=savas).pack()
pencereI.mainloop()