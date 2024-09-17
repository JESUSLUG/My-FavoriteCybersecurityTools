import os
import subprocess

# Ruta del archivo donde se guardarán los repos
repos_file = "repos.txt"

# Función para leer los repositorios guardados en el archivo
def read_repos():
    repos = []
    if os.path.exists(repos_file):
        with open(repos_file, "r") as f:
            repos = f.readlines()
    return [repo.strip() for repo in repos]

# Función para guardar un nuevo repositorio en el archivo
def save_repo(repo):
    with open(repos_file, "a") as f:
        f.write(repo + "\n")

# Función para clonar un repositorio
def clone_repo(repo_url):
    print(f"Clonando {repo_url}...")
    subprocess.run(["git", "clone", repo_url])

# Función para añadir un nuevo repositorio
def add_repo():
    repo_url = input("Introduce la URL del repositorio: ")
    save_repo(repo_url)
    print("Repositorio guardado.")

# Función para listar y seleccionar repositorios
def list_repos(repos):
    for i, repo in enumerate(repos, 1):
        print(f"{i}. {repo}")
    choice = input("\n¿Quieres clonar todos los repositorios? (S/n): ").lower()
    if choice == 'n':
        selected = input("Selecciona los números de los repositorios a clonar (separados por comas): ")
        selected_indices = [int(num) - 1 for num in selected.split(",")]
        return [repos[i] for i in selected_indices]
    else:
        return repos

# Función principal
def main():
    repos = read_repos()

    # Si no hay repos en el archivo, añadir el repositorio inicial
    if not repos:
        default_repo = "https://github.com/Rannden-SHA/EnumeRannden.git"
        save_repo(default_repo)
        repos.append(default_repo)

    while True:
        print("\n1. Clonar repositorios")
        print("2. Agregar un nuevo repositorio")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            if repos:
                repos_to_clone = list_repos(repos)
                for repo in repos_to_clone:
                    clone_repo(repo)
            else:
                print("No hay repositorios guardados.")
        elif choice == "2":
            add_repo()
        elif choice == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
