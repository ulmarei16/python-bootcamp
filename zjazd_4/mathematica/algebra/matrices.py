def add_matrices(m1,m2):
    result=[]
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Różna ilość wierszy.")

    for row_i in range(len(m1)):
        # print("a: ", m1[row_i])
        # print("b: ", m2[row_i])
        # for col_i in range(len(m1[row_i])):
        #     print(m1[row_i][col_i] + m2[row_i][col_i])
        new_row = []
        for col_i in range(len(m1[row_i])):
            new_row.append(m1[row_i][col_i] + m2[row_i][col_i])
        result.append(new_row)

    return result

def sub_matrices(m1,m2):
    result = []
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        raise ValueError("Różna ilość wierszy.")

    for row_i in range(len(m1)):
        # print("a: ", m1[row_i])
        # print("b: ", m2[row_i])
        # for col_i in range(len(m1[row_i])):
        #     print(m1[row_i][col_i] + m2[row_i][col_i])
        new_row = []
        for col_i in range(len(m1[row_i])):
            new_row.append(m1[row_i][col_i] - m2[row_i][col_i])
        result.append(new_row)

    return result

print(__name__) #drukuje __main__

if __name__ == "__main__":  #powoduje, że jeżeli moduł będzie gdzieś importowany to nie będzie wykonywany w tym imporcie, tylko obiekty będą wykonywane (klasy, funkcje itp)
    a = [
        [1, 2, 3],
        [4, 5, 6]
        ]
    b = [
        [7, 8, 9],
        [10, 11, 12]
        ]
    print(add_matrices(a,b))
