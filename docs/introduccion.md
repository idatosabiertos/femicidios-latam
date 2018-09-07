# Modelo de Datos

## Introducción

Este documento intenta dar una detallada descripción de un borrador del protocolo de datos de feminicidios para Latinoamérica. Para esto hemos utilizado datos de bases ya existentes de Argentina, México, Costa Rica y otros paises, así como notas de las discusiones en la reunión presencial en Costa Rica de Agosto del 2017.

La intención es crear un espacio de discusión para construcción colectiva de este protocolo. Necesitamos comentarios así como preguntas para cada parte del mismo.

## Feminicidios

La [tipificación de feminicidios o femicidios](feminicidio.net/articulo/tipos-de-feminicidio-o-las-variantes-de-violencia-extrema-patriarcal) varía de país a país en América Latina. Para el contexto de estandarización de datos entendemos feminicidio como la muerte violenta de una mujer por razón de su género, utilizando la definición inicial acuñada por Diana Russell. Entendemos que la discusión en cuanto a feminicidios es mucho más amplia y necesitamos tomar una definición para este trabajo específico.

## Apertura de datos

El principio general es que los datos recolectados, organizados y expresados serán abiertos. Entendemos la publicación de datos en un espectro dependiendo de quien puede acceder a los mismos y como los pueden usar. Esto es imprescindible en el manejo de datos sensibles como los de feminicidios, que pueden afectar a varias comunidades relacionadas con la víctima y sobrevivientes.  Utilizamos las siguientes categorías para acceso a datos:
* Privado: Accesibles a personas y organizaciones específicas (datos sensibles).
* Semi-privado: Accesibles a personas, organizaciones y medios específicas bajo ciertos criterios.
* Acceso público bajo ciertos criterios.
* Público: Abiertos para cualquier persona compartir y usar.
    * Accessible
    * Disponible en CSV ó JSON
    * Licencia libre

El estándard de datos propuesto incluye una serie de datos que deben ser recolectados y procesados, y asumen distintos niveles de publicidad, conforme los criterios de información pública, información reservada e información personal o privada. En líneas generales el estándard debe ser adecuado a la legislación vigente en cada país en esta materia. A modo de ejemplo  los datos sensibles podrían no ser publicados pero si serán recolectados para entender los casos. En este archivo identificamos con la palabra "sensible" datos que en principio no estarán en el dominio público

## Licencia

Este protocolo tiene licencia Creative Commons Attribution Share Alike 4.0, por lo que se puede compartir así como adaptar para cualquier fin bajo los términos de atribución (proximamente, disponible en español).

## Modelo Conceptual

### Lista de Códigos

Cada lista de códigos es una enumeración de términos y su significado. Representa los únicos valores permitidos en ese tipo de datos. No todos los datos de cada entidad necesitan una lista de códigos.

Definir listas de códigos es muy importante para establecer un vocabulario común que puede diferir de sistema a sistema

#### Tipo de Organismo

En qué institución u organismo los datos fueron generados.

| Código |             Nombre              |                         Descripción |
|:-------|:-------------------------------:|------------------------------------:|
| 1      |            Policial             |                  Organismo policial |
| 2      |            Judicial             |                  Organismo Judicial |
| 3      |            Fiscalia             |                            Fiscalia |
| 4      |              Salud              |                Institución de salud |
| 5      | Ministerio de Desarrollo Social |     Ministerio de Desarrollo Social |
| 6      |       Justicia provincial       |                 Justicia provincial |
| 7      |    Ministerio público fiscal    |           Ministerio público fiscal |
| 8      |     Ministerio de justicia      |              Ministerio de Justicia |
| 9      |            Medicina             |            Medicina Legal o Forense |
| 10     |     Secretaría de la mujer      | Ministerio o Secretaría de la Mujer |

#### Identidad de Género

Alude a la percepción que una persona tiene sobre su género.

