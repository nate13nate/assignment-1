import sys

def getLetterGrade(percentage: float) -> str:
    if percentage >= .9: return 'A'
    if percentage >= .8: return 'B'
    if percentage >= .7: return 'C'
    if percentage >= .6: return 'D'
    return 'F'

if len(sys.argv) < 2:
    print('Error: required command line argument not provided')
else:
    print(getLetterGrade(float(sys.argv[1])))
