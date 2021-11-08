from random import randint, uniform
from matrix import *


class DiagonalMatrix(Matrix):
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
        for i in range(self.__rows):
            data = input_stream.readline().split()
            if len(data) != self.__rows:
                print("Incorrect matrix content\n")
                return False
            for j in range(self.__columns):
                try:
                    self.__matrix.append(float(data[j]))
                except:
                    print("Incorrect format of matrix content\n")
                    return False
        return True

    # генерация матрицы случайных значений
    def rand_fill(self):
        self.__rows = self.__columns = randint(1, 15)
        for i in range(self.__rows * self.__columns):
            if i % self.__columns == i / self.__rows:
                self.__matrix.append(uniform(-100, 100))
            else:
                self.__matrix.append(0)

    # запись матрицы в файл
    def print(self, output_stream):
        i = 0
        while i < self.__rows * self.__columns:
            for j in range(self.__columns):
                output_stream.write("{:.2f} ".format(self.__matrix[i]))
                i += 1
            output_stream.write("\n")

    # функция возвращает  среднее арифметическое матрицы
    def average(self):
        sum = 0
        for i in range(self.__rows * self.__columns):
            sum += self.__matrix[i]
        return sum / (self.__rows * self.__columns)
