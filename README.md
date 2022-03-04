# CONVERTIR PX A IN A CM A MM

Píxeles por pulgada y otras consideraciones:
Es probable que, si estás buscando información para pasar de píxeles a cm, hayas visto en muchos sitios las siglas **DPI**, **PPI** o **PPP**. ¿Qué significan?
**DPI** corresponde a las siglas de Dots Per Inch (puntos por pulgada) mientras que **PPP** hace referencia a píxeles por pulgada. Ambos términos hacen referencia a la resolución y son exactamente iguales. En algunos sitios puede que también veas PPI (Points Per Inch) pero de nuevo, hace referencia a los mismos conceptos.
Cuando hablamos de **píxeles por pulgada** nos referimos a la resolución, es decir, la **cantidad de píxeles que hay dentro de una pulgada** o lo que es lo mismo, 2,54 centímetros.
De lo anterior deducimos que **cuantos más píxeles haya por pulgada, mayor será la calidad** de la imagen. El claro ejemplo lo tenemos en las pantallas de los tablets y móviles de última generación con resoluciones de hasta 4k, ofreciendo una densidad de píxeles por pulgada muy alta con los que obtenemos un grado de definición difícil de superar.

![alt dpi](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/dpi.jpg?raw=true)


Si quieres **imprimir una fotografía** que tienes en el ordenador, es conveniente que al menos lo hagas con una resolución de 150 píxeles por pulgada para obtener unos resultados aceptables. **A partir de 300 ppp** conseguimos resultados mejores.


Si quieres saber cómo pasar de píxeles a centímetros, a continuación, te lo vamos a explicar paso a paso.
De partida tenemos que tener los siguientes datos para poder hacer la conversión:

-  Altura y anchura de la foto en píxeles
-  Resolución en píxeles por pulgada

A continuación, simplemente tenemos que **realizar las siguientes operaciones:**

[^1]:**o con el factor de : 1/2.54  =  0.393701**

|Formula| Resultado en Pulgadas|
| ------------ | ----------- |
| Width / ppp  |     Inch    |
| Height / ppp |     Inch    |

#### Ejemplo:
|  Width   |  Heigh  |   PPP  |
| -------- | ------- | ------ |
| 1700 | 2200 |  200  |


>![alt calc1](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/calc1.png?raw=true)
>
>![alt calc2](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/calc2.png?raw=true)
>
> **Resultado:**
> **(8.5 x 11)in**
> 

Una vez que hemos hecho las divisiones anteriores, tenemos que pasar la **medida en pulgadas a centímetros.**
| px | ppp | fact[^1]|
| -- | --- | ------- |
| 1700 | 200 | **0.393701** |
| 2200 | 200 | **0.393701** |

> **Conversion:**
> 
>![alt calc3](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/calc3.png?raw=true)
> 
>![alt calc4](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/calc4.png?raw=true)
>
>![alt calc5](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/calc5.png?raw=true)

>**Convertir de cm a mm**
>
>![alt calc6](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/calc6.png?raw=true)

>[^1]:> **Factor obtendio de:** 
>![alt calc7](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/calc7.png?raw=true)

### Cómo convertir de in a píxeles
Para convertir de in a píxeles tenemos que hacer la operación contraria a la anterior, es decir
- Ancho (in) x ppp
- Alto (in) x ppp
> 
> ![alt calc8](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/calc8.png?raw=true)
> 
> ![alt calc9](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/calc9.png?raw=true)


### Cómo convertir de cm a píxeles
Para convertir de cm a píxeles tenemos que hacer la operación contraria a la anterior, es decir:
- Alto (cm) x ppp x 0,393701[^1]
- Ancho (cm) x ppp x 0,393701[^1]
> ![alt calc10](https://github.com/yetto-tools/calcpxtocm/blob/main/assets/calc10.png?raw=true)