import csv


with open('graphtest1.txt', 'r') as csv_file:
    file_handle = csv.reader(csv_file)
    data = next(file_handle)

number_of_vertices = int(data[0])
graph = [[0 for i in range(number_of_vertices)] for j in range(number_of_vertices)]
edges = []
k = 0

for i in range(0, number_of_vertices):
    for j in range(0, number_of_vertices):
        k += 1
        graph[i][j] = int(data[k])
        if int(data[k]) != 0:
            edges.append((int(data[k]), i, j))

edges.sort()


def print_matrix(g):
    for row in g:
        print(row)


print_matrix(graph)
