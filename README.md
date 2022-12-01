# Proyecto: Proyecto Django Coderhouse 34640
## Estudiante: Facundo Mercado

### Inicializando el proyecto
Una vez clonado el proyecto, situandonos en la carpeta "CoderHouse/Proyecto34640", iniciamos el proyecto con el comando:
>python manage.py runserver

Ahora el proyecto estara funcionando localmente.
Nos dirigimos a la URL de inicio:
>http://127.0.0.1:8000/Institucion/

Ya desde ahí podremos ingresar a cualquiera de las otras rutas disponibles, con la excepcion del Panel de administracion.
Para ingresar al panel de administracion:
>http://127.0.0.1:8000/admin/

Credenciales de administrador:
><sub>usuario: Admin
contraseña: usuario123</sub>

### Utilizando el proyecto
Una vez en la URL de inicio, veremos en la parte superior de la pagina 4 botones que nos llevan a diferentes vistas:
- Inicio
- Pagina de estudiantes
- Pagina de materias
- Pagina de profesores

A su vez, dentro de la pagina de estudiantes, materias y profesores, veremos botones que nos permiten ingresar nuevos estudiantes, materias y profesores a la base de datos.

La pagina de estudiantes tambien cuenta con un boton para buscar un estudiante en la base de datos segun el **_nombre_**

### Listado de rutas disponibles

| Vista  | Url |
| ------------- | ------------- |
| Inicio  | http://127.0.0.1:8000/Institucion/  |
| Panel de administrador | http://127.0.0.1:8000/admin/ |
| Pagina de estudiantes | http://127.0.0.1:8000/Institucion/estudiantes/  |
| Formulario: ingresar estudiante | http://127.0.0.1:8000/Institucion/estudiantesFormulario/ |
| Formulario: buscar estudiante | http://127.0.0.1:8000/Institucion/busquedaEstudiante/ |
| Formulario: fallo la busqueda del estudiante (no se ingresaron datos) | http://127.0.0.1:8000/Institucion/resultadoBusqEst/?nombre= |
| Pagina de materias | http://127.0.0.1:8000/Institucion/materias/ |
| Formulario: ingresar una materia | http://127.0.0.1:8000/Institucion/materiasFormulario/ |
| Pagina de profesores | http://127.0.0.1:8000/Institucion/profesores/
| Formulario: ingresar un profesor | http://127.0.0.1:8000/Institucion/profesoresFormulario/ |
