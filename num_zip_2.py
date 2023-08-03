num_list_1 = [1, 2, 3, 4, 5]
num_list_2 = [6, 7]

def num_2(num_list_2):
    for num in range(len(num_list_2)+(len(num_list_1)-(len(num_list_2)))):
        if num_list_2[num] < num_list_2[-1]:
            num_list_2.append(num_list_2[num]+2)
    return num_list_2

def zip_num():
    for num1,num2 in zip(num_list_1, num_2(num_list_2)):
        print((num1,num2))

def main():
    zip_num()

if __name__ == "__main__":
    main()