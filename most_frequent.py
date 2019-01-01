# Implement most frequent item in a list
def most_frequent(given_list):
    max_count = -1
    max_item = None
    count = {}      # dictionary, at ith key of count assign value
    for i in given_list:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

        if count[i] > max_count:
            max_count = count[i]
            max_item = i
    return max_item

list1 = [1, 3, 1, 3, 2, 1]

print most_frequent(list1)

list2 = [3, 3, 1, 3, 2, 1]

print most_frequent(list2)

list3 = []

print most_frequent(list3)

list4 = [0]

print most_frequent(list4)

list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

print most_frequent(list5)
