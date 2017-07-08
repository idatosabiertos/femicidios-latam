# Esquema de Datos

*En Construcción – última revisión - 2017/07/08*

## Introducción

Hacer una puesta en común de datos recolectados sobre feminicidios en diferentes lugares de Latinoamerica. Crear guias y recomendaciones sobre datos a recolectar, con que metodologias y como publicarlos.

## Fuente de los Datos

1. Protocolo de bogota sobre homicidios en general.

2. Datos de Argentina sobre feminicidios, del Ministerio de Justicia.

Campos: numero,edad,identidad_genero,tipo_victima,lugar_hecho,modalidad_comisiva,fecha_hecho

3. Datos sobre feminicidios de Mexico recolectados desde la prensa.

Campos: incidente, latitud, longitud, rango de edad, asesinadas por, situacion del feminicida, conexion, municipio, entidad federativa, link, descripcion

## Entidades

**Víctima**

Es la persona que fue objetivo del asesinato. 
A considerar:
* la palabra “Victima” tal vez no sea la mejor forma de nombrarla
* se necesita chequear la posible identificación de la persona con los datos pedidos

Campos:

Identificador: Identificador único en el sistema.
Identidad de Genero: Aqui considerando si incluir personas transgenero o no binarias.
Rango de Edad: En que rango de edad cae.

**Feminicidio**

Datos sobre el asesinato mismo.

A considerar:
* se necesita chequear la posible identificación de la persona con los datos pedidos

Campos:

Identificador: Identificador único en el sistema.
Lugar: Lugar de la agresión.
Fecha: Fecha de la agresión
Descripción: Información relevante.

**Asesino**

Es la persona que cometió el asesinato. 

A considerar:
* la palabra “Asesino” tal vez no sea la mejor. "Culpable" ?
* se necesita chequear la posible identificación de la persona con los datos pedidos.
* considerar si usar lenguaje relacionado con la posible inocencia o no (“presunto victimario” usan en el protocolo de bogota).

Campos:

Identificador: Identificador único en el sistema.
Identidad de Genero: Aquí considerando si incluir personas transgenero o no binarias.
Rango de Edad: En que rango de edad cae.
Relación con la victima: Que tipo de relación previa tenian.

## Calidad de los datos

*por hacer*

## Licencia

*por hacer*
