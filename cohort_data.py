def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called 'houses' that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army",
                    "Order of the Phoenix"
            ])

    """
    cohort_file = open(filename)
    houses = set()  #create empty set
    for line in cohort_file:
        new_line = line.strip("\n")
        new_line = new_line.split("|")
        if new_line[2] != "":  # as long as it's not empty
            houses.add(new_line[2])  #add to houses set 

    cohort_file.close()
    return houses


def sort_by_cohort(filename):
    """TODO: Sort students by cohort.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name and tas separately. Returns list of lists.

        ex. winter_15 = ["alice tsao", "amanda gilmore", "anne vetto", "..." ]
        ex. all_students = [winter_15, spring_15, summer_15, tas]

    """
    cohort_file = open(filename)
    all_students = []
    winter_15 = []
    spring_15 = []
    summer_15 = []
    tas = []
    for line in cohort_file:
        new_line = line.strip("\n")
        new_line = line.split("|")
        if new_line[-1] == "Winter 2015":
            winter_15.append(new_line[:2])
        elif new_line[-1] == "Spring 2015":
            spring_15.append(new_line[:2])
        elif new_line[-1] == "Summer 2015":
            summer_15.append(new_line[:2])
        elif new_line[-1] == "TA":
            tas.append(new_line[:2])
    all_students.append(winter_15)
    all_students.append(spring_15)
    all_students.append(summer_15)
    all_students.append(tas)
    cohort_file.close()
    return all_students


def students_by_house(filename):
    """TODO: Sort students by house.

    Iterate over the data to create a list for each house, and sort students
    into their appropriate houses by last name. Sort TAs into a list called "tas"
    and instructors in to a list called "instructors".
    Return all lists in one list of lists.
        ex. hufflepuff = ["Gaikwad", "Le", "..." ]
        ex. tas = ["Bryant", "Lefevre", "..."]
        ex. all_students = [ hufflepuff,
                        gryffindor,
                        ravenclaw,
                        slytherin,
                        dumbledores_army,
                        order_of_the_phoenix,
                        tas,
                        instructors
            ]
    """

    cohort_file = open(filename)
    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    order_of_the_phoenix = []
    ravenclaw = []
    tas = []
    instructors = []

    for line in cohort_file:
        new_line = line.strip("\n")
        new_line = new_line.split("|")
        if new_line[1] == "Gryffindor":
            gryffindor.append(new_line[1])
        elif new_line[1] == "Hufflepuff":
            hufflepuff.append(new_line[1])
        elif new_line[1] == "Slytherin":
            hufflepuff.append(new_line[1])
        elif new_line[1] == "Dumbledore's Army":
            dumbledores_army.append(new_line[1])
        elif new_line[1] == "Order of the Phoenix":
            order_of_the_phoenix.append(new_line[1])
        elif new_line[1] == "Ravenclaw":
            ravenclaw.append(new_line[1])
        elif new_line[-1] == "TA":
            tas.append(new_line[1])
        elif new_line[-1] == "I":
            instructors.append(new_line[1])
    all_students.append(gryffindor)
    all_students.append(hufflepuff)
    all_students.append(slytherin)
    all_students.append(dumbledores_army)
    all_students.append(order_of_the_phoenix)
    all_students.append(ravenclaw)
    all_students.append(tas)
    all_students.append(instructors)

    cohort_file.close()
    return all_students

def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. all_people = [
                ("Alice Tsao", "Slytherin", "Kristen", "Winter 2015"),
                ("Amanda Gilmore", "Hufflepuff", "Meggie", "Winter 2015"),
                # ...
            ]
    """

    student_list = []
    cohort_file = open(filename)
    for line in cohort_file:
        new_line = line.strip("\n")
        new_line = new_line.split("|")
        if (new_line[-1] != 'TA') and (new_line[-1] != 'I'):
            first_last_name = new_line[0] + ' ' + new_line[1]
            del new_line[0]
            new_line[0] = first_last_name
            student_list.append(tuple(new_line))
    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Use the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name, returns that student's cohort, or returns
    'Student not found.' when appropriate. """

    user_input = raw_input("Enter a Hackbright student's first and last name ")
    user_input.rstrip()
    for student_data in student_list:
        if user_input in student_data:
            return student_data
    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student first names that have duplicates.

    Iterates over the data to find any first names that exist across multiple cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Sarah"])

    """

    duplicate_names = set()
    winter_15 = set()
    spring_15 = set()
    summer_15 = set()

    cohort_data = open(filename)
    for line in cohort_data:
        line.strip("\n")
        line = line.split("|")
        if 'Winter' in line[-1]: 
          winter_15.add(line[0])
        elif 'Spring' in line[-1]:
          spring_15.add(line[0])
        elif 'Summer' in line[-1]:
          summer_15.add(line[0])
    duplicate_names = winter_15 & spring_15 & summer_15
    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Use the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student's house."""

    # Code goes here
    student_input = raw_input("Input a Hackbright student name: first and last ")
    students_in_the_same_house = []
    student_house_name = ''
    student_cohort_time = ''
    for student_data in student_list: 
        # Loop through the list to get tuples
        if student_input in student_data:
            student_house_name = student_data[1]
            student_cohort_time = student_data[-1]

    for student_data in student_list:
        if student_house_name != '' and student_cohort_time != '':
          if (student_house_name in student_data) and \
              (student_cohort_time in student_data):
            students_in_the_same_house.append((student_data[0], \
                student_data[1], student_data[-1]))

    return students_in_the_same_house


#########################################################################################

# Here is some useful code to run these functions!

print unique_houses("cohort_data.txt")
print sort_by_cohort("cohort_data.txt")
students_by_house("cohort_data.txt")
all_students_data = all_students_tuple_list("cohort_data.txt")
print all_students_data
find_cohort_by_student_name(all_students_data)
print find_name_duplicates("cohort_data.txt")
find_house_members_by_student_name(all_students_data)
