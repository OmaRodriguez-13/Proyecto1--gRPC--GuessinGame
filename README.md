# [PROYECTO1: gRPC: GUESSING GAME]

## Descripción general

El proyecto consiste en un juego de adivinanza númerica:

1. El servidor se encarga de generar un número aleatorio entre 1 y 100.
2. El o los cliente(s) tendrán oportunidades ilimitadas hasta adivinar el número. 

## Instalación y Configuración

### Source code

Descargar el zip que contiene los archivos fuente del proyecto.

### Vía git 

```bash
git clone https://github.com/OmaRodriguez-13/Proyecto1--gRPC--GuessinGame.git
```

## Guía Rápida

### Requerimientos

- Importante: Conexión a la misma red.
- Desactivar Firewall de Windows para evitar cualquier error de conexión.
- Tener libre el puerto 50051.
- Editor de código (por ejemplo: [Visual Studio Code]).
- Python 3.11.2

#### grpcio:

```bash
pip install grpcio
```

### Instrucciones de uso

Para el caso de este proyecto no es necesario utilizar algún comando propio de la tecnología empleada (gRPC), puesto que el proyecto ya contiene los archivos generados (guess_pb2_grpc.py y guess_pb2.py) a partir del archivo fuente (guess.proto).

[![proto.png](https://i.postimg.cc/3wzdpb2z/proto.png)](https://postimg.cc/FfgrXpWx)

## Ejecución

Si no conoce su dirección ip de su equipo, puede usar el siguiente comando en cmd.

```bash
ipconfig
```

### Servidor

Abra un terminal y ejecute [server.py] con alguno de los siguiente comandos:

```bash
py server.py
```

```bash
python server.py
```

### Cliente

En otra terminal, ejecute [gui.py] con alguno de los siguientes comandos:

```bash
py gui.py
```

```bash
python gui.py
```

En la ventana siguiente deberá ingresar la ip del equipo que funciona como servidor.

[![ip.png](https://i.postimg.cc/SQ3DRyXG/ip.png)](https://postimg.cc/pyQD1MJ9)

## Testeo

### Servidor [server.py]

El servidor mostrará el número aleatorio generado. Así como el puerto que utilizará para la comunicación (50051 predeterminado).  

[![random.png](https://i.postimg.cc/CL6YznGQ/random.png)](https://postimg.cc/crYPzH5R)

[![server.png](https://i.postimg.cc/Gh9nw3WJ/server.png)](https://postimg.cc/crqbfW4r)

### Cliente [gui.py]

[![gui.png](https://i.postimg.cc/brhMGprr/gui.png)](https://postimg.cc/MM9tNkyJ)

Ya iniciado el programa cliente, el usuario deberá ir introduciendo números uno a uno hasta lograr adivinar el número secreto.
Nota: No hay límite de intentos. Únicamente irá recibiendo mensajes de si el número es mayor o menor al que haya ingresado.

[![mayor.png](https://i.postimg.cc/vB8Sr3ML/mayor.png)](https://postimg.cc/Y4V3kNvh)

[![menor.png](https://i.postimg.cc/wMZfdzN0/menor.png)](https://postimg.cc/BP5cxdMK)

[![acierto.png](https://i.postimg.cc/SRBrvr0P/acierto.png)](https://postimg.cc/1VKwgD30)
