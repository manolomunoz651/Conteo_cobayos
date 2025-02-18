# Conteo_cobayos
Detector y Contador de Cobayos (Cuyes) con YOLOv11 Este proyecto utiliza un dataset propio para entrenar un modelo basado en YOLOv11, diseñado para la detección y conteo de cobayos (cuyes). Implementado en Google Colab, el flujo incluye Python, OpenCV y técnicas avanzadas de visión por computadora. Ideal para aplicaciones en agricultura.

¡Por supuesto! Aquí tienes un ejemplo de un archivo **README.md** bien estructurado y profesional para tu repositorio. Este archivo incluye una descripción general del proyecto, detalles técnicos, instrucciones de uso y los datos sobre los conjuntos de entrenamiento, prueba y validación.

---

# Detector y Contador de Cobayos (Cuyes) con YOLOv11

Este proyecto implementa un modelo de detección y conteo de cobayos (cuyes) utilizando **YOLOv11**, un algoritmo avanzado de visión por computadora. El modelo fue entrenado con un dataset propio, diseñado específicamente para identificar y contar cobayos en imágenes. Este trabajo tiene aplicaciones potenciales en agricultura, investigación científica y automatización de granjas.

---

## Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Dataset](#dataset)
3. [Tecnologías Utilizadas](#tecnologías-utilizadas)
4. [Requisitos](#requisitos)
5. [Instrucciones de Uso](#instrucciones-de-uso)
6. [Resultados](#resultados)

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
- **Roboflow**: Herramienta para etiquetar las imágenes del dataset.  

---

## Requisitos

Para ejecutar este proyecto, necesitarás lo siguiente:

1. **Google Colab** (recomendado para entrenamiento).  
2. **Python** instalado en tu sistema.  
3. Las siguientes bibliotecas de Python:  
   - `opencv-python`  
   - `ultralytics` (para YOLOv11)  


Puedes instalar las dependencias necesarias ejecutando el siguiente comando:

```bash
pip install opencv-python ultralytics 
```

---

## Instrucciones de Uso

1. **Preparar el Dataset**  
   Asegúrate de tener el dataset organizado en las carpetas `train`, `val` y `test`. Si deseas usar tu propio dataset, etiqueta las imágenes utilizando la herramienta **Roboflow**.

2. **Entrenar el Modelo**  
   Sube el código a Google Colab y ejecuta el script de entrenamiento. Asegúrate de configurar correctamente las rutas del dataset.

3. **Probar el Modelo**  
   Una vez entrenado, puedes probar el modelo cargando imágenes de prueba y visualizando las detecciones.

---

## Resultados

El modelo entrenado logró un rendimiento sólido en la detección y conteo de cobayos. A continuación, se muestran algunos ejemplos de las predicciones realizadas por el modelo:

<img src="https://github.com/manolomunoz651/Conteo_cobayos/blob/main/photo_5017113257835605701_w.jpg" width="400" alt="Matriz de confusión">

<img src="https://github.com/manolomunoz651/Conteo_cobayos/blob/main/photo_5017113257835605702_w.jpg" width="600" alt="Ejemplo de detección de cobayos">

---

Si necesitas personalizar alguna sección o agregar más detalles, no dudes en decírmelo. ¡Espero que este README sea útil para tu repositorio! 😊
