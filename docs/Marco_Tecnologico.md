# Marco Tecnológico

##Alcance

### **Alcance Técnico**
- **Infraestructura base en AWS:** Implementación sobre Amazon EC2 con instancias optimizadas para desarrollo, red configurada mediante Amazon VPC, subredes públicas/privadas, reglas de seguridad (Security Groups), NACLs y servicios esenciales como DHCP, DNS interno, SSH y control de tráfico mediante AWS Firewall Manager.
- **Sistema de base de datos gestionado:** Uso de Amazon RDS (MySQL o PostgreSQL) con despliegue multi-AZ, backups automáticos, cifrado en reposo (KMS) y gestión de accesos mediante IAM y roles con privilegios mínimos.
- **Aplicación web profesional:** Servidor Apache o Nginx desplegado en EC2, integrando un WordPress personalizado para el portafolio de videojuegos. Almacenamiento de contenido multimedia en Amazon S3 y distribución global mediante Amazon CloudFront.
- **Seguridad y mantenimiento avanzado:** Certificados SSL/TLS gestionados con AWS Certificate Manager, copias de seguridad automatizadas en S3 y Glacier, scripts de automatización en AWS Lambda, y monitorización centralizada del sistema con Amazon CloudWatch.

### **Exclusiones en fase inicial**
Las siguientes funcionalidades quedan excluidas de la fase inicial del proyecto y podrán ser implementadas en futuras iteraciones:

- **Integración con Steam/Epic:** La integración con plataformas de distribución de videojuegos como Steam o Epic Games Store no está contemplada en esta fase inicial.

- **Sistema de descargas:** No se implementará un sistema propio de descarga directa de videojuegos en esta fase.

- **Foros o comentarios:** La funcionalidad de foros de discusión o sistema de comentarios en los videojuegos no está incluida en el alcance inicial.

### **Alcance Temporal**

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
| **Plataforma web con portafolio** | - | ✓ | ✓ | ✓ | ✓ | En desarrollo |
| **Panel de administración** | ✓ | ✓ | ✓ | ✓ | ✓ | En desarrollo |
| **Gestión de Proyectos** | ✓ | ✓ | ✓ | - | ✓ | En desarrollo |
| **Tiempo de carga < 2 segundos** | - | ✓ | ✓ | ✓ | - | Pendiente |
| **Backup diario** | ✓ | ✓ | - | - | ✓ | Pendiente |
| **Seguridad (HTTPS, encriptación)** | ✓ | ✓ | ✓ | ✓ | ✓ | En desarrollo |
| **Crear presencia web profesional** | - | ✓ | ✓ | ✓ | ✓ | En desarrollo |
| **Mostrar los videojuegos** | - | ✓ | ✓ | ✓ | - | En desarrollo |

**Leyenda:**
- ✓ = Módulo relacionado con el requisito
- - = Módulo no relacionado con el requisito
- **Estados:** Pendiente, En desarrollo, Completado

### Roles del equipo

- Líder de proyecto: Alejandro Mariño.
- Administrador de sistemas: Iker Sanchez.
- Desarrollador web: Alejandro Mariño.
- Administrador de base de datos: Alejandro Mariño y Iker Sanchez.
- Especialista en seguridad: Iker Sanchez.
- Documentador: Alejandro Mariño y Iker Sanchez.