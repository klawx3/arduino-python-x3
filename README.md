# Proyecto de conexión a Arduino 🔌 con Python 🐍

Este es un pequeño proyecto que facilita la conexión entre un dispositivo Serial (Arduino Uno o variaciones) con Python.

Incluye su propio hilo de ejecución para dar flexibilidad en su utilización

para utilizar en el código puede ejecutar el archivo `main.py` de ejemplo que esta en el repositorio

## 📨 Uso del proyecto

Clonando el repositorio usando [git](https://git-scm.com/)

```sh
git clone repo
cd repo
```

antes de usar el proyecto se debe descargar las dependencias usando `pip`

> esta librería es solo compatible con Python 3.x

```sh
pip install -r requeriments.txt
```
### 🧪 Probando el proyecto

para probar si funciona *Out of the box* se recomienda primero cargar una aplicación `Echo` en arduino

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  while(Serial.available() > 0){
    char val = (char) Serial.read();
    Serial.println(val);
  }
}
```
#### 🔥 Ejecutando
luego de cargar esta aplicación solo basta con cambiar la variable `puerto` a el utilizado por Arduino, debería obtener la siguiente salida en el programa:
```
> Arduino: Intentando conexión a -> COM3
> Arduino: Iniciando hilo de arduino
> Arduino: Conexion: True
> Dato de arduino: h
> Dato de arduino: o
> Dato de arduino: l
> Dato de arduino: a
```
Esto indicaría que todo esta 👌

