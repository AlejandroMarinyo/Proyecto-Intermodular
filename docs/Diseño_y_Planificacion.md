# Diseño y planificación



### **Decisiones de Diseño**



- **Infraestructura base en AWS:** Implementación sobre Amazon EC2 con **cuatro instancias** especializadas dentro de una VPC, red configurada con subredes, **Security Groups** por servicio, acceso remoto SSH y direcciones **Elastic IP** para estabilidad pública.

- **Separación de capas:** WordPress (CMS corporativo), aplicación PHP (gestión del catálogo), DNS (BIND) y base de datos MySQL desplegados en instancias independientes para aislar responsabilidades y aplicar el principio de menor privilegio.

- **Sistema de base de datos:** MySQL 8.0 en contenedor Docker sobre una instancia EC2 dedicada, con volumen persistente, **phpMyAdmin** para administración visual y acceso al puerto 3306 restringido únicamente al servidor web de la aplicación.

- **Contenerización con Docker:** WordPress, la aplicación PHP, MySQL y phpMyAdmin orquestados mediante **Docker Compose**, lo que garantiza entornos reproducibles y facilita el mantenimiento.

- **Servicios de red:** Servidor DNS propio con **BIND** (`named`) en instancia dedicada, con reglas de firewall para los puertos 53 (UDP/TCP) y 22 (SSH).

- **Aplicación web:** Sitio corporativo con **WordPress** y aplicación personalizada en **PHP 8.2 + Apache** para la gestión de usuarios y videojuegos del estudio.



## Infraestructura del proyecto



La infraestructura final del proyecto se organiza en una **VPC** con **cuatro instancias EC2** Linux, cada una con un rol definido y comunicación interna a través de la red privada `172.31.0.0/16`:



| Instancia | Rol | Tipo | IP privada | Descripción |
|-----------|-----|------|------------|-------------|
| **1** | WordPress | `t2.medium` | Red VPC | CMS corporativo con MySQL propio en Docker |
| **2** | Aplicación web PHP | `t3.small` | `172.31.79.239` | Aplicación de gestión conectada a MySQL remoto |
| **3** | DNS (BIND) | EC2 Linux | Red VPC | Resolución de nombres con Elastic IP |
| **4** | Base de datos | EC2 Linux | `172.31.17.200` | MySQL 8.0 + phpMyAdmin en Docker |



### Comunicación entre servicios



- La **instancia 2** (aplicación PHP) se conecta a la **instancia 4** (MySQL) mediante la IP privada `172.31.17.200` en el puerto **3306**.

- El **Security Group** de la base de datos (`SQL-Separado`) permite tráfico MySQL solo desde `172.31.79.239/32`.

- La **instancia 1** (WordPress) opera de forma autónoma con su propio contenedor MySQL interno.

- La **instancia 3** (DNS) resuelve nombres hacia las direcciones públicas fijas del resto de servicios.



