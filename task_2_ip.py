# -*- coding: utf-8 -*-
#
# Задача с ip адресами
# Есть файл со строками вида:
# <host>\t<ip>\t<page>\n
# Нужно вывести 5 айпи-адресов, которые встречаются чаще других.

SOURCE_FILE = 'путь до файла'


storage = {}
with open(SOURCE_FILE, 'r', encoding='utf-8') as file:
    for line in file:
        host, ip, page = line.split()
        if ip in storage:
            storage[ip] += 1
        else:
            storage[ip] = 1

ip_list = (list(storage.items()))
ip_list.sort(key=lambda item: - item[1])

for popular_ip in ip_list[0:5]:
    print(f'{popular_ip[0]} - {popular_ip[1]}')
