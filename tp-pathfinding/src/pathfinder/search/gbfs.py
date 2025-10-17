from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def heuristica(grid: Grid, nodo_c:Node):
    eje_x, eje_y = nodo_c.state
    eje_x_obj, eje_y_obj = grid.end
    return abs(eje_x_obj - eje_x) + abs(eje_y_obj - eje_y)


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        frontera = PriorityQueueFrontier()
        frontera.add(root, heuristica(grid, root)) #ver

        # Initialize reached with the initial state
        alcanzados = {}
        alcanzados[root.state] = root.cost

        while True:
            if frontera.is_empty():
                return NoSolution(alcanzados)
            nodo = frontera.pop()
            if grid.objective_test(nodo.state):
                return Solution(nodo, alcanzados)
            for accion in grid.actions(nodo.state):
                nuevo_estado=grid.result(nodo.state, accion)
                costo = nodo.cost + grid.individual_cost(nodo.state, accion)
                if nuevo_estado not in alcanzados or costo < alcanzados[nuevo_estado]:
                    nuevo_nodo = Node("", state=nuevo_estado, cost=costo, parent=nodo, action=accion)
                    alcanzados[nuevo_estado] = costo
                    frontera.add(nuevo_nodo, heuristica(grid, nuevo_nodo))
            

        
