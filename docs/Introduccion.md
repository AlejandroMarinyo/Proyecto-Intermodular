# Introducción

## **_Caracterización_**

### **Título**
Infraestructura completa de TI y plataforma web para CreviPlay

### **Contexto**
CreviPlay es un nuevo estudio de desarrollo de videojuegos independiente que se está estableciendo en Crevillent, Alicante. Formado por un pequeño equipo de desarrolladores locales con talento y pasión, el estudio se centra en crear videojuegos casuales e indie para múltiples plataformas.

Nuestro objetivo es destacar en la industria de videojuegos independientes con proyectos creativos y de calidad que lleguen a jugadores de todo el mundo.

### **Problemática**
**_Infraestructura inexistente_**

- No existe ningún servidor, base de datos ni servicios de red configurados para operar

**_Sin presencia Web_**

- Falta de plataforma profesional para mostrar el portafolio de videojuegos en desarrollo

**_Ausencia de seguridad_**

- Sin medidas de protección, sistema de respaldo ni acceso remoto seguro implementados

**_Sin gestión centralizada_**

- Necesidad urgente de gestionar proyectos, desarrolladores y contactos con publishers

### **Objetivos**
1. **Crear infraestructura completa de TI desde cero:** Diseñar e implementar toda la infraestructura de TI: servidores, topología de red y servicios fundamentales.
2. **Servicios de red profesionales:** Configurar DHCP, DNS, SSH y Apache para garantizar conectividad y funcionalidad óptima.
3. **Base de datos robusta:** Instalar y configurar la base de datos para gestionar proyectos, desarrolladores y contactos del estudio.
4. **Plataforma web profesional:** Desarrollar sitio web con WordPress para mostrar el portafolio de videojuegos y facilitar contacto con la industria.
5. **Seguridad y respaldo:** Implementar firewall, encriptación, acceso remoto seguro y sistema automático de copias de seguridad.
6. **Automatización inteligente:** Crear scripts para automatizar tareas administrativas, mantenimiento y respaldos del sistema.

### **Interesados**
- **Stakeholders primarios**
  - Alumnos responsables del diseño, implementación y despliegue de toda la solución tecnológica
- **Stakeholders secundarios**
  - Clientes potenciales, publishers, partners e instituciones públicas

### **Análisis DAFO**

| Fortalezas | Debilidades | Oportunidades | Amenazas |
|---|---|---|---|
| - Equipo joven, motivado y con conocimiento técnico sólido<br>- Flexibilidad para adaptarse rápidamente a cambios<br>- Enfoque en nichos creativos del mercado indie | - Falta total de infraestructura TI previa<br>- Recursos económicos limitados como startup<br>- Poca experiencia empresarial del equipo | - Mercado de videojuegos indie en constante crecimiento<br>- Tecnologías cloud accesibles y escalables<br>- Apoyo de instituciones locales y regionales | - Competencia intensa de estudios consolidados<br>- Rápidos cambios tecnológicos en la industria<br>- Dependencia de plataformas de distribución |

### **Alcance**
- **Infraestructura base en AWS:** Implementación sobre Amazon EC2 con instancias optimizadas para desarrollo, red configurada mediante Amazon VPC, subredes públicas/privadas, reglas de seguridad (Security Groups), NACLs y servicios esenciales como DHCP, DNS interno, SSH y control de tráfico mediante AWS Firewall Manager.
- **Sistema de base de datos gestionado:** Uso de Amazon RDS (MySQL o PostgreSQL) con despliegue multi-AZ, backups automáticos, cifrado en reposo (KMS) y gestión de accesos mediante IAM y roles con privilegios mínimos.
- **Aplicación web profesional:** Servidor Apache o Nginx desplegado en EC2, integrando un WordPress personalizado para el portafolio de videojuegos. Almacenamiento de contenido multimedia en Amazon S3 y distribución global mediante Amazon CloudFront.
- **Seguridad y mantenimiento avanzado:** Certificados SSL/TLS gestionados con AWS Certificate Manager, copias de seguridad automatizadas en S3 y Glacier, scripts de automatización en AWS Lambda, y monitorización centralizada del sistema con Amazon CloudWatch.

### **Requisitos principales**
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

---

**Metadatos / Fechas (origen del documento):**

- Last update: December 3, 2025
- Created: December 3, 2025
