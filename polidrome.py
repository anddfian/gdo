import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def palindrome():
    text = input("Masukkan Teks/Angka : ")
    print("Hasil Membalikkan   :", text[::-1])
    print("=====================================")
    if text == text[::-1]:
        print("Teks/Angka tersebut Palindrome")
    else:
        print("Teks/Angka tersebut Tidak Palindrome")
    print("=====================================")
    back_to_menu()

def back_to_menu():
    input("\nTekan 'Enter' untuk melanjutkan...")
    show_menu()

def show_menu():
    clear_screen()
    print("=====================================")
    print("|         PROGRAM PALINDROME        |")
    print("=====================================")
    print("|       OLEH ANGGOTA KELOMPOK       |")
    print("=====================================")
    print("| ANDI ALFIAN BAHTIAR  (2009106002) |")
    print("| ALFI SYACHDIAN NOOR  (2009106023) |")
    print("| M. ARSY DEWANTARA    (2009106033) |")
    print("| FATHAN GHOJI ADZIKRA (2009106044) |")
    print("| M. AMRI RASYID R.    (2009106047) |")
    print("=====================================")
    print("| Info: Tekan CTRL + C untuk keluar |")
    print("=====================================")
    try:
        palindrome()
    except KeyboardInterrupt:
        print("\n=====================================")
        print("|            Terima Kasih           |")
        print("=====================================")
        exit()

if __name__ == "__main__":
    show_menu()
