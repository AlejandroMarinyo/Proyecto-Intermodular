# Introducción

## **_Caracterización_**

### **Título**
Infraestructura completa de TI y plataforma web para CreviPlay

### **Contexto**
CreviPlay es un nuevo estudio de desarrollo de videojuegos independiente que se está estableciendo en Crevillent, Alicante. Formado por un pequeño equipo de desarrolladores locales con talento y pasión, el estudio se centra en crear videojuegos casuales e indie para múltiples plataformas.

Nuestro objetivo es destacar en la industria de videojuegos independientes con proyectos creativos y de calidad que lleguen a jugadores de todo el mundo.

### **Problemática**
**_Infraestructura inexistente_**

- No existía ningún servidor, base de datos ni servicios de red configurados para operar.

**_Sin presencia Web_**

- Falta de plataforma profesional para mostrar el portafolio de videojuegos en desarrollo.

**_Ausencia de seguridad_**

- Sin medidas de protección, sistema de respaldo ni acceso remoto seguro implementados.

**_Sin gestión centralizada_**

- Necesidad urgente de gestionar proyectos, desarrolladores y contactos con publishers.

### **Objetivos**
1. **Crear infraestructura completa de TI desde cero:** Diseñar e implementar toda la infraestructura de TI con **cuatro instancias EC2** especializadas (WordPress, aplicación PHP, DNS y base de datos), topología de red y servicios fundamentales.
2. **Servicios de red profesionales:** Configurar **DNS (BIND)**, SSH y Apache para garantizar conectividad y funcionalidad óptima.
3. **Base de datos robusta:** Instalar y configurar **MySQL 8.0** en instancia dedicada con phpMyAdmin para gestionar proyectos, desarrolladores y el catálogo de videojuegos del estudio.
4. **Plataforma web profesional:** Desplegar **WordPress** como CMS corporativo y una **aplicación PHP** personalizada para la gestión del catálogo y panel de administración.
5. **Seguridad y respaldo:** Implementar Security Groups con principio de menor privilegio, acceso remoto SSH y copias de seguridad de la base de datos.
6. **Contenerización con Docker:** Orquestar todos los servicios con **Docker Compose** para garantizar entornos reproducibles y portables.

### **Interesados**
- **Stakeholders primarios**
  - Alumnos responsables del diseño, implementación y despliegue de toda la solución tecnológica
- **Stakeholders secundarios**
  - Clientes potenciales, publishers, partners e instituciones públicas

### **Matriz de trazabilidad de requisitos**

La siguiente tabla relaciona cada requisito con los módulos del ciclo formativo y su estado de implementación:

| Requisito | ASGBD | ASO | IAW | Servicios de Red | Seguridad | Estado |
|-----------|-------|-----|-----|-----------------|-----------|--------|
| **Plataforma web con portafolio** | - | ✓ | ✓ | ✓ | ✓ | Completado |
| **Panel de administración** | ✓ | ✓ | ✓ | ✓ | ✓ | Completado |
| **Gestión de Proyectos** | ✓ | ✓ | ✓ | - | ✓ | Completado |
| **Tiempo de carga < 2 segundos** | - | ✓ | ✓ | ✓ | - | Completado |
| **Servidor DNS propio (BIND)** | - | - | - | ✓ | ✓ | Completado |
| **Base de datos en instancia dedicada** | ✓ | ✓ | - | ✓ | ✓ | Completado |
| **Backup diario** | ✓ | ✓ | - | - | ✓ | Pendiente |
| **Seguridad (HTTPS, encriptación)** | ✓ | ✓ | ✓ | ✓ | ✓ | Pendiente |
| **Crear presencia web profesional** | - | ✓ | ✓ | ✓ | ✓ | Completado |
| **Mostrar los videojuegos** | - | ✓ | ✓ | ✓ | - | Completado |

**Leyenda:**

- Módulo relacionado con el requisito = ✓
- Módulo no relacionado con el requisito = -
- **Estados:** Pendiente, En desarrollo, Completado

### **Análisis DAFO**

| Fortalezas | Debilidades | Oportunidades | Amenazas |
|---|---|---|---|
| - Equipo joven, motivado y con conocimiento técnico sólido<br>- Flexibilidad para adaptarse rápidamente a cambios<br>- Enfoque en nichos creativos del mercado indie<br>- Infraestructura modular con cuatro instancias especializadas | - Recursos económicos limitados como startup<br>- Poca experiencia empresarial del equipo<br>- HTTPS y backups automáticos aún pendientes | - Mercado de videojuegos indie en constante crecimiento<br>- Tecnologías cloud accesibles y escalables<br>- Apoyo de instituciones locales y regionales | - Competencia intensa de estudios consolidados<br>- Rápidos cambios tecnológicos en la industria<br>- Dependencia de plataformas de distribución |

---

**Metadatos / Fechas:**

- Last update: Junio 7, 2026
- Created: December 3, 2025
