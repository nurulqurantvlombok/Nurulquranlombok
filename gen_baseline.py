# -*- coding: utf-8 -*-
# Generator baseline news.js & site-data.js — datanya sama dengan DEF di admin.html
import json, datetime, os
DIR = os.path.dirname(os.path.abspath(__file__))
def today(off=0):
    d = datetime.date.today() + datetime.timedelta(days=off)
    return d.isoformat()

news = [
 {"id":"n1","tanggal":today(),"kategori":"Pengumuman","judul":"Website Resmi Yayasan Nurul Qur'an Aktif","penulis":"Humas Nurul Qur'an","foto":"","tampil":True,
  "ringkasan":"Situs resmi Yayasan Nurul Qur'an kini aktif — berita kegiatan, agenda, PPDB santri baru, dan informasi pesantren akan diperbarui melalui halaman ini.",
  "isi":"Assalamu'alaikum warahmatullahi wabarakatuh.||Situs resmi Yayasan Nurul Qur'an, Lendang Simbe, Mertak Tombok, Praya, Lombok Tengah, NTB, resmi aktif. Melalui situs ini masyarakat dapat memperoleh informasi mengenai program pendidikan Al-Qur'an, agenda kegiatan, penerimaan santri baru, dan kabar kegiatan pesantren.||Seluruh informasi resmi akan diperbarui secara berkala oleh pengelola. Barakallahu fiikum."},
 {"id":"n2","tanggal":today(-14),"kategori":"Kegiatan","judul":"Kegiatan Pendidikan Al-Qur'an Berjalan di Yayasan Nurul Qur'an","penulis":"Humas Nurul Qur'an","foto":"tgh,sabarudin.jpg","tampil":True,
  "ringkasan":"Kegiatan tahfidz, tilawah, dan khat & qira'atul kutub santri berjalan rutin di kompleks pesantren, Lendang Simbe, Praya.",
  "isi":"Alhamdulillah, kegiatan pendidikan Al-Qur'an di Yayasan Nurul Qur'an berjalan dengan lancar. Santri mengikuti halaqah tahfidz pagi dan sore, setoran tilawah, serta kajian khat & qira'atul kutub di bawah bimbingan para asatidz.||Kegiatan ini merupakan bagian dari pembinaan rutin untuk membentuk generasi Qur'ani yang berilmu dan berakhlak mulia.||Dokumentasi kegiatan dapat dilihat pada bagian galeri di situs ini."}
]

