import csv

# -------- Copy rows from one file to another -------------

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     with open('new_names.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file)

#         for line in csv_reader:
#             csv_writer.writerow(line)


# ------ Append a row ---------------------

# with open('new_names.csv', 'a') as new_row:
#     csv_row = csv.writer(new_row)

#     csv_row.writerow(['Ruben', 'van der Wolf', 'r.vanderwolf@gmail.com'])


# ------- Read csv file and print specific column -------

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line['email'])


with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
