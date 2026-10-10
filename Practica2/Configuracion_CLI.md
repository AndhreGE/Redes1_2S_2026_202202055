# Configuración CLI — Práctica 2: Cayalá

**Carnet:** 202202055

Estos bloques documentan la configuración funcional para reconstruir el laboratorio en equipos nuevos, con las conexiones indicadas en el manual.

Cada bloque corresponde exclusivamente al switch señalado. El archivo final entregado ya tiene su configuración guardada.

Configurar primero SW-CORP y después los demás equipos. Los clientes VTP reciben las VLANs mediante las troncales.

Las IP de las PCs se introducen desde **Desktop → IP Configuration**, según la tabla del manual.

## 1. SW-CORP — Cisco 3560

```text
enable
configure terminal
hostname SW-CORP
no ip domain-lookup
ip routing

vtp domain 202202055
vtp password Cayala2026
vtp version 2
vtp mode server

vlan 15
 name CORPORATIVA
exit
vlan 25
 name CAYIBEL
exit
vlan 35
 name CINE
exit
vlan 45
 name RESIDENCIAL
exit
vlan 55
 name BANCO
exit
vlan 99
 name GESTION
exit
vlan 999
 name BLACKHOLE
exit

spanning-tree mode rapid-pvst
spanning-tree vlan 15,99 priority 4096
spanning-tree vlan 25,35,45,55 priority 8192

interface range fa0/1 - 2
 description MIEMBRO_PO1_A_SW_CAYIBEL
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,55,99
 switchport nonegotiate
 channel-group 1 mode desirable
 no shutdown
exit

interface port-channel 1
 description ETHERCHANNEL_A_SW_CAYIBEL
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,55,99
 switchport nonegotiate
 no shutdown
exit

interface range fa0/3 - 4
 description MIEMBRO_PO2_A_SW_RES
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 45,99
 switchport nonegotiate
 channel-group 2 mode desirable
 no shutdown
exit

interface port-channel 2
 description ETHERCHANNEL_A_SW_RES
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 45,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface fa0/5
 description TRONCAL_A_SW_BANCO
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,55,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface fa0/6
 description TRONCAL_A_SW_CINE
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 35,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface fa0/10
 description PC_CORP_01
 switchport mode access
 switchport access vlan 15
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface range fa0/23 - 24
 description MIEMBROS_PO3_SW_CORP_ACC
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 15,99
 switchport nonegotiate
 channel-group 3 mode desirable
 no shutdown
exit

interface port-channel 3
 description TRUNK_SW_CORP_SW_CORP_ACC
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 15,99
 switchport nonegotiate
 no shutdown
exit

interface range fa0/7 - 9
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range fa0/11 - 22
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range gi0/1 - 2
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface vlan 1
 no ip address
exit

interface vlan 15
 description GATEWAY_CORPORATIVA
 ip address 192.168.55.1 255.255.255.192
 no shutdown
exit

interface vlan 25
 description GATEWAY_CAYIBEL
 ip address 192.168.55.129 255.255.255.224
 no shutdown
exit

interface vlan 35
 description GATEWAY_CINE
 ip address 192.168.55.161 255.255.255.240
 no shutdown
exit

interface vlan 45
 description GATEWAY_RESIDENCIAL
 ip address 192.168.55.65 255.255.255.192
 no shutdown
exit

interface vlan 55
 description GATEWAY_BANCO
 ip address 192.168.55.177 255.255.255.240
 no shutdown
exit

interface vlan 99
 description GESTION_SW_CORP
 ip address 192.168.55.193 255.255.255.240
 no shutdown
exit

line console 0
 logging synchronous
exit

end
copy running-config startup-config
```

## 2. SW-CORP-ACC — Cisco 2960

