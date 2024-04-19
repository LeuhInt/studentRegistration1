def degreeList():
    degrees = {
        1: ['Computer Science', 3200],
        2: ['Software Engineering', 3500],
        3: ['System Information Technology', 3100]
    }
    return degrees


def courseList():
    courses = {
        1: ['Maths I', 1, 'no requisites', 60, 'John', 'Bloco I sala 10'],
        2: ['Maths II', 1, 'Maths I', 60, 'Mary', 'Bloco I sala 12'],
        3: ['Programming Languages I', 1, 'no requisites', 60, 'Joseph', 'Bloco I sala 13'],
        4: ['Programming Languages II', 2, 'Programming Languages I', 60, 'Stuart', 'Bloco II sala 10'],
        5: ['Software Engineering I', 1, 'no requisites', 60, 'Max', 'Bloco II sala 15'],
        6: ['Software Engineering II', 2, 'Software Engineering I', 60, 'John', 'Bloco I sala 5'],
        7: ['Hardware Engineering I', 1, 'no requisites', 60, 'Ellis', 'Bloco II sala 14'],
        8: ['Hardware Engineering II', 2, 'Hardware Engineering I', 60, 'Clair', 'Bloco III sala 9'],
    }
    return courses


def printFormat(data):
    for key, value in data.items():
        print(f'{key}: Degree: {value[0]}, Duration: {value[1]}')


