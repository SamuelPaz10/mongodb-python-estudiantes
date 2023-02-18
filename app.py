from classes import Student
from dotenv import load_dotenv

def main():
    student = Student("Ricardo","Dona","33563254")
    student.save()
    #student = Student("Mumuchumu","Doblas","31487539")
    student.last_name = "Montaner"
    student.update_student()
    student.delete_student()
    
if __name__ == "__main__": 
    load_dotenv()
    main()




