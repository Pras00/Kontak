import time, os

def clear():
    os.system('cls' or 'clear')

class ContactManager:
    def __init__(self):
        self.contacts = []

    def create_contact(self, name, phone_number):
        contact = {'name': name, 'phone_number': phone_number}
        self.contacts.append(contact)
        print(f"Kontak '{name}' dengan nomor '{phone_number}' berhasil ditambahkan.")

    def show_contact(self):
        if not self.contacts:
            print("Daftar kontak kosong.")
        else:
            print("Daftar Kontak:")
            no = 1
            for contact in self.contacts:
                print(f"{no}. Nama: {contact['name']}, Nomor Telepon: {contact['phone_number']}")
                no += 1

    def search_contact(self, search_name):
        found_contacts = [contact for contact in self.contacts if contact['name'].lower() == search_name.lower()]
        if found_contacts:
            print(f"Kontak ditemukan:")
            for contact in found_contacts:
                print(f"Nama: {contact['name']}, Nomor Telepon: {contact['phone_number']}")
        else:
            print(f"Kontak dengan nama {search_name} tidak ditemukan.")

    def edit_contact(self, search_name):
        found_contact = next((contact for contact in self.contacts if contact['name'].lower() == search_name.lower()), None)
        if found_contact:
            new_phone_number = input("Masukkan nomor telepon baru: ")
            found_contact['phone_number'] = new_phone_number
            print(f"Nomor telepon kontak {search_name} berhasil diperbarui.")
        else:
            print(f"Kontak dengan nama {search_name} tidak ditemukan.")


    def delete_contact(self, search_name):
        original_len = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if contact['name'].lower() != search_name.lower()]
        if len(self.contacts) == original_len:
            print(f"Kontak dengan nama {search_name} tidak ditemukan.")
        else:
            print(f"Kontak dengan nama {search_name} berhasil dihapus.")



def main():
    contact_manager = ContactManager()

    while True:
        clear()
        print("-"*35)
        print('|' + ' '*4 + "===> APLIKASI KONTAK <===" + ' '*4 + '|')
        print(f"| {' ':<31} |")
        print(f"| {'[1] Lihat Daftar Kotak':<31} |")
        print(f"| {'[2] Tambah Kontak Baru':<31} |")
        print(f"| {'[3] Cari Kontak':<31} |")
        print(f"| {'[4] Edit Kontak':<31} |")
        print(f"| {'[5] Hapus Kontak':<31} |")
        print(f"| {'[0] Keluar / Logout':<31} |")
        print("-"*35)

        pilihan = input("Pilih menu --> ")

        if pilihan == '1':
            clear()
            contact_manager.show_contact()
            input("\nTekan Enter untuk kembali...")
        elif pilihan == '2':
            clear()
            print('-'*30)  
            name = input("Nama          : ")
            phone_number = input("No. Telepon   : ")
            print('-'*30)
            contact_manager.create_contact(name, phone_number)
            input("\nTekan Enter untuk kembali...")
        elif pilihan == '3':
            clear()
            search_name = input("Masukkan nama kontak yang dicari: ")
            clear()
            contact_manager.search_contact(search_name)
            input("\nTekan Enter untuk kembali...")
        elif pilihan == '4':
            clear()
            search_name = input("Masukkan nama kontak yang ingin diedit: ")
            contact_manager.edit_contact(search_name)
            input("\nTekan Enter untuk kembali...")
        elif pilihan == '5':
            clear()
            search_name = input("Masukkan nama kontak yang ingin dihapus: ")
            contact_manager.delete_contact(search_name)
            input("\nTekan Enter untuk kembali...")
        elif pilihan == '0':
            clear()
            print("Program selesai.")
            time.sleep(1)
            exit()
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")

if __name__ == "__main__":
    main()
