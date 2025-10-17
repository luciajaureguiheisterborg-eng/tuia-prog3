from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        if grid.objective_test(root.state):
            return Solution(root)
        
        frontera= QueueFrontier()
        frontera.add(root)
        

        # Initialize explored with the initial state
        alcanzados = {}
        alcanzados[root.state] = True
        while True:
            if frontera.is_empty():
                return NoSolution(alcanzados)
            nodo= frontera.remove()
          
            for accion in grid.actions(nodo.state):
                nuevo_estado=grid.result(nodo.state,accion)
                if nuevo_estado not in alcanzados:
                    nodo_hijo = Node("",nuevo_estado, parent=nodo, action=accion, cost=nodo.cost + grid.individual_cost(nodo.state, accion))
                    if grid.objective_test(nuevo_estado):
                        return Solution(nodo_hijo,alcanzados)
                    alcanzados[nuevo_estado]=True
                    frontera.add(nodo_hijo)