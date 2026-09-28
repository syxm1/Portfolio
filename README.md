# Portfolio Web (Tugas Individu PBP)

Proyek web ini dibuat oleh

Nama : Hisyam Prasetyo \
NPM : 2506614763 \
Kelas : PBP D

sebagai tugas individu untuk mata kuliah PBP (Platform-based Programming) Fasilkom UI.
Proyek ini dibuat dengan bantuan AI Chatbot Claude Sonnet 5 dari Anthropic (Lebih detail terkait penggunaan AI tercantum di bagian [AI Disclosure](#ai-disclosure)).

## Cara Menjalankan (Lokal Linux, Mac)

Clone repository ini ke folder lokal.

``` bash
git clone https://github.com/syxm1/myportofolio
cd myportofolio
```

Di bawah direktori `myportofolio`, buat dan aktifkan python virtual environment baru.

```bash
python3 -m venv env
source env/bin/activate
```

Install requirements yang diperlukan.

```bash
pip install -r requirements.txt
```

Run command di bawah untuk mulai menjalakan web.

```bash
python manage.py runserver
```

Buka browser, masuk ke halaman `localhost:8000` untuk memuat web. Virtual environment bisa dinonaktifkan dengan command `deactivate`

```bash
deactivate
```

## Seeding (Linux, Mac)

```bash
chmod +x seeding.sh
./seeding.sh
```

## AI Disclosure

Proyek ini dibuat dengan menggunakan bantuan AI Claude dengan model Sonnet 5. Strategi prompting yang  dilakukan adalah dengan memberikan attachment berupa file kode yang ingin dikerjakan ke model untuk mengatur konteks kemudian memberikan spesifikasi fitur yang ingin dibuat kepada model dan melakukan review pada kode yang digenerate model.

Prompt Log:
- [Tugas 2](https://claude.ai/share/8e15ecd3-8402-4af8-8dd9-761accac1c1e)
- [Tugas 3](https://claude.ai/share/2bb6a5b6-6e53-4336-946b-837d2388e11d)
- [Tugas 4](https://claude.ai/share/2ddfc100-2000-4b43-a16b-b83cbe441090)

## Weekly Tracker

- Week 1 (31 Agustus 2026 - 7 September 2026) : Membuat static page untuk section profile, skills, dan experience.
- Week 2 (8 September 2026 - 14 September 2026) : Mengimplementasikan Django MVT.
- Week 3 (15 September 2026 - 21 Sepetember 2026) : Mengimplementasikan Django Form untuk Create, Update, dan Delete instances pada Section Experience dan Education.
- Week 4 (22 September 2026 - 28 September 2026) : Authentication dan Authorization.

## Pertanyaan Reflektif

### Tugas 1
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>`? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
```
Pada proyek ini, digunakan beberapa elemen semantik seperti <header> untuk navbar, <main> untuk konten utama, <section> untuk membagi konten pada web menjadi beberapa blok (id="profile" untuk profil, id="skills" untuk daftar skill, dan id="experience" untuk daftar pengalaman), dan <footer> untuk bagian bawah halaman. <nav> juga dipakai di dalam header untuk grup tautan navigasi.

Elemen semantik seperti <section> memang tidak berpengaruh secara visual tetapi dapat berguna untuk developer yang membaca kode untuk memberitahukan 'makna' dari konten di dalamnya (tidak seperti jika hanya menggunakan <div> biasa yang bisa berisi konten dengan makna general).
```
2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
```
Tantangan utama muncul di bagian skills dan experience. Kartu skill punya lebar tetap yang di mobile terasa terlalu lebar, jadi diperkecil ke 160px lewat breakpoint agar kartu berikutnya tetap terlihat sebagai petunjuk scroll. Di bagian experience, header kartu (judul, subtitle, tanggal) yang sejajar horizontal jadi berdesakan saat judul panjang, sehingga diubah jadi bertumpuk vertikal di layar sempit.
```
3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
```
Batasan yang terdapat pada static web murni adalah minimnya interaktivitas yang bisa dilakukan antar user dan web. Fungsionalitas dinamis yang ingin diterapkan di web nantinya adalah opsi untuk user memilih menggunakan tema gelap/terang pada website ini.
```

### Tugas 2
1. Ketika pengguna membuka halaman portofolio, browser mengirim request yang pertama dicek oleh urls.py proyek untuk menentukan prefix URL mana yang diarahkan ke app mana lewat include(). Request lalu diteruskan ke urls.py aplikasi, yang memetakan path spesifik ke sebuah view. View mengambil data dengan query ke model (misalnya Project.objects.all()), lalu model menerjemahkan query itu ke SQL dan mengembalikan objek Python berisi data dari database. Data tersebut dikirim view ke template lewat context, dan template merendernya jadi HTML menggunakan tag seperti {% for %} dan {{ }}. Hasil render dibungkus jadi HttpResponse dan dikirim balik ke browser untuk ditampilkan.
2. Data portofolio sebaiknya disimpan di model, bukan hardcode di template, karena template seharusnya hanya urusan tampilan, bukan penyimpanan data. Dengan model, data bisa diubah lewat admin tanpa edit kode atau deploy ulang, lebih skalabel untuk banyak entri (cukup satu loop di template), bisa dipakai ulang di banyak halaman tanpa duplikasi, dan punya validasi/struktur yang jelas sehingga tidak rawan typo atau inkonsistensi seperti kalau ditulis manual di HTML.
3. makemigrations membuat file migrasi berdasarkan perubahan di models.py (mencatat rencana perubahan), sedangkan migrate mengeksekusi file itu ke database. Contoh: menambah field baru thumbnail = models.URLField(blank=True) di model Experience yang mengharuskan untuk menjalankan makemigrations guna membuat file migrasi, lalu migrate untuk benar-benar menambahkan kolom itu ke tabel database.

### Tugas 3
1. Kita menggunakan ModelForm di Django karena form ini secara otomatis dibuat berdasarkan struktur model yang sudah kita definisikan, sehingga kita tidak perlu menuliskan ulang field, tipe data, dan aturan validasi secara manual seperti pada form HTML biasa. Sementara itu, {% csrf_token %} wajib ditambahkan karena Django menerapkan proteksi terhadap serangan Cross-Site Request Forgery (CSRF), yaitu ketika pihak jahat mencoba mengirim request atas nama pengguna yang sedang login tanpa sepengetahuannya.
2. JSON lebih disukai dalam pengembangan web modern karena strukturnya jauh lebih ringkas dibanding XML yang memerlukan closing tag untuk setiap elemen, sehingga ukuran data yang dikirim lebih kecil dan lebih hemat bandwidth. Selain itu, JSON pada dasarnya adalah representasi objek JavaScript, sehingga browser bisa langsung mem-parsingnya menggunakan JSON.parse() tanpa memerlukan parser tambahan seperti yang dibutuhkan XML.
3. Saat sebuah fungsi view dipanggil untuk mengembalikan data portofolio dalam bentuk JSON, alurnya dimulai dari client yang mengirim request ke URL tertentu, kemudian view akan mengambil data dari database melalui query model Django. Karena objek Python ini tidak bisa langsung dikirim lewat HTTP yang hanya mendukung format teks, data tersebut perlu melalui proses serialization menggunakan modul seperti django.core.serializers untuk diubah menjadi format JSON, lalu dikembalikan ke client menggunakan JsonResponse atau HttpResponse dengan content_type="application/json". Proses serialization ini penting karena objek model Django menyimpan banyak informasi internal seperti method dan referensi database yang tidak relevan untuk dikirim, sehingga perlu disederhanakan menjadi struktur data standar.