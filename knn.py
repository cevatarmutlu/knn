import xlrd
import math
import numpy
from xlwt import Workbook


def open_excel(path: str, sheet_index: int):
    wb = xlrd.open_workbook(path)
    return wb.sheet_by_index(sheet_index)


def write_excel(name, array, tag=[]):
    wb = Workbook()
    sheet = wb.add_sheet(name)
    for i in range(len(array)):
        if len(tag) == 0:
            row = dataset.row_values(array[i])
        else:
            row = dataset.row_values(array[i])[0:tag_index]
            row = row + [tags[i]]
        for j in range(len(row)):
            sheet.write(i, j, row[j])
    wb.save(name + '.xlsx')


def config_sets(dataset):
    fun_training = []
    fun_test = []
    for i in range(dataset.nrows):
        if i % 5 == 0:
            fun_test.append(i)
        else:
            fun_training.append(i)
    return fun_training, fun_test


def str_to_float(array):
    return list(map(float, array))


def get_row(set, index, str_value=False):
    row = dataset.row_values(set[index])[0:tag_index]
    if str_value:
        return row
    else:
        return str_to_float(row)


def euclidean(row_training, row_test):
    return math.sqrt(sum([pow(x[0] - x[1], 2) for x in zip(row_training, row_test)]))


def calculate_distance(training_set, test_row):
    distances = []
    for i in range(len(training_set)):
        distance = euclidean(get_row(training_set, i), test_row)
        distances.append(distance)
    return distances


def find_min_k_value(k, array):
    temp_array = array.copy()
    temp_array = sorted(temp_array)
    temp_array = temp_array[0:k]
    min_values = [array.index(temp_array[x]) for x in range(k)]
    return min_values


def weighted(min_values_array):
    tags = [dataset.row_values(min_values_array[x])[tag_index] for x in range(len(min_values_array))]
    tags_values = {}
    for i in range(len(tags)):
        tag_name = tags[0]
        count = tags.count(tag_name)
        for j in range(count):
            tags.remove(tag_name)
        tags_values.update({tag_name: count})
        if len(tags) == 0:
            break
    max_index = numpy.argmax(list(tags_values.values()))
    return list(tags_values.keys())[max_index]


def find_tag():
    tags = []
    for i in range(len(test)):
        distance_array = calculate_distance(training, get_row(test, i))
        min_k_rows_array = find_min_k_value(k, distance_array)
        tag = weighted(min_k_rows_array)
        tags.append(tag)
    return tags


def error_percentage():
    error_tag = 0
    for i in range(len(test)):
        print(dataset.row_values(test[i])[tag_index], tags[i])
        test_tag = dataset.row_values(test[i])[tag_index]
        tag = tags[i]
        if test_tag != tag:
            error_tag += 1
    print(error_tag / len(test) * 100)


if __name__ == "__main__":
    
    excel_path = 'iris.xlsx'
    sheet_index = 0

    k = 3
    # k = int(input('k değerini giriniz'))

    dataset = open_excel(excel_path, sheet_index)

    tag_index = dataset.ncols - 1  # Etiketin hangi indiste bulunduğunu belirtiyoruz

    training, test = config_sets(dataset)
    tags = find_tag()

    write_excel("training", training)
    write_excel("test", test)
    write_excel("result", test, tags)

    error_percentage()



