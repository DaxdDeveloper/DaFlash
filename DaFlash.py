#!/data/data/com.termux/files/usr/bin/python

import os
import subprocess
import time

# Install required packages
def install_packages():
    packages = ["wget", "curl", "tar", "python", "tsu", "fastboot", "adb", "termux-api"]
    for pkg in packages:
        subprocess.run(["pkg", "install", pkg, "-y"], check=True)

# Setup storage
subprocess.run(["termux-setup-storage"], check=True)

# Main menu
def main_menu():
    os.system("clear")
    print("\033[1;33m")
    print("   ____       _____ _          _ _       ")
    print("  |  _ \     |  ___| |__   ___| | | ___  ")
    print("  | | | |    | |_  | '_ \ / __| | |/ _ \ ")
    print("  | |_| |    |  _| | | | | (__| | |  __/ ")
    print("  |____/     |_|   |_| |_| \___|_|_|\___|\033[0m")
    print("\nSelamat Datang Miui Lovers.")
    print("DaFlash mempermudah user untuk melakukan flashing tanpa memerlukan komputer.")
    print("\nSelamat menggunakan.")
    print("Salam hangat Daxd Developer\n")
    print("1. Flash Rom Fastboot")
    print("2. Flash Recovery (TWRP)")
    choice = input("Pilih opsi: ")
    if choice == "1":
        flash_fastboot()
    elif choice == "2":
        flash_recovery()
    else:
        main_menu()

# Flash Fastboot
def flash_fastboot():
    os.system("clear")
    print("Mencari file ROM fastboot (.tgz)...")
    result = subprocess.run(["find", "/sdcard", "-type", "f", "-name", "*.tgz"], capture_output=True, text=True)
    rom_files = result.stdout.split()
    if not rom_files:
        print("Tidak ditemukan file ROM fastboot (.tgz)")
        input("Tekan Enter untuk kembali ke menu utama")
        main_menu()
    else:
        print(f"File ROM ditemukan: {rom_files[0]}")
        print("1. Ekstrak sekarang")
        print("2. Batalkan")
        extract_choice = input("Pilih opsi: ")
        if extract_choice == "1":
            extract_rom(rom_files[0])
        elif extract_choice == "2":
            main_menu()
        else:
            flash_fastboot()

# Extract ROM
def extract_rom(rom_file):
    os.system("clear")
    print("Mengekstrak ROM...")
    os.makedirs("/sdcard/DaFlash", exist_ok=True)
    subprocess.run(["tar", "-xzf", rom_file, "-C", "/sdcard/DaFlash"], check=True)
    print("Ekstrak selesai.")
    check_fastboot()

# Check Fastboot
def check_fastboot():
    print("Masukkan perangkat ke mode fastboot...")
    while True:
        result = subprocess.run(["fastboot", "devices"], capture_output=True, text=True)
        if "fastboot" in result.stdout:
            start_flash()
            break
        print("Perangkat tidak terdeteksi di mode fastboot.")
        input("Tekan Enter untuk mencoba lagi")

# Start Flash
def start_flash():
    os.system("clear")
    print("Memulai proses flashing...")
    os.chdir("/sdcard/DaFlash")
    for script in os.listdir():
        if script.endswith(".sh"):
            print(f"Menjalankan {script}...")
            subprocess.run(["chmod", "+x", script], check=True)
            subprocess.run(["./" + script], check=True)
            print(f"{script} selesai.")
    flash_complete()

# Flash Recovery
def flash_recovery():
    os.system("clear")
    print("Mencari file recovery (.img)...")
    result = subprocess.run(["find", "/sdcard", "-type", "f", "-name", "*.img"], capture_output=True, text=True)
    img_files = result.stdout.split()
    if not img_files:
        print("Tidak ditemukan file recovery (.img)")
        input("Tekan Enter untuk kembali ke menu utama")
        main_menu()
    else:
        print("File recovery ditemukan:")
        for i, img in enumerate(img_files, 1):
            print(f"{i}. {os.path.basename(img)}")
        img_choice = input("Pilih file recovery: ")
        try:
            selected_img = img_files[int(img_choice) - 1]
            check_fastboot_recovery(selected_img)
        except (IndexError, ValueError):
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali")
            flash_recovery()

# Check Fastboot for Recovery
def check_fastboot_recovery(selected_img):
    print("Masukkan perangkat ke mode fastboot...")
    while True:
        result = subprocess.run(["fastboot", "devices"], capture_output=True, text=True)
        if "fastboot" in result.stdout:
            start_flash_recovery(selected_img)
            break
        print("Perangkat tidak terdeteksi di mode fastboot.")
        input("Tekan Enter untuk mencoba lagi")

# Start Flash Recovery
def start_flash_recovery(selected_img):
    os.system("clear")
    print("Memulai flashing recovery...")
    subprocess.run(["fastboot", "flash", "boot", selected_img], check=True)
    print("Flashing recovery selesai.")
    subprocess.run(["fastboot", "reboot", "recovery"], check=True)
    print("Reboot ke recovery berhasil.")
    flash_complete()

# Flash Complete
def flash_complete():
    os.system("clear")
    print("\nHai, Flashing sudah selesai.")
    print("Selamat Menggunakan.")
    print("\nBeri ucapan terimakasih kepada Daxd sebagai kepuasan kamu")
    print("1. Kembali")
    complete_choice = input("Pilih opsi: ")
    if complete_choice == "1":
        main_menu()
    else:
        flash_complete()

if __name__ == "__main__":
    install_packages()
    main_menu(
