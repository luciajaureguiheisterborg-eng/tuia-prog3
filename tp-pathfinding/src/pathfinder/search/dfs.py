from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        if grid.objective_test(root.state):
            return Solution(root)
        
        frontera= StackFrontier()
        frontera.add(root)
        

        # Initialize explored with the initial state
        expandidos = {}
        while True:
            if frontera.is_empty():
                return NoSolution(expandidos)
            nodo= frontera.remove()
            if nodo.state in expandidos:
                continue 
            expandidos[nodo.state] = True
          
            for accion in grid.actions(nodo.state):
                nuevo_estado=grid.result(nodo.state,accion)
                if nuevo_estado not in expandidos:
                    nodo_hijo=Node("",nuevo_estado,nodo.cost + grid.individual_cost(nodo.state,accion), nodo,accion)
                    if grid.objective_test(nuevo_estado):
                        return Solution(nodo_hijo,expandidos)
                    frontera.add(nodo_hijo)


        # Initialize frontier with the root node
        # TODO Complete the rest!!
        # ...
