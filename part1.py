import sys

from part1a import main as part1a
from part1b import main as part1b

def main(string: str, num1: float, num2: float):
    aOutput = part1a(string)
    bOutput = part1b(num1, num2)

    print(f'Part 1a output: "{aOutput}"\n')
    print(
        'Part 1b output:\n' +
       f'  add: {bOutput["add"]}\n' +
       f'  sub: {bOutput["sub"]}\n' +
       f'  mult: {bOutput["mult"]}\n' +
       f'  div: {bOutput["div"]}'
    )

if len(sys.argv) > 3:
    main(sys.argv[1], float(sys.argv[2]), float(sys.argv[3]))
else:
    print('Error: Please provide the required command line arguments.')
