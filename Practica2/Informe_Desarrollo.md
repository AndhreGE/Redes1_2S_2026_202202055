# Informe de desarrollo — Práctica 2: Cayalá

**Estudiante:** Andhre Gonzalez  
**Carnet:** 202202055  
**Curso:** Redes de Computadoras 1  
**Periodo:** Segundo semestre de 2026

## 1. Propósito

Implementar una red para cinco zonas del complejo Cayalá, considerando sus diferencias de tráfico y criticidad.

La red se construyó en Cisco Packet Tracer 8.2.2 con switches Cisco 3560 y 2960, enlaces de cobre y tres PCs funcionales por VLAN de usuarios.

## 2. Investigación y planificación

Se identificaron cinco referencias reales:

- Regus Cayalá: zona corporativa.
- Cayibel: zona gastronómica.
- Cinépolis Cayalá: entretenimiento.
- Nogales de Cayalá: zona residencial.
- Banco Industrial Cayalá: servicios bancarios.

Se asignaron las VLANs 15, 25, 35, 45 y 55. También se incorporaron VLAN 99 para gestión y VLAN nativa, y VLAN 999 para puertos sin uso.

El direccionamiento VLSM se dimensionó para los 157 hosts nominales, aunque la simulación utiliza 15 PCs.

Las estimaciones de tráfico son supuestos académicos relacionados con las actividades de cada zona.

## 3. Implementación

El trabajo se realizó por switches y por zonas:

1. Se construyó la topología y se verificaron los puertos de conexión.
2. Se configuró SW-CORP como switch central.
3. Se creó el dominio VTP 202202055, versión 2.
4. Se establecieron los switches principales como Server y los de acceso como Client.
5. Se configuraron las VLANs y los puertos de usuarios.
6. Se habilitaron las troncales con VLAN nativa 99 y listas explícitas de VLANs permitidas.
7. Se configuró Rapid PVST y la prioridad de cada raíz.
8. Se implementaron cuatro EtherChannels mediante PAgP.
9. Se asignaron los puertos sin uso a VLAN 999 y se apagaron.
10. Se configuraron las direcciones de las PCs y las interfaces SVI.
11. Se habilitó el enrutamiento entre VLANs en SW-CORP.
12. Se comprobaron las comunicaciones y se guardaron las configuraciones.

La configuración CLI se documenta en [Configuracion_CLI.md](Configuracion_CLI.md).

## 4. Dificultades y ajustes

Durante las pruebas del acceso bancario se observaron pérdidas de conectividad al restaurar miembros del EtherChannel Po3.

Se revisaron los estados de EtherChannel y STP, las troncales, las direcciones IP, las tablas MAC y ARP, y las configuraciones de los dos switches.

No se estableció con certeza una causa única para los fallos observados.

La solución final del acceso bancario utiliza dos troncales independientes:

- Fa0/24: principal, costo STP 19.
- Fa0/23: respaldo, costo STP 25.

Se mantuvo Rapid PVST para controlar la redundancia y prevenir ciclos. El enlace temporal de diagnóstico por Fa0/22 se retiró de la topología final.

La prueba de caída del enlace principal Fa0/24 del área bancaria fue omitida. Por ello, el informe no certifica la conmutación bancaria mediante esa prueba.

## 5. Resultados finales

El archivo final contiene:

| Elemento | Resultado |
|---|---|
| Switches | 10 |
| PCs funcionales | 15 |
| VLANs de usuarios | 5 |
| VLAN de gestión y nativa | 99 |
| VLAN para puertos sin uso | 999 |
| EtherChannels | 4, con PAgP |
| Enlaces Ethernet físicos | 30 |
| VTP | Versión 2, revisión 113 en los diez switches |
| SVI en SW-CORP | Seis interfaces observadas en estado up/up |
| Configuraciones guardadas | Running-config y startup-config coinciden en los diez switches |

En las pruebas finales se confirmó respuesta desde PC-CORP-01 hacia las otras catorce PCs.

También se confirmó comunicación desde PC-CORP-02 y PC-CORP-03 hacia PC-BANCO-03.

La red dispone de seis redes directamente conectadas en SW-CORP. La segmentación separa los dominios de broadcast y las SVI permiten la comunicación entre VLANs.

## 6. Alcance y limitaciones

El diseño permite estudiar segmentación, agregación de enlaces, redundancia y enrutamiento entre VLANs.

La capacidad de los enlaces se describe de forma teórica; no se realizaron mediciones de rendimiento.

La redundancia física no elimina la dependencia de SW-CORP como único equipo de enrutamiento.

Los resultados de ping corresponden al funcionamiento normal. La prueba de caída de Fa0/24 del área bancaria no forma parte de la validación final.

## 7. Entregables

- [Archivo Packet Tracer](Cayala_202202055_Final.pkt).
- [Manual técnico](Manual_Tecnico.md).
- [Configuración CLI](Configuracion_CLI.md).
- Este informe de desarrollo.
- Capturas de evidencia dentro de la carpeta `evidencias`.