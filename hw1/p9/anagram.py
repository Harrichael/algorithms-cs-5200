"""
This file creates two anagram generators and compares them
"""

def anagram1(string):
    """
    This anagram func uses multiple recursive calls
    """
    if string == '':
        return ['']
    else:
        anagrams = []
        for i, c in enumerate(string):
            string_part = string[:i] + string[i+1:]
            for sub_anagram in anagram1(string_part):
                new_anagram = c + sub_anagram
                anagrams.append(new_anagram)

        return anagrams

def anagram2(string):
    """
    This anagram func uses one recursive call
    """

    if not string:
        return ['']
    else:
        anagrams = []
        head = string[0]
        tail = string[1:]
        for sub_anagram in anagram2(tail):
            for i in range(len(sub_anagram)+1):
                new_anagram = sub_anagram[:i] + head + sub_anagram[i:]
                anagrams.append(new_anagram)

        return anagrams            

if __name__ == '__main__':
    anagram1('hello wor')
    anagram2('hello wor')

