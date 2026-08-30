# Análisis de Spanning Tree: PVST y Rapid PVST

## Topología implementada

Se implementó una red formada por tres switches Cisco 2960 conectados
mediante una topología triangular. Los enlaces entre switches fueron
configurados como troncales para transportar las VLAN 10 y 20.

La VLAN 10 corresponde al área de Ventas y utiliza la red
192.168.15.0/24. La VLAN 20 corresponde al área de Compras y utiliza
la red 192.168.25.0/24.

La conexión triangular proporciona redundancia, pero también crea un
posible bucle de capa 2 si no se utiliza Spanning Tree.

## Comportamiento sin STP

Al desactivar STP se observó que las tramas de broadcast comenzaron a
circular por los enlaces redundantes. Los switches generaban y
reenviaban múltiples copias de las mismas tramas, provocando una
tormenta de broadcast.

También se pudo observar inestabilidad en la comunicación, posibles
pérdidas de paquetes y aprendizaje de direcciones MAC a través de
distintos puertos. Esto sucede porque las tramas Ethernet no poseen un
TTL que las elimine cuando circulan dentro de un bucle.

## Elección del switch raíz

Switch0 fue configurado como switch raíz para las VLAN 10 y 20 mediante
una prioridad de 4096. Los demás switches conservaron la prioridad
predeterminada de 32768.

STP elige como raíz al switch que posea el Bridge ID más bajo. Como
Switch0 tiene la prioridad más baja, fue seleccionado como raíz. Si
todos los switches hubieran tenido la misma prioridad, se habría elegido
el switch con la dirección MAC más baja.

## Puertos bloqueados

Switch1 y Switch2 poseen enlaces directos hacia Switch0. Por esta razón,
estos enlaces funcionan como caminos principales hacia el switch raíz.

En el enlace redundante entre Switch1 y Switch2, uno de los puertos fue
seleccionado como designado y el otro quedó como alternativo/bloqueado.
El puerto bloqueado evita que las tramas circulen indefinidamente por
el triángulo, pero permanece disponible en caso de que falle un enlace
principal.

## Prueba con PVST

Se ejecutó un ping continuo desde PC0 hacia PC1. Mientras el ping se
encontraba activo, se deshabilitó el enlace entre Switch0 y Switch2.

Se perdieron aproximadamente 4 paquetes y la comunicación tardó
aproximadamente 0.05 segundos en recuperarse.

Sí existió convergencia. PVST detectó la falla y cambió el puerto
alternativo desde el estado bloqueado hasta el estado forwarding. Sin
embargo, durante la transición se perdieron varios paquetes.

## Prueba con Rapid PVST

Posteriormente se configuró el modo Rapid PVST en los tres switches y se
repitió exactamente la misma prueba.

Se perdieron aproximadamente 4 paquetes y la comunicación tardó
aproximadamente 0.05 segundos en recuperarse.

Rapid PVST también logró la convergencia, pero lo hizo más rápidamente
que PVST. El protocolo utilizó el puerto alternativo para restablecer el
camino sin esperar todos los temporizadores utilizados por STP
tradicional.

## Conclusión

STP permite implementar enlaces redundantes sin provocar bucles de
capa 2. En condiciones normales, mantiene uno de los caminos bloqueado
y, cuando ocurre una falla, habilita el camino alternativo.

PVST y Rapid PVST evitan los bucles y proporcionan redundancia. La
principal diferencia observada fue el tiempo de convergencia: Rapid
PVST recuperó la conectividad en menos tiempo y provocó una menor
pérdida de paquetes.