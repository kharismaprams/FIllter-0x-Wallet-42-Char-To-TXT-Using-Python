# Filter Alamat Ethereum dengan Panjang 42 Karakter

Dokumen ini memberikan panduan langkah demi langkah tentang bagaimana cara menggunakan skrip Python untuk memfilter alamat Ethereum dengan panjang 42 karakter yang dimulai dengan "0x" dan menyimpan hasilnya dalam sebuah file `.txt`.

## Persiapan Awal

1. Pastikan Anda memiliki Python terinstal di komputer Anda. Jika belum, Anda dapat mengunduhnya dari [python.org](https://www.python.org/downloads/).

## Langkah 1: Menyiapkan Daftar Alamat

1. Buka file `addresses.txt` dan salin alamat-alamat Ethereum yang ingin Anda filter. Pastikan alamat-alamat tersebut memiliki panjang 42 karakter dan diawali dengan "0x". Setiap alamat diletakkan pada baris yang berbeda.

## Langkah 2: Menjalankan Skrip Python

1. Simpan skrip Python di bawah ini dalam sebuah file dengan ekstensi `.py`, misalnya `filter_addresses.py`.

```python
import re
# Masukan alamat wallet anda dibawah
addresses = """ 
0xAddress1
0xAddress2
0xAddress3
...
"""

# Pisahkan alamat wallet menjadi daftar
address_list = re.findall(r'0x\w{42}', addresses)

# Tulis alamat wallet yang telah difilter ke dalam file .txt
with open("filtered_addresses.txt", "w") as f:
    for address in address_list:
        f.write(address + '\\n')
```

Buka terminal dan navigasi ke direktori di mana skrip Python (filter_addresses.py) disimpan.
Jalankan skrip dengan perintah berikut:
`python filter_addresses.py`

## Langkah 3: Hasil Filter
1. Setelah menjalankan skrip, Anda akan mendapatkan file `filtered_addresses.txt` yang berisi daftar alamat Ethereum yang telah difilter.

## Catatan Penting
1. Pastikan alamat-alamat yang ingin Anda filter memiliki panjang tepat 42 karakter dan diawali dengan "0x".
2. Skrip ini hanya memfilter alamat berdasarkan panjang dan formatnya, bukan validitas alamat Ethereum sebenarnya.
3. Gunakan dengan bijak dan hati-hati saat berurusan dengan data pribadi atau sensitif.

Dengan mengikuti panduan di atas, Anda dapat dengan mudah memfilter alamat Ethereum dengan panjang 42 karakter yang dimulai dengan "0x" dan menyimpan hasilnya dalam sebuah file `.txt.`


Pastikan untuk menyesuaikan nama file dan ekstensinya sesuai dengan yang Anda gunakan, serta menambahkan informasi atau perubahan lain yang Anda anggap perlu dalam dokumentasi ini.
