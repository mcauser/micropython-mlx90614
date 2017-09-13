Usage Examples
**************

Connect your sensor in following way:

    * ``vin`` ↔ ``3V``
    * ``gnd`` ↔ ``gnd``
    * ``scl`` ↔ ``gpio5``
    * ``sda`` ↔ ``gpio4``

Now, to make basic measurement::

    import mlx90614
    from machine import I2C, Pin
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    sensor = mlx90614.MLX90614(i2c)
    print(sensor.read_ambient_temp())
    print(sensor.read_object_temp())
    if sensor.dual_zone:
        print(sensor.object2_temp)

To perform continuous measurement::

    import time
    while True:
        print(sensor.read_ambient_temp(), sensor.read_object_temp())
        time.sleep_ms(500)

There are some useful properties:
    * ``.dual_zone`` - set to ``True`` if the sensor has two thermopiles
    * ``.ambient_temp`` - equivalent to read_ambient_temp(), also works for object and object2