![Estructura del Proyecto](Estructura%20Proyecto.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">
    Figura: topología final con cuatro instancias EC2 en la VPC — WordPress, aplicación PHP, DNS (BIND) y base de datos MySQL
</p>



## Diseño de la Base de Datos



El diseño de la base de datos está basado en un modelo Entidad-Relación (ER) que refleja las necesidades principales de la plataforma CreviPlay: gestión de usuarios y de videojuegos. Un usuario del sistema puede gestionar múltiples videojuegos mediante la relación **gestiona**. La estructura garantiza la integridad de los datos y permite escalar el catálogo de videojuegos de forma ordenada.



La base de datos principal de la aplicación se denomina **`EstudioVideojuegos`** y reside en la instancia dedicada a MySQL.



### Principales entidades y relaciones



- **Usuario**: Almacena la información de cada usuario del sistema. Atributos principales: `id` (clave primaria, autoincremental), `usuario` (único, para login), `password` (almacenada de forma hasheada), `nombre` y `fecha_registro` (timestamp por defecto).

- **Videojuego**: Contiene el catálogo de videojuegos. Incluye `codigo` (clave primaria, autoincremental), `titulo`, `desarrollador`, `plataforma` (enum: PC, PlayStation, Xbox, Nintendo Switch, Mobile, Multiplataforma), `genero` (enum: Casual, Indie, Aventura, Puzzle, Estrategia, Simulación, Otros), `fechaLanzamiento`, `precio` (decimal 6,2), `descripcion`, y `estado` (enum: En desarrollo, Lanzado, En actualización; por defecto «En desarrollo»).

- **Relación gestiona**: Es una relación **uno a muchos** (1:N) entre Usuario y Videojuego. Un usuario puede gestionar cero o muchos videojuegos; cada videojuego es gestionado por un único usuario. La clave foránea se implementa en la tabla Videojuego referenciando el `id` del Usuario.



### Diagrama Entidad-Relación



A continuación se muestra el modelo ER realizado. El diagrama resume de forma visual la estructura de la base de datos, sus tablas principales, atributos y relaciones clave.



![Modelo Entidad-Relación CreviPlay](Diagrama_ER_Mermaid.png)



<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">

    Figura: Modelo Entidad-Relación principal de la base de datos CreviPlay

</p>



## Diseño de la página web



Para este proyecto de 2º de ASIR se ha optado por una solución dual que combina un CMS y una aplicación a medida:



- **WordPress** como sistema de gestión de contenidos para la web corporativa de CreviPlay (portafolio, información del estudio, contacto).

- **Aplicación PHP personalizada** para la gestión del catálogo de videojuegos, usuarios y panel de administración, conectada a la base de datos `EstudioVideojuegos`.

- **Frontend de referencia** (`frontend/`) con HTML, CSS y JavaScript como prototipo responsive de las secciones principales del sitio.



### **Estructura y funcionalidades básicas**



La plataforma web de CreviPlay incluye las siguientes secciones principales:



- **Página de inicio (Home)**: Presentación del estudio, información básica y acceso rápido a los proyectos destacados.

- **Portafolio de videojuegos**: Galería donde se muestran los proyectos en desarrollo, con imágenes, descripciones y estado de cada proyecto.

- **Sobre nosotros**: Información sobre el equipo de desarrollo y el estudio.

- **Contacto**: Formulario de contacto para que publishers o clientes puedan ponerse en contacto con el estudio.

- **Panel de administración (aplicación PHP)**: Gestión de usuarios y catálogo de videojuegos del estudio.



### **Características técnicas**



- **WordPress**: Tema personalizado con los colores y logo de CreviPlay, desplegado en Docker con MySQL propio.

- **Aplicación PHP**: Servidor Apache con PHP 8.2 en contenedor Docker, extensión `mysqli` y fichero `config.php` con variables de entorno para la conexión remota a MySQL.

- **Plugins esenciales**: Plugins básicos en WordPress para formularios de contacto y optimización de imágenes.

- **Responsive design**: Tanto el tema WordPress como el frontend de referencia son accesibles desde dispositivos móviles.



### **Consideraciones de diseño**



Dado que este es un proyecto académico de segundo curso, el enfoque se centra en:



- **Funcionalidad sobre estética**: Priorizar que todas las funcionalidades básicas funcionen correctamente.

- **Simplicidad**: Evitar diseños excesivamente complejos que puedan generar problemas técnicos.

- **Modularidad**: Separar CMS, aplicación, DNS y base de datos en instancias independientes para facilitar el mantenimiento y la escalabilidad.



### **Diagrama de Gantt**



Este es el diagrama de Gantt de nuestro proyecto (sujeto a cambios):



![Diagrama de Gantt](Gantt.png)



<a href="https://trello.com/invite/b/692dd6254cc1eb9200f5c982/ATTI7a99346f596d27f1b6ba5ae0d74a60ff4779E02B/proyecto-intermodular" target="_blank" rel="noopener noreferrer">Enlace a Trello</a>



### **Matriz de riesgos con estrategias de mitigación**



La siguiente tabla identifica los principales riesgos que podrían surgir durante la implementación práctica del proyecto, junto con estrategias de mitigación para cada uno:



| Riesgo | Descripción | Probabilidad | Impacto | Estrategia de Mitigación |
|--------|-------------|--------------|---------|-------------------------|
| **Sobrecostos inesperados en AWS** | Uso excesivo de recursos que genera facturas elevadas | 🔴 Alta | 🔴 Alto | Usar instancias de tamaño apropiado (`t2.medium`, `t3.small`).<br>Apagar instancias fuera del horario de laboratorio.<br>Consolidar servicios cuando sea posible. |
| **Fallos en la base de datos MySQL** | Errores de conexión entre la aplicación PHP y MySQL remoto, o pérdida de datos en el contenedor | 🟡 Media | 🔴 Alto | Volumen persistente en Docker.<br>Security Group restringido.<br>phpMyAdmin para diagnóstico.<br>Volcado previo a migraciones. |
| **Pérdida de acceso remoto** | Problemas con SSH o acceso a instancias EC2 que impiden la administración | 🟢 Baja | 🔴 Alto | Mantener claves SSH de forma segura.<br>Documentar IPs elásticas y privadas de cada instancia. |



**Leyenda de Probabilidad e Impacto:**



- **Probabilidad:** Alta (frecuente), Media (ocasional), Baja (raro)

- **Impacto:** Alto (crítico para el proyecto), Medio (afecta funcionalidad), Bajo (menor inconveniente)



### **Roles del equipo**



- Líder de proyecto: Alejandro Mariño.

- Administrador de sistemas: Iker Sanchez.

- Desarrollador web: Alejandro Mariño.

- Administrador de base de datos: Alejandro Mariño y Iker Sanchez.

- Especialista en seguridad: Iker Sanchez.

- Documentador: Alejandro Mariño y Iker Sanchez.

