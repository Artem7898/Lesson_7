"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""

from timeit import default_timer as timer

start = timer()

def shellSort(m):
    sublistcount = len(m)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(m,startposition,sublistcount)

      print('После увеличения размера',sublistcount,
                                   'Список',m)

      sublistcount = sublistcount // 2

def gapInsertionSort(m,start,gap):
    for i in range(start+gap,len(m),gap):

        currentvalue = m[i]
        position = i

        while position>=gap and m[position-gap]>currentvalue:
            m[position]=m[position-gap]
            position = position-gap

        m[position]=currentvalue

m = [10, 45, 35, 47, 50, 20, 25, 55, 15]
shellSort(m)
print(m)
print('----------------------------------------------------------------------')
print('Сортировка Шелла')
end = timer()
print(end - start)
