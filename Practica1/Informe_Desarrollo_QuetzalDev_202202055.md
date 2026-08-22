# Informe de desarrollo

## Diseño de infraestructura física de red para QuetzalDev S.A.

**Estudiante:** Fernando Andhre Gonzalez Espinoza  
**Carné:** 202202055  
**Curso:** Redes de Computadoras 1  
**Fecha:** 21/08/2026

---

## 1. Proceso de diseño

El desarrollo de la propuesta inició con la interpretación del plano arquitectónico asignado. El edificio cuenta con un único nivel de aproximadamente 28 m de largo por 21 m de ancho. En la parte superior se encuentran Recepción, Recursos Humanos, Legal y la Sala de Capacitación. En la parte inferior se ubican Diseño e Innovación, Dirección General, Backend y el Data Center, además del vestíbulo y el área abierta.

El primer paso consistió en comprobar la cantidad de dispositivos solicitados. Los valores por departamento suman 42 equipos de usuario y 6 servidores. Los 42 equipos se distribuyeron como 30 computadoras de escritorio y 12 laptops. Después se asignó un punto de red individual a cada dispositivo y se definieron etiquetas consecutivas para evitar duplicidad.

La distribución seleccionada fue la siguiente: Recepción tiene tres PC y un servidor; Recursos Humanos, seis PC y dos laptops; Legal, dos PC y dos laptops; Capacitación, ocho PC y dos laptops; Diseño e Innovación, cuatro PC, tres laptops y un servidor; Dirección General, una PC y tres laptops; Backend, seis PC y un servidor; y el Data Center, tres servidores principales.

Una vez distribuidos los dispositivos, se ubicó un switch de acceso en cada departamento. Los switches se colocaron cerca del muro que limita con la ruta principal de canalización, con el propósito de reducir los recorridos internos y facilitar su enlace con el MDF. Cada switch se acompaña de un patch panel y una pequeña terminación óptica dentro de un gabinete de pared.

## 2. Selección de la topología

La topología seleccionada para el edificio es una estrella jerárquica. En el primer nivel se encuentra SW-CORE, instalado en el MDF; en el segundo nivel se encuentran los ocho switches departamentales; y en el tercer nivel están las PC, laptops y servidores.

Dentro de cada departamento se utiliza una estrella simple. Cada dispositivo posee un cable Cat 6A independiente hacia el patch panel y el switch local. Aunque en el diagrama varios cables recorren una misma canalización y parecen agruparse, no existe un empalme ni un cable compartido. Los nodos de derivación únicamente representan cajas donde la canaleta o escalerilla cambia de dirección o se divide.

La estrella se consideró más conveniente que una topología bus o anillo porque permite que la falla de un cable afecte únicamente al dispositivo asociado. También facilita localizar averías, agregar puntos y cambiar un equipo de puerto sin modificar toda la red. La desventaja es la dependencia del switch local y del switch principal, por lo que se eligieron equipos administrables y se dejó capacidad libre para futuras mejoras o enlaces redundantes.

## 3. Selección de medios de transmisión

Para el cableado horizontal se seleccionó UTP Cat 6A. Este medio utiliza conectores RJ45, es apropiado para computadoras y servidores, tiene un costo inferior a la fibra en los puestos de trabajo y proporciona capacidad suficiente para Gigabit Ethernet y futuras conexiones de 10 Gigabit Ethernet dentro de las distancias admitidas.

Todos los componentes del canal de cobre deben mantener la misma categoría: cable permanente, keystones, patch panels y patch cords. Los 48 enlaces se terminarán con T568B en ambos extremos, por lo que corresponden a cables directos o straight-through. Los cables cruzados se documentan como evidencia académica, pero no se instalan porque los enlaces entre switches utilizan fibra óptica.

Para el troncal se seleccionó fibra multimodo OM3 dúplex con conectores LC. Cada switch departamental se conecta de forma independiente con SW-CORE. La fibra fue preferida sobre UTP por su inmunidad a interferencias electromagnéticas, aislamiento eléctrico entre gabinetes y capacidad de actualizar los uplinks sin reemplazar el medio instalado.

El enlace más largo del edificio es inferior a 30 m. Esta distancia también podría cubrirse con Cat 6A; sin embargo, utilizar cobre para el troncal aumentaría la exposición a ruido eléctrico y limitaría el aislamiento entre áreas. OM3 ofrece un margen muy superior y puede soportar 10 Gigabit Ethernet hasta 300 m con transceptores compatibles, por lo que constituye una inversión orientada al crecimiento de una empresa de desarrollo de software.

## 4. Selección del MDF y equipo activo

El MDF se ubicó dentro del Data Center. La ubicación no coincide con el centro geométrico exacto del edificio, pero proporciona ventajas operativas que compensan los metros adicionales de fibra hacia Recepción y Recursos Humanos. El Data Center permite controlar el acceso, la temperatura, la limpieza, la alimentación eléctrica y la puesta a tierra. También evita instalar el equipo principal dentro de una oficina ocupada.

El edificio tiene dimensiones reducidas y todos los enlaces quedan ampliamente por debajo de los límites técnicos. Por esta razón, la seguridad y el control ambiental tuvieron mayor peso que una centralidad puramente geométrica.

En el MDF se propuso un rack de piso de 24U con SW-CORE, ODF, organizadores, PDU y UPS. El switch principal debe contar con al menos 16 puertos SFP/SFP+: ocho para los enlaces actuales y ocho para crecimiento. El ODF de 24 puertos utiliza 16 fibras para los ocho enlaces dúplex y conserva ocho fibras libres.