| Código |    Nombre    |                                                   Descripción |
|:-------|:------------:|--------------------------------------------------------------:|
| 1      |  Cis Hombre  |     Hombre que se identifica con el genero asignado al nacer. |
| 2      |  Cis Mujer   |      Mujer que se identifica con el genero asignado al nacer. |
| 3      |  No Binario  | Persona que no se identifica con genero femenino o masculino. |
| 4      |     Otro     |                                          Otra identificación. |
| 5      | Se Desconoce |                                       Se desconoce el genero. |
| 6      | Mujer trans  |   Mujer que no se identifica con el genero asignado al nacer. |
| 7      | Hombre trans |  Hombre que no se identifica con el genero asignado al nacer. |

#### Modalidad

La modalidad del crimen determina la existencia de armas de fuego, armas blancas u otro tipo de objetos.

| Código |      Nombre      |                         Descripción |
|:-------|:----------------:|------------------------------------:|
| 1      |      Golpes      |                  Muerte por golpes. |
| 2      | Disparo de bala  |         Muerte por disparo de bala. |
| 3      |  Apuñalamiento   |           Muerte por apuñalamiento. |
| 4      |    Quemaduras    |              Muerte por quemaduras. |
| 5      |     Asfixia      |                 Muerte por asfixia. |
| 6      |   Ahogamiento    |             Muerte por ahogamiento. |
| 7      |  Ataladramiento  |          Muerte por ataladramiento. |
| 8      | Atropellamiento  |         Muerte por atropellamiento. |
| 9      | Estrangulamiento |         Muerte por estangulamiento. |
| 10     |   Otros medios   |            Muerte por otros medios. |
| 11     |   Se desconoce   | Se desconoce moedalidad del crimen. |

#### Tipo de Victima

Si fue la victima principal del asesinato o secundaria.

| Código |  Nombre   |                            Descripción |
|:-------|:---------:|---------------------------------------:|
| 1      | Principal |  La víctima principal del feminicidio. |
| 2      | Vinculado | Víctima vinculada al crimen principal. |

#### Tipo de Relación

Tipo de relación entre la victima y el victimario.

| Código |     Nombre      |                                      Descripción |
|:-------|:---------------:|-------------------------------------------------:|
| 1      |      Padre      |               Victimario es padre de la victima. |
| 2      |      Madre      |               Victimario es madre de la victima. |
| 3      |    Padrastro    |           Victimario es padrastro de la victima. |
| 4      |    Madrastra    |           Victimario es madrastra de la victima. |
| 5      |     Tutor/a     |             Victimario es tutor/a de la victima. |
| 6      |    Esposo/a     |            Victimario es esposo/a de la victima. |
| 7      |   Concubino/a   |         Victimario es concubino/a de la victima. |
| 8      |     Novio/a     |             Victimario es novio/a de la victima. |
| 9      |     Amante      |              Victimario es amante de la victima. |
| 10     | Pareja anterior |         Pareja o cónyuge anterior de la victima. |
| 11     |    Pariente     |            Victimario es pariente de la victima. |
| 12     |     Laboral     | Victimario es empleado/a o colega de la victima. |
| 13     |    Conocido     |          Victimario es conocido/a de la victima. |
| 14     |      Amigo      |             Victimario es amigo/a de la victima. |
| 15     |      Otro       |                           Otro tipo de relación. |
| 16     |    Autoridad    |                           Autoridades oficiales. |
| 17     |   Desconocido   |      Victimario no es conocido/a  de la victima. |
| 18     |  Se desconoce   |                Se desconoce el tipo de relación. |


#### Orientación Sexual

Se refiere a un patrón de atracción sexual, erótica, emocional o amorosa a determinado grupo de personas definidas por su sexo.

| Código |    Nombre     | Descripción |
|:-------|:-------------:|------------:|
| 1      |   Lesbiana    |             |
| 2      |      Gay      |             |
| 3      | Hetereosexual |             |
| 4      |   Bisexual    |             |
| 5      |    Asexual    |             |
| 6      |     Otro      |             |
| 7      | Se desconoce  |             |


#### Nivel Educativo

Fuente: http://unesdoc.unesco.org/images/0022/002207/220782s.pdf

