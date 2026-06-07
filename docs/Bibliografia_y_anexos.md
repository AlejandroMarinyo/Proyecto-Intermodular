# Bibliografía y anexos

## Bibliografía

### Infraestructura cloud (AWS)

- Amazon Web Services. (2024). *Amazon EC2 User Guide*. https://docs.aws.amazon.com/ec2/
- Amazon Web Services. (2024). *Amazon VPC User Guide*. https://docs.aws.amazon.com/vpc/
- Amazon Web Services. (2024). *Security Groups for Your VPC*. https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html

### Contenedores y Docker

- Docker Inc. (2024). *Docker Documentation*. https://docs.docker.com/
- Docker Inc. (2024). *Compose file reference*. https://docs.docker.com/compose/compose-file/
- Turnbull, J. (2021). *The Docker Book* (Edición actualizada). James Turnbull.

### WordPress y PHP

- WordPress Foundation. (2024). *WordPress Codex*. https://codex.wordpress.org/
- PHP Group. (2024). *PHP Manual*. https://www.php.net/manual/es/
- The Apache Software Foundation. (2024). *Apache HTTP Server Documentation*. https://httpd.apache.org/docs/

### Base de datos MySQL

- Oracle Corporation. (2024). *MySQL 8.0 Reference Manual*. https://dev.mysql.com/doc/refman/8.0/en/
- phpMyAdmin Team. (2024). *phpMyAdmin Documentation*. https://docs.phpmyadmin.net/

### Servicios de red (DNS)

- Internet Systems Consortium. (2024). *BIND 9 Administrator Reference Manual*. https://bind9.readthedocs.io/
- RFC 1034 — Domain Names — Concepts and Facilities. IETF. https://datatracker.ietf.org/doc/html/rfc1034
- RFC 1035 — Domain Names — Implementation and Specification. IETF. https://datatracker.ietf.org/doc/html/rfc1035

### Seguridad

- OWASP Foundation. (2024). *OWASP Top Ten*. https://owasp.org/www-project-top-ten/
- NIST. (2024). *Cybersecurity Framework*. https://www.nist.gov/cyberframework

### Documentación del proyecto

- Documentación MkDocs Material. https://squidfunk.github.io/mkdocs-material/
- Repositorio del proyecto: https://github.com/AlejandroMarinyo/Proyecto-Intermodular

---

## Anexos

### Anexo A – Topología de red

La infraestructura final se compone de cuatro instancias EC2 dentro de una VPC con red privada `172.31.0.0/16`:

| Instancia | Rol | IP privada | IP pública |
|-----------|-----|------------|------------|
| 1 | WordPress | Red VPC | `32.192.151.244` |
| 2 | Aplicación PHP | `172.31.79.239` | `18.210.185.204` |
| 3 | DNS (BIND) | Red VPC | Elastic IP dedicada |
| 4 | MySQL + phpMyAdmin | `172.31.17.200` | — |

### Anexo B – Parámetros de conexión a la base de datos

| Parámetro | Valor |
|-----------|-------|
| **DB_HOST** | `172.31.17.200` |
| **DB_USER** | `root` |
| **DB_PASSWORD** | `rootpass` |
| **DB_NAME** | `EstudioVideojuegos` |

### Anexo C – Puertos y servicios

| Instancia | Puerto | Protocolo | Servicio |
|-----------|--------|-----------|----------|
| WordPress | 22 | TCP | SSH |
| WordPress | 80 | TCP | HTTP |
| WordPress | 443 | TCP | HTTPS |
| Aplicación PHP | 22 | TCP | SSH |
| Aplicación PHP | 80 | TCP | HTTP (Apache/PHP) |
| Aplicación PHP | 443 | TCP | HTTPS |
| DNS | 22 | TCP | SSH |
| DNS | 53 | UDP/TCP | BIND |
| Base de datos | 22 | TCP | SSH |
| Base de datos | 3306 | TCP | MySQL |
| Base de datos | 8080 | TCP | phpMyAdmin |

### Anexo D – Estructura del repositorio

```
Proyecto-Intermodular/
├── docs/                          # Documentación MkDocs
│   ├── Introduccion.md
│   ├── Diseño_y_Planificacion.md
│   ├── Desarrollo.md
│   ├── Resultados.md
│   ├── Conclusiones.md
│   ├── Bibliografia_y_anexos.md
│   └── imagenes/                  # Capturas del despliegue
├── frontend/                      # Prototipo HTML/CSS/JS
│   ├── index.html
│   ├── css/styles.css
│   └── js/script.js
├── .github/workflows/             # CI/CD para GitHub Pages
│   └── deploy-pages.yml
├── mkdocs.yml                     # Configuración del sitio
└── requirements.txt               # Dependencias Python (MkDocs)
```

### Anexo E – Enlaces de gestión del proyecto

- **Trello:** [Tablero del proyecto](https://trello.com/invite/b/692dd6254cc1eb9200f5c982/ATTI7a99346f596d27f1b6ba5ae0d74a60ff4779E02B/proyecto-intermodular)
- **Documentación publicada:** https://AlejandroMarinyo.github.io/Proyecto-Intermodular/
- **Repositorio GitHub:** https://github.com/AlejandroMarinyo/Proyecto-Intermodular

### Anexo F – Equipo del proyecto

| Rol | Responsable |
|-----|-------------|
| Líder de proyecto | Alejandro Mariño |
| Administrador de sistemas | Iker Sanchez |
| Desarrollador web | Alejandro Mariño |
| Administrador de base de datos | Alejandro Mariño, Iker Sanchez |
| Especialista en seguridad | Iker Sanchez |
| Documentador | Alejandro Mariño, Iker Sanchez |
