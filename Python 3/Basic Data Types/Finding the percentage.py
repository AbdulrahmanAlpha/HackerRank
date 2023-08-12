# function
def StudentAverage(StudentMarks,QueryName):
    for key,value in StudentMarks.items():
        if key == QueryName:
            average_score = sum(value)/len(value)
    print('{:.2f}'.format(average_score))    



# main 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    StudentAverage(student_marks,query_name)
