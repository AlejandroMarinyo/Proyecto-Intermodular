# Conclusiones y mejoras futuras

## Conclusiones

El proyecto CreviPlay ha permitido diseñar e implementar desde cero una infraestructura de TI completa para un estudio de videojuegos independiente, cubriendo los objetivos planteados en la fase de planificación y demostrando competencias adquiridas en los módulos de ASIR.

### Logros principales

1. **Infraestructura modular en AWS:** Se desplegaron **cuatro instancias EC2** con roles claramente definidos (WordPress, aplicación PHP, DNS y base de datos), lo que facilita el mantenimiento independiente de cada servicio y reduce el impacto de posibles fallos.

2. **Contenerización con Docker:** El uso de **Docker Compose** en WordPress, la aplicación PHP y la base de datos ha demostrado ser una solución eficaz para crear entornos reproducibles, portables y fáciles de gestionar con un único comando.

3. **Separación de capas:** La migración de MySQL desde el servidor web a una instancia dedicada (`172.31.17.200`), con acceso restringido por Security Group, refuerza la seguridad aplicando el principio de **menor privilegio** y desacopla la capa de datos de la capa de aplicación.

4. **Servicios de red propios:** La configuración de un servidor **DNS con BIND** en instancia independiente proporciona control total sobre la resolución de nombres del proyecto, alineada con las Elastic IPs de cada servicio.

5. **Plataforma web dual:** La combinación de **WordPress** (CMS corporativo) y **aplicación PHP** (gestión del catálogo) cubre tanto la presencia pública del estudio como la administración interna de usuarios y videojuegos.

6. **Documentación automatizada:** La publicación continua en **GitHub Pages** con MkDocs garantiza que la documentación del proyecto esté siempre actualizada y accesible.

### Dificultades encontradas

- La **reestructuración de la base de datos** (pasar de un despliegue monolítico web+MySQL a instancias separadas) requirió planificar una migración con volcado previo (`backup.sql`) y actualizar la configuración de conexión en Docker Compose y `config.php`.
- La **configuración de Security Groups** entre instancias exigió pruebas de conectividad cuidadosas para garantizar que la aplicación PHP pudiera acceder a MySQL por IP privada sin exponer el puerto 3306 a internet.
- La **gestión de costes en AWS** obligó a seleccionar tipos de instancia adecuados (`t2.medium`, `t3.small`) y apagar recursos fuera del horario de laboratorio.

## Mejoras futuras

| Área | Mejora propuesta | Prioridad |
|------|------------------|-----------|
| **Seguridad** | Configurar certificados **SSL/TLS** (Let's Encrypt o AWS Certificate Manager) para habilitar HTTPS en WordPress y la aplicación PHP | Alta |
| **Backups** | Automatizar copias de seguridad diarias de MySQL con `cron` + `mysqldump` y almacenamiento en S3 | Alta |
| **Monitorización** | Implementar alertas con **CloudWatch** para CPU, memoria y disponibilidad de los servicios | Media |
| **Alta disponibilidad** | Evaluar despliegue multi-AZ o balanceador de carga (ELB) para la capa web | Baja |
| **CI/CD** | Integrar despliegue automatizado de la aplicación PHP y actualizaciones de WordPress | Media |
| **Dominio propio** | Registrar un dominio (`creviplay.com`) y apuntar los registros DNS del servidor BIND | Media |
| **Optimización** | Implementar caché (Redis o plugin de caché en WordPress) y CDN para recursos estáticos | Baja |

## Valoración final

El proyecto ha cumplido con la mayoría de los requisitos funcionales planteados, dejando como pendientes la automatización de backups y la implementación de HTTPS. La arquitectura resultante es sólida, modular y preparada para evolucionar conforme crezcan las necesidades del estudio CreviPlay.
