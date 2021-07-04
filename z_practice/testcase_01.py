def get_data():
    for i in range(1,10):
        for j in range(1,10):
            if i%j == 2:
                return i,j
print(get_data())