| Código |                      Nombre                      | Descripción |
|:-------|:------------------------------------------------:|------------:|
| 0      |        Educación de la primera infancia.         |             |
| 1      |                Menos que primaria                |             |
| 2      |                Educación primaria                |             |
| 3      |            Educación secundaria baja             |             |
| 4      |            Educación secundaria alta             |             |
| 5      |      Educación postsecundaria no terciaria       |             |
| 6      |        Educación terciaria de ciclo corto        |             |
| 7      | Grado en educación terciaria o nivel equivalente |             |
| 8      | Nivel de maestría, especialización o equivalente |             |
| 9      |         Nivel de doctorado o equivalente         |             |
| 10     |                   Se desconoce                   |             |

#### Situación jurídica

Situación jurídica de la persona victimario.

| Código |         Nombre          |                        Descripción |
|:-------|:-----------------------:|-----------------------------------:|
| 1      |        Imputado         |                                    |
| 2      |        Indagado         |                                    |
| 3      |        Procesado        |                                    |
| 4      |         Acusado         |                                    |
| 5      |        Condenado        |                                    |
| 6      |        Fugitivo         |                                    |
| 7      | En libertad condicional |                                    |
| 8      |       Preventiva        |                 Presión preventiva |
| 9      |          Otro           |                                    |
| 10     |      Se desconoce       | Se desconoce la situación juridica |


#### Tipo de Lugar

Tipo de lugar del hecho

| Código |        Nombre         |                            Descripción |
|:-------|:---------------------:|---------------------------------------:|
| 1      |   Domicilio victima   |                                        |
| 2      | Domicilio victimario  |                                        |
| 3      | Domicilio particular  |                                        |
| 4      |    Espacio abierto    |                                        |
| 5      |   Puesto de Trabajo   |                                        |
| 6      | Institución educativa |                                        |
| 7      |        Prisión        | Instituciones penales o correcionales. |
| 8      |      Institución      |     Entornos de atención institucional |
| 9      |         Otro          |                                        |
| 10     |     Se desconoce      |                                        |

## Modelo Conceptual

Un modelo conceptual es la representación de un sistema que ayuda a entender como todos los componentes se relacionan entre si. En este caso tendremos un diagrama con los diferentes conceptos que necesitamos capturar en un feminicidio. Cada dato dentro de cada concepto tendrá diferentes niveles de acceso dependiendo de la intención en su uso.

(*) Datos sensibles con asterisco.

### Entidad “Victima”

* ID: Identificador en nuestro sistema de la persona. Cada ID es única
* DNI : Documento de Identidad (*)
* Nombre: Nombre completo de la persona. (*)
* Identidad de Género
* Orientación Sexual (*)
* Edad
* Lugar del Nacimiento (*)
* Nacionalidad (*)
* Nivel de Educación
* Ocupación
* Domicilio (*)
* Lugar de Residencia
* Discapacidad (*)
* Condición Migratoria (*)
* Etnia (*)
* Medidas de protección: Son todas medidas cautelares (tobilleras, restricción perimetral, etc)
* Denuncias previas: Almacenadas con ID
* Hijos: Tiene Hijos/Hijas. Este valor es binario.
* Organismo Fuente: En donde fue el dato recolectado. Policial, Judicial, Fiscalía, Salud.
* Rol de quien recolectó datos: Rol de la persona en la fuente que genera estos datos.

### Entidad “Victimario”

* ID: Identificador en nuestro sistema de la persona.
* DNI: Documento de Identidad No publicable. (*)
* Nombre: Nombre completo de la persona. (*)
* Identidad de Género
* Orientación Sexual (*)
* Lugar de Nacimiento (*)
* Edad
* Nacionalidad
* Nivel de Educación
* Ocupación
* Domicilio (*)
* Lugar de Residencia
* Condición Migratoria (*)
* Etnia (*)
* Situación jurídica: Procesado, condenado, indagado, etc
* Estado conyugal: sin necesariamente estar relacionado con la víctima
* Permiso de portación de armas
* Pertenencia a una fuerza de seguridad
* Antecedentes: Violencia previa, medidas de protección, otros delitos
* Organismo Fuente: Organismo en donde fue recolectado. Policial, Judicial, Fiscalía, Salud.
* Suicidio: Consumado o tentativa de suicidio

