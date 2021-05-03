"""
File: largest_digit.py
Name: Julie
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""
lar = 0
new_lar = 0

import time

def main():
	star = time.time()
	print(find_largest_digit(12345))  # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9
	end = time.time()
	print("執行時間：%f 秒" % (end - star))

def find_largest_digit(n):
	"""
	:param n:
	:return:lar
	"""
	global lar, new_lar
	if abs(n) > 0:
		r = abs(n) % 10 # 取（剩下的數字）最後的數字 用餘數來取
		if lar < r:
			lar = r
			new_lar = r
		find_largest_digit(int(n/10))  # 取剩下的數字
		lar = 0 # for the next to compare
		return new_lar





if __name__ == '__main__':
	main()
