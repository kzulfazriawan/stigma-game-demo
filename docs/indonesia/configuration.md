# Konfigurasi
***
## Pengantar
semua konfigurasi disimpan didalam direktori `config/`. Ada beberapa module python yang bisa
anda gunakan untuk mengatur applikasi anda seperti `base.py` untuk mengatur dasar applikasi anda,
bebaskan diri anda untuk melihat kode tersebut dan ubah sesuai dengan keinginan anda.

## Konfigurasi dasar
konfigurasi dasar sangat mudah, anda hanya perlu menulis ulang sesuai keinginan anda karena kode tersebut
relatif dengan applikasi anda dari inti. Ini adalah beberapa contoh tentang variabel dictionary didalam file
`base.py`:

main:{'path' : '/home/your path' , ...}

adalah konfigurasi utama untuk applikasi anda jadi berhati-hati dengan nilai variabel tersebut karena itu
tidak hanya relatif dengan inti applikasi tapi nilai tersebut memang dibutuhkan oleh applikasi, ada beberapa
indeks kunci yang seharusnya anda atur sendiri, berikut indeks kunci didalam variabel utama: 

     - path, this key is used for managing your application `root path`, you can set it into default with value it with `None`, the application will automatically finding your root path.
     
graphics{'width': int width, height: int height, ...}
variable ini menghasilkan informasi grafis applikasi anda, seperti lebar, tinggi dan lainnya untuk applikasi anda.

      - width, this key will provide information window width, you can set it with you wanted to set but you only can set it as integer value for example `1024` if you wanted to change width your window application into 1024 pixel.

      - height, same as width but it used to manage your height window, you can only set it as integer value, for example `768` if you wanted to set your window application into 768 pixel.
      

kivy{'exit_on_escape': '0/1' , ...}
sejak stigma dibangung berdasarkan kivy anda harus mengikuti aturan kivy. berikut adalah beberapa contoh indeks kunci pada
kivy:

      - exit_on_escape, this key is provide for escape key function as the default of kivy configuration escape key will destroy the application, so you may set this key if you wanted to develop application for PC platform and the application will not destroy with just press escape button.