# Part 1
def read_csv(filename : str):
    """
    Reads CSV data stored in a file

    Parameters
    ---------
    filename : str
        file containing CSV data to be read
    
    Returns
    ---------
    list, nested list
        a list of headers/column labels
        a nested list of data

    Example:
    >>> read_csv(pre-u-enrolment-by-age.csv)
    ["year", "age", "sex", "enrolment-jc"], [[1984, "17 YRS", "MF", 8710], [1984, "17 YRS", "F", 4960], ...]
    
    """

    with open (filename, "r") as file:
        header = file.readline().replace("\n", "").split(",")
        datas = file.readlines()
        data = []
        for row in datas:
            row = row.replace("\n", "").split(",")
            for word in row:
                if word.isdigit():
                    row[row.index(word)] = int(word)
            data.append(row)
            
        return header, data
        #f.close() is called automatically


# Part 2
def filter_gender(enrolment_by_age, sex):
    """
    Filters gender out and returns list without gender

    Parameters
    ---------
    enrolment_by_age : list
        a list of data
    sex : str
        gender to filter

    Returns
    ---------
    nested list
        a nested list of data excluding gender

    Example:
    >>> mf_enrolment = filter_gender(enrolment_data, "MF")
    >>> mf_enrolment
    [[1984, '17 YRS', 8710],
     [1984, '18 YRS', 3927],
     [...],
     [...],
     ...]
    """
    new_data = []
    for row in enrolment_by_age:
        if(sex in row):
            row.remove(sex)
            new_data.append(row)

    return new_data


# Part 3
def sum_by_year(enrolment):
    """
    Adds up the total enrolment by year

    Parameters
    ---------
    enrolment : list
        data of enrolment

    Returns
    ---------
    nested list
        a nested list of data containing year and total enrolment for that year

    Example:
    >>> enrolment_by_year = sum_by_year(mf_enrolment)
    >>> enrolment_by_year
    [[1984, 21471],
     [1985, 24699],
     [...],
     [...],
     ...]
    """

    new_data = []
    year_list = []
    years = []
    enrolment_amount = 0
    for row in range(len(enrolment)):
        year = enrolment[row][0]    
        if year in years:
            if row + 1 != len(enrolment):
                if (year == enrolment[row + 1][0]):
                    enrolment_amount = enrolment_amount + enrolment[row][len(enrolment[row])-1]
                elif year != enrolment[row + 1][0]:
                    enrolment_amount = enrolment_amount + enrolment[row][len(enrolment[row])-1]
                    year_list.append(enrolment_amount)
                    new_data.append(year_list)
                    year_list = []
            else:
                enrolment_amount = enrolment_amount + enrolment[row][len(enrolment[row])-1]
                year_list.append(enrolment_amount)
                new_data.append(year_list)
                year_list = []
        else:
            year_list.append(year)
            years.append(year)
            enrolment_amount = enrolment[row][len(enrolment[row])-1]
            
    return new_data


# Part 4
def write_csv(filename, header, data):
    """
    Writes header and data to file

    Parameters
    ---------
    filename : str
        name of file
    header : list
        list of headers to write
    data : list
        list of data to write

    Returns
    ---------
    integer
        integer of lines written in file

    Example:
    >>> filename = 'total-enrolment-by-year.csv'
    >>> header = ["year", "total_enrolment"]
    >>> write_csv(filename, header, enrolment_by_year)
    35
    """
    lines_written = 0
    with open (filename, "w") as file:
        new_header = ",".join(header)
        file.write(new_header + "\n")
        lines_written = lines_written + 1
        #f.close() is called automatically
    with open (filename, "a") as file:
        for year in data:
            for i in range(len(year)):
                year[i] = str(year[i])
            line = ",".join(year)
            file.writelines(line + "\n")
            lines_written = lines_written + 1

        #f.close() is called automatically

    return lines_written


# TESTING
# You can write code below to call the above functions
# and test the output

header, enrolment = read_csv("pre-u-enrolment-by-age.csv")
mf_enrolment = filter_gender(enrolment, "MF")
sum_by_year(mf_enrolment)