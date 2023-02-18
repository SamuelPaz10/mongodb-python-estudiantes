from classes import Student
from dotenv import load_dotenv

def main():
    student = Student("Leo","Dona","33563254")
    student.save()
    #student = Student("Mumuchumu","Doblas","31487539")
    student.last_name = "Messi"
    student.update_student()
    
if __name__ == "__main__":
    load_dotenv()
    main()




