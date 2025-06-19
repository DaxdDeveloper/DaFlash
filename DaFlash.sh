#!/data/data/com.termux/files/usr/bin/bash

clear
pkg install wget curl tar python tsu fastboot adb -y
pkg install termux-api -y
termux-setup-storage

main_menu() {
    clear
    echo -e "\033[1;33m"
    echo "   ____       _____ _          _ _       
  |  _ \     |  ___| |__   ___| | | ___  
  | | | |    | |_  | '_ \ / __| | |/ _ \ 
  | |_| |    |  _| | | | | (__| | |  __/ 
  |____/     |_|   |_| |_| \___|_|_|\___|\033[0m"
    echo -e "\nSelamat Datang Miui Lovers."
    echo "DaFlash mempermudah user untuk melakukan flashing tanpa memerlukan komputer."
    echo -e "\nSelamat menggunakan."
    echo -e "Salam hangat Daxd Developer\n"
    echo "1. Flash Rom Fastboot"
    echo "2. Flash Recovery (TWRP)"
    read -p "Pilih opsi: " choice
    case $choice in
        1) flash_fastboot ;;
        2) flash_recovery ;;
        *) main_menu ;;
    esac
}

flash_fastboot() {
    clear
    echo "Mencari file ROM fastboot (.tgz)..."
    rom_files=($(find /sdcard -type f -name "*.tgz"))
    if [ ${#rom_files[@]} -eq 0 ]; then
        echo "Tidak ditemukan file ROM fastboot (.tgz)"
        read -p "Tekan Enter untuk kembali ke menu utama"
        main_menu
    else
        echo "File ROM ditemukan: ${rom_files[0]}"
        echo "1. Ekstrak sekarang"
        echo "2. Batalkan"
        read -p "Pilih opsi: " extract_choice
        case $extract_choice in
            1) extract_rom ;;
            2) main_menu ;;
            *) flash_fastboot ;;
        esac
    fi
}

extract_rom() {
    clear
    echo "Mengekstrak ROM..."
    mkdir -p /sdcard/DaFlash
    tar -xzf "${rom_files[0]}" -C /sdcard/DaFlash
    if [ $? -eq 0 ]; then
        echo "Ekstrak selesai."
        check_fastboot
    else
        echo "Gagal mengekstrak ROM."
        read -p "Tekan Enter untuk kembali ke menu utama"
        main_menu
    fi
}

check_fastboot() {
    echo "Masukkan perangkat ke mode fastboot..."
    fastboot devices | grep -q fastboot
    if [ $? -eq 0 ]; then
        start_flash
    else
        echo "Perangkat tidak terdeteksi di mode fastboot."
        read -p "Tekan Enter untuk mencoba lagi"
        check_fastboot
    fi
}

start_flash() {
    clear
    echo "Memulai proses flashing..."
    cd /sdcard/DaFlash/*/
    for script in *.sh; do
        if [ -f "$script" ]; then
            echo "Menjalankan $script..."
            chmod +x "$script"
            ./$script
            if [ $? -eq 0 ]; then
                echo "$script selesai."
            else
                echo "Gagal menjalankan $script."
                read -p "Tekan Enter untuk kembali ke menu utama"
                main_menu
            fi
        fi
    done
    flash_complete
}

flash_recovery() {
    clear
    echo "Mencari file recovery (.img)..."
    img_files=($(find /sdcard -type f -name "*.img"))
    if [ ${#img_files[@]} -eq 0 ]; then
        echo "Tidak ditemukan file recovery (.img)"
        read -p "Tekan Enter untuk kembali ke menu utama"
        main_menu
    else
        echo "File recovery ditemukan:"
        for i in "${!img_files[@]}"; do
            echo "$((i+1)). ${img_files[i]##*/}"
        done
        read -p "Pilih file recovery: " img_choice
        if [[ $img_choice -ge 1 && $img_choice -le ${#img_files[@]} ]]; then
            selected_img=${img_files[$((img_choice-1))]}
            check_fastboot_recovery
        else
            echo "Pilihan tidak valid."
            read -p "Tekan Enter untuk kembali"
            flash_recovery
        fi
    fi
}

check_fastboot_recovery() {
    echo "Masukkan perangkat ke mode fastboot..."
    fastboot devices | grep -q fastboot
    if [ $? -eq 0 ]; then
        start_flash_recovery
    else
        echo "Perangkat tidak terdeteksi di mode fastboot."
        read -p "Tekan Enter untuk mencoba lagi"
        check_fastboot_recovery
    fi
}

start_flash_recovery() {
    clear
    echo "Memulai flashing recovery..."
    fastboot flash boot "$selected_img"
    if [ $? -eq 0 ]; then
        echo "Flashing recovery selesai."
        fastboot reboot recovery
        if [ $? -eq 0 ]; then
            echo "Reboot ke recovery berhasil."
            flash_complete
        else
            echo "Gagal reboot ke recovery."
            read -p "Tekan Enter untuk kembali ke menu utama"
            main_menu
        fi
    else
        echo "Gagal flashing recovery."
        read -p "Tekan Enter untuk kembali ke menu utama"
        main_menu
    fi
}

flash_complete() {
    clear
    echo -e "\nHai, Flashing sudah selesai."
    echo "Selamat Menggunakan."
    echo -e "\nBeri ucapan terimakasih kepada Daxd sebagai kepuasan kamu"
    echo "1. Kembali"
    read -p "Pilih opsi: " complete_choice
    if [ "$complete_choice" == "1" ]; then
        main_menu
    else
        flash_complete
    fi
}

main_menu