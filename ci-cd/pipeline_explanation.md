# Explicación del Pipeline

- **Herramienta**: GitHub Actions por su integración nativa con Git y facilidad de uso.
- **Flujo**:
  1. **Build**: Construye la imagen Docker.
  2. **Test**: Ejecuta pruebas unitarias (simuladas).
  3. **Deploy**: Sube la imagen a ECR y actualiza el servicio ECS.
- **Justificación**: Automatiza el despliegue, reduce errores humanos y permite iteraciones rápidas.
