def main():
    studentFile = 'input.txt'
    resultFile = 'output.txt'
    stu = {}
    with open(studenFile, 'r') as file:
        for line in file:
            name, unit, mark, weight = line.strip().split(', ')
            mark, weight = float(mark), float(weight)
            if name not in stu:
                stu[name] = []
            stu[name].append((mark, weight))
    with open(resultFile, 'w') as file:
        for name, marks_weights in stu.items():
            total_marks = sum(mark * (weight / 100) for mark, weight in markWeights)
            if totaMarks >= 70:
                grade = "Distinction"
            elif totalMarks >= 60:
                grade = "Merit"
            elif totalMarks >= 50:
                grade = "Pass"
            else:
                grade = "Fail"
            file.write("{name}, {total_marks:.1f}, {grade}\n".format)
if __name__ == "__main__":
    main

