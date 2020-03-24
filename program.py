from __future__ import print_function
from ortools.linear_solver import pywraplp


def main():
    solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    infinity = solver.infinity()

    x1 = solver.NumVar(0, infinity, 'x1')
    x2 = solver.NumVar(0, infinity, 'x2')
    x3 = solver.NumVar(0, infinity, 'x3')


    solver.Add(15 * x1 + 10 * x2 + 4 * x3 <= 80)
    solver.Add(15 * x1 + 12 * x2 + 5 * x3 <= 120)
    solver.Add(7 * x1 + 21 * x2 + 3 * x3 <= 84)

    solver.Maximize(20 * x1 + 15 * x2 + 18 * x3)

    solver.Solve()

    print('Solution:')
    print('Objective value =', solver.Objective().Value())
    print('x1 =', x1.solution_value())
    print('X2 =', x2.solution_value())
    print('X3 =', x3.solution_value())


if __name__ == '__main__':
    main()