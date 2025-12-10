numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
k = len(numbers)
a = numbers.index(None)
s = sum(n for n in numbers if n is not None)
new = s / k
numbers[a] = new
print("Измененный список:", numbers)
