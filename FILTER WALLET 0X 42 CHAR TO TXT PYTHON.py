import re

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