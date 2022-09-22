# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:27:05 2022

@author: Linh Truong

Nội dung: giới thiệu một số câu lệnh cơ bản trên python
"""
# ---------------------------------------------------------------
# Để ghi chú trên một dòng bạn dùng dấu #

# ---------------------------------------------------------------
# 1. Biến
x = 6
print(type(x))
print(x)
print(f'x={x}\n')


y = 7.89
print(type(y))
print(y)
print(f'y={y}\n')

s = "Hello, Iam a string"
print(type(s))
print(s)
print(f's={s}\n')

z = 6
print(f'\nz = {z}')
print(f'Kieu du lieu cua z: {type(z)}')
z = (float)(z)
print(f'\nz = {z}')
print(f'Kieu du lieu cua z: {type(z)}')

# ---------------------------------------------------------------
# 2. Nhập, Xuất

# number = int(input('\nNhap vao mot so nguyen: '))
# print(f'number = {number}')
# print(f'Kieu du lieu cua number: {type(number)}')

# ---------------------------------------------------------------
# 3. Câu lệnh điều kiện
num = 3.4
'''
if num >= 0:
    if num > 0:
        print(f'\n{num} là số dương')
    else:
        print(f'\n{num} bằng 0')
else:
    print(f'\n{num} là số âm')
'''

if num >= 0:
    print(f'\n{num} là số dương')
elif num == 0:
    print(f'\n{num} bằng 0')
else:
    print(f'\n{num} là số âm')
    
# ---------------------------------------------------------------
# 4. Câu lệnh lặp

# In các số từ 0..10
print('\n')
for i in range(11):
    print(i)

    
# In các số từ 1..10
print('\n')
for i in range(1, 10):
    print(i)
    
# In các số lẻ từ 1..10
print('\n')
# for i in range(1, 10):
#     if i%2!=0:
#         print(i)

print('\n')
for i in range(1, 10, 2):
    print(i)
    
# In các số trong list
print('\n')
a = [3, 7, 8, 4, 6]

# print(f'\nĐộ dài của a: {len(a)}')
# for i in range(len(a)):
#     print(f'a[{i}] = {a[i]}')

for value in a:
    print(value)
    
# Tính tổng các giá trị của mảng a
# tong = 0
# for value in a:
#     tong += value

# print(f'\nTong: {tong}')

tong = 0
i = 0
while i < len(a):
    tong += a[i]
    i += 1
    
print(f'\nTong: {tong}')

# ---------------------------------------------------------------
# 5. Hàm (Function)
def xin_chao():
    '''    
    Chao ban sring.
    '''
    print('\nChao ban!')

def tinh_tong(num1, num2):
    '''
    Parameters
    ----------
    num1 : a number
    num2 : a number
    
    Returns
    -------
    sum of two number: num1 and num2

    '''    
    return num1 + num2

x = 3
y = 5
xin_chao()

tong2so = tinh_tong(x, y)
print(f'Tong 2 so la: {tong2so}')