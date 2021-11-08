import square_matrix
import diagonal_matrix
import triangle_matrix
from random import randint


class Container:
    # максимальное количество элементов контейнера
    MAX_CAPACITY = 10000

    def __init__(self):
        self.__matrices = []

    # расчёт среденго арифметического для всего контейнера
    def average(self):
        sum_matrix_average = 0.
        for i in range(len(self.__matrices)):
            sum_matrix_average += self.__matrices[i].average()
        return sum_matrix_average / len(self.__matrices)

    # сортировка по среднему арифметическому
    def sort(self):
        average = self.average()
        iterator = 0
        for i in range(len(self.__matrices) - iterator):
            if self.__matrices[i].average() > average:
                iterator += 1
                for j in range(len(self.__matrices) - 1):
                    tmp = self.__matrices[j]
                    self.__matrices[j] = self.__matrices[j + 1]
                    self.__matrices[j + 1] = tmp
                i -= 1

    # заполнение контейнера матрицами из файла
    def fill_from_file(self, length, input_stream):
        for i in range(length):
            try:
                type_of_matrix = int(input_stream.readline())
            except:
                print("Incorrect format of matrix type\n")
            if type_of_matrix == 1:
                matrix = square_matrix.SquareMatrix()
            elif type_of_matrix == 2:
                matrix = diagonal_matrix.DiagonalMatrix()
            elif type_of_matrix == 3:
                matrix = triangle_matrix.TriangleMatrix()
            else:
                print("Incorrect matrix type\n")
                return False
            if not matrix.fill_from_file(input_stream):
                return False
            self.__matrices.append(matrix)
        return True

    # заполнение контейнера матрицами случайных значений
    def rand_fill(self, number_of_elements):
        for i in range(number_of_elements):
            type_of_matrix = randint(1, 3)
            if type_of_matrix == 1:
                matrix = square_matrix.SquareMatrix()
            elif type_of_matrix == 2:
                matrix = diagonal_matrix.DiagonalMatrix()
            else:
                matrix = triangle_matrix.TriangleMatrix()
            matrix.rand_fill()
            self.__matrices.append(matrix)

    # запись контейнера в файл
    def print(self, output_stream):
        output_stream.write("Total number of matrices in Container: {}\n".format(len(self.__matrices)))
        for matrix in self.__matrices:
            matrix.print(output_stream)
            output_stream.write("\n")
        pass
