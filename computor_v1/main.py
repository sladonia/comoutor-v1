import click

from computor_v1.polynom import Equation, Solver
from computor_v1.polynom import InputError


@click.command()
@click.argument('equation_str')
@click.option('-f', '--filename', default=None)
def run(filename, equation_str):
    """
    cli tool that solves simple polynomial equations
    """
    equation = Equation(equation_str)
    try:
        equation.validate_equation()
        equation.parse_equation()
    except InputError as e:
        print(str(e))
        exit(0)
    equation.print_info()
    if not equation.validare_polynomial_degree():
        exit(0)
    solver = Solver(equation.equation)


if __name__ == '__main__':
    run()