sd = {
 "profile":{"nama":"Yayasan Nurul Qur'an","tagline":"Membentuk generasi Qur'ani yang berilmu, berakhlak mulia, dan bermanfaat bagi agama, bangsa, dan masyarakat",
  "hero":{"judul":"Membentuk Generasi <em>Qur'ani</em><br>yang Berilmu &amp; Berakhlak Mulia.",
   "sub":"Yayasan Nurul Qur'an di Lendang Simbe, Mertak Tombok, Praya, Lombok Tengah — membina santri melalui Tahfidz, Tilawah, serta Khat & Qira'atul Kutub dalam lingkungan yang asri, disiplin, dan penuh keberkahan."},
  "visi":"Membentuk generasi Qur'ani yang berilmu, berakhlak mulia, dan bermanfaat bagi agama, bangsa, dan masyarakat.",
  "misi":["Menyelenggarakan pendidikan Al-Qur'an (tahfidz & tilawah) secara terarah dan terukur.","Membina akhlak santri melalui keteladanan, kedisiplinan, dan pembiasaan ibadah harian.","Mendalami ilmu-ilmu keislaman melalui khat & qira'atul kutub dan kajian kitab.","Mengembangkan kemandirian dan keterampilan hidup santri.","Membangun kerja sama dengan masyarakat, wali santri, alumni, dan instansi terkait."],
  "sejarah":"Yayasan Nurul Qur'an berdiri sejak tahun 2004 di Lendang Simbe, Desa Mertak Tombok, Kecamatan Praya, Kabupaten Lombok Tengah, Nusa Tenggara Barat. Berawal dari kegiatan pengajian dan pembinaan Al-Qur'an bagi anak-anak di sekitar pesantren, lembaga ini terus bertumbuh menjadi pusat pendidikan Al-Qur'an yang membina santri dari berbagai daerah dengan semangat menjaga, menghafal, dan mengamalkan Al-Qur'an.",
  "stats":{"santri":0,"ustadz":0,"alumni":0,"berdiri":2004}},
 "programs":[
  {"id":"p1","ic":"quran","judul":"Tahfidzul Qur'an","desk":"Program menghafal Al-Qur'an dengan metode talaqqi, setoran berkala, dan murajaah terbimbing bersama musyrif.","kat":"Tahfidz"},
  {"id":"p2","ic":"star","judul":"Tilawah & Tajwid","desk":"Pembinaan bacaan Al-Qur'an sesuai kaidah tajwid, dari tingkat dasar hingga mahir dengan munaqasyah berkala.","kat":"Tilawah"},
  {"id":"p3","ic":"buku","judul":"Khat & Qira'atul Kutub","desk":"Pendalaman kitab-kitab turats dengan metode khataman dan qira'ah di hadapan musykil.","kat":"Khat & Qira'atul Kutub"},
  {"id":"p4","ic":"masjid","judul":"Madrasah Diniyah","desk":"Pendidikan keislaman berjenjang: akidah akhlak, fiqih, dan bahasa Arab dasar.","kat":"Madrasah Diniyah"},
  {"id":"p5","ic":"kelas","judul":"Pendidikan Formal","desk":"Dukungan pendidikan sekolah formal agar santri berkembang seimbang antara diniyah dan umum.","kat":"Pendidikan"},
  {"id":"p6","ic":"heart","judul":"Pembinaan Akhlak & Kemandirian","desk":"Pembiasaan ibadah berjamaah, kedisiplinan harian, dan keterampilan kemandirian santri.","kat":"Kegiatan"}],
 "agenda":[
  {"id":"a1","tanggal":today(7),"waktu":"08.00–13.00 WITA","judul":"Pendaftaran Santri Baru","tempat":"Sekretariat Yayasan"},
  {"id":"a2","tanggal":today(30),"waktu":"09.00–12.00 WITA","judul":"Khataman & Haflah Khusnul Khatimah","tempat":"Aula Pesantren"}],
 "ppdb":{"status":"Segera","tahun":"2026/2027","mulai":today(7),"selesai":today(60),"kuota":"","biaya":"","wa":"",
  "syarat":["Mengisi formulir pendaftaran (datang langsung ke sekretariat)","Fotokopi ijazah / SKL","Fotokopi Kartu Keluarga & Akta Kelahiran","Pas foto terbaru","Surat keterangan sehat"],
  "catatan":"Informasi lengkap PPDB dapat ditanyakan langsung kepada panitia."},
 "gallery":[
  {"id":"g1","judul":"Bersama Santri & Pengurus","foto":"beground.png","yt":"","tag":""},
  {"id":"g2","judul":"Kajian & Pengajian","foto":"tgh,sabarudin.jpg","yt":"","tag":""},
  {"id":"g3","judul":"Barisan Santri Putri","foto":"galeri (1).jpg","yt":"","tag":"Kegiatan"},
  {"id":"g4","judul":"Paduan Suara Santri","foto":"galeri (5).jpg","yt":"","tag":"Kegiatan"},
  {"id":"g5","judul":"Musyawarah Yayasan","foto":"galeri (9).jpg","yt":"","tag":""},
  {"id":"g6","judul":"Munaqasyah Santri","foto":"galeri (13).jpg","yt":"","tag":"Tahfidz"},
  {"id":"g7","judul":"Apel Bersama Santri","foto":"galeri (17).jpg","yt":"","tag":""},
  {"id":"g8","judul":"Pengajian Malam","foto":"galeri (21).jpg","yt":"","tag":"Kajian"}],
 "settings":{"email":"","phone":"","address":"Lendang Simbe, Desa Mertak Tombok, Kec. Praya, Kab. Lombok Tengah, NTB","maps":"","ig":"","fb":"","yt":"","siteUrl":"",
  "donasi":{"bank":"","norek":"","an":"","qris":""},
  "images":{"hero":"beground.png","tentang":"tgh,sabarudin.jpg"}}
}

stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
with open(os.path.join(DIR,'news.js'),'w',encoding='utf-8') as f:
    f.write("/* Diterbitkan otomatis — Admin Nurul Qur'an — "+stamp+" */\nwindow.NEWS = "+json.dumps(news,ensure_ascii=False,indent=2)+";\n")
with open(os.path.join(DIR,'site-data.js'),'w',encoding='utf-8') as f:
    f.write("/* Diterbitkan otomatis — Admin Nurul Qur'an — "+stamp+" */\nwindow.SITEDATA = "+json.dumps(sd,ensure_ascii=False,indent=2)+";\n")
print("OK: news.js & site-data.js dibuat.")