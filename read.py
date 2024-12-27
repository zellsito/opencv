import cv2
import numpy as np
import sys

# Verificar que se pasaron los parámetros necesarios
if len(sys.argv) < 2:
    print("Error: Debes proporcionar el nombre del archivo de imagen.")
    exit()

# Obtener el nombre del archivo de imagen desde los parámetros
img_path = sys.argv[1]

# Cargar la imagen y la plantilla
img_rgb = cv2.imread(img_path)
template = cv2.imread('aguja.png', 0)

# Verificar si las imágenes se cargaron correctamente
if img_rgb is None or template is None:
    print("Error: No se pudo cargar las imágenes.")
    exit()

# Convertir la imagen a escala de grises
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
w, h = template.shape[::-1]

# Realizar la coincidencia de plantillas
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.85
loc = np.where(res >= threshold)

# Contar las coincidencias y dibujar rectángulos
match_count = 0
for pt in zip(*loc[::-1]):  # Las coordenadas de las coincidencias
    match_count += 1
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)  # Dibuja un rectángulo en la imagen

# Guardar la imagen con los rectángulos dibujados
cv2.imwrite('res.png', img_rgb)

# Mostrar el número de coincidencias
print(f"Found {match_count} matches.")