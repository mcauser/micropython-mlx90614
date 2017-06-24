# MicroPython MLX90614

A MicroPython library for interfacing with a MLX90614 IR temperature sensor.

![demo](docs/GY-906-MLX90614.jpg)

#### Examples

Basic measurement

```
import mlx90614
from machine import I2C, Pin
i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = mlx90614.MLX90614(i2c)
print(sensor.read_ambient_temp())
print(sensor.read_object_temp())
```

Continuous measurement

```
import time
import mlx90614
from machine import I2C, Pin
i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = mlx90614.MLX90614(i2c)

while True:
	print(sensor.read_ambient_temp(), sensor.read_object_temp())
	time.sleep_ms(500)
```

For full documentation see http://micropython-mlx90614.rtfd.io/.