```text
enable
configure terminal
hostname SW-CORP-ACC
no ip domain-lookup

vtp domain 202202055
vtp password Cayala2026
vtp version 2
vtp mode client

spanning-tree mode rapid-pvst

interface fa0/1
 description PC_CORP_02
 switchport mode access
 switchport access vlan 15
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/2
 description PC_CORP_03
 switchport mode access
 switchport access vlan 15
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface range fa0/23 - 24
 description MIEMBROS_PO3_SW_CORP
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 15,99
 switchport nonegotiate
 channel-group 3 mode desirable
 no shutdown
exit

interface port-channel 3
 description TRUNK_SW_CORP_ACC_SW_CORP
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 15,99
 switchport nonegotiate
 no shutdown
exit

interface range fa0/3 - 22
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range gi0/1 - 2
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface vlan 1
 no ip address
 shutdown
exit

interface vlan 99
 description GESTION_SW_CORP_ACC
 ip address 192.168.55.194 255.255.255.240
 no shutdown
exit

ip default-gateway 192.168.55.193

line console 0
 logging synchronous
exit

end
copy running-config startup-config
```

## 3. SW-CAYIBEL — Cisco 2960

```text
enable
configure terminal
hostname SW-CAYIBEL
no ip domain-lookup

vtp domain 202202055
vtp password Cayala2026
vtp version 2
vtp mode server

spanning-tree mode rapid-pvst
spanning-tree vlan 25 priority 4096

interface range fa0/1 - 2
 description MIEMBRO_PO1_A_SW_CORP
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,55,99
 switchport nonegotiate
 channel-group 1 mode desirable
 no shutdown
exit

interface port-channel 1
 description ETHERCHANNEL_A_SW_CORP
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,55,99
 switchport nonegotiate
 no shutdown
exit

interface fa0/3
 description TRONCAL_A_SW_BANCO
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,55,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface fa0/10
 description PC_CAYIBEL_01
 switchport mode access
 switchport access vlan 25
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface range fa0/23 - 24
 description MIEMBRO_PO3_A_SW_CAYIBEL_ACC
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,99
 switchport nonegotiate
 channel-group 3 mode desirable
 no shutdown
exit

interface port-channel 3
 description ETHERCHANNEL_A_SW_CAYIBEL_ACC
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface range fa0/4 - 9
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range fa0/11 - 22
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range gi0/1 - 2
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface vlan 1
 no ip address
 shutdown
exit

interface vlan 99
 description GESTION_SW_CAYIBEL
 ip address 192.168.55.195 255.255.255.240
 no shutdown
exit

ip default-gateway 192.168.55.193

line console 0
 logging synchronous
exit

end
copy running-config startup-config
```

## 4. SW-CAYIBEL-ACC — Cisco 2960

```text
enable
configure terminal
hostname SW-CAYIBEL-ACC
no ip domain-lookup

vtp domain 202202055
vtp password Cayala2026
vtp version 2
vtp mode client

spanning-tree mode rapid-pvst

interface fa0/1
 description PC_CAYIBEL_02
 switchport mode access
 switchport access vlan 25
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/2
 description PC_CAYIBEL_03
 switchport mode access
 switchport access vlan 25
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface range fa0/23 - 24
 description MIEMBRO_PO3_A_SW_CAYIBEL
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,99
 switchport nonegotiate
 channel-group 3 mode desirable
 no shutdown
exit

interface port-channel 3
 description ETHERCHANNEL_A_SW_CAYIBEL
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface range fa0/3 - 22
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range gi0/1 - 2
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface vlan 1
 no ip address
 shutdown
exit

interface vlan 99
 description GESTION_SW_CAYIBEL_ACC
 ip address 192.168.55.196 255.255.255.240
 no shutdown
exit

ip default-gateway 192.168.55.193

line console 0
 logging synchronous
exit

end
copy running-config startup-config
```

## 5. SW-CINE — Cisco 2960

