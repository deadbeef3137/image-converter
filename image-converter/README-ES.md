***
### Autor: [@deadbeef3137](https://github.com/deadbeef3137)
***

# Image Converter

## Descripción
Este programa permite convertir imágenes en formato PNG, JPG, GIF, BMP, entre otros, a cualquier otro formato de imagen compatible con la librería PIL (Python Imaging Library).

## Uso
El uso es simple, primero se debe tener instalado Python en el equipo. Luego, descargar el archivo image_converter.py y ejecutarlo en la terminal o en la línea de comandos.

```
python image_converter.py
```

## Entrada
Por defecto, el programa buscará imágenes en el mismo directorio donde se encuentra el archivo image_converter.py. Las imágenes convertidas se guardarán en una carpeta llamada ico_files en el mismo directorio.

Además, el usuario puede especificar el tamaño de la imagen de salida utilizando el parámetro -s o --size. Si se especifica un tamaño, la imagen se redimensionará a ese tamaño antes de ser guardada. Si se especifica full, la imagen se guardará en tamaño original.

```
python image_converter.py -s 128
```

## Salida
El programa también le permite especificar el formato de salida. Para hacer esto, puede utilizar la siguiente estructura:

```
python image_converter.py -s 128 -f png
```

Las imágenes convertidas se guardarán en una carpeta con el nombre del formato de salida seguido de "_files" en el mismo directorio. Por ejemplo, si el formato de salida es PNG, las imágenes se guardarán en una carpeta llamada "png_files".

## Requisitos
- Python 3.x
- La librería PIL (Python Imaging Library)

Para instalar la librería PIL, ejecute en la terminal o en la línea de comandos:

```
pip install pillow
```