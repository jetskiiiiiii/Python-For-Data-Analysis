# # calling tuple function
# a = tuple('str')
# print(f'This is a tuple: {a}')

# # calling list function
# b = list(a)
# print(f'This is a list: {b}')

# gen = range(10)
# l = list(gen)
# print(l)

# seq_1 = ["a", "b", "c", "d"]
# seq_2 = [1, 2, 3, 4]

new_dict = {}
# for key, value in zip(seq_1, seq_2):
#     new_dict[key] = value
    
# new_dict = dict(zip(seq_1, seq_2))
# print(new_dict)

###

# categorizing a list into a dictionary

# list_of_words = ["apple", "grape", "airflow", "game", "grass", "ants"]

# from collections import defaultdict

# even_better_dict = defaultdict(list)

# for word in list_of_words:
#     even_better_dict[word[0]].append(word)
    
# print(even_better_dict)

###


# tup = [(1,2), (3, 4), (5, 6)]
# for i in tup:
#     print(i)
    
# for a, b in tup:
#     print(a, b)
    
# tup2 = 1, 2, 3, 4, 5
# a, b, *_ = tup2
# print(*_)