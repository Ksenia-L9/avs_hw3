from random import randint, uniform
from matrix import *


class SquareMatrix(Matrix):
    def __init__(self):
        self.__rows = 0
        self.__columns = 0
        self.__matrix = []

    # заполнение матрицы значениями из файла
    def fill_from_file(self, input_stream):
        param_string = input_stream.readline().split()
        if len(param_string) != 2:
            print("Incorrect format of matrix params\n")
            return False
        try:
            self.__rows = int(param_string[0])
            self.__columns = int(param_string[1])
        except:
            print("Incorrect format of matrix params\n")
            return False
        if self.__rows != self.__columns or self.__rows <= 0 or self.__columns <= 0:
            print("Incorrect number of rows/columns\n")
            return False
        self.__matrix = []
        for i in range(self.__rows):
            data = input_stream.readline().split()
            if len(data) != self.__rows:
                print("Incorrect matrix content\n")
                return False
            for j in range(self.__columns):
                try:
                    data[j] = float(data[j])
                except:
                    print("Incorrect format of matrix content\n")
                    return False
            self.__matrix.append(data)
        return True

    # генерация матрицы случайных значений
    def rand_fill(self):
        self.__rows = randint(1, 15)
        self.__columns = randint(1, 15)
        for i in range(self.__rows):
            row = []
            for j in range(self.__columns):
                row.append(uniform(-1000, 1000))
            self.__matrix.append(row)

    # запись матрицы в файл
    def print(self, output_stream):
        for i in range(self.__rows):
            for j in range(self.__columns):
                output_stream.write("{:.2f} ".format(self.__matrix[i][j]))
            output_stream.write("\n")

    # функция возвращает  среднее арифметическое матрицы
    def average(self):
        sum = 0
        for i in range(self.__rows):
            for j in range(self.__columns):
                sum += self.__matrix[i][j]
        return sum / (self.__rows * self.__columns)
