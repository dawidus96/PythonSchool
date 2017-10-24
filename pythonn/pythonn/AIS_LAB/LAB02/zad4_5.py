def insertion_sort_string(A):
    for i in xrange(1, len(A)):
        j = i
        print cmp_string(A[j - 1], A[j])
        while j > 0 and cmp_string(A[j], A[j - 1]) is True:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1
    return A


def cmp_string(word1, word2):
    dict_num = {'0': 999, '1': 1000, '2': 1001, '3': 1002, '4': 1003,
                '5': 1004, '6': 1005, '7': 1006, '8': 1007, '9': 1008,
                'a': 90, 'c': 92, 'b': 91, 'e': 94, 'd': 93, 'g': 96,
                'f': 95, 'i': 98, 'h': 97, 'k': 100, 'j': 99, 'm': 102,
                'l': 101, 'o': 104, 'n': 103, 'p': 105, 's': 107, 'r': 106,
                'u': 109, 't': 108, 'w': 111, 'v': 110, 'y': 112, 'z': 113,
                'A': 90, 'C': 92, 'B': 91, 'E': 94, 'D': 93, 'G': 96,
                'F': 95, 'I': 98, 'H': 97, 'K': 100, 'J': 99, 'M': 102,
                'L': 101, 'O': 104, 'N': 103, 'P': 105, 'S': 107, 'R': 106,
                'U': 109, 'T': 108, 'W': 111, 'V': 110, 'Y': 112, 'Z': 113}

    i = 0
    while i < len(word1) - 1 or i < len(word2) - 1:
        a = dict_num.get(word1[i])
        b = dict_num.get(word2[i])
        if a == b:
            i += 1
        elif a > b:
            return False
        elif a < b:
            return True

string_list = ['a2e', 'brr', 'az99', 'chomicz', '1ar2']
# s1 < s2 == TRUE
print insertion_sort_string(string_list)
