# Desarrollo

En esta fase se ha llevado a cabo el despliegue de toda la infraestructura necesaria para el funcionamiento de la web corporativa de **CreviPlay** y del gestor de contenidos basado en **WordPress**, utilizando servicios de **AWS** y contenedores **Docker** para garantizar portabilidad, escalabilidad y facilidad de mantenimiento.

## Infraestructura en AWS

Se han desplegado **dos instancias EC2** independientes, ambas en la misma región y con sistema operativo Linux, cada una con un rol claramente diferenciado:

![Instancias EC2 en ejecución](imagenes/instancias-ec2.png)

### Instancia 1 – Servidor WordPress

La primera instancia está dedicada exclusivamente a alojar el servidor de **WordPress**:

- Tipo de instancia: `t2.medium`.
- Seguridad gestionada mediante un *Security Group* específico, con las siguientes reglas de entrada:
  - **SSH (TCP 22)** abierto para administración remota.
  - **HTTP (TCP 80)** para permitir el acceso web sin cifrar.
  - **HTTPS (TCP 443)** para futuras conexiones seguras.
- Asociada a una **Elastic IP**, lo que permite disponer de una dirección pública fija para acceder al sitio WordPress desde cualquier lugar.

### Instancia 2 – Aplicación web personalizada

La segunda instancia se encarga de ejecutar la **aplicación web personalizada** desarrollada a medida:

- Tipo de instancia: `t3.small`.
- Seguridad gestionada con otro *Security Group* independiente, también con acceso **SSH (22)**, **HTTP (80)** y **HTTPS (443)**.
- Asociada igualmente a una **Elastic IP** para facilitar el acceso a la aplicación web desarrollada a medida.

Esta separación de instancias permite aislar el CMS de la aplicación personalizada, mejorando la seguridad y facilitando el escalado o mantenimiento independiente de cada servicio.

En ambos casos se han definido *Security Groups* específicos donde se han habilitado de forma controlada los puertos necesarios para SSH y para el tráfico web.

![Reglas de seguridad del servidor Docker](imagenes/sg-docker.png)

![Reglas de seguridad del servidor WordPress](imagenes/sg-wordpress.png)

Finalmente, se han asociado **direcciones IP elásticas** a cada instancia para garantizar direcciones públicas fijas.

![Direcciones IP elásticas asignadas](imagenes/elastic-ips.png)

## Despliegue con Docker en el servidor de WordPress

En la instancia destinada a WordPress se ha utilizado **Docker Compose** para orquestar un entorno formado por dos contenedores principales que colaboran entre sí:

![Fichero docker-compose para WordPress, MySQL y phpMyAdmin](imagenes/docker-compose-wordpress.png)

### Contenedor de base de datos MySQL

El primer servicio es la **base de datos MySQL**, responsable de almacenar toda la información del sitio:

- Imagen utilizada: `mysql:latest`.
- Variables de entorno configuradas para definir el usuario administrador, la contraseña de **MySQL** y la base de datos específica para WordPress.
- Política de reinicio `always` para asegurar su disponibilidad continua.

### Contenedor de WordPress

El segundo servicio es el propio **WordPress**, que se conecta a la base de datos anterior:

- Imagen utilizada: `wordpress:latest`.
- Dependencia explícita del contenedor de base de datos mediante `depends_on`.
- Puerto **80** del contenedor expuesto al exterior para servir el sitio web.
- Variables de entorno que conectan WordPress con MySQL (host, usuario, contraseña y nombre de la base de datos).
- Volumen asociado al directorio `/var/www/html` para persistir los datos del CMS.

Con este `docker-compose.yml` se consigue un entorno completo de WordPress, con base de datos y herramienta de administración, totalmente reproducible y fácil de levantar o detener con un único comando.

## Despliegue con Docker en el servidor de la aplicación web

La segunda instancia EC2 aloja la **aplicación web propia de CreviPlay**, desarrollada en **PHP** y conectada a una base de datos **MySQL**. También se ha utilizado **Docker Compose**, en este caso con dos servicios principales claramente diferenciados:

![Fichero docker-compose de la aplicación web](imagenes/docker-compose-app.png)

### Servicio `web`

El servicio `web` representa la aplicación PHP que se expone al usuario final:

- Se construye a partir de un **Dockerfile** personalizado.
- Expone el puerto **80** para servir la aplicación web.
- Utiliza variables de entorno para configurar la conexión a la base de datos (host, usuario, contraseña y nombre de la BD `EstudioVideojuegos`).
- Declara una dependencia del servicio de base de datos para asegurarse de que el contenedor de MySQL está disponible antes de iniciar Apache/PHP.

### Servicio `db` (MySQL 8.0)

El servicio `db` es la base de datos de la aplicación:

- Utiliza la imagen `mysql:8.0`.
- Define mediante variables de entorno la contraseña del usuario root, el usuario de aplicación y su contraseña, así como el nombre de la base de datos principal.
- Asocia un volumen persistente (`db_data`) a `/var/lib/mysql` para conservar la información aunque el contenedor se recree.

### Dockerfile de la aplicación PHP

