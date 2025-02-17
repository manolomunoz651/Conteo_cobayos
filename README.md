# Conteo_cobayos
Detector y Contador de Cobayos (Cuyes) con YOLOv11 Este proyecto utiliza un dataset propio para entrenar un modelo basado en YOLOv11, diseñado para la detección y conteo de cobayos (cuyes). Implementado en Google Colab, el flujo incluye Python, OpenCV y técnicas avanzadas de visión por computadora. Ideal para aplicaciones en agricultura.

¡Por supuesto! Aquí tienes un ejemplo de un archivo **README.md** bien estructurado y profesional para tu repositorio. Este archivo incluye una descripción general del proyecto, detalles técnicos, instrucciones de uso y los datos sobre los conjuntos de entrenamiento, prueba y validación.

---

# Detector y Contador de Cobayos (Cuyes) con YOLOv11

![GitHub Logo](https://via.placeholder.com/800x200?text=YOLOv11+Cobayos+Detector)  
*(Puedes reemplazar la URL anterior con una imagen representativa de tu proyecto si deseas)*

Este proyecto implementa un modelo de detección y conteo de cobayos (cuyes) utilizando **YOLOv11**, un algoritmo avanzado de visión por computadora. El modelo fue entrenado con un dataset propio, diseñado específicamente para identificar y contar cobayos en imágenes. Este trabajo tiene aplicaciones potenciales en agricultura, investigación científica y automatización de granjas.

---

## Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Dataset](#dataset)
3. [Tecnologías Utilizadas](#tecnologías-utilizadas)
4. [Requisitos](#requisitos)
5. [Instrucciones de Uso](#instrucciones-de-uso)
6. [Resultados](#resultados)
7. [Contribuciones](#contribuciones)
8. [Licencia](#licencia)

---

## Descripción del Proyecto

El objetivo de este proyecto es desarrollar un sistema automatizado capaz de detectar y contar cobayos (cuyes) en imágenes. Para lograrlo, se utilizó **YOLOv11**, un modelo de última generación para detección de objetos, junto con herramientas como **Google Colab**, **Python**, y **OpenCV**.

Este modelo puede ser utilizado en entornos agrícolas o de investigación para monitorear y gestionar poblaciones de cobayos de manera eficiente.

---

## Dataset

El dataset utilizado en este proyecto fue creado específicamente para entrenar el modelo. Está compuesto por imágenes etiquetadas que contienen cobayos en diferentes escenarios. A continuación, se detalla la distribución del dataset:

- **Conjunto de Entrenamiento**: 267 imágenes  
- **Conjunto de Validación**: 25 imágenes  
- **Conjunto de Prueba**: 13 imágenes  

El dataset fue dividido cuidadosamente para garantizar un entrenamiento equilibrado y evaluar el rendimiento del modelo de manera precisa.

---

## Tecnologías Utilizadas

- **YOLOv11**: Modelo de detección de objetos utilizado para identificar cobayos.  
- **Google Colab**: Entorno de desarrollo en la nube utilizado para entrenar el modelo.  
- **Python**: Lenguaje de programación principal utilizado en el proyecto.  
- **OpenCV**: Biblioteca utilizada para procesamiento de imágenes y visualización de resultados.  
- **LabelImg**: Herramienta para etiquetar las imágenes del dataset.  

---

## Requisitos

Para ejecutar este proyecto, necesitarás lo siguiente:

1. **Google Colab** (recomendado para entrenamiento).  
2. **Python 3.x** instalado en tu sistema.  
3. Las siguientes bibliotecas de Python:  
   - `opencv-python`  
   - `torch`  
   - `ultralytics` (para YOLOv11)  
   - `matplotlib` (opcional, para visualización).  

Puedes instalar las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install opencv-python torch ultralytics matplotlib
```

---

## Instrucciones de Uso

1. **Clonar el Repositorio**  
   Clona este repositorio en tu máquina local usando el siguiente comando:

   ```bash
   git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
   ```

2. **Preparar el Dataset**  
   Asegúrate de tener el dataset organizado en las carpetas `train`, `val` y `test`. Si deseas usar tu propio dataset, etiqueta las imágenes utilizando una herramienta como **LabelImg**.

3. **Entrenar el Modelo**  
   Sube el código a Google Colab y ejecuta el script de entrenamiento. Asegúrate de configurar correctamente las rutas del dataset.

4. **Probar el Modelo**  
   Una vez entrenado, puedes probar el modelo cargando imágenes de prueba y visualizando las detecciones.

---

## Resultados

El modelo entrenado logró un rendimiento sólido en la detección y conteo de cobayos. A continuación, se muestran algunos ejemplos de las predicciones realizadas por el modelo:

*(Aquí puedes agregar imágenes o gráficos mostrando ejemplos de detección. Puedes usar Markdown para insertar imágenes: `![Descripción](URL_IMAGEN)`)*

---

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.  
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).  
3. Realiza tus cambios y haz commit (`git commit -m "Añadir nueva funcionalidad"`).  
4. Envía tus cambios (`git push origin feature/nueva-funcionalidad`).  
5. Abre un pull request.  

---

## Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

Si necesitas personalizar alguna sección o agregar más detalles, no dudes en decírmelo. ¡Espero que este README sea útil para tu repositorio! 😊
