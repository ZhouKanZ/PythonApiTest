def insert_sort(lists):
    count = len(lists)
    for i in range(1,count):
        key = lists[i]
        j = i-1
        while j>=0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists = key
            j -=1

    return lists






