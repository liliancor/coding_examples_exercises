def find_smallest_int(arr):
    num = arr[0]
    print("Começando com o numero ", num)
    for current_number in arr:
        print(f"Comparando {num} com {current_number} ")
        if current_number < num:
            num = current_number
    return num        


lista = [108, 31, 8, 15, 20, 280]

num = find_smallest_int(lista)

print("O menor numero da minha lista é: {}".format(num))
