# DaFlash

DaFlash adalah alat berbasis Termux untuk mempermudah pengguna Xiaomi melakukan flashing ROM fastboot atau recovery (TWRP) tanpa memerlukan PC/laptop. Dibuat untuk Miui Lovers yang ingin proses flashing cepat dan mudah melalui perangkat Android.

## Fitur
- **Flash ROM Fastboot**: Otomatis mendeteksi dan mengekstrak file ROM (.tgz) serta melakukan flashing.
- **Flash Recovery (TWRP)**: Mendeteksi file recovery (.img) dan mem-flash-nya ke perangkat.
- Antarmuka ramah pengguna dengan menu interaktif.
- Dukungan Termux:API untuk deteksi perangkat otomatis.
- Tidak memerlukan komputer, cukup perangkat Android dengan Termux.

## Persyaratan
- Perangkat Android dengan aplikasi **Termux** dan **Termux:API** terinstal.
- Perangkat Xiaomi dengan bootloader sudah di-unlock.
- File ROM fastboot (.tgz) atau recovery (.img) di penyimpanan internal (/sdcard).
- Kabel USB untuk menghubungkan perangkat Android (Termux) dengan perangkat Xiaomi.
- USB Debugging diaktifkan pada kedua perangkat.

## Instalasi
Lihat panduan lengkap di [docs/installation.md](docs/installation.md) untuk langkah-langkah instalasi dan penggunaan.

## Cara Menggunakan
1. Unduh `DaFlash.sh` dari [Releases](https://github.com/daxd13/DaFlash/releases) atau clone repository ini.
2. Jalankan script di Termux:
   ```bash
   chmod +x DaFlash.sh
   ./DaFlash.sh
