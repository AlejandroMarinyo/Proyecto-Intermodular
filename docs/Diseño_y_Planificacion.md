# Diseño y planificación

##Infraestructura del proyecto

![Estructura del Proyecto](Estructura%20Proyecto.png)

## Diseño de la Base de Datos

El diseño de la base de datos está basado en un modelo Entidad-Relación (ER) que busca reflejar las necesidades principales de la plataforma CreviPlay: gestión de usuarios, proyectos de videojuegos, medios, categorías, desarrolladores, contactos y registro de logs de actividad. La estructura facilita la integridad de los datos y escalabilidad del sistema.

### Principales entidades y relaciones

- **Usuarios**: Contiene la información básica y de autenticación de cada usuario del sistema.
- **Proyectos**: Almacena el detalle de cada videojuego desarrollado, su estado y relación con el usuario creador.
- **Medios**: Gestiona los recursos multimedia asociados a cada proyecto (imágenes, videos, archivos).
- **Categorias**: Permite clasificar los proyectos por temáticas o géneros.
- **Desarrolladores**: Registra los miembros del equipo que participan en proyectos específicos.
- **Contactos**: Almacena posibles contactos externos y su relación con proyectos.
- **Logs_sistema**: Mantiene un historial detallado de las acciones realizadas en el sistema por los usuarios.
- **Tablas de unión**: Se han diseñado relaciones N:M para proyectos-categorías, proyectos-desarrolladores y proyectos-contactos, permitiendo flexibilidad en la gestión de participaciones y clasificaciones.

### Diagrama Entidad-Relación

A continuación se muestra el modelo ER realizado. El diagrama resume de forma visual la estructura de la base de datos, sus tablas principales, atributos y relaciones clave.

![Modelo Entidad-Relación CreviPlay](Diagrama_ER_Mermaid.png)

<p style="text-align: center; font-size: 0.9em; color: #666; margin-top: 8px; font-style: italic;">
    Figura: Modelo Entidad-Relación principal de la base de datos CreviPlay
</p>

## Diseño de la pagina web

Para este proyecto de 2º de ASIR, se ha optado por una solución práctica y funcional que permita demostrar los conocimientos adquiridos sin requerir un nivel de complejidad excesivo. La página web se desarrollará utilizando **WordPress** como sistema de gestión de contenidos (CMS), lo que facilitará la implementación y permitirá centrarse en los aspectos de infraestructura y administración del sistema.

### **Estructura y funcionalidades básicas**

La página web de CreviPlay contará con las siguientes secciones principales:

- **Página de inicio (Home)**: Presentación del estudio, información básica y acceso rápido a los proyectos destacados.
- **Portafolio de videojuegos**: Galería donde se mostrarán los proyectos en desarrollo, con imágenes, descripciones y estado de cada proyecto.
- **Sobre nosotros**: Información sobre el equipo de desarrollo y el estudio.
- **Contacto**: Formulario de contacto básico para que publishers o clientes puedan ponerse en contacto con el estudio.

### **Características técnicas**

- **Tema WordPress**: Se utilizará un tema gratuito o de bajo coste, personalizado con los colores y logo de CreviPlay.
- **Plugins esenciales**: Se instalarán plugins básicos para gestión de formularios de contacto y optimización de imágenes.
- **Responsive design**: El tema seleccionado será responsive para que la página sea accesible desde dispositivos móviles.
- **Panel de administración**: Acceso al panel de WordPress para gestionar contenidos, proyectos y usuarios.

### **Consideraciones de diseño**

Dado que este es un proyecto académico de segundo curso, el enfoque se centrará en:

- **Funcionalidad sobre estética**: Priorizar que todas las funcionalidades básicas funcionen correctamente.
- **Simplicidad**: Evitar diseños excesivamente complejos que puedan generar problemas técnicos.
- **Aprendizaje práctico**: Utilizar la implementación como oportunidad para aprender sobre despliegue web, configuración de servidores y gestión de contenidos.

El objetivo principal es demostrar la capacidad de desplegar y administrar una aplicación web funcional en un entorno AWS, más que crear una página web de nivel profesional comercial.

## **Requisitos principales**
**Funcionales:**
- Plataforma web con portafolio
- Panel de administración
- Gestión de Proyectos

**No funcionales:**
- Tiempo de carga < 2 segundos
- Backup diario
- Seguridad (HTTPS, encriptación)

**Del negocio:**
- Crear presencia web profesional
- Mostrar los videojuegos

### **Matriz de trazabilidad de requisitos**

La siguiente tabla relaciona cada requisito con los módulos del ciclo formativo y su estado de implementación:

| Requisito | ASGBD | ASO | IAW | Servicios de Red | Seguridad | Estado |
|-----------|-------|-----|-----|-----------------|-----------|--------|
| **Plataforma web con portafolio** | - | ✓ | ✓ | ✓ | ✓ | Pendiente |
| **Panel de administración** | ✓ | ✓ | ✓ | ✓ | ✓ | Pendiente |
| **Gestión de Proyectos** | ✓ | ✓ | ✓ | - | ✓ | Pendiente |
| **Tiempo de carga < 2 segundos** | - | ✓ | ✓ | ✓ | - | Pendiente |
| **Backup diario** | ✓ | ✓ | - | - | ✓ | Pendiente |
| **Seguridad (HTTPS, encriptación)** | ✓ | ✓ | ✓ | ✓ | ✓ | Pendiente |
| **Crear presencia web profesional** | - | ✓ | ✓ | ✓ | ✓ | Pendiente |
| **Mostrar los videojuegos** | - | ✓ | ✓ | ✓ | - | Pendiente |