```text
enable
configure terminal
hostname SW-CINE
no ip domain-lookup

vtp domain 202202055
vtp password Cayala2026
vtp version 2
vtp mode server

spanning-tree mode rapid-pvst
spanning-tree vlan 35 priority 4096

interface fa0/1
 description TRONCAL_A_SW_CORP
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 35,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface fa0/10
 description PC_CINE_01
 switchport mode access
 switchport access vlan 35
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/24
 description TRONCAL_A_SW_CINE_ACC
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 35,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface range fa0/2 - 9
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range fa0/11 - 23
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range gi0/1 - 2
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface vlan 1
 no ip address
 shutdown
exit

interface vlan 99
 description GESTION_SW_CINE
 ip address 192.168.55.197 255.255.255.240
 no shutdown
exit

ip default-gateway 192.168.55.193

line console 0
 logging synchronous
exit

end
copy running-config startup-config
```

## 6. SW-CINE-ACC — Cisco 2960

```text
enable
configure terminal
hostname SW-CINE-ACC
no ip domain-lookup

vtp domain 202202055
vtp password Cayala2026
vtp version 2
vtp mode client

spanning-tree mode rapid-pvst

interface fa0/1
 description PC_CINE_02
 switchport mode access
 switchport access vlan 35
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/2
 description PC_CINE_03
 switchport mode access
 switchport access vlan 35
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/24
 description TRONCAL_A_SW_CINE
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 35,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface range fa0/3 - 23
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range gi0/1 - 2
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface vlan 1
 no ip address
 shutdown
exit

interface vlan 99
 description GESTION_SW_CINE_ACC
 ip address 192.168.55.198 255.255.255.240
 no shutdown
exit

ip default-gateway 192.168.55.193

line console 0
 logging synchronous
exit

end
copy running-config startup-config
```

## 7. SW-RES — Cisco 2960

```text
enable
configure terminal
hostname SW-RES
no ip domain-lookup

vtp domain 202202055
vtp password Cayala2026
vtp version 2
vtp mode server

spanning-tree mode rapid-pvst
spanning-tree vlan 45 priority 4096

interface range fa0/1 - 2
 description MIEMBRO_PO2_A_SW_CORP
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 45,99
 switchport nonegotiate
 channel-group 2 mode desirable
 no shutdown
exit

interface port-channel 2
 description ETHERCHANNEL_A_SW_CORP
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 45,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface fa0/10
 description PC_RES_01
 switchport mode access
 switchport access vlan 45
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/24
 description TRONCAL_A_SW_RES_ACC
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 45,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface range fa0/3 - 9
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range fa0/11 - 23
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range gi0/1 - 2
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface vlan 1
 no ip address
 shutdown
exit

interface vlan 99
 description ADMINISTRACION_SW_RES
 ip address 192.168.55.199 255.255.255.240
 no shutdown
exit

ip default-gateway 192.168.55.193

line console 0
 logging synchronous
exit

end
copy running-config startup-config
```

## 8. SW-RES-ACC — Cisco 2960

```text
enable
configure terminal
hostname SW-RES-ACC
no ip domain-lookup

vtp domain 202202055
vtp password Cayala2026
vtp version 2
vtp mode client

spanning-tree mode rapid-pvst

interface fa0/1
 description PC_RES_02
 switchport mode access
 switchport access vlan 45
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/2
 description PC_RES_03
 switchport mode access
 switchport access vlan 45
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/24
 description TRONCAL_A_SW_RES
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 45,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface range fa0/3 - 23
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range gi0/1 - 2
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface vlan 1
 no ip address
 shutdown
exit

interface vlan 99
 description ADMINISTRACION_SW_RES_ACC
 ip address 192.168.55.200 255.255.255.240
 no shutdown
exit

ip default-gateway 192.168.55.193

line console 0
 logging synchronous
exit

end
copy running-config startup-config
```

## 9. SW-BANCO — Cisco 2960

Fa0/23 y Fa0/24 son troncales independientes. No se configura Po3 en este switch.

