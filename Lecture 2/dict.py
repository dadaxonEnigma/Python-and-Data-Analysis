# empty_dict = {}
d1 = {"a":"some value",
      "b": [1,2,3,4]}
# print(d1)
# d1[7] = "an integer"
# print(d1)
# res = "b" in d1 
# print(res)

# ---------------- удаления del и pop (return del elem)
d1[5] = 'some value'
d1['dummy'] = 'another value'
# print(d1)
# del d1[5]
# print(d1)

# ----------keys , values , items
# print(list(d1.keys()))
# print(list(d1.values()))
# print(list(d1.items()))

# --------------- update
# d1.update({'c':'hello', 'd':'world'})
# print(d1)

# Создание словаря из последовательностей
# key_list = [1,2,3,4,5]
# value_list = ['one','two','three','four','five']
# mapping = {}
# for key,val in zip(key_list, value_list):
#     mapping[key] = val
# print(mapping)

# # 2 method
# mapping = dict(zip(key_list, value_list))
# print(mapping)

