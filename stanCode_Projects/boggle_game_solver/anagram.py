"""
File: anagram.py
Name:Julie
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
lis = []



def main():
    star = time.time()
    read_dictionary(FILE)
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = str(input('Find anagrams for:'))
        if s == EXIT:
            break
        else:
            has_prefix(s)
            word = find_anagrams(s)
            c = len(word)
            print(str(c) + ' anagrams' + str(word))
    end = time.time()
    print("執行時間：%f 秒" % (end - star))


def read_dictionary(FILE):
    global lis
    with open(FILE, 'r') as f:
        for line in f: # 每一行用list 去看 因為只有list 可以分開
            line = line.strip('\n') #去掉分隔符號
            lis.append(line)


def find_anagrams(s):
    """
    :param s:
    :return: ans = target_list
    """
    global lis
    ans = []
    for word in lis:
        if anagram(word, s):
            print('Searching...')
            print('Found:  '+ str(word))
            # put those com
            ans.append(word)
    return ans


def anagram(str1, str2):
    # straightly to see if they have same combination
    return sorted(str1) == sorted(str2)


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:bool
    """
    # In order to accelerate program
    for i in lis:
        if sub_s.startswith(i) is True:
            return True
        return False


if __name__ == '__main__':
    main()
