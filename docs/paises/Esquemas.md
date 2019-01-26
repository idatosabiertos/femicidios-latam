# Esquema de Datos

*En Construcción – última revisión - 2017/07/20*

## Introducción

Hacer una puesta en común de datos recolectados sobre feminicidios en diferentes lugares de Latinoamerica. Crear guias y recomendaciones sobre datos a recolectar, con que metodologias y como publicarlos.

##  Fuente de los Datos

Fuentes Oficiales

* Ministerio de Justicia - Corte
* Organismo de la mujer - Ministerio de la mujer - Consejo Nacional de la Mujer,
* Policia - Ministerio del Interior
* Instituto de Estadistica

### Por País que tiene tipo penal del femicidio/feminicidio ###

#### __Argentina__

En Argentina hay un [Registro Nacional de Femicidios]((https://www.oas.org/es/mesecvi/docs/DeclaracionFemicidio-ES.pdf)). 

##### Ministerio de Justicia y Derechos Humanos

Feminicidos desde el 2012 al 2017: [Fuente Original](http://datos.jus.gob.ar/dataset/registro-sistematizacion-y-seguimiento-de-femicidios-y-homicidios-agravados-por-el-genero).

##### Organizaciones Sociales

- [Casa del Encuentro](http://www.lacasadelencuentro.org/)
- [Observatorio de Igualdad de Genero de America Latina y Caribe](http://oig.cepal.org/es/documentos/registro-nacional-femicidios-la-justicia-argentina-datos-estadisticos-poder-judicial)


##### Campos

* numero (int): número de caso
* edad (int): edad de la víctima
* identidad_genero (string): identidad de género
* tipo_victima (string): tipo de víctima (si se trata de un femicidio directo o vinculado)
* lugar_hecho (string): lugar del hecho
* modalidad_comisiva (string): modalidad comisiva
* fecha_hecho (date): fecha del hecho

#### Brasil

No tenemos datos aún.


#### __Chile__

No tenemos datos aún.

#### Colombia

#### Costa Rica

No tenemos datos aún.

#### El Salvador

No tenemos datos aún.

#### Guatemala

No tenemos datos aún.

#### Mexico

No tenemos datos oficiales aún.

#### Nicaragua

No tenemos datos aún.

#### Peru

##### Ministerio Publico - Observatorio de Criminalidad

[Fuente Original](http://portal.mpfn.gob.pe/boletininformativo/infoestadfeminicidio).

#### Uruguay

##### Sistema de Gestión de Seguridad Pública del Ministerio del Interior

[Fuente Original](https://www.minterior.gub.uy/images/2017/femicidios.pdf).

- circunstancias en las que ocurrio el evento (lugar, motivo, tipo de relacion o vinculo entre autor y victima, hora, numero de participantes, tipo de armas empleadas)
- caracterizticas de los autores y victima (sexo, edad, estado civil)

##### Organizaciones Sociales

- ONG Caminos
- Observatorio de Violencia y Criminalidad 


### Por País que NO tiene "definición de feminicidio" en la ley

#### Colombia

No tiene tipo penal especifico pero incorporo en su código penal el homicidio cometido "contra una mujer por el hecho de ser mujer".

- Datos Policia Nacional:
    * Delitos de homicidio para 2017 (a mayo) https://www.datos.gov.co/Seguridad-y-Defensa/Homicidios-2017/uej7-h7uq

    * Delitos de homicidio para 2015 https://www.datos.gov.co/Seguridad-y-Defensa/Delito-Homicidios/cfga-dm6m

    * Delitos de homicidio para 2014 https://www.datos.gov.co/Seguridad-y-Defensa/Delito-Homicidio/fbrt-d6qx

## Campos disponibles

1. Datos de Argentina sobre feminicidios, del Ministerio de Justicia.

Campos: numero,edad,identidad_genero,tipo_victima,lugar_hecho,modalidad_comisiva,fecha_hecho

2. Datos sobre feminicidios de Mexico recolectados desde la prensa.

Campos: incidente, latitud, longitud, rango de edad, asesinadas por, situacion del feminicida, conexion, municipio, entidad federativa, link, descripcion

## Entidades

**Metodologia de recolección de datos**

**Víctima**

Es la persona que fue objetivo del asesinato. 
A considerar:
* la palabra “Victima” tal vez no sea la mejor forma de nombrarla
* se necesita chequear la posible identificación de la persona con los datos pedidos

Campos:

Identificador: Identificador único en el sistema.
Identidad de Genero: Aqui considerando si incluir personas transgenero o no binarias.
Rango de Edad: En que rango de edad cae. 

        "numero"
        "edad",
        "genero",
        "tipo_victima",
        "lugar_hecho",
        "modalidad_comisiva",
        "fecha_hecho"
        
**Hecho**
 
Datos sobre el asesinato mismo.

A considerar:
* se necesita chequear la posible identificación de la persona con los datos pedidos

Campos:

* Identificador: Identificador único en el sistema.
* Lugar: Lugar de la agresión.
* Fecha: Fecha de la agresión
* Descripción: Información relevante.
* Vinculo: Vinculo entre victima e imputado.
         - Pareja: ex-pareja, uniones convivenciales, conyugal, noviazgo
         - Familiares: fraternal, filial, otros familiares
         - Conocidos: otros no familiares
         - Extraños: inexistente
         - Sin Datos
* Estado procesal:
        - En proceso de investigación
        - Auto de sobreseimento
        - En proceso de juicio oral
        - Con sentencia condenatoria
        - Con sentencia absolutoria
        - Otra forma de terminación del proceso
* Registro de denuncias previas por violencia de genero
        - Si/No

**Imputado**

Es la persona que cometió el asesinato. 

A considerar:
* la palabra “Asesino” tal vez no sea la mejor. "Culpable" ?
* se necesita chequear la posible identificación de la persona con los datos pedidos.
* considerar si usar lenguaje relacionado con la posible inocencia o no (“presunto victimario” usan en el protocolo de bogota).

Campos:

* Identificador: Identificador único en el sistema.
* Identidad de Genero: Aquí considerando si incluir personas transgenero o no binarias.
* Rango de Edad: En que rango de edad cae.
* Relación con la victima: Que tipo de relación previa tenian.

## Calidad de los datos

*por hacer*

## Licencia

*por hacer*
