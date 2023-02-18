from classes import Estudiante
from dotenv import load_dotenv

# 

def main():
    estudiante = Estudiante("Mario","AS","33563254")
    #estudiante.save()
    #estudiante = Estudiante("Mumuchumu","Doblas","31487539")
    estudiante.apellido = "Pérez"
    estudiante.update_student()
    
if __name__ == "__main__":
    load_dotenv()
    main()