El **Dockerfile** utilizado para construir la imagen de la aplicación se basa en la imagen oficial `php:8.2-apache` e incluye los siguientes aspectos clave:

![Contenido del Dockerfile de la aplicación PHP](imagenes/dockerfile-app.png)

- Instalación de la extensión **mysqli**, necesaria para conectar con MySQL mediante `docker-php-ext-install mysqli`.
- Copia del código fuente de la aplicación al directorio `/var/www/html`, que es el *DocumentRoot* de Apache dentro del contenedor.

Gracias a este enfoque, la aplicación queda empaquetada junto con todas sus dependencias, evitando problemas de configuración entre entornos y facilitando la replicación del servidor en el futuro.

## Instancia 3 - Servicio DNS


Junto a las instancias de **WordPress** y de la **aplicación web**, se ha aprovisionado una **tercera instancia EC2** solo para **DNS**, con **BIND** (`named` en Linux).

### Creación de la instancia

Se ha desplegado el **servidor de nombres** en una instancia propia, separandolo de las demás para tener un control sobre ella.

![Instancia EC2 del servidor DNS](imagenes/Instancia_DNS.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: instancia dedicada al rol DNS, en el mismo criterio de región e imagen base que el resto del despliegue</p>

### Dirección IP Elástica

Con una **Elastic IP** enlazada a la instancia DNS, los **registros** que apunten a esa IP (por ejemplo, un dominio o subdominio) **siguen teniendo sentido** tras un reinicio o un cambio de mantenimiento, sin reetiquetar a mano direcciones que hayan “saltado”.

![Elastic IP asociada a la instancia DNS](imagenes/IP_elastica_DNS.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: IP elástica asociada al servidor de nombres, alineada con el enfoque del resto de instancias</p>

### Reglas de red (Security Group)

El **Security Group** restringe la exposición: **SSH (TCP 22)** solo para la administración remota, y **DNS (UDP 53 y TCP 53)** para que clientes o servicios hagan resolución correctamente. Así, la hoja de reglas se puede **revisar de un vistazo** (quién entra, para qué y por qué puerto).

![Reglas de entrada del Security Group del servidor DNS](imagenes/Reglas_Entrada_DNS.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: reglas mínimas para administración (22) y servicio de nombres (53)</p>

### Configuración de BIND: fichero principal e *includes*

**Fichero base** (`named.conf` o raíz de la configuración): directivas, inclusiones hacia el resto de fragmentos e integración con el despliegue de `bind` en el sistema.

![Fichero principal de configuración de named](imagenes/Configuracion_named.conf.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: punto de entrada: referencias a opciones, zonas por defecto y dominios bajo vuestro control</p>

**Archivo named.options**: afinan escucha, política de reenvío o recursión, y criterios de seguridad del demonio, sin mezclar con las definiciones de zona.

![Configuración de opciones de named](imagenes/Configuracion_named.conf.options.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: hoja de opciones: comportamiento del servidor, separada de las definiciones de zona</p>

**Archivo named.conf.local**: declaraciones de `zone` hacia el fichero de **registros** que materializan nombres y destinos reales en el entorno CreviPlay.

![Zona y declaraciones locales de named](imagenes/Configuracion_named.conf.local.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: zona y vínculo con el fichero de datos DNS del proyecto</p>

**Archivo named.conf.default-zones**: deja claro qué resuelve o delega el sistema *antes* de añadir lo propio, y sirve de referencia al contrastar con la **zona local** anterior.

![Zonas por defecto o include en named](imagenes/Configuracion_named.conf.default-zones.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: bloque de includes de zonas predefinidas, como referencia frente a la zona personalizada</p>

## Instancia 4 - Base de datos

Para mejorar la **separación de responsabilidades** y reforzar la seguridad del entorno, se ha desplegado una **cuarta instancia EC2** dedicada exclusivamente a la **base de datos MySQL** de la aplicación CreviPlay. De este modo, el motor de datos queda aislado del servidor web, lo que facilita el mantenimiento, las copias de seguridad y el control del acceso a nivel de red.

### Despliegue con Docker Compose

En la instancia de base de datos (`172.31.17.200`) se ha levantado un entorno formado por **MySQL 8.0** y **phpMyAdmin** mediante **Docker Compose**, con persistencia de datos, exposición del puerto **3306** para la aplicación y del puerto **8080** para la administración web:

![Fichero docker-compose actualizado de la base de datos con phpMyAdmin](imagenes/NuevoDockerFilebasededatos.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: servicios `db` y `phpmyadmin` orquestados en la misma red Docker, con volumen persistente y acceso web al puerto 8080</p>

#### Servicio `db` (MySQL 8.0)

- Imagen utilizada: `mysql:8.0`, con nombre de contenedor `mysql-creviplay`.
- Base de datos principal: `EstudioVideojuegos`, con usuario de aplicación y contraseñas definidos mediante variables de entorno.
- Volumen persistente (`db_data`) montado en `/var/lib/mysql` para conservar los datos aunque el contenedor se reinicie o se recree.
- Puerto **3306** publicado hacia el exterior para permitir la conexión remota desde el servidor web.
- Política de reinicio `unless-stopped` para mantener el servicio disponible de forma continua.

#### Servicio `phpmyadmin`

Para **consultar y administrar la base de datos desde el navegador**, se ha añadido un segundo contenedor con la imagen `phpmyadmin:latest`:

- Contenedor: `phpmyadmin-creviplay`.
- Conexión interna al servicio `db` mediante las variables `PMA_HOST: db` y `PMA_PORT: 3306`.
- Puerto **8080** del host mapeado al puerto **80** del contenedor, de modo que la interfaz queda accesible en `http://IP_PUBLICA:8080`.
- Dependencia explícita de `db` con `depends_on`, de forma que MySQL arranca antes que phpMyAdmin.
- Política de reinicio `unless-stopped`.

Tras ejecutar `docker compose up -d`, el acceso web se realiza con las credenciales de MySQL (`root` / `rootpass` o `usuario` / `password`). En AWS, además del Security Group de MySQL, debe permitirse el tráfico entrante en el puerto **8080** (o bien usar un túnel SSH hacia `localhost:8080` para no exponer la interfaz a internet).

### Reglas de red (Security Group)

El **Security Group** `SQL-Separado` limita el acceso al servicio de base de datos únicamente a los orígenes necesarios:

![Reglas de entrada del Security Group de la base de datos](imagenes/reglas%20de%20entrada%20Base%20de%20Datos.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: SSH (22) para administración y MySQL (3306) restringido a la IP privada del servidor web</p>

- **SSH (TCP 22)**: acceso remoto para la administración de la instancia.
- **MySQL (TCP 3306)**: tráfico de base de datos permitido solo desde la IP privada `172.31.79.239/32`, correspondiente al servidor web de la aplicación.

Con esta configuración se evita que el puerto de MySQL quede expuesto a cualquier origen, aplicando el principio de **menor privilegio** en la capa de red.

### Copia de seguridad y migración de datos

Antes de completar la separación, se generó una **copia de seguridad** de la base de datos en el servidor web original. En el directorio `~/ServidorWeb` quedaron disponibles el volcado `backup.sql`, el código de la aplicación y el fichero de orquestación:

![Copia de seguridad de la base de datos en el servidor web](imagenes/Crear%20backup%20de%20la%20base%20de%20datos%20en%20servidor.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: fichero `backup.sql` generado junto al proyecto `CreviPlay` antes de migrar MySQL a su propia instancia</p>

Este volcado permitió trasladar los datos existentes al nuevo contenedor MySQL sin pérdida de información durante la reestructuración de la infraestructura.

### Actualización del servidor web

Una vez desplegada la base de datos en su instancia dedicada, el **servidor web** (`172.31.79.239`) se simplificó: el `docker-compose.yml` pasa a definir únicamente el servicio `web`, eliminando el contenedor local de MySQL y apuntando las variables de entorno hacia la IP privada de la nueva instancia:

![Docker Compose actualizado del servidor web](imagenes/ServerWebActualizado.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: servicio web con conexión remota a MySQL mediante `DB_HOST`, `DB_USER`, `DB_PASSWORD` y `DB_NAME`</p>

La aplicación PHP también incorpora esta configuración en su fichero `config.php`, utilizando variables de entorno en Docker y valores por defecto orientados al entorno remoto:

![Configuración de conexión en config.php](imagenes/configphp%20del%20serverweb.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">Figura: constantes `DB_HOST`, `DB_USER`, `DB_PASSWORD` y `DB_NAME` con soporte para entorno Docker y desarrollo local</p>

Los parámetros de conexión quedan así alineados entre Docker Compose y la aplicación:

| Parámetro | Valor |
|-----------|-------|
| **DB_HOST** | `172.31.17.200` |
| **DB_USER** | `root` |
| **DB_PASSWORD** | `rootpass` |
| **DB_NAME** | `EstudioVideojuegos` |

Gracias a este cambio, la capa web y la capa de datos quedan **desacopladas**: el servidor de aplicación puede reiniciarse o escalarse sin afectar directamente al motor de base de datos, y el acceso a MySQL queda restringido por reglas de firewall a la instancia que realmente lo necesita.


## Conclusiones de la fase de desarrollo e implantación

El uso combinado de **AWS EC2**, **Elastic IPs**, **Security Groups** y **Docker/Docker Compose** ha permitido desplegar una infraestructura modular y escalable, en la que:

- WordPress funciona como gestor de contenidos independiente para la parte más corporativa.
- La aplicación PHP personalizada gestiona la lógica específica del estudio de videojuegos.
- El servicio **DNS (BIND/named)** en su propia instancia aporta resolución de nombres alineada con las direcciones públicas fijas del proyecto.
- La **base de datos MySQL** en una instancia dedicada centraliza el almacenamiento de la aplicación, restringe el acceso al puerto 3306 solo desde el servidor web e incorpora **phpMyAdmin** para su gestión visual desde el navegador.
- La separación de WordPress, aplicación, DNS y base de datos reduce el impacto de posibles fallos y amplía las opciones de crecimiento del proyecto a medio y largo plazo.