# Insertion sort array in Python
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        # Bandingkan kunci dengan setiap elemen di sebelah kirinya hingga elemen yang lebih kecil darinya ditemukan
        # Untuk urutan menurun, ubah key<array[j] menjadi key>array[j].       
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Tempatkan kunci setelah elemen hanya lebih kecil darinya.
        array[j + 1] = key
        
data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)