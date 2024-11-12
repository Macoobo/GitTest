from config import USERNAME, PASSWORD

user = USERNAME
password = PASSWORD

def access_with_credentials():
    print(f"Accessing with username: {user} and password: {password}")
    print(f"Bienvenido {user}! ")
    # Aquí puedes añadir la lógica de acceso, como conectarte a una base de datos o servicio.

if __name__ == "__main__":
    access_with_credentials()