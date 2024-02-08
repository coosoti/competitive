if __name__ == '__main__':

    N = int(input())
    
    students = []
    
    for _ in range(N):
        name = input()
        score = float(input())
        students.append([name, score])
    
    students.sort(key=lambda x: x[1])
    
    unique_grades = sorted(set(score for name, score in students))
    second_lowest_grade = unique_grades[1]
    
    second_lowest_students = [name for name, score in students if score == second_lowest_grade]
    
    for name in sorted(second_lowest_students):
        print(name)
