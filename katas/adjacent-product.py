def adjacentElementsProduct(array):
    product = [int1 * int2 for int1, int2 in zip(array, array[1:])]
    print(max(products))


a = [3, 6, -2, -5, 7, 3]
adjacentElementsProduct(a)
