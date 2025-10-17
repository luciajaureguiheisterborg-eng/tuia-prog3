from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)
        
        frontera= PriorityQueueFrontier()
        
        frontera.add(root,root.cost)
        alcanzados = {}
        alcanzados[root.state]=root.cost

        while True:
        
            if frontera.is_empty():
                return NoSolution(alcanzados)
            nodo= frontera.pop()
          
            if grid.objective_test(nodo.state):
             return Solution(nodo, alcanzados)
        
            for accion in grid.actions(nodo.state):
                nuevo_estado=grid.result(nodo.state,accion)
                costo=nodo.cost + grid.individual_cost(nodo.state,accion)
                if nuevo_estado not in alcanzados or costo < alcanzados[nuevo_estado]:
                    nodo_hijo = Node("",nuevo_estado, cost=costo,parent=nodo, action=accion)
                    alcanzados[nuevo_estado]=costo
                    frontera.add(nodo_hijo,costo)
