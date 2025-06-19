# Panduan Instalasi dan Penggunaan DaFlash

## Persyaratan
- Aplikasi **Termux** dan **Termux:API** terinstal di perangkat Android.
- Perangkat Xiaomi dengan bootloader sudah di-unlock.
- File ROM fastboot (.tgz) atau recovery (.img) tersimpan di `/sdcard`.
- Kabel USB untuk menghubungkan perangkat Android (Termux) dengan perangkat Xiaomi.
- USB Debugging diaktifkan di kedua perangkat.

## Langkah Instalasi
1. Instal Termux dari [Google Play Store](https://play.google.com/store/apps/details?id=com.termux) atau [F-Droid](https://f-droid.org/en/packages/com.termux/).
2. Instal Termux:API dari Google Play Store atau F-Droid.
3. Buka Termux dan perbarui paket:
   ```bash
   pkg update && pkg upgrade
