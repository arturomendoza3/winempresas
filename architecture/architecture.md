# Arquitectura de la Solución

## Componentes
- **S3**: Almacenamiento de imágenes por su escalabilidad y bajo costo.
- **ALB**: Balanceo de carga para alta disponibilidad (multi-AZ).
- **ECS Fargate**: Contenedores sin gestión de servidores, ideal para picos de tráfico.
- **DynamoDB**: Base NoSQL para rapidez en consultas y escalabilidad.
- **CloudWatch**: Monitoreo de logs y métricas para identificar fallos.

## Escalado Automático
- Métricas: CPU > 70% o latencia > 500ms.
- Políticas: Aumentar 2 tareas ECS por evento, reducir a 1 tarea en calma.

## Seguridad
- **VPC**: Subredes privadas para ECS y DynamoDB, públicas para ALB.
- **IAM**: Roles específicos para ECS y S3 con permisos mínimos.
- **Grupos de Seguridad**: Solo tráfico HTTP/HTTPS permitido al ALB.
