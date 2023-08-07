# PushUpCounter
Menghitung jumlah push up dengan menggunakan library mediapipe sehingga pose estimastion akan keluar dari situ kita akan menghitung rumus untuk mencari sudut tengah sehingga kita bisa menghitung push up

# Program Menghitung Push Up dengan Deteksi Sudut Menggunakan MediaPipe
Selamat datang di proyek ini! Ini adalah program sederhana yang menghitung jumlah push up dengan deteksi sudut tengah siku dan sudut tengah mata kaki menggunakan MediaPipe Pose Estimation.

# Cara Program Bekerja
Program akan menggunakan webcam untuk mengambil gambar pengguna.
MediaPipe Pose Estimation akan mendeteksi pose tubuh pengguna.
Program akan menghitung sudut antara lengan dan tubuh (siku) serta sudut antara paha dan tubuh (mata kaki) untuk mengidentifikasi gerakan push up.
Jumlah push up akan ditampilkan di layar.
# Rumus Perhitungan Sudut
Sudut Tengah Siku: sudut_siku = arctan(dy / dx), dengan dx sebagai selisih titik bahu dan pergelangan tangan (sumbu x) serta dy sebagai selisih tinggi antara bahu dan pergelangan tangan (sumbu y).
Sudut Tengah Mata Kaki: sudut_mata_kaki = arctan(dy / dx), dengan dx sebagai selisih titik pinggul dan lutut (sumbu x) serta dy sebagai selisih tinggi antara pinggul dan lutut (sumbu y).

# Hasil
![Screenshot (202)](https://github.com/adrianwib/PushUpCounter/assets/103250981/ab285d4b-d33d-46ef-8297-303c9f659bff)
Perhitungan akan dimulai dari posisi sudut 170 ke atas untuk siku


![Screenshot (203)](https://github.com/adrianwib/PushUpCounter/assets/103250981/f47b3079-061d-4dcc-9dde-3beebf442200)
Dia akan bertambah saat sudut siku dan sudut mata kaki dibawah 100


![Screenshot (206)](https://github.com/adrianwib/PushUpCounter/assets/103250981/e39ad11c-9a27-4187-a0f5-4ff1cbf5e1fb)

![Screenshot (207)](https://github.com/adrianwib/PushUpCounter/assets/103250981/f34641b2-12a1-4063-be78-01ce0a0ac741)
Hasil nya 6
