

from tabulate import tabulate

import regex as re

database = [
        {'Kode' : 1, 'Nama': 'Aji', 'Divisi': 'Marketing', 'Level': 'Manager', 'Kota': 'Jakarta', 'Email': 'aji@xyzcompany.com'},
        {'Kode' : 2, 'Nama': 'Budi', 'Divisi': 'Recruitment', 'Level': 'Staff','Kota': 'Jakarta', 'Email': 'budi@xyzcompany.com'},
        {'Kode' : 3, 'Nama': 'Caca', 'Divisi': 'Operasional', 'Level': 'Staff', 'Kota': 'Bogor', 'Email': 'caca@xyzcompany.com'},
        {'Kode' : 4, 'Nama': 'Dika', 'Divisi': 'Sales', 'Level': 'Manager', 'Kota': 'Bekasi', 'Email': 'dika@xyzcompany.com'},
        {'Kode' : 5, 'Nama': 'Eva', 'Divisi': 'Operasional', 'Level': 'Staff', 'Kota': 'Bogor', 'Email': 'eva@xyzcompany.com'}
]

# Fungsi Input Numerik
def input_numerik(prompt):
    while True:
        inputan = input(prompt)
        if inputan.isdigit():
            return int(inputan)
        else:
            print('Input anda bukan angka')

#Fungsi input alfabet
def input_alfabet(prompt):
    while True:
        inputan = input(prompt)
        if inputan.isalpha():
            return str(inputan)
        else:
            print('Input anda bukan huruf')

#fungsi input email
def input_email(prompt):
    while True:
        inputan = input(prompt)
        if re.fullmatch("\w+@xyzcompany.com", inputan):
            return str(inputan)
        else:
            print("Format salah. Harus menggunakan '@xyzcompany.com'")


# Read Data
def read_data(data):
    print('\nRead Data')
    print(tabulate(data, headers = 'keys', tablefmt = 'pretty'))

# Create Data
def create_data():
    print('\nCreate Data')
    kode = input_numerik('Masukkan kode: ')
    nama = input_alfabet('Masukkan nama: ').title()
    divisi = input_alfabet('Masukkan divisi: ').title()
    level = input_alfabet('Masukkan level: ').title()
    kota = input_alfabet('Masukkan kota: ').title()
    email = input_email('Masukkan email: ')
    data_baru = {'Kode': kode, 'Nama': nama, 'Divisi': divisi, 'Level': level, 'Kota': kota, 'Email': email}
    database.append(data_baru)
    print('Data berhasil ditambahkan!')

# Update Data
def update_data():
    print('\nUpdate Data')
    kode = input_numerik("Masukkan kode karyawan yang ingin diupdate: ")
    for item in database:
        if item["Kode"] == kode:
            nama = input_alfabet(f"Masukkan nama baru untuk kode {kode} (sekarang {item['Nama']}): ").title()
            divisi = input_alfabet(f"Masukkan divisi baru untuk kode {kode} (sekarang {item['Divisi']}): ").title()
            level = input_alfabet(f"Masukkan level baru untuk kode {kode} (sekarang {item['Level']}): ").title()
            kota = input_alfabet(f"Masukkan kota baru untuk kode {kode} (sekarang {item['Kota']}): ").title()
            email = input_email(f"Masukkan email baru untuk kode {kode} (sekarang {item['Email']}):)")
            item.update({'Nama': nama, 'Divisi': divisi, 'Level': level, 'Kota': kota, 'Email': email})
            print(f"Data karyawan dengan kode {kode} berhasil diperbarui.")
            return
    print(f"Tidak ada data karyawan dengan kode {kode}.")

# Delete Data
def delete_data():
    print('\nDelete Data')
    kode = input_numerik("Masukkan kode karyawan yang ingin dihapus: ")
    kode_list = [item["Kode"] for item in database]
    if kode in kode_list:
        database[:] = [item for item in database if item["Kode"] != kode]
        print(f"Data karyawan dengan kode {kode} telah dihapus.")
    else:
        print(f"Tidak ada data karyawan dengan kode {kode}.")

# Filter Data
def filter_data():
    print('\nFilter Data')
    key = input_alfabet("Masukkan kunci filter (Nama, Divisi, Level, Kota): ").title()
    value = input_alfabet(f"Masukkan nilai untuk filter berdasarkan {key}: ").title()
    if key in ["Nama", "Divisi", "Level", "Kota"]:
        filtered_data = [item for item in database if item[key] == value]
        if filtered_data:
            print(tabulate(filtered_data, headers='keys', tablefmt='pretty'))
        else:
            print(f"Tidak ada data karyawan dengan {key} {value}.")
    else:
        print("Kunci filter tidak valid. Pilihan yang tersedia: Nama, Divisi, Level, Kota.")


# Main 
def main():
    while True:
        print('''
        =====================
        DATA KARYAWAN PT XYZ
        =====================
        1. Read Data
        2. Create Data
        3. Update Data
        4. Delete Data
        5. Filter Data
        6. Exit
        =====================
        ''')

        inputan = input('Masukkan menu: ')
        if inputan == '1':
            read_data(database)
        elif inputan == '2':
            create_data()
        elif inputan == '3':
            update_data()
        elif inputan == '4':
            delete_data()
        elif inputan == '5':
            filter_data()
        elif inputan == '6':
            print('Program selesai')
            break
        else:
            print('Menu tidak ada')

main()
