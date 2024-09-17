# CyberSecurity Tool Installer

Este script en Python tiene como objetivo facilitar la recopilación, organización e instalación de tus herramientas favoritas de ciberseguridad desde repositorios de GitHub. La idea es mantener una lista personalizada de herramientas que puedes clonar y gestionar fácilmente desde un solo script.

## Características

- **Agregar herramientas**: Puedes agregar las URLs de los repositorios de herramientas que prefieras.
- **Clonar repositorios**: El script te permite clonar todos los repositorios guardados o seleccionar individualmente cuáles deseas clonar.
- **Gestión simple**: Las URLs de las herramientas se guardan en un archivo de texto (`repos.txt`), lo que permite tener acceso rápido y agregar más repositorios de manera sencilla.
- **Interfaz interactiva**: El script te proporciona un menú fácil de usar, donde puedes elegir entre clonar repositorios o agregar nuevos.

## Requisitos

- **Python 3.x** instalado.
- **Git** instalado en tu sistema (para clonar los repositorios).

## Instrucciones de Uso

### 1. Clonar este repositorio o copiar el script en tu máquina local.

```bash
git clone https://github.com/tu-usuario/tu-repo.git
```

```bash
cd tu-repo
```

### 2. Ejecutar el script

Puedes ejecutar el script directamente desde la terminal:

```bash
python3 ReposFavs.py
```

### 3. Usar el menú interactivo

Cuando ejecutes el script, verás un menú con las siguientes opciones:

- **1. Clonar repositorios**: Esta opción te permitirá clonar las herramientas guardadas en tu archivo `repos.txt`. Podrás elegir si clonas todos los repos o seleccionas algunos por su número de listado.
- **2. Agregar un nuevo repositorio**: Si tienes una nueva herramienta de ciberseguridad que deseas agregar, selecciona esta opción e introduce la URL del repositorio. El script la guardará en `repos.txt` para uso futuro.
- **3. Salir**: Finaliza el programa.

### 4. Agregar más herramientas

Puedes seguir agregando más herramientas de ciberseguridad ingresando las URLs de sus repositorios de GitHub. Estas se guardarán en `repos.txt` y estarán disponibles para clonar en futuras ejecuciones del script.

### Ejemplo

Supongamos que quieres agregar el siguiente repositorio:

```bash
https://github.com/Rannden-SHA/EnumeRannden.git
```

Puedes usar la opción "2. Agregar un nuevo repositorio" para incluir esta herramienta en tu lista personalizada.

## Personalización

El archivo `repos.txt` contiene todas las URLs de repositorios. Si lo deseas, puedes editarlo directamente para agregar o eliminar repositorios manualmente.

## Contribuciones

Si tienes sugerencias, mejoras o nuevas funcionalidades que te gustaría agregar, siéntete libre de hacer un pull request o crear un issue en el repositorio.
