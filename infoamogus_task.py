
 
# lst = [1, 234, 22, 95, 53, 19, 11, 999] другой список чисел

lst = [3, 14, 1, 7, 9, 8, 11, 6, 4, 2]

# Создаем функцию, для листа с 2+ значениями, добавляя левую и правую часть 
# Худщий - O(n * log n), Лучший - Omega(n * log n)
def mergeSort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2 # Середина списка = длина / пополам НАЦЕЛО
        left = lst[:mid]
        right = lst[mid:]

        # Идем налево и направо + сортируем их 
        mergeSort(left)
        mergeSort(right)

        # Указатели элементов
        i = 0 # for LEFT 
        j = 0 # for RIGHT 
        
        # 
        k = 0
        
        while i < len(left) and j < len(right):
            # Смотрим кто у нас будет первым идти, если элемент левого <= правого, то мы закинем его в основной lst 
            if left[i] <= right[j]:
              # Поставили в lst новый элемент
              lst[k] = left[i]
              # Указатель двигается на 1 позицию ==>
              i += 1
              # Но если правая часть >= левой, то в lst кидаем из правой части
            else:
                lst[k] = right[j]
                # Указатель двигается на 1 позицию ==>
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k]=right[j]
            j += 1
            k += 1

mergeSort(lst)
print(lst)
