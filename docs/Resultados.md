# Resultados

Tras completar la fase de desarrollo e implantación, el proyecto CreviPlay dispone de una infraestructura de TI funcional desplegada en **AWS** con **cuatro instancias EC2** especializadas. A continuación se resumen los resultados obtenidos en cada ámbito.

## Infraestructura desplegada

| Componente | Resultado | Estado |
|------------|-----------|--------|
| **Instancia WordPress** (`t2.medium`) | CMS corporativo con MySQL en Docker, accesible vía Elastic IP `32.192.151.244` | Operativo |
| **Instancia aplicación PHP** (`t3.small`) | Aplicación web con Apache/PHP 8.2 en Docker, IP privada `172.31.79.239` | Operativo |
| **Instancia DNS** | Servidor BIND (`named`) con Elastic IP y Security Group para puertos 53 y 22 | Operativo |
| **Instancia base de datos** | MySQL 8.0 + phpMyAdmin en Docker, IP privada `172.31.17.200` | Operativo |

## Servicios implementados

### WordPress (CMS corporativo)

- Sitio web corporativo desplegado con **Docker Compose** (contenedores WordPress + MySQL).
- Acceso público mediante Elastic IP con puertos HTTP (80) y HTTPS (443) preparados.
- Volumen persistente para conservar los contenidos del CMS.

### Aplicación PHP de gestión

- Aplicación personalizada desplegada con **Dockerfile** basado en `php:8.2-apache`.
- Conexión remota a MySQL en la instancia dedicada mediante variables de entorno y `config.php`.
- Panel de administración funcional para la gestión de usuarios y catálogo de videojuegos.

### Base de datos MySQL

- Base de datos **`EstudioVideojuegos`** con modelo ER implementado (entidades Usuario y Videojuego, relación 1:N).
- Acceso restringido por Security Group `SQL-Separado` (solo desde `172.31.79.239/32`).
- **phpMyAdmin** disponible en el puerto 8080 para administración visual.
- Migración completada desde la configuración con volcado `backup.sql` previo.

### Servidor DNS

- **BIND** configurado con ficheros `named.conf`, `named.options`, `named.conf.local` y `named.conf.default-zones`.
- Resolución de nombres alineada con las Elastic IPs del proyecto.

## Seguridad aplicada

- **Security Groups** independientes por instancia con reglas mínimas necesarias.
- Principio de **menor privilegio** en el acceso a MySQL (puerto 3306 restringido a la IP del servidor web).
- Acceso remoto SSH habilitado para administración de todas las instancias.
- Separación de capas: web, datos, DNS y CMS en máquinas distintas.

## Frontend de referencia

En el repositorio del proyecto se incluye un **frontend prototipo** (`frontend/`) con HTML, CSS y JavaScript que implementa las secciones principales del sitio (Inicio, Portafolio, Sobre nosotros, Contacto) con diseño responsive, sirviendo como referencia para el tema WordPress.

## Requisitos pendientes

| Requisito | Estado actual |
|-----------|---------------|
| **Backup diario automatizado** | Se realizó volcado manual (`backup.sql`) durante la migración; falta automatización periódica |
| **HTTPS / certificados SSL** | Puertos 443 abiertos en Security Groups; certificados TLS aún no configurados |

## Documentación

La documentación completa del proyecto se publica automáticamente en **GitHub Pages** mediante MkDocs con cada push a la rama `main`, incluyendo diseño, planificación, desarrollo, resultados y conclusiones.