**Leyenda:**
- ✓ = Módulo relacionado con el requisito
- - = Módulo no relacionado con el requisito
- **Estados:** Pendiente, En desarrollo, Completado

### **Diagrama de Gantt**

Este es el diagrama de Gantt de nuestro proyecto (Sujeto a cambios)

![Diagrama de Gantt](Gantt.png)

<a href="https://trello.com/invite/b/692dd6254cc1eb9200f5c982/ATTI7a99346f596d27f1b6ba5ae0d74a60ff4779E02B/proyecto-intermodular" target="_blank" rel="noopener noreferrer">Enlace a Trello</a>

### **Matriz de riesgos con estrategias de mitigación**

La siguiente tabla identifica los principales riesgos que podrían surgir durante la implementación práctica del proyecto, junto con estrategias de mitigación para cada uno:

| Riesgo | Descripción | Probabilidad | Impacto | Estrategia de Mitigación |
|--------|-------------|--------------|---------|-------------------------|
| **Configuración incorrecta de Security Groups** | Reglas de firewall mal configuradas que permiten acceso no autorizado o bloquean tráfico legítimo | Media | Alto | Documentar todas las reglas antes de implementar, usar plantillas de seguridad probadas, realizar pruebas de conectividad después de cada cambio, implementar principio de menor privilegio |
| **Pérdida de datos por falta de backups** | Fallo en el sistema de respaldo automático o pérdida de datos críticos | Baja | Alto | Configurar backups automáticos diarios en RDS, verificar regularmente la integridad de los backups |
| **Sobrecostos inesperados en AWS** | Uso excesivo de recursos que genera facturas elevadas | Alta | Alta | Usar instancias de tamaño apropiado, pensar en hacerlo en varios laboratorios y al final levantarlo todo en un mismo laboratorio |
| **Problemas de conectividad de red** | Configuración incorrecta de VPC, subredes o rutas que impide la comunicación entre servicios | Media | Alto | Diseñar topología de red antes de implementar, usar diagramas de red, probar conectividad entre cada componente, documentar todas las configuraciones de red |
| **Rendimiento insuficiente** | Tiempos de carga superiores a 2 segundos o saturación del servidor | Media | Medio | Implementar CloudFront, optimizar imágenes y recursos estáticos, usar caché en WordPress, realizar pruebas de carga antes del despliegue |
| **Problemas con la base de datos RDS** | Fallos de conexión, pérdida de rendimiento o errores en consultas | Baja | Alto | Configurar RDS multi-AZ para alta disponibilidad, monitorear métricas de rendimiento, optimizar consultas SQL, realizar mantenimiento preventivo regular |
| **Pérdida de acceso remoto** | Problemas con SSH o acceso a instancias EC2 que impiden la administración | Baja | Alto | Mantener múltiples métodos de acceso (SSH, RDP), almacenar claves de forma segura |

**Leyenda de Probabilidad e Impacto:**
- **Probabilidad:** Alta (frecuente), Media (ocasional), Baja (raro)
- **Impacto:** Alto (crítico para el proyecto), Medio (afecta funcionalidad), Bajo (menor inconveniente)

### **Decisiones de Diseño**
- **Infraestructura base en AWS:** Implementación sobre Amazon EC2 con instancias optimizadas para desarrollo, red configurada mediante Amazon VPC, subredes públicas/privadas, reglas de seguridad (Security Groups), NACLs y servicios esenciales como DHCP, DNS interno, SSH y control de tráfico mediante AWS Firewall Manager.
- **Sistema de base de datos gestionado:** Uso de Amazon RDS (MySQL o PostgreSQL) con despliegue multi-AZ, backups automáticos, cifrado en reposo (KMS) y gestión de accesos mediante IAM y roles con privilegios mínimos.
- **Aplicación web profesional:** Servidor Apache o Nginx desplegado en EC2, integrando un WordPress personalizado para el portafolio de videojuegos. Almacenamiento de contenido multimedia en Amazon S3 y distribución global mediante Amazon CloudFront.
- **Seguridad y mantenimiento avanzado:** Certificados SSL/TLS gestionados con AWS Certificate Manager, copias de seguridad automatizadas en S3 y Glacier, scripts de automatización en AWS Lambda, y monitorización centralizada del sistema con Amazon CloudWatch.

### **Exclusiones en fase inicial**
Las siguientes funcionalidades quedan excluidas de la fase inicial del proyecto y podrán ser implementadas en futuras iteraciones:

- **Integración con Steam/Epic:** La integración con plataformas de distribución de videojuegos como Steam o Epic Games Store no está contemplada en esta fase inicial.

- **Sistema de descargas:** No se implementará un sistema propio de descarga directa de videojuegos en esta fase.

- **Foros o comentarios:** La funcionalidad de foros de discusión o sistema de comentarios en los videojuegos no está incluida en el alcance inicial.


### **Roles del equipo**

- Líder de proyecto: Alejandro Mariño.
- Administrador de sistemas: Iker Sanchez.
- Desarrollador web: Alejandro Mariño.
- Administrador de base de datos: Alejandro Mariño y Iker Sanchez.
- Especialista en seguridad: Iker Sanchez.
- Documentador: Alejandro Mariño y Iker Sanchez.