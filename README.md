Markdown
# Tarea 3.0 - Sistema de Inventario CI/CD

Este proyecto es una aplicación de gestión de inventario simple en Python, configurada con **pruebas automatizadas** (pytest) y un **pipeline de CI/CD** mediante GitHub Actions que publica una imagen Docker en el registro de paquetes de GitHub (GHCR).

## 🚀 Estructura del Proyecto
```text
PAGE.DEVOPS
├── .github/workflows/python-application.yml  # Configuración CI/CD
├── app.py              # Lógica del inventario
├── test_app.py         # Pruebas unitarias
├── requirements.txt    # Dependencias del proyecto
├── Dockerfile          # Configuración de la imagen Docker
└── README.md           # Documentación
🛠️ Tecnologías Utilizadas
Lenguaje: Python 3.12

Testing: Pytest

Contenedores: Docker

CI/CD: GitHub Actions

📦 Cómo ejecutar localmente
Clonar el repositorio:

Bash
git clone https://github.com/landerz180603/Taller-3-.git
Instalar dependencias:

Bash
pip install -r requirements.txt
Ejecutar las pruebas:

Bash
pytest
Ejecutar la aplicación:

Bash
python app.py
🐳 Docker
Para construir y ejecutar la imagen localmente:

Bash
docker build -t ejercicio:3.0.0 .
docker run ejercicio:3.0.0
🔄 CI/CD Pipeline
El proyecto incluye un flujo de trabajo de GitHub Actions que realiza automáticamente:

Verificación del código.

Ejecución de pruebas unitarias.

Construcción y publicación de la imagen Docker en GitHub Container Registry (GHCR).

Nota: Puedes verificar el estado de los despliegues en la pestaña Actions de este repositorio.


---

### Tips adicionales para tu entrega:

1.  **Captura de pantalla:** Para la sección de "Captura de GitHub Actions", te recomiendo tomar una captura donde se vea la marca de verificación verde (`✔`) en todos los pasos del job `build-test-deploy`. Guárdala como `workflow_success.png` en la raíz de tu proyecto.
2.  **Visibilidad de la imagen:** Recuerda que para que tu imagen publicada en GHCR sea visible públicamente, a veces es necesario configurar los permisos en los ajustes de tu repositorio o de tu cuenta de GitHub (Package settings: *Change package visibility to Public*).
3.  **URL de entrega:** Asegúrate de que el repositorio sea **Público** (como solicitaba la tarea), de lo contrario, el profesor no podrá ver ni el código ni los resultados de las Actions.

¿Te gustaría que te ayude a redactar algún mensaje específico para enviar al profesor junto con el link del reposito