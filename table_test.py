from rich.console import Console
from rich.table import Table
import csv

table = Table(title='Names and email')

table.add_column("First Name", justify="center", style="cyan")
table.add_column("Last Name", justify="center", style="magenta")
table.add_column("E-mail address", justify="center", style="green")

with open('new_names.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        column_1 = str(row[0])
        column_2 = str(row[1])
        column_3 = str(row[2])
        table.add_row(column_1, column_2, column_3)

console = Console()
console.print(table)
