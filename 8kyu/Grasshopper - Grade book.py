'''
Description

Grade book
Complete the function so that it finds the average of the three scores passed to it and returns the letter value 
associated with that grade.

Numerical Score	Letter Grade
90 <= score <= 100	'A'
80 <= score < 90	'B'
70 <= score < 80	'C'
60 <= score < 70	'D'
0 <= score < 60	'F'

Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
'''

def get_grade(s1, s2, s3):
    score = (s1 + s2 + s3) / 3
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    return 'F'