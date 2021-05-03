"""
File: boggle.py
Name: Julie
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
lis = []
count = 0
s_lis = [] #因為不能重複
big_bag = []


def main():
	"""
	TODO:
	"""
	global big_bag
	read_dictionary()

	for i in range(4): # 要做4排輸入
		s = input(str(i+1)+' row of letters:').lower() #Case Insentive
		c_lis = s.split() # 去掉空白
		big_bag.append(c_lis) # 加到矩陣
		if len(c_lis) != 4: # 如果一行超過4個
			print('Illegal Input')
			break
	print(big_bag)
	play_boggle()
	print('There are ' + str(count)+ ' words in total.')


def play_boggle():
	global s_lis

	for i in range(4):
		for j in range(4):
			# 用過的lis先清空
			s_lis = []
			word = ''
			word += big_bag[i][j] #第一個第二個位置
			s_lis.append((i, j)) # p_lis 存位置得點
			found_word(word, [i, j], [i, j])


def found_word(word, old_p, new_p):
	global big_bag, s_lis, count
	old_p = new_p  # 換上一個位置
	if has_prefix(word):  # ㄒ開始跑
		if word in lis:
			if len(word) >= 4:
				lis.remove(word)  # 如果前面四的字一樣會一起loop
				print('Found: ' + word)
				count += 1  # 開始跑
				found_word(word, old_p, new_p) # 呼叫自己
		else:
			for i in range(-1, 2, 1):
				for j in range(-1, 2, 1):
					x = old_p[0] + i
					y = old_p[1] + j
					if 0 <= x < 4 and 0 <= y < 4:
						if (x, y) not in s_lis:   # 看位置有沒有用過
							s_lis.append((x, y))  # 加上去確認可以串
							# choose
							word += big_bag[x][y]
							new_p = [x, y]
							# explore
							found_word(word, old_p, new_p)
							# unchoose
							s_lis.pop()
							word = word[:len(word)-1]





def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global lis
	with open(FILE, 'r') as f:
		for line in f:  # 每一行用list 去看 因為只有list 可以分開
			line = line.strip('\n')  # 去掉分隔符號
			if len(line) >= 4:
				lis.append(line)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	# In order to accelerate program
	for i in lis:
		if i.startswith(sub_s) is True:
			return True
	return False


if __name__ == '__main__':
	main()
