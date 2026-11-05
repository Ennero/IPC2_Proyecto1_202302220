# Procesamiento de matrices XML y visualización con Graphviz

Aplicación por consola que carga matrices desde XML, construye representaciones binarias/reducidas con listas enlazadas y genera reportes gráficos y archivos de salida.

## Requisitos

Python 3, paquete graphviz de requirements.txt y Graphviz instalado como programa del sistema (comando dot).

## Ejecución

Los comandos parten de la raíz del repositorio, salvo donde se indica otra terminal.

```bash
python -m pip install -r requirements.txt
python menu.py
```

## Recorrido de demostración

Cargar basico.xml o avanzado.xml desde el menú, procesar la matriz y solicitar un reporte. Los archivos de salida y gráficas se generan en el directorio de ejecución.

## Organización

Carpetas de la entrega: [`Documentacion/`](Documentacion/).

## Alcance y límites

menu.py es el punto de entrada y apuntador.py contiene las estructuras. El paquete Python graphviz no instala por sí solo el ejecutable dot.

## Contexto y licencia

Trabajo académico o de aprendizaje conservado en el portafolio de [Enner Mendizabal](https://github.com/Ennero). Los créditos de los trabajos en grupo se conservan en sus entregas y manuales.

Consultar [LICENSE](LICENSE) para la licencia de la raíz. Las dependencias y los componentes con avisos o licencias propios conservan sus condiciones.
