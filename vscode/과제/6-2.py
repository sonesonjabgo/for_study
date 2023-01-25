grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

grain_lst = dict(grain_lst)

max_price = max(grain_lst.values())
print([key for key, value in grain_lst.items() if value == max_price][0])