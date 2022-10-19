# goal = add 3 arguments using argparse command, and return the arguments in a list

import argparse
import csv
from rich.console import Console
from rich.table import Table

# create parser 'container'
parser = argparse.ArgumentParser(description='Print full name')

# add arguments
parser.add_argument('-f', '--first', type=str, metavar='',
                    required=True, help='First Name')
parser.add_argument('-m', '--middle', type=str, metavar='',
                    required=True, help='Middle Name')
parser.add_argument('-l', '--last', type=str, metavar='',
                    required=True, help='Last Name')
parser.add_argument(
    '-o', '--output', help='Output result to a csv file', action='store_true')
parser.add_argument(
    '-t', '--table', help='Print a table of all rows in csv file', action='store_true')

# parse arguments
args = parser.parse_args()


# print name in terminal
def print_name(first, middle, last):
    return f'{first} {middle} {last}'


if __name__ == '__main__':
    full_name = print_name(args.first, args.middle, args.last)
    print(full_name)
    if args.output:
        with open('full_name.csv', 'a') as new_name:
            csv_row = csv.writer(new_name)
            csv_row.writerow([full_name])
    if args.table:
        table = Table(title='Full Name')

        table.add_column("First Name", justify="center", style="cyan")
        table.add_column("Middle Name", justify="center", style="magenta")
        table.add_column("Last Name", justify="center", style="green")

        with open('full_name.csv', 'r') as file:
            reader = csv.reader(file)

            for row in reader:
                column_1 = str(row[0])
                column_2 = str(row[1])
                column_3 = str(row[2])
                table.add_row(column_1, column_2, column_3)

        console = Console()
        console.print(table)
