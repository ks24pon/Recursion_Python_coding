# Studentクラス
class Student:
    def __init__(self,studentId, firstName, lastName, gradeLevel):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.gradeLevel = gradeLevel

    # 生徒の情報を「識別番号：フルネーム(学年)」として返す
    def getStudentInfo(self):
        return self.studentId+": "+self.firstName+" "+self.lastName+"("+str(self.gradeLevel)+"gr)"




# Classroomクラス
class Classroom:
    def __init__(self, students, courseName, teacher):
        self.students = students
        self.courseName = courseName
        self.teacher = teacher

    # 教室の情報を「科目名managed by 教員名」として返す
    def getClassIdentity(self):
        print(self.courseName+" managed by "+self.teacher)

    # 生徒の数
    def getNumberOfStudents(self):
        print(len(self.students))

def printHonorsStudents(school):
    # schoolはClassroomインスタンスのリスト
    for classroom in school:
        for student in classroom.students:
            # 10以上の場合、成績優秀者
            if student.gradeLevel >= 10:
                print(
                    student.getStudentInfo() + " from " + classroom.teacher + "'s class"
                )

# Classroomのインスタンス作成
classroom1 = Classroom(
    [   # 1つ目のクラスに所属する生徒
        Student("AC-343424", "James", "Smith", 6),
        Student("AC-343428", "Maria", "Garcia", 5),
        Student("AC-343434", "Robert", "Johnson", 3),
        Student("AC-343454","Danny", "Robertson",10)
    ],
    "Algebra II",
    "Emily Theodore"
)

classroom2 = Classroom(
    [
        Student("AC-340014","Kent", "Carter",9),
        Student("AC-340024","Isaiah", "Chambers",10),
        Student("AC-340018","Leta", "Ferguson", 7)
    ],
    "English",
    "Daniel Pherb"
)

school = [classroom1, classroom2]
printHonorsStudents(school)