Los switches departamentales se estandarizaron en 16 puertos RJ45 y dos ranuras SFP. Aunque varios departamentos utilizan menos de ocho puertos, la estandarización simplifica compras, repuestos y mantenimiento. Cada switch se instala junto a un patch panel modular de 16 posiciones, cumpliendo el criterio de que la capacidad del switch sea igual o mayor a la del panel asociado.

## 5. Planificación de rutas y canalización

La canalización principal parte del MDF y recorre los muros de circulación que separan los bloques de oficinas. Se seleccionó escalerilla metálica cerrada porque protege los cables contra polvo, manipulación y daños accidentales. Las derivaciones internas utilizan canaleta cerrada de PVC o material de baja emisión de humo.

Los nodos de derivación se colocaron en los puntos donde la ruta principal ingresa a cada departamento y donde la canalización interna se distribuye hacia grupos de tomas. Estos nodos permanecerán accesibles para inspección. Los cables de datos no se cortan ni se empalman dentro de ellos.

Las tomas unitarias y dobles se ubicaron cerca de los puestos de trabajo. En las áreas con mesas centrales se consideraron cajas de piso o descensos protegidos. También se evitó colocar tomas detrás de puertas, muebles fijos o zonas húmedas, especialmente cerca del baño contiguo a Capacitación.

## 6. Estimación de distancias y materiales

Las distancias se calcularon utilizando la escala general del plano y recorridos ortogonales. Se estimaron 238 m de cable UTP Cat 6A para los 48 puntos. Al agregar 15 % por holgura, curvas, terminación y desperdicio, el resultado es aproximadamente 273.7 m. Por lo tanto, una bobina estándar de 305 m es suficiente y deja cerca de 31.3 m disponibles.

Para la fibra se estimaron 118 m antes de reserva y 135.7 m al agregar 15 %. Se propuso adquirir enlaces preterminados en longitudes comerciales que suman aproximadamente 155 m. La selección de fibra preterminada reduce la necesidad de fusionar conectores en el edificio y facilita las pruebas de continuidad y pérdida.

## 7. Respaldo eléctrico

El consumo estimado del switch principal, ocho switches de acceso y dieciséis transceptores es cercano a 180 W. Con un margen de 30 %, la carga de diseño es de 234 W. Por ello se recomendó un UPS en línea de 1500 VA, con capacidad real de salida de al menos 900 W.

La propuesta supone circuitos eléctricos dedicados y respaldados desde el MDF hacia los gabinetes departamentales. Si esa distribución eléctrica no fuera posible, cada gabinete necesitaría un UPS local y el UPS central protegería únicamente el equipo instalado en el MDF. Los servidores requieren un estudio de potencia separado y no se incluyeron en este dimensionamiento.

## 8. Retos encontrados

El primer reto fue interpretar una distribución en la que el MDF debía minimizar distancias, pero el plano ya incluía un Data Center en un extremo del edificio. Se comparó la centralidad geométrica con factores de seguridad, energía y ambiente. Finalmente se eligió el Data Center porque los recorridos continúan siendo cortos y es el espacio técnicamente más adecuado.

El segundo reto fue diferenciar el cableado horizontal del troncal. El enunciado solicita un switch por departamento y un switch principal, por lo que el UTP termina localmente y la conexión desde cada switch al MDF corresponde al troncal. Para presentar un cálculo transparente, se midieron por separado los 48 enlaces horizontales y los ocho enlaces ópticos.

El tercer reto fue representar numerosos cables sin saturar el plano. Se emplearon colores diferentes, etiquetas y nodos de derivación. Fue necesario aclarar que una línea común de canalización puede contener varios cables independientes y que Ethernet no debe empalmarse como una instalación eléctrica.

El cuarto reto fue dimensionar el equipo sin utilizar configuraciones lógicas. Se seleccionaron switches por número de puertos, tipo de uplink, montaje, consumo y capacidad de crecimiento, sin definir VLAN, direcciones IP ni protocolos.

## 9. Resultado final

El diseño final conecta 48 dispositivos por medio de ocho switches departamentales y un switch principal. Utiliza Cat 6A para los enlaces horizontales, OM3 para los troncales, escalerilla metálica cerrada para la ruta principal y canaleta cerrada para las derivaciones internas.

La solución mantiene enlaces independientes, documentación de pines, etiquetas para ambos extremos y capacidad de crecimiento en switches, patch panels, ODF y rack. El presupuesto aproximado, incluyendo materiales, instalación, pruebas y una contingencia de 10 %, es de Q106,522.90. El valor debe confirmarse mediante cotizaciones antes de ejecutar el proyecto.

## 10. Conclusión

El proceso permitió transformar el plano arquitectónico en una propuesta física ordenada y verificable. La combinación de estrella jerárquica, Cat 6A y fibra OM3 proporciona un equilibrio entre costo, desempeño y escalabilidad. La ubicación del MDF dentro del Data Center mejora la seguridad y el mantenimiento, mientras que el etiquetado y la documentación permiten identificar cada enlace desde la toma hasta el switch principal.

El diseño no representa una configuración funcional ni una simulación; constituye una planificación de Capa 1 que puede utilizarse como base para compra, instalación, certificación y posterior configuración lógica de la red.