### Entidad “Hecho”

* ID: Identificador en nuestro sistema del caso.
* Lugar: Lugar del Hecho.
* Tipo de Víctima: Relación de la víctima de acuerdo al hecho.
* Tipo de Relación: Relación o parentesco entre victimaria y víctima.
* Modalidad: Existencia o no de armas de fuego, armas blancas u otro tipo de objetos
* Agresión Sexual: Hubo agresión sexual
* Fecha: Fecha en que sucedió
* Hora: Hora estimada en que sucedió
* Denuncia previa: Tenía denuncia previa al hecho
* Proceso Judicial: Puede incluir si el proceso esta activo. (*)
* Organismo fuente: Organismo desde donde vienen los datos.

### Entidad “Relación con la víctima”

* Tipo de Relación: tipo de relación de acuerdo a la lista de códigos.
* Tiempo: Tiempo de la relación
* Detalles: Cualquier otra observación.

### Entidad “Lugar”

* Descripción
* Tipo de Lugar
* Dirección (*)
* Ciudad
* Pais
* Codigo Postal

### Entidad “Proceso Judicial”

* Estado procesal: Hubo un proceso de investigación (*) <--- agregar esto a posible discusión
* Denunciante: Quien denunció.  (*)
* Fecha de apertura.
* Número de personas imputadas.
* Agravantes (*)
* Partes intervinientes.
* Tipo de delito que se categoriza.

### Entidad “Organismo Fuente”

* Nombre: Nombre del organismo.
* Tipo de Organismo: Tipo de organismo según lista de códigos.
* Rol Responsable: Que rol dentro del organismo recolecta datos.
* Contacto: Correo para contactar al organismo por datos.


## Casos de Uso

### Posibles usos por parte de actores de sociedad civil:

* Aplicaciones informativas
* Aplicaciones para denunciar
* Prensa
* Para investigación
* Sensibilización y educación
* Para transparencia y rendición de cuentas
* Programas de prevención


### Posibles usos de actores estatales:

* Comprensión del fenómeno
* Diagnóstico/línea de base
* Diseño/toma de decisiones/ M&E
* Asignación de presupuesto (asignación y localización)
* Adaptar la cobertura de servicios para que sean eficazes
* Segmentación de población para atención focalizada
* Enmiendas a legislación existente o sanción de nuevas leyes
* Formación continua de personal y continua de operadores
* Creación de Programas Sociales
* Identificar la necesidad de elaborar guías o protocolos (de reacción/acción/respuesta ante una situación de crisis/emergencia, entre otros).

## Ejemplos de Uso de datos

* Mapa de feminicidios de México:  Feminicidios recolectados de datos publicados en prensa en 2016 y 2017 en Mexico.: https://aristeguinoticias.com/2104/mexico/crean-en-google-mapa-de-feminicidios-en-mexico-interactivo/
* Registro de feminicidios en Uruguay: Registro no oficial de feminicidios en Uruguay. https://sites.google.com/view/feminicidiouruguay
* Feminicidios en Uruguay. https://www.facebook.com/notes/feminicidio-uruguay/femicidiofeminicidio/1655396977883366/
* Feminicidio.net (el registro geofeminicidio no está funcionando en este momento, pero es una base de datos con alrededor de 50 campos por caso) https://informes.feminicidio.net/listado-de-feminicidios-y-otros-asesinatos-de-mujeres-en-2018/

* Información sistematizada de violencia de Paraguay, que incluye datos sobre feminicidios http://informativomujer.org.py/cuadros/
* [Propuesta de medición de femicidios del Ministerio Público Fiscal de Argentina.] (https://www.mpf.gob.ar/ufem/files/2017/11/UFEM_Medici%C3%B3nFemicidios2017.pdf)

* [Mapeando femicidios en la región](https://www.google.com/maps/d/u/0/viewer?ll=-0.8483637028616582%2C-74.79742390000001&hl=en&z=3&mid=1y2xG5YwASOtwMve2BT9zOOrIQKs)