```text
enable
configure terminal
hostname SW-BANCO
no ip domain-lookup

vtp domain 202202055
vtp password Cayala2026
vtp version 2
vtp mode server

spanning-tree mode rapid-pvst
spanning-tree vlan 55 priority 4096

interface fa0/1
 description TRONCAL_A_SW_CORP
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,55,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface fa0/2
 description TRONCAL_A_SW_CAYIBEL
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 25,55,99
 switchport nonegotiate
 spanning-tree link-type point-to-point
 no shutdown
exit

interface fa0/10
 description PC_BANCO_01
 switchport mode access
 switchport access vlan 55
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/23
 description TRONCAL_RESPALDO_A_SW_BANCO_ACC
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 55,99
 switchport nonegotiate
 speed 100
 duplex full
 spanning-tree cost 25
 spanning-tree link-type point-to-point
 no shutdown
exit

interface fa0/24
 description TRONCAL_PRINCIPAL_A_SW_BANCO_ACC
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 55,99
 switchport nonegotiate
 speed 100
 duplex full
 spanning-tree cost 19
 spanning-tree link-type point-to-point
 no shutdown
exit

interface range fa0/3 - 9
 description PUERTO_SIN_USO
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range fa0/11 - 22
 description PUERTO_SIN_USO
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range gi0/1 - 2
 description PUERTO_SIN_USO
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface vlan 1
 no ip address
 shutdown
exit

interface vlan 99
 description ADMINISTRACION_SW_BANCO
 ip address 192.168.55.201 255.255.255.240
 no shutdown
exit

ip default-gateway 192.168.55.193

line console 0
 logging synchronous
exit

end
copy running-config startup-config
```

## 10. SW-BANCO-ACC — Cisco 2960

La configuración final conserva PortFast por defecto para puertos access. Los enlaces Fa0/23 y Fa0/24 son troncales y participan en STP.

```text
enable
configure terminal
hostname SW-BANCO-ACC
no ip domain-lookup

vtp domain 202202055
vtp password Cayala2026
vtp version 2
vtp mode client

spanning-tree mode rapid-pvst
spanning-tree portfast default

interface fa0/1
 description PC_BANCO_02
 switchport mode access
 switchport access vlan 55
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/2
 description PC_BANCO_03
 switchport mode access
 switchport access vlan 55
 spanning-tree portfast
 spanning-tree bpduguard enable
 no shutdown
exit

interface fa0/23
 description TRONCAL_RESPALDO_A_SW_BANCO
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 55,99
 switchport nonegotiate
 speed 100
 duplex full
 spanning-tree cost 25
 spanning-tree link-type point-to-point
 no shutdown
exit

interface fa0/24
 description TRONCAL_PRINCIPAL_A_SW_BANCO
 switchport mode trunk
 switchport trunk native vlan 99
 switchport trunk allowed vlan 55,99
 switchport nonegotiate
 speed 100
 duplex full
 spanning-tree cost 19
 spanning-tree link-type point-to-point
 no shutdown
exit

interface range fa0/3 - 22
 description PUERTO_SIN_USO
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface range gi0/1 - 2
 description PUERTO_SIN_USO
 switchport mode access
 switchport access vlan 999
 shutdown
exit

interface vlan 1
 no ip address
 shutdown
exit

interface vlan 99
 description ADMINISTRACION_SW_BANCO_ACC
 ip address 192.168.55.202 255.255.255.240
 no shutdown
exit

ip default-gateway 192.168.55.193

line console 0
 logging synchronous
exit

end
copy running-config startup-config
```

## 11. Comandos de verificación

En los switches:

```text
show vlan brief
show vtp status
show spanning-tree summary
show interfaces trunk
show interfaces status
show ip interface brief
show running-config
show startup-config
```

En los switches que tienen EtherChannel:

```text
show etherchannel summary
```

En SW-CORP:

```text
show spanning-tree vlan 15
show spanning-tree vlan 99
show ip route
```

En SW-BANCO-ACC:

```text
show spanning-tree vlan 55
show spanning-tree vlan 99
```

Las pruebas de ping y los nombres de las capturas se encuentran en el manual técnico.

La prueba de caída del enlace principal Fa0/24 del área bancaria fue omitida.