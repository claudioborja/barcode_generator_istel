from PIL import Image, ImageDraw, ImageFont
import barcode
from barcode.writer import ImageWriter

# Función para generar el código de barras alfanumérico
def generar_codigo_barras(codigo):
    # Crear un objeto Code128 para el código de barras
    codigo_barras = barcode.codex.Code128(codigo, writer=ImageWriter())
    # Guardar el código de barras como una imagen PNG
    codigo_barras_ruta = f"{codigo}.png"
    with open(codigo_barras_ruta, "wb") as f:
        codigo_barras.write(f)
    return codigo_barras_ruta

# Función para crear la imagen PNG final
def crear_imagen(logo, titulo_texto, codigo_barras_ruta, nombre_imagen, font_size):
    # Abrir el logotipo
    logo_img = Image.open(logo)
    codigo_barras = Image.open(codigo_barras_ruta)
    
    # Crear una nueva imagen en blanco
    ancho = logo_img.width + codigo_barras.width + 20
    alto = logo_img.height + 20
    imagen = Image.new('RGB', (ancho, alto), color='white')
    
    # Dibujar el logotipo y el código de barras en la imagen
    imagen.paste(logo_img, (10, 10))
    imagen.paste(codigo_barras, (logo_img.width + 40,60))
    
    
    # Configurar el tamaño del texto del título
    font = ImageFont.truetype("arial.ttf", font_size)

    # Dibujar el título en la imagen sobre el logotipo
    draw = ImageDraw.Draw(imagen)
    texto_ancho, texto_alto = draw.textbbox((0, 0), titulo_texto)[2:]
    x = (imagen.width - texto_ancho) // 3
    y=10
    draw.text((x, y), titulo_texto, fill='black', font=font)
    
    # Guardar la imagen final
    imagen.save(nombre_imagen)

# Leer los códigos desde el archivo de texto
with open("codigos.txt", "r") as file:
    codigos = file.readlines()

# Ejemplo de uso
logo_path = 'logo.png'
titulo_texto = 'UNIDAD ADMINISTRATIVA FINANCIERA'

for codigo_barras_texto in codigos:
    codigo_barras_texto = codigo_barras_texto.strip()  # Eliminar espacios en blanco y saltos de línea
    codigo_barras_ruta = generar_codigo_barras(codigo_barras_texto)
    nombre_imagen = f"{codigo_barras_texto}.png"
    longitud = len(codigo_barras_texto)


    if longitud < 30:
        crear_imagen(logo_path, titulo_texto, codigo_barras_ruta, nombre_imagen, 37)
    else:
        crear_imagen(logo_path, titulo_texto, codigo_barras_ruta, nombre_imagen, 45)
