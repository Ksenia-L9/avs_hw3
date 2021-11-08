import sys
import random
from container import Container

# проверка количества аргументов командной строки
if len(sys.argv) != 3:
    print("Incorrect command line\n")
    sys.exit(1)

# открытие файлового потока с входными данными
try:
    input_file = open(sys.argv[1], "r")
except:
    print("Cannot access file\n")
    sys.exit(1)

# открытие файлового потока для записи выходных данных
try:
    output_file = open(sys.argv[2], "w")
except:
    print("Cannot access file\n")
    sys.exit(1)

# проверка формата количества элементов контейнера
try:
    container_length = int(input_file.readline())
except:
    print("Incorrect format of container size")
    sys.exit(1)

if container_length > Container.MAX_CAPACITY or container_length <= 0:
    print("Invalid container size\n")
    sys.exit(1)

# создание контейнера
container = Container()
if container_length >= 20:
    # заполнение контейнера случайными величинами
    random.seed()
    container.rand_fill(container_length)
else:
    # заполнение контейнера из файла
    if not container.fill_from_file(container_length, input_file):
        sys.exit(1)

# вывод исходного контейнера в файл
container.print(output_file)

# сортировка контейнера
container.sort()
# вывод отсортированного контейнера в файл
output_file.writelines("\nSorted:\n")
container.print(output_file)

# закрытие файловых потоков
output_file.close()
input_file.close()