import pandas as pd
from Student.models import Student

def main():
    df = pd.read_csv('student-info.csv')
    # print(df['Student Name'][0])

    for i in range(len(df)):
        # print(df['Student ID'][i],df['Student Name'][i],df['Email'][i],df['Section'][i])
        student = Student(student_id = df['Student ID'][i],
                          student_name=df['Student Name'][i],
                          email = df['Email'][i],
                          section = df['Section'][i]
                          )
        student.save()

if __name__ == '__main__':
    main()
