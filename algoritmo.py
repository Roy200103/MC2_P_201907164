from collections import defaultdict
from heapq import *




def prim(vertexs, edges,start='D'):
    adjacent_dict = defaultdict(list) # NOTA: DEFAULTEDDICT (LISTA) DEBE SER VARIABLES EN LA LISTA
    for weight,v1, v2 in edges:
        adjacent_dict[v1].append((weight, v1, v2))
        adjacent_dict[v2].append((weight, v2, v1))
    '''
         Después de la operación anterior, la gráfica se convierte en la siguiente forma adyacente:
    {'A': [(7, 'A', 'B'), (5, 'A', 'D')], 
     'C': [(8, 'C', 'B'), (5, 'C', 'E')], 
     'B': [(7, 'B', 'A'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E')], 
     'E': [(7, 'E', 'B'), (5, 'E', 'C'), (15, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G')], 
     'D': [(5, 'D', 'A'), (9, 'D', 'B'), (15, 'D', 'E'), (6, 'D', 'F')], 
     'G': [(9, 'G', 'E'), (11, 'G', 'F')], 
     'F': [(6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G')]})
    '''
    minu_tree = []  # Resultado de árbol de almacenamiento generado mínimo
    visited = [start] #Seleccione los vértices a los que se accede, preste atención al punto de inicio especificado
    adjacent_vertexs_edges = adjacent_dict[start]
    heapify(adjacent_vertexs_edges) # Traducir en pilas pequeñas, fácil de encontrar el peso más pequeño
    while adjacent_vertexs_edges:
        weight, v1, v2 = heappop(adjacent_vertexs_edges) # El lado más pequeño y retírelo del montón. 
        if v2 not in visited:
            visited.append(v2)  # Hay un primer punto seleccionado 'A' en el utilizado, y se obtiene el punto más cercano 'D' del punto de un punto, y el ejemplo es 5. Añadir 'd' a los usados
            minu_tree.append((weight, v1, v2))
            #On y encuentre puntos adyacentes a D, si no en montón, aplique Malleza para presionar la pila para unirse a la fila de clasificación
            for next_edge in adjacent_dict[v2]: # Encuentra el borde de v2 adyacente
                if next_edge[2] not in visited: # Si no se ha accedido a V2, agregue el montón
                    heappush(adjacent_vertexs_edges, next_edge)
    return minu_tree




#vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H']
#edges = [(7, 'A', 'B'),
#         (5, 'A', 'D'),
#         (8, 'B', 'C'),
#         (9, 'B', 'D'),
#         (7, 'B', 'E'),
#         (5, 'C', 'E'),
#         (15, 'D', 'E'),
#         (6, 'D', 'F'),
#         (8, 'E', 'F'),
#         (9, 'E', 'G'),
#         (11, 'F', 'G'),
#         (3, 'B', 'H'),
#         ]


