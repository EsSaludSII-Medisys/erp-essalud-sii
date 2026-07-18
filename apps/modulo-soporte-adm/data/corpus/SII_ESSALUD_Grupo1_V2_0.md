**UNIVERSIDAD PRIVADA ANTENOR ORREGO FACULTAD DE INGENIERÍA**

**PROGRAMA DE ESTUDIOS DE INGENIERÍA DE SISTEMAS E INTELIGENCIA ARTIFICIAL**

SISTEMAS DE INFORMACIÓN INTEGRADOS

**SII - Implementación de una ERP en EsSalud - La Libertad**

**Módulo de Procesos de Soporte Administrativo y Prestaciones Económicas**

DOCENTE:

	- MENDOZA CORPUS, CARLOS ALFREDO

AUTORES:

	- Lescano León, Jared

	- Medina Tirado, Diego

	- Mezones Burgos, Carlos

	- Valverde Vásquez, Francisco

**NRC: 5633**

Trujillo – 2026

	**INDICE**

	I. ANTECEDENTES	3

	II. PROBLEMA A RESOLVER	3

	III. OBJETIVOS	4

	IV. MATRIZ RACI	5

	V. CRONOGRAMA DE ACTIVIDADES	7

	VI. PROCESOS	8

	VII. REQUISITOS	14

	Requisitos No Funcionales	20

	VIII. CASOS DE USO	26

	IX. DIAGRAMA DE ACTIVIDADES	44

	X. MODELO DE DATOS	49

	XI. ELECCIÓN DEL GESTOR DE BASE DE DATOS	56

	XII. PROPUESTA DE MARCO NORMATIVO Y CUMPLIMIENTO LEGAL	67

	XIII. IMPLEMENTACIÓN DE LA METODOLOGÍA UWE BAJO EL ESTÁNDAR UML	94

	**XIV. REFERENCIAS BIBLIOGRÁFICAS**	**126**

	

	

	

	##### ANTECEDENTES

EsSalud es una de las principales instituciones de salud en Perú, encargada de brindar servicios médicos a millones de asegurados a través de una red de hospitales y centros de atención a nivel nacional.

En los últimos años, el crecimiento de la demanda de servicios de salud ha evidenciado limitaciones en sus sistemas de información, especialmente en procesos críticos como la gestión de citas médicas. Según la Organización para la Cooperación y el Desarrollo Económicos (OCDE), el sistema de salud en Perú se caracteriza por estar segmentado en múltiples subsistemas, tales como EsSalud y el Ministerio de Salud del Perú, que operan con estructuras y sistemas de información independientes, lo que limita la coordinación y la interoperabilidad entre ellos (OCDE, 2025)

Esta fragmentación no solo es organizacional, sino también tecnológica. En el ámbito de los sistemas de información en salud, la interoperabilidad sigue siendo un desafío. Estudios técnicos desarrollados en el entorno de EsSalud indican que la interoperabilidad requiere integración a nivel técnico, sintáctico y semántico para garantizar la calidad de los datos, condición que aún no se cumple plenamente en muchos establecimientos de salud (EsSalud, 2024)

La magnitud del problema se evidencia en datos recientes. Durante el primer semestre de 2025, en EsSalud se registró la pérdida de más de 917,000 citas médicas debido a inasistencias y fallas en la gestión del sistema, lo que representa una ineficiencia significativa en el uso de recursos disponibles (Infobae, 2025). Asimismo, la institución proyecta atender más de 24 millones de consultas externas anuales, lo que refleja una alta presión sobre el sistema y la necesidad de optimizar los procesos de atención (EsSalud, 2025).

	##### PROBLEMA A RESOLVER

En la gestión actual de citas médicas dentro de EsSalud se identifican las siguientes problemáticas:

	- Sistemas de citas no completamente integrados entre establecimientos

	- Dificultad para acceder a disponibilidad en tiempo real

	- Duplicidad de registros de pacientes

	- Asignación ineficiente de citas

	- Procesos manuales que generan retrasos en la atención

	##### OBJETIVOS

	- Objetivo General

Diseñar una propuesta de modernización e integración del sistema de EsSalud mediante el uso de arquitecturas orientadas a servicios, modelado de procesos y estrategias de gestión de datos, con el fin de mejorar la eficiencia operativa y la calidad de atención.

	- Objetivos Específicos

	- Analizar el estado actual (AS-IS) del proceso de gestión de citas médicas, identificando deficiencias en la integración y flujo de información.

	- Modelar el proceso de gestión de citas mediante BPMN, identificando cuellos de botella y oportunidades de mejora.

	- Diseñar una arquitectura de integración (TO-BE) basada en APIs y middleware que permita la interoperabilidad entre sistemas de citas de diferentes establecimientos.

	- Proponer un modelo de gestión de datos, orientado a evitar duplicidad de pacientes y garantizar consistencia de la información.

	- Definir una estrategia de despliegue en la nube, que permita escalabilidad y disponibilidad del sistema.

	- Diseñar prototipos (mockups) del sistema de citas modernizado, incluyendo interfaces para pacientes y personal administrativo.

	- Evaluar la viabilidad del proyecto, considerando factores críticos como gestión del cambio, adopción tecnológica y sostenibilidad.

	##### MATRIZ RACI

	Roles de matriz

	- Ahumada Soles, Carlos: Consulted (Consultado)

	- Lescano León, Jared: Informed (Informado)

	- Medina Tirado, Diego: Responsible (Responsable)

	- Valverde Vásquez, Francisco: Accountable (Aprobador)

	Leyenda:

	- R: Responsible

	- A: Accountable

	- C: Consulted

	- I: Informed

| **Actividad / Entregable** | **Gerente de Proyecto** | **Responsable de Procesos** | **Responsable Técnico** | **Responsable de Datos** | **Documentador** |
| --- | --- | --- | --- | --- | --- |
| **FASE 1: PREPARACIÓN DEL PROYECTO** |
| Definición del Alcance y Gobernanza | A | R | C | C | I |
| Delimitar Submódulos SISGEDO y Prestaciones Econ. | A | R | C | C | I |
| Identificar Stakeholders (Jefaturas y Auxiliares) | A | R | C | I | I |
| Configuración del Entorno Inicial | C | I | R | I | A |
| Preparar Servidores de Desarrollo y Pruebas | I | I | R | C | A |
| **FASE 2: PLANO EMPRESARIAL (BUSINESS BLUEPRINT)** |
| Modelado de Negocio y Procesos | C | R | I | I | A |
| Analizar Flujo Documentario Actual (AS-IS) | I | R | C | C | A |
| Diseñar Flujo Optimizado de Derivaciones (TO-BE) | C | R | I | I | A |
| Especificación de Requisitos (SRS) | A | R | C | C | I |
| Documentar Casos de Uso (CU-01 al CU-06) | C | R | C | I | A |
| Diseñar Modelo Entidad-Relación (MER) | C | I | C | R | A |
| Definir Matriz de Seguridad y Auditoría | A | C | R | R | I |
| **FASE 3: REALIZACIÓN (DESARROLLO HÍBRIDO)** |
| Parametrización Estándar SAP | C | R | C | I | A |
| Configurar Estructura Organizativa y Unidades de la Red | C | R | C | I | A |
| Desarrollo a Medida (Microservicios) | C | C | R | I | A |
| Programar Mesa de Partes Digital (MPD) | C | C | R | I | A |
| Implementar Motor de Liquidación de Subsidios | C | I | R | C | A |
| Integrar Módulo de Firma Digital | C | I | R | C | I |
| Integración de Sistemas (APIs) | A | C | R | C | I |
| Construir Conexión con Núcleo Asistencial (CITT) | C | I | R | C | I |
| Construir Conexión con Talento Humano (Planillas) | C | I | R | C | I |
| **FASE 4: PREPARACIÓN FINAL** |
| Aseguramiento de Calidad (Testing) | A | C | R | C | I |
| Ejecutar Pruebas Unitarias de Cálculo de Prestaciones | A | C | R | C | I |
| Ejecutar Pruebas Integrales (Flujo Completo de Expediente) | A | C | R | C | I |
| Transición y Gestión del Cambio | A | R | C | C | C |
| Migrar Datos Legacy de Expedientes Antiguos | C | I | C | R | A |
| Ejecutar Capacitación al Personal Administrativo | A | R | C | I | C |
| **FASE 5: PUESTA EN MARCHA (GO-LIVE)** |
| Despliegue a Producción | A | C | R | C | I |
| Activar el Entorno de Producción | A | C | R | C | I |
| Liberar el Acceso a la Mesa de Partes Digital (Go-Live) | A | C | R | I | I |
| Soporte Temprano | A | C | R | C | I |
| Monitorear Tiempos de Respuesta (RNF de Rendimiento) | C | I | R | C | A |
| Atender Incidencias Funcionales en Tiempo Real | A | C | R | C | I |

	

	##### CRONOGRAMA DE ACTIVIDADES

	**FIGURA 1 - CRONOGRAMA DE ACTIVIDADES DEL PROYECTO**

	

	##### PROCESOS

	El sistema propuesto para EsSalud se concibe bajo un enfoque de arquitectura empresarial orientada a procesos, en el cual las diferentes áreas funcionales se integran mediante flujos de información y actividades interrelacionadas. Esta estructura permite organizar las operaciones institucionales en función de su propósito y nivel de impacto dentro de la organización.

	- Estructura

	- Procesos Estratégicos

	Procesos orientados a la planificación, dirección y control institucional. Incluyen la toma de decisiones, definición de políticas y supervisión de resultados a nivel organizacional.

	- Procesos Operativos (Core)

	Procesos orientados a la planificación, dirección y control institucional. Incluyen la toma de decisiones, definición de políticas y supervisión de resultados a nivel organizacional.

	- Procesos de Soporte

	Procesos que respaldan el funcionamiento de los procesos operativos y estratégicos. Incluyen actividades administrativas, financieras, logísticas y de gestión documental, permitiendo la continuidad y eficiencia de las operaciones institucionales.

| **Nro** | **Gestión** | **Módulo / Unidad** | **Submódulo** | **Estado** |
| --- | --- | --- | --- | --- |
| 1 | Núcleo asistencial | - | Gestión de citas médicas | Asignado |
|  |  | - | Historia Clínica Electrónica | Asignado |
|  |  | - | Gestión de Farmacia y Dispensación | Asignado |
| 2 | Cadena de Suministro y Logística | - | Gestión de Almacenes | Asignado |
|  |  | - | Compras y Adquisiciones | Asignado |
|  |  | - | Trazabilidad de Insumos | Asignado |
| 3 | Gestión Financiera y de Seguros | - | Facturación y Liquidación | Asignado |
|  |  | - | Contabilidad y Presupuesto | Asignado |
|  |  | - | Gestión de Prestaciones Económicas | Asignado |
| 4 | Oficina de Finanzas | Unidad de Tesorería y Presupuesto | Tesorería | Asignado |
|  |  | Unidad de Tesorería y Presupuesto | Presupuesto | Asignado |
|  |  | Unidad de Contabilidad y Costos | Contabilidad | Asignado |
|  |  | Unidad de Contabilidad y Costos | Costos | Asignado |
| 5 | Gestión del Talento Humano | - | Control de Asistencia y Turnos | Asignado |
|  |  | - | Planillas (Payroll) | Asignado |
|  |  | - | Capacitación y Legajo | Asignado |
| 6 | Procesos de Soporte Administrativo | - | Trámite Documentario (SISGEDO) | En Desarrollo (Grupo 1-A) |
|  |  | - | Gestión de Prestaciones Económicas | En Desarrollo (Grupo 1-A) |

	

	- Proceso Seleccionado

	Dentro de los procesos de soporte, se ha seleccionado para su análisis y desarrollo: Módulo de Procesos de Soporte Administrativo

	Este proceso comprende la recepción, registro, clasificación, derivación, evaluación y resolución de documentos administrativos dentro de EsSalud. Su finalidad es garantizar el flujo ordenado y trazable de la documentación institucional, facilitando la comunicación formal entre las distintas áreas.

	Este proceso abarca la gestión integral de cartas, oficios y expedientes técnicos que circulan entre las diversas dependencias de la Red La Libertad. Su función principal es garantizar la interoperabilidad entre la Mesa de Partes Digital y el flujo de trabajo interno, permitiendo que cada documento sea registrado, derivado y atendido mediante firmas digitales, manteniendo una visibilidad total de la trazabilidad desde su origen hasta su archivo final. Este proceso es crítico para reducir los cuellos de botella administrativos y asegurar que la comunicación institucional sea eficiente y auditable.

			Diagrama de Procesos

	Figura 1 - Diagrama de Procesos BPMN del Proceso de Gestión Documentaria Externa

	Fuente: [Oficina de Gestión Documentaria](https://drive.google.com/file/d/1raGwQ20rRAiFABv9KFoFNsKJLlVtalnf/view?usp=sharing)

	Descripción del modelo

	El diagrama BPMN representa el proceso de Gestión de Trámite Documentario y Mesa de Partes Digital para la Red La Libertad de EsSalud. Como especialista, he analizado la secuencia lógica y el flujo de información, el cual se estructura en cuatro carriles operativos que aseguran la trazabilidad desde el ingreso externo hasta la resolución institucional.

	- Actores

	- Solicitante (Ciudadano/Institución): Es el agente externo que inicia el flujo mediante una necesidad de trámite.

	- Mesa de Partes Digital (Sistema): Actúa como la interfaz automatizada de validación primaria y recepción.

	- Auxiliar de Oficina (Gestión Documentaria): Responsable de la verificación técnica y el registro formal en el sistema SGD.

	- Unidad Orgánica (Destinatario): Es el área técnica encargada de procesar el fondo del asunto y emitir una respuesta legal.

	- Descripción del Flujo Operativo

	Fase I: Recepción e Ingesta Automatizada

	El proceso comienza cuando el Solicitante accede a la plataforma y carga los documentos en formato PDF.

	- La Mesa de Partes Digital ejecuta una validación de datos: si los campos están incompletos, notifica el error de inmediato; si son válidos, genera el cargo de recepción y asigna un número de expediente.

	- Esta fase reduce la carga administrativa inicial al filtrar solicitudes mal formuladas antes de que lleguen al personal humano.

	Fase II: Verificación y Registro Formal

	Una vez recibido el expediente virtual, el Auxiliar de Oficina asume el control:

	- Realiza la Verificación Documentaria: si la documentación no es conforme (faltan anexos o hay errores de forma), se observa el trámite y se notifica al solicitante para su subsanación.

	- Si la documentación es conforme, se procede al Registro Formal en el SGD y se realiza la Derivación Electrónica a la Unidad Orgánica competente.

	Fase III: Procesamiento y Resolución

	- El expediente llega al buzón de la Unidad Orgánica correspondiente:

	- El personal revisa el contenido y procede a la Atención del Trámite, lo que implica la elaboración de una respuesta técnica o administrativa.

	- Un paso crítico identificado en el diagrama es la Firma Digital: el documento de respuesta debe ser validado con certificado digital para garantizar su autenticidad y valor legal.

	- Finalmente, el sistema Notifica al Solicitante sobre la resolución, cerrando el ciclo del trámite documentario.

	##### REQUISITOS

	**Requisitos Funcionales**

	

| **Identificación del requisito:** | RF-01 |
| --- | --- |
| **Nombre del requisito:** | Registro de Perfiles de Usuario |
| **Características** | El sistema permitirá el alta de nuevos trabajadores administrativos en el módulo, vinculándolos a una unidad orgánica y asignando credenciales iniciales. |
| **Descripción del requisito** | El sistema debe proporcionar un formulario para agregar nuevos perfiles de usuario al directorio, capturando datos obligatorios como DNI, nombres, apellidos, unidad orgánica de pertenencia y el rol técnico asignado. |
| **Requisito NF** | RNF-01, RNF-05 |
| **Prioridad del requisito:** Alta |

	

	

	

	

	

	

	

	

	

| **Identificación del requisito:** | RF-02 |
| --- | --- |
| **Nombre del requisito:** | Modificar perfil de usuario |
| **Características** | El sistema permitirá la actualización de los privilegios o datos del personal cuando existan cambios en sus funciones o rotaciones internas en la Red La Libertad. |
| **Descripción del requisito** | El sistema debe permitir editar la información de las cuentas existentes, permitiendo el cambio de cargo, actualización de correo institucional y la reasignación de roles de acceso. |
| **Requisito NF** | RNF-01, RNF-04 |
| **Prioridad del requisito:** Alta |

	

| **Identificación del requisito:** | RF-03 |
| --- | --- |
| **Nombre del requisito:** | Eliminar perfil de usuario |
| **Características** | El sistema debe restringir el acceso de manera inmediata a aquellos usuarios que ya no laboran en la oficina o han sido suspendidos. |
| **Descripción del requisito** | El sistema debe permitir al administrador borrar o inhabilitar el estado de una cuenta de usuario, impidiendo el inicio de sesión y el acceso a la información de los expedientes. |
| **Requisito NF** | RNF-01, RNF-02 |
| **Prioridad del requisito:** Alta |

	

	

	

	

	

	

	

	

	

| **Identificación del requisito:** | RF-04 |
| --- | --- |
| **Nombre del requisito:** | Registrar Expediente en Mesa de Partes Digital (MPD) |
| **Características** | Datos de entrada: Identificación (DNI/RUC, nombres, correo electrónico), metadatos del trámite (asunto, folios) y archivo adjunto principal (formato PDF). Resultados esperados: Creación del registro en la base de datos con estado "Pendiente de Verificación", generación de número correlativo institucional y envío automático del cargo de recepción al correo del solicitante. |
| **Descripción del requisito** | El sistema debe proveer un formulario web público que permita al solicitante ingresar un nuevo trámite. El sistema validará de forma síncrona que todos los campos obligatorios cumplan con la estructura de datos requerida y que el archivo adjunto sea estrictamente un documento PDF, respetando el límite de peso máximo configurado para prevenir saturación del servidor. Una vez superadas las validaciones, el sistema insertará el expediente en la base de datos, asignará automáticamente un código correlativo único y aperturará la cabecera de la trazabilidad (Hoja de Ruta) en un solo flujo continuo, notificando finalmente al usuario. |
| **Requisito NF** | RNF-01, RNF-09 |
| **Prioridad del requisito:** Alta |

	

| **Identificación del requisito:** | RF-05 |
| --- | --- |
| **Nombre del requisito:** | Consultar Expedientes Registrados |
| **Características** | El sistema debe proporcionar visibilidad inmediata de los registros ingresados para su posterior verificación técnica. |
| **Descripción del requisito** | El sistema debe permitir consultar la información y los documentos adjuntos de los expedientes que han sido ingresados por la Mesa de Partes Digital, facilitando la revisión inicial por parte del personal de la Red La Libertad. |
| **Requisito NF** | RNF-01, RNF-07 |
| **Prioridad del requisito:** Alta |

	

	

	

	

	

	

	

	

| **Identificación del requisito:** | RF-06 |
| --- | --- |
| **Nombre del requisito:** | Modificar datos del Registro. |
| **Características** | La edición está restringida a la etapa previa a la derivación oficial para mantener la integridad del trámite. |
| **Descripción del requisito** | El sistema debe permitir editar la información capturada durante el registro (como el asunto o la unidad orgánica de destino) para corregir errores materiales detectados durante la fase de verificación. |
| **Requisito NF** | RNF-01, RNF-05 |
| **Prioridad del requisito:** Media |

	

	

| **Identificación del requisito:** | RF-08 |
| --- | --- |
| **Nombre del requisito:** | Anulación de Registros en Mesa de Partes Digital |
| **Características** | Toda anulación debe quedar registrada en los logs de auditoría con el motivo de la acción y el usuario responsable. |
| **Descripción del requisito** | El sistema debe permitir anular (borrar lógicamente) registros de expedientes que presenten vicios de forma, documentos ilegibles o duplicidad, impidiendo que continúen hacia el flujo interno de derivación. |
| **Requisito NF** | RNF-05, RNF-07 |
| **Prioridad del requisito:** Alta |

	

| **Identificación del requisito:** | RF-09 |
| --- | --- |
| **Nombre del requisito:** | Generar Correlativo |
| **Características** | Asignación de un identificador alfanumérico al momento del ingreso de un nuevo trámite. |
| **Descripción del requisito** | El sistema debe crear y asignar un número correlativo a cada expediente nuevo registrado a través de la Mesa de Partes Digital. |
| **Requisito NF** | RNF-11 |
| **Prioridad del requisito:** Alta |

	

| **Identificación del requisito:** | RF-10 |
| --- | --- |
| **Nombre del requisito:** | Abrir Hoja de Ruta |
| **Características** | Creación del contenedor lógico para el registro de movimientos. |
| **Descripción del requisito** | El sistema debe crear un registro inicial de hoja de ruta y vincularlo directamente al expediente recién generado. |
| **Requisito NF** | RNF- |
| **Prioridad del requisito:** Alta |

	

	

	

	

	

	

	

| **Identificación del requisito:** | RF-11 |
| --- | --- |
| **Nombre del requisito:** | Consultar Correlativo y Hoja de Ruta |
| **Características** | Visualización de los identificadores asignados para control del usuario. |
| **Descripción del requisito** | El sistema debe permitir consultar el número de correlativo asignado y los detalles iniciales de la hoja de ruta aperturada. |
| **Requisito NF** | RNF-01, RNF-07 |
| **Prioridad del requisito:** Alta |

	

	

	

	

	

	

| **Identificación del requisito:** | RF-12 |
| --- | --- |
| **Nombre del requisito:** | Notificar Vencimiento |
| **Características** | El sistema debe integrar un motor de monitoreo de plazos que consulte diariamente la fecha de registro en la hoja de ruta y calcule los días hábiles transcurridos según el calendario institucional de EsSalud |
| **Descripción del requisito** | El sistema debe emitir alertas visuales en el tablero de control del usuario y enviar notificaciones automáticas por correo electrónico institucional cuando un trámite se acerque al límite de los 30 días hábiles estipulados por ley. |
| **Requisito NF** | RNF-02, RNF-03 |
| **Prioridad del requisito:** Media |

| **Identificación del requisito:** | RF-13 |
| --- | --- |
| **Nombre del requisito:** | Calcular Subsidio Económico |
| **Características** | El motor de cálculo debe aplicar las fórmulas legales vigentes de EsSalud de forma automatizada basándose en los datos recuperados. |
| **Descripción del requisito** | El sistema debe permitir calcular el monto exacto de la prestación económica, procesando los días de descanso validados y el promedio de remuneraciones del asegurado para generar la propuesta de liquidación |
| **Requisito NF** | RNF-01, RNF-05, RNF-11 |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RF-14 |
| --- | --- |
| **Nombre del requisito:** | Validar Prestación Económica vía Interoperabilidad |
| **Características** | Actor: Técnico Administrativo (o sistema automático en segundo plano).Entradas / Salidas: Datos del asegurado (DNI/Autogenerado) $\rightarrow$ Estado de calificación (Aprobado/Rechazado). |
| **Descripción del requisito** | El sistema debe evaluar si un asegurado cumple con los requisitos legales para recibir un subsidio económico (ej. lactancia, maternidad, sepelio). Para ejecutar esta validación, el sistema consultará de forma síncrona, mediante APIs, la información médica en el módulo de Núcleo Asistencial (como la vigencia del Certificado de Incapacidad Temporal - CITT) y los registros de aportes en el módulo de Talento Humano. Solo si las validaciones externas son conformes, se habilitará el cálculo del monto a pagar. |
| **Requisito NF** | RNF-06, RNF-02 |
| **Prioridad del requisito:** Alta |

	

	

	

	

	

	

	

	

	

	

	

	

	

	

| **Identificación del requisito:** | RF-15 |
| --- | --- |
| **Nombre del requisito:** | Consultar Trazabilidad y Estado de trámites |
| **Características** | El sistema debe disponer de un portal de consulta pública para que el solicitante verifique el avance de su trámite mediante su número de expediente. |
| **Descripción del requisito** | El sistema debe permitir la búsqueda y visualización del estado actual y el historial de oficinas por las que ha transitado un documento específico dentro de la institución. |
| **Requisito NF** | RNF-12 |
| **Prioridad del requisito:** Media |

	

	

	

	

	

	

	

	

	

	

	

	

	

	

	

	##### **Requisitos No Funcionales**

| **Identificación del requisito:** | RNF-01 |
| --- | --- |
| **Nombre del requisito:** | Seguridad y Cifrado de Información |
| **Características** | El sistema debe implementar protocolos de cifrado TLS 1.2 o superior para las comunicaciones y contar con mecanismos de autenticación multifactor (MFA) para el acceso de personal autorizado. |
| **Características ISO 25010** | Seguridad |
| **Subcaracterísticas** | Confidencialidad / Integridad |
| **Descripción del requisito** | El sistema debe garantizar que toda la comunicación entre el cliente y el servidor, así como el almacenamiento de expedientes y montos de subsidios, se realice bajo cifrado robusto para prevenir el acceso no autorizado de agentes internos o externos. |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RNF-02 |
| --- | --- |
| **Nombre del requisito:** | Tiempo de Respuesta |
| **Características** | El sistema debe estar optimizado mediante indexación de base de datos para asegurar que las peticiones de búsqueda no generen latencia perceptible por el personal administrativo. |
| **Características ISO 25010** | Eficiencia de desempeño |
| **Subcaracterísticas** | Comportamiento temporal |
| **Descripción del requisito** | Las operaciones de búsqueda de expedientes deben mostrar resultados en un máximo de 3 segundos bajo carga normal. |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RNF-03 |
| --- | --- |
| **Nombre del requisito:** | Arquitectura Modular |
| **Características** | El sistema debe estructurarse en microservicios independientes, permitiendo que el administrador realice actualizaciones o parches en el módulo de Soporte Administrativo sin desconectar todo el ERP institucional. |
| **Características ISO 25010** | Mantenibilidad |
| **Subcaracterísticas** | Modularidad |
| **Descripción del requisito** | El sistema debe diseñarse mediante microservicios independientes para facilitar el mantenimiento del módulo de Soporte Administrativo. |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RNF-04 |
| --- | --- |
| **Nombre del requisito:** | Interfaz Intuitiva |
| **Características** | El sistema debe seguir la guía de estilos visuales de EsSalud y contar con una navegación simplificada para reducir la curva de aprendizaje del personal de la Red La Libertad. |
| **Características ISO 25010** | Usabilidad |
| **Subcaracterísticas** | Inteligibilidad / Estética de la interfaz |
| **Descripción del requisito** | El diseño UI debe ser consistente con el portal oficial de EsSalud, garantizando facilidad de uso para el personal técnico. |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RNF-05 |
| --- | --- |
| **Nombre del requisito:** | Disponibilidad y Continuidad Operativa |
| **Características** | El sistema opera bajo una arquitectura de alta disponibilidad con redundancia en servidores para asegurar el servicio ininterrumpido durante la jornada laboral de la Red La Libertad |
| **Características ISO 25010** | Fiabilidad |
| **Subcaracterísticas** | Disponibilidad |
| **Descripción del requisito** | La plataforma debe garantizar una disponibilidad del 99.5% durante el horario administrativo (07:00 - 18:00), asegurando que los servicios de trámite documentario y liquidación de prestaciones no sufran interrupciones que afecten la atención al asegurado. |
| **Prioridad del requisito:** Alta/media/baja |

| **Identificación del requisito:** | RNF-06 |
| --- | --- |
| **Nombre del requisito:** | Interoperabilidad de Datos |
| **Características** | El sistema debe contar con una documentación técnica detallada de APIs (Swagger) y un diccionario de datos que coincida con el acta de elección de base de datos única para el resto de módulos. |
| **Características ISO 25010** | Compatibilidad |
| **Subcaracterísticas** | Interoperabilidad |
| **Descripción del requisito** | El sistema debe ser capaz de intercambiar información con los otros módulos (Finanzas, Talento Humano, Núcleo Asistencial) mediante servicios web RESTful para asegurar que los expedientes de SISGEDO y las Prestaciones Económicas mantengan consistencia en todo el ERP |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RNF-07 |
| --- | --- |
| **Nombre del requisito:** | Tolerancia a Fallos |
| **Características** | El sistema debe poseer mecanismos de recuperación ante desastres y un registro detallado de errores para que el administrador pueda restaurar el servicio en el menor tiempo posible. |
| **Características ISO 25010** | Fiabilidad |
| **Subcaracterísticas** | Tolerancia a fallos |
| **Descripción del requisito** | El sistema debe ser capaz de mantener un nivel de prestación de servicio ante fallos técnicos accidentales, garantizando que no exista pérdida de información en trámites documentarios o registros de subsidios económicos de la Red La Libertad. |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RNF-09 |
| --- | --- |
| **Nombre del requisito:** | Protección ante acceso no autorizado |
| **Características** | El sistema deberá implementar un módulo de auditoría que registre cada intento de acceso y modificación de documentos, permitiendo al administrador supervisar la actividad de los usuarios. |
| **Características ISO 25010** | Portabilidad |
| **Subcaracterísticas** | Facilidad de instalación / Adaptabilidad |
| **Descripción del requisito** | El sistema debe impedir el acceso de personas o sistemas no autorizados a datos confidenciales de trámites internos o información de pagos a asegurados mediante validaciones de seguridad multicapa |
| **Prioridad del requisito:** Alta |

	

| **Identificación del requisito:** | RNF-08 |
| --- | --- |
| **Nombre del requisito:** | Capacidad de despliegue e instalación en la nube |
| **Características** | El sistema deberá contar con scripts de configuración y contenedores que faciliten su despliegue en entornos escalables conforme a la planificación de infraestructuras del proyecto. |
| **Características ISO 25010** | Portabilidad |
| **Subcaracterísticas** | Inestalabilidad / Adaptabilidad |
| **Descripción del requisito** | El sistema debe estar diseñado bajo una arquitectura que permita su instalación, configuración y ejecución en entornos de computación en la nube (nube privada o pública) sin necesidad de refactorizar el código fuente. Asimismo, debe ser adaptable para escalar dinámicamente según los recursos de hardware aprovisionados por la infraestructura de EsSalud, garantizando una migración fluida desde entornos de prueba a producción. |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RF-09 |
| --- | --- |
| **Nombre del requisito:** | Protección contra Acceso No Autorizado y Trazabilidad de Auditoría |
| **Características** | El sistema debe responder ante cualquier tipo de acceso no autorizado |
| **Características ISO 25010** | Seguridad |
| **Subcaracterística** | Confidencialidad / Responsabilidad (Accountability) |
| **Descripción del requisito** | El sistema debe bloquear sistemáticamente cualquier intento de acceso lateral o no autorizado a los módulos de datos sensibles (expedientes y liquidaciones económicas). Solo los usuarios con tokens de sesión válidos y permisos explícitos podrán visualizar la información (Confidencialidad). Además, el sistema debe registrar automáticamente la identidad del usuario, la marca de tiempo y la dirección IP en una tabla de auditoría por cada acción ejecutada, garantizando que todo cambio en la base de datos sea rastreable hasta su autor (Responsabilidad/Accountability). |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RF-10 |
| --- | --- |
| **Nombre del requisito:** | Unicidad y Concurrencia de Correlativos |
| **Características** | El sistema debe registrar un historial detallado (log) de cada traslado, incluyendo fecha, hora y responsable de la oficina emisora y receptora |
| **Características ISO 25010** | Fiabilidad |
| **Subcaracterísticas** | Tolerancia a fallos / Madurez |
| **Descripción del requisito** | El sistema debe garantizar que el número correlativo generado sea estrictamente único y secuencial, evitando cualquier duplicidad incluso cuando múltiples solicitantes registren expedientes de forma simultánea |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RNF-11 |
| --- | --- |
| **Nombre del requisito:** | Integridad de Trazabilidad |
| **Características** | El sistema debe registrar un historial detallado (log) de cada traslado, incluyendo fecha, hora y responsable de la oficina emisora y receptora |
| **Características ISO 25010** | Fiabilidad |
| **Subcaracterísticas** | Tolerancia a fallos / Madurez |
| **Descripción del requisito** | El sistema debe garantizar que la hoja de ruta generada no pueda ser alterada, borrada o desvinculada del correlativo original, asegurando una trazabilidad auditable de extremo a extremo. |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RNF-12 |
| --- | --- |
| **Nombre del requisito:** | Autenticidad y No Repudio |
| **Características** | El sistema debe |
| **Características ISO 25010** | Seguridad |
| **Subcaracterísticas** | No repudio / Autenticidad |
| **Descripción del requisito** | El sistema debe garantizar que el número correlativo generado sea estrictamente único y secuencial, evitando cualquier duplicidad incluso cuando múltiples solicitantes registren expedientes de forma simultánea |
| **Prioridad del requisito:** Alta |

| **Identificación del requisito:** | RNF-13 |
| --- | --- |
| **Nombre del requisito:** | Unicidad y Concurrencia en la Generación de Correlativos |
| **Características** | Mecanismos de Control: Transacciones ACID estrictas, uso de secuencias nativas del motor PostgreSQL y bloqueos a nivel de fila (Row-level locking) para evitar deadlocks. |
| **Características ISO 25010** | Fiabilidad |
| **Subcaracterísticas** | Tolerancia a fallos / Madurez |
| **Descripción del requisito** | El sistema debe garantizar matemáticamente que el número correlativo asignado a cada nuevo expediente sea estrictamente único e irrepetible. Ante un escenario de alta concurrencia (donde múltiples solicitantes o auxiliares ingresen trámites en la Mesa de Partes Digital exactamente en el mismo milisegundo), el motor de base de datos deberá encolar, aislar y resolver las peticiones concurrentes sin generar colisiones, sobreescrituras ni caídas del servicio. |
| **Prioridad del requisito:** Alta |

	

	##### **CASOS DE USO**

	- **CU-01: Registrar Expediente en MPD**

| **Caso de Uso** | Registrar Expediente en MPD |
| --- | --- |
| **Actores** | Solicitante |
| **Objetivo** | Permitir al usuario externo ingresar documentos digitales para iniciar un trámite formal en la institución. |
| **Flujo Básico:** |
| **Curso normal de Eventos** |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. Ingresa a la plataforma de Mesa de Partes Digital y selecciona "Nuevo Trámite". 3. Llena los datos obligatorios (DNI/RUC, correo, asunto) y adjunta el archivo PDF. 5. Hace clic en el botón "Enviar Solicitud". | 2. Muestra el formulario electrónico de registro. 4. Valida temporalmente que los campos estén completos y que el archivo cumpla con los parámetros técnicos. 6. Guarda el registro, genera un número de expediente único (correlativo), y emite un cargo de recepción con fecha y hora, enviando una copia al correo del solicitante. |
|  |  |
|  |  |
|  |  |
|  |  |
| **Flujos Alternos** |
| Archivo inválido: Si el archivo no es PDF o supera el peso máximo permitido, el sistema muestra el mensaje de error "Formato inválido o tamaño excedido" y bloquea el botón de envío hasta que se corrija. |
| **Pre-condiciones** |
| El solicitante debe contar con acceso a internet y el documento sustentatorio debe estar digitalizado en formato PDF. |
| **Post-condiciones** |
| El expediente queda almacenado en la base de datos en estado "Pendiente de Verificación". |

	

	

	

	- **CU-02: Verificar y Validar Expediente**

| **Caso de Uso** | Verificar y Validar Expediente |
| --- | --- |
| **Actores** | Auxiliar de Oficina |
| **Objetivo** | Revisar la conformidad de los documentos ingresados por la MPD antes de su derivación oficial al flujo interno. |
| **Flujo Básico:** |
| **Curso normal de Eventos** |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. Selecciona un expediente desde la bandeja de entrada de verificación. 3. Revisa el documento y selecciona la opción "Validar y Aceptar". | 2. Despliega los metadatos del trámite y el visor del documento PDF adjunto. 4. Actualiza el estado del expediente a "Registrado/Conforme" y habilita las opciones para su derivación. |
|  |  |
|  |  |
|  |  |
|  |  |
| **Flujos Alternos** |
| Expediente con observaciones: Si el documento es ilegible o faltan anexos requeridos, el usuario selecciona "Observar/Anular" e ingresa el motivo. El sistema cambia el estado a "Observado", archiva lógicamente el registro y envía un correo automático al solicitante para que subsane el error. |
| **Pre-condiciones** |
| Debe existir al menos un expediente en estado "Pendiente de Verificación" en el sistema. El Auxiliar de Oficina debe estar autenticado. |
| **Post-condiciones** |
| El expediente queda listo para ser trasladado a la unidad orgánica de destino, o el trámite se detiene por observación. |

	

	

	

	- **CU-03: Derivar Expediente**

| **Caso de Uso** | Derivar Expediente |
| --- | --- |
| **Actores** | Auxiliar de Oficina |
| **Objetivo** | Trasladar digitalmente un expediente hacia otra unidad orgánica para su atención o resolución. |
| **Flujo Básico:** |
| **Curso normal de Eventos** |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. Selecciona el expediente en su bandeja y presiona "Derivar". 3. Selecciona la unidad destino, redacta un proveído (indicación técnica) y confirma la acción. | 2. Despliega el formulario de derivación mostrando el catálogo de unidades orgánicas de la Red La Libertad. 4. Graba el movimiento en el historial (hoja de ruta), actualiza la ubicación lógica del expediente y lanza una notificación a la bandeja de la unidad receptora. |
|  |  |
|  |  |
|  |  |
|  |  |
| **Flujos Alternos** |
| Error de conexión: Si la base de datos central experimenta una caída momentánea, el sistema aborta la operación, muestra "Error al derivar, intente nuevamente" y el expediente permanece en la bandeja de origen. |
| **Pre-condiciones** |
| El expediente debe encontrarse en estado "Registrado/Conforme" o en "Proceso". El usuario debe tener los permisos de derivación en su perfil. |
| **Post-condiciones** |
| El expediente aparece como "Recibido" o "Pendiente de Atención" en la bandeja de la oficina destino, y el historial de trazabilidad queda actualizado. |

	

	

	- **CU-04: Consultar Estado de Trámite**

| **Caso de Uso** | Consultar Estado de Trámite |
| --- | --- |
| **Actores** | Usuario de Sistema / Administrador |
| **Objetivo** | Permitir la visualización de la trazabilidad, ubicación actual y el historial de oficinas de un expediente. |
| **Flujo Básico:** |
| **Curso normal de Eventos** |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. Ingresa el número de expediente en la barra de búsqueda y presiona "Consultar". 3. Revisa la interfaz de resultados. | 2. Realiza la consulta a la base de datos de expedientes y movimientos. 4. Despliega una tabla o línea de tiempo detallando: fecha, hora, unidad de origen, unidad destino, usuario responsable y estado actual del trámite. |
|  |  |
|  |  |
|  |  |
|  |  |
| **Flujos Alternos** |
| Número inexistente: Si el código ingresado no tiene coincidencias en la base de datos, el sistema muestra el mensaje "El expediente no existe, verifique el número ingresado". |
| **Pre-condiciones** |
| El sistema debe estar operativo y el expediente buscado debe haber sido generado formalmente (tener un ID o número asignado). |
| **Post-condiciones** |
| Ninguna (es una operación de solo lectura). El usuario obtiene la información solicitada. |

	

	.

	- **CU-05: Liquidar Prestación Económica**

| **Caso de Uso** | Liquidar Prestación Económica |
| --- | --- |
| **Actores** | Técnico de Prestaciones Económicas |
| **Objetivo** | Calcular, procesar y aprobar el monto de un subsidio económico cruzando información clínica y laboral del asegurado. |
| **Flujo Básico:** |
| **Curso normal de Eventos** |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. Ingresa el DNI del asegurado e inicia el proceso de "Generar Liquidación". 3. Revisa la información precargada en pantalla y presiona "Calcular". 5. Presiona "Aprobar Liquidación". | 2. Consume los servicios web de Historia Clínica (para validar descansos/CITT) y de Planillas (para validar sueldos y aportes). 4. Ejecuta el motor de reglas de negocio (fórmulas de ley) y arroja el monto a pagar. 6. Genera el registro de pago, cambia el estado a "Liquidado" y envía la orden a la Unidad de Tesorería (Finanzas). |
|  |  |
|  |  |
|  |  |
|  |  |
| **Flujos Alternos** |
| Incumplimiento de aportes: Si al consumir la API de Talento Humano se detecta que el trabajador no tiene los meses de aporte mínimos, el sistema bloquea el cálculo, lanza una alerta de "Derecho no aplicable" y permite al técnico emitir una resolución de rechazo. |
| **Pre-condiciones** |
| Debe existir un expediente sustentatorio derivado al área de Prestaciones. El módulo debe tener conexión activa por API con los módulos de "Núcleo Asistencial" y "Talento Humano". |
| **Post-condiciones** |
| Se crea una orden de prestación económica lista para ser desembolsada y se actualiza el expediente como "Atendido". |

	

	- **CU-06: Gestionar Perfiles de Usuario**

| **Caso de Uso** | Gestionar Perfiles de Usuario |
| --- | --- |
| **Actores** | Administrador del Sistema. |
| **Objetivo** | Centralizar la creación, modificación e inhabilitación de las cuentas de acceso y operarios del ERP dentro de la Red La Libertad, asegurando el control basado en roles (RBAC) y la aplicación estricta del principio de mínimo privilegio. |
| **Flujo Básico:** |
| **Curso normal de Eventos** |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. Ingresa alEl Administrador ingresa al panel de configuración de seguridad y selecciona la opción “Gestión de Usuarios”. 3. El Administrador presiona “Registrar Nuevo Usuario” y completa el formulario electrónico con los datos obligatorios: DNI, nombres, unidad orgánica, rol transaccional y correo institucional. 5. El Administrador presiona el botón “Confirmar Registro”. | 2. Despliega el directorio de usuarios actuales y habilita las opciones "Nuevo", "Editar" e "Inhabilitar". 4. El sistema valida en tiempo real el formato y obligatoriedad de los campos ingresados. 6. El sistema verifica que el DNI no se encuentre duplicado en la base de datos.  7. Si la validación es correcta, el sistema inserta el nuevo registro en la tabla USUARIO con el estado activo (estado_activo = true). 8.El sistema genera una credencial temporal cifrada y envía automáticamente una notificación al correo institucional del usuario registrado con las instrucciones de acceso inicial. |
|  |  |
|  |  |
|  |  |
|  |  |
| **Flujos Alternos** |
| Flujo Alterno A: Modificación de Parámetros del Perfil |
| **Curso normal de Eventos** |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. El Administrador selecciona un usuario existente y presiona “Modificar Datos”. 3. El Administrador actualiza los campos permitidos y presiona “Guardar Cambios”. | 2. El sistema muestra el formulario cargando la información actual del usuario seleccionado. 4. El sistema ejecuta la actualización de datos (UPDATE), refresca los privilegios del usuario y registra automáticamente la operación en la tabla de auditoría. |
| Flujo Alterno B: Inhabilitación Lógica de la Cuenta |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. El Administrador selecciona un usuario y presiona “Inhabilitar Perfil”. 3. El Administrador confirma la acción. | 2. El sistema solicita una confirmación explícita mediante una ventana emergente de seguridad. 4. El sistema realiza un borrado lógico actualizando el parámetro estado_activo = false, revoca las sesiones activas y bloquea inmediatamente el acceso al ERP. |
| Flujo Alterno C: Intento de Registro Duplicado |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. El Administrador intenta registrar un usuario con un DNI ya existente. | 2. El sistema interrumpe la transacción y muestra el mensaje: “Error: El documento de identidad ya se encuentra asociado a un perfil activo”. |
| **Pre-condiciones** |
| El Administrador debe encontrarse autenticado en la plataforma mediante una sesión activa y cifrada con privilegios de alta seguridad. |
| **Post-condiciones** |
| La base de datos actualiza el estado transaccional del operario, habilitando o restringiendo el acceso a las APIs del ERP de manera inmediata. Asimismo, el sistema genera un registro inalterable en la bitácora de auditoría con fecha, hora e IP de la operación realizada. |

	

	

	- **CU-07: Modificar Datos de Expediente**

| **Caso de Uso** | Modificar Datos de Expediente |
| --- | --- |
| **Actores** | Auxiliar de Oficina |
| **Objetivo** | Permitir la corrección de errores materiales detectados en los metadatos de un expediente antes de que este sea derivado oficialmente al flujo de trabajo interno. |
| **Flujo Básico:** |
| **Curso normal de Eventos** |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. Busca un expediente en estado "Pendiente" y selecciona la opción "Modificar Datos". 3. Corrige la información errónea y presiona "Guardar Cambios". | 2. Despliega el formulario de registro con los campos habilitados para su edición (ej. Asunto, Unidad Orgánica de destino). 4. Valida la integridad de los nuevos datos, actualiza el registro en la base de datos y guarda la acción en la tabla de auditoría. |
|  |  |
|  |  |
|  |  |
|  |  |
| **Flujos Alternos** |
| Intento de edición fuera de plazo: Si el usuario intenta modificar un expediente que ya ha sido derivado (estado "En Proceso"), el sistema bloquea los campos y muestra la alerta: "No se puede editar: el expediente ya ingresó al flujo de derivación". |
| **Pre-condiciones** |
| El expediente debe estar obligatoriamente en la etapa previa a la derivación oficial. |
| **Post-condiciones** |
| La metadata del expediente queda corregida y lista para continuar su flujo normal. |

	

	- **CU-08: Liquidar Prestación Económica**

| **Caso de Uso** | Liquidar Prestación Económica |
| --- | --- |
| **Actores** | Técnico Administrativo (de la Unidad de Prestaciones Económicas). |
| **Objetivo** | Validar los requisitos legales de aportación y condición clínica del asegurado mediante interoperabilidad síncrona, para posteriormente calcular y aprobar el desembolso financiero del subsidio correspondiente (Lactancia, Maternidad o Sepelio). |
| **Flujo Básico:** |
| **Curso normal de Eventos** |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 1. El Técnico Administrativo ingresa al submódulo de "Prestaciones Económicas" y selecciona un expediente en estado "Conforme" para su procesamiento. 5. El Técnico Administrativo revisa la consistencia de los datos calculados y presiona el botón "Aprobar Orden de Pago". | 2. El sistema renderiza la pantalla de liquidación, extrayendo automáticamente el tipo de trámite, los datos de identidad del asegurado (id_asegurado) y el catálogo de reglas de negocio asociado desde la entidad TIPO_SUBSIDIO. 3. De forma automática y en segundo plano, el sistema ejecuta consultas síncronas vía API RESTful hacia los módulos satélites del ERP: Consulta al módulo de Núcleo Asistencial para validar la vigencia y autenticidad del Certificado de Incapacidad Temporal para el Trabajo (CITT) o partidas de nacimiento/defunción según corresponda. Consulta al módulo de Talento Humano para verificar que el asegurado cuente con el número mínimo de meses de aportes consecutivos exigidos por ley. 4. Al recibir la conformidad de los módulos externos, el motor de cálculo matemático del sistema procesa los montos basándose en los campos porcentaje_calculo y remuneraciones del asegurado, desplegando en pantalla el desglose del monto final a pagar (monto_calculado). 6. El sistema abre una transacción ACID ininterrumpida donde: Inserta el registro correspondiente en la entidad PRESTACION_ECONOMICA con el campo estado_pago = 'Pendiente de Desembolso'. Actualiza el estado del expediente principal a "Liquidado". Inserta la traza inmutable en la tabla de AUDITORIA detallando el ID del usuario, la acción INSERT y los datos del host. Despacha una notificación automática con el estado del proceso al correo electrónico del solicitante. |
|  |  |
|  |  |
|  |  |
|  |  |
| **Flujos Alternos** |
| Flujo Alterno A: Rechazo por Incumplimiento de Requisitos Legales |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 6a. El Técnico confirma el rechazo, registrando la prestación económica con el estado estado_pago = 'Rechazado', lo cual finaliza el ciclo del expediente enviando el sustento técnico al ciudadano. | 4a. Si las llamadas de API hacia los módulos de Talento Humano o Núcleo Asistencial devuelven que el asegurado no cumple con los meses mínimos de aporte o que el CITT no se encuentra registrado en el sistema clínico, el motor interrumpe el cálculo automático. 5a. El sistema bloquea el botón de aprobación, cambia visualmente el flujo a modo de rechazo y genera una propuesta de resolución denegatoria. |
| Flujo Alterno B: Intervención o Edición Manual del Monto (Excepción) |
| **Acción de Usuario** | **Respuesta del Sistema** |
| 5b. Ante un mandato judicial o contingencia administrativa excepcional que requiera modificar el cálculo del sistema, el Técnico (con autorización jerárquica) selecciona la opción "Modificación Manual de Monto". | 6b. El sistema habilita el campo de texto e incrementa la rigurosidad de la bitácora, obligando al usuario a registrar el sustento legal de la edición. Al guardar, se almacena el estado modificando los indicadores de la tasa de automatización para la posterior auditoría del sistema. |
| Flujo Alterno C: Caída de Conexión con Módulos Satélites (Time-out) |
| **Acción de Usuario** | **Respuesta del Sistema** |
|  | 4c. Si las APIs de los módulos externos no responden en un lapso de tiempo seguro (latencia superior a la tolerada), el sistema interrumpe el proceso de manera controlada para evitar datos corruptos. 5c. El sistema muestra un mensaje de advertencia: "Error de comunicación: No se pudo conectar con el módulo asistencial/planilla. Intente de nuevo en unos minutos", manteniendo el expediente intacto en la cola de trabajo sin realizar ninguna inserción en la base de datos. |
| **Pre-condiciones** |
| El expediente asociado al trámite debe haber sido verificado previamente por el Auxiliar de Oficina y encontrarse en estado "Conforme" dentro de la cola de trabajo del submódulo financiero. |
| **Post-condiciones** |
| Se consolida de forma segura el estado contable de la prestación en la base de datos de la Red La Libertad, se libera la orden para el desembolso en el módulo de Finanzas y queda registrado el evento en los logs criptográficos del sistema para auditorías de la norma ISO 27001. |

	

	

	

	##### DIAGRAMA DE ACTIVIDADES

	- CU-01: Registrar Expediente en MPD

	Figura 9 - Diagrama de Actividades CU-01

	- CU-02: Verificar y Validar Expediente

	Figura 10 - Diagrama de Actividades CU-02

	

	

	- CU-03: Derivar Expediente

	Figura 11 - Diagrama de Actividades CU-03

	- CU-04: Consultar Estado de Trámite

	Figura 12 - Diagrama de Actividades CU-04

	- CU-05: Liquidar Prestación Económica

	Figura 13 - Diagrama de Actividades CU-05

	- CU-06: Gestionar Perfiles de Usuario

	Figura 14 - Diagrama de Actividades CU-06

	

	- CU-07: Modificar Datos de Expediente

	Figura 15 - Diagrama de Actividades CU-07

	

	- CU-08: Liquidar Prestación Económica

	Figura 16 - Diagrama de Actividades CU-08

	

	##### MODELO DE DATOS

	- **Identificar las Entidades**

	El primer paso consiste en abstraer los objetos del mundo real que interactúan en la Red La Libertad. Se han identificado las siguientes entidades críticas:

	- **USUARIO:** Representa tanto a los solicitantes externos (ciudadanos/asegurados) como al personal interno (Auxiliar, Jefe de Oficina, Técnico) que interactúa con el sistema.

	- **SOLICITANTE**: Persona o institución que inicia el trámite.

	- **DOCUMENTO**: Los archivos físicos o digitales que componen el expediente.

	- **EXPEDIENTE:** Es el núcleo y contenedor lógico del trámite documentario originado en la Mesa de Partes Digital.

	- **MOVIMIENTO**: Cada paso individual de derivación.

	- **UNIDAD_ORGANICA:** Las diversas dependencias o áreas funcionales de la Red La Libertad.

	- **HOJA_RUTA:** Entidad transaccional que registra la trazabilidad, derivaciones y envíos electrónicos de un expediente entre distintas oficinas.

	- **FIRMA_DIGITAL:** Entidad que gestiona los certificados y sellos de tiempo que garantizan la validez legal e inalterabilidad de los documentos institucionales.

	- **PRESTACION_ECONOMICA:** Registro de los subsidios o beneficios a liquidar para los asegurados.

	- **TIPO_SUBSIDIO**: Catálogo legal de beneficios.

	- **ASEGURADO**: El titular del derecho (puede ser distinto al solicitante).

	- **Atributos y Dominio**

	Se definen las características de cada entidad y el tipo de dato (dominio) que almacenarán para garantizar la calidad de la información. Fiel a la lógica de negocio estructurada, se mantiene una separación estricta entre el estado situacional y el estado lógico del registro.

| **Entidad** | **Atributo** | **Dominio Lógico** |
| --- | --- | --- |
| **USUARIO** | dni_ruc    nombre    rol    email    status    is_active | VARCHAR(15)    VARCHAR(150)    ENUM('Auxiliar', 'Jefe_Oficina', 'Tecnico', 'Ciudadano')    VARCHAR(100)    VARCHAR(50)    BOOLEAN |
| **EXPEDIENTE** | numero_correlativo    asunto    archivo_pdf_url    fecha_registro    fecha_vencimiento    status | VARCHAR(20)    VARCHAR(255)    VARCHAR(255)    DATETIME    DATETIME    VARCHAR(50) |
| **SOLICITANTE** | id_solicitante   tipo_doc   nro_doc   nombre_razon_social   correo_electronico | STRING(10)   STRING   STRING(15)   STRING(150)   STRING(100) |
| **DOCUMENTO** | id_documento  id_expediente  tipo_doc  url_archivo  hash_firma | STRING(10)  STRING  STRING(50)  STRING(255)  STRING(255) |
| **MOVIMIENTO** | id_movimiento  id_hoja_ruta  id_unidad_origen  id_unidad_destino  id_usuario  fecha_traslado | STRING(10)  STRING  STRING(10)  STRING(10)  STRING  TIMESTAMP |
| **UNIDAD_ORGANICA** | nombre_dependencia    is_active | VARCHAR(100)    BOOLEAN |
| **HOJA_RUTA** | fecha_traslado    proveido | DATETIME    TEXT |
| **FIRMA_DIGITAL** | certificado_hash    sello_tiempo | VARCHAR(255)    DATETIME |
| **PRESTACIONE_ECONOMICA** | tipo_subsidio    monto    estado_validacion | VARCHAR(50)    DECIMAL(10,2)    VARCHAR(30) |
| **TIPO_SUBSIDIO** | id_tipo_subsidio  nombre_subsidio  meses_aporte_requerido  porcentaje_calculo  estado_vigencia | STRING  STRING(100)  NUMERIC  DECIMAL(5,2)  BOOLEAN |
| **ASEGURADO** | id_asegurado  autogenerado  dni  condicion_laboral | STRING  STRING(20)  STRING(8)  STRING(50) |

	- **Determinar el Identificador Principal (Clave Primaria)**

	Para asegurar que cada registro sea único en la base de datos, se extraen los identificadores principales (PK):

	- **USUARIO:** id (Autonumérico/INTEGER)

	- SOLICITANTE

	- DOCUMENTO

	- MOVIMIENTO

	- **EXPEDIENTE:** id (Autonumérico/INTEGER)

	- **UNIDAD_ORGANICA:** id (Autonumérico/INTEGER)

	- **HOJA_RUTA:** id (Autonumérico/INTEGER)

	- **FIRMA_DIGITAL:** id (Autonumérico/INTEGER)

	- **PRESTACION_ECONOMICA:** id (Autonumérico/INTEGER)

	- TIPO_SUBSIDIO

	- ASEGURADO

	- **Relaciones y Determinar Cardinalidad**

	Se establecen los verbos que conectan las entidades y los límites numéricos (cardinalidad) de dicha asociación, fundamentales para entender el flujo operativo de EsSalud, en el módulo de Soporte Administrativo

| **Entidad Origen** | **Relación** | **Entidad Destino** | **Cardinalidad** | **Justificación Analítica** |
| --- | --- | --- | --- | --- |
| **USUARIO** | Genera | **EXPEDIENTE** | 1 : N | Un ciudadano o institución externa puede registrar múltiples expedientes en la Mesa de Partes Digital, pero un expediente pertenece a un solo remitente. |
|  |  |  |  |  |
| **EXPEDIENTE** | Registra | **HOJA_RUTA** | 1 : N | La trazabilidad de un expediente genera múltiples movimientos por las diferentes unidades orgánicas. |
| **HOJA_RUTA** | Origen / Destino | **UNIDAD_ORGANICA** | N : 1 | Un movimiento de traslado documentario vincula de forma exacta una oficina emisora y una oficina receptora. |
| **USUARIOS** (Responsable) | Ejecuta | **HOJA_RUTA** | 1 : N | Un auxiliar técnico es el responsable de realizar la derivación electrónica del expediente y añadir los proveídos. |
| **EXPEDIENTES** | Recibe | **FIRMA_DIGITAL** | 1 : N | Un documento institucional o resolución de expediente puede ser firmado digitalmente por varios jefes de oficina para otorgarle validez legal. |
| **USUARIOS** (Funcionario) | Emite | **FIRMA_DIGITAL** | 1 : N | Un funcionario autorizado puede firmar digitalmente múltiples expedientes distintos en su flujo de trabajo. |
| **EXPEDIENTES** | Respalda | **PRESTACION_ECONOMICA** | 1 : 1 | Un expediente validado dispara y justifica el proceso de un (1) subsidio o beneficio económico específico. |
| **USUARIOS** (Asegurado) | Beneficia a | **PRESTACION_ECONOMICA** | 1 : N | Un asegurado puede solicitar o ser receptor de múltiples subsidios económicos a lo largo del tiempo. |

	

	Figura 17 - Diagrama ER

	

	##### ELECCIÓN DEL GESTOR DE BASE DE DATOS

	- Comparación y Elección del Gestor de Base de Datos (DBMS)

	Considerando que el sistema va a manejar flujos documentales continuos y datos financieros sensibles (prestaciones económicas), la elección del motor relacional debe garantizar transaccionalidad estricta (ACID) e interoperabilidad.

| **Gestor de BD** | **Características Principales** | **Ventajas** | **Desventajas** |
| --- | --- | --- | --- |
| **PostgreSQL** | Open-source, arquitectura orientada a objetos-relacional, soporte nativo para JSONB (ideal para metadatos de documentos). | Excelente manejo de alta concurrencia (MVCC), costo de licencia cero, alto cumplimiento del estándar SQL, ideal para arquitecturas de microservicios. | Curva de aprendizaje técnica más empinada para afinamiento (tuning) avanzado en comparación con opciones comerciales |
| **Oracle Database** | Motor comercial líder, arquitectura multi-tenant, opciones avanzadas de encriptación (TDE) y particionamiento. | Rendimiento extremo en volúmenes masivos, seguridad de grado gubernamental, altamente establecido en instituciones públicas. | Costos de licenciamiento y soporte sumamente elevados. Dependencia de un proveedor.. |
| **Microsoft SQL Server** | Motor comercial robusto, profunda integración con ecosistemas de Microsoft y herramientas analíticas (SSIS, SSAS). | Curva de aprendizaje amigable, excelentes herramientas gráficas de administración, integración nativa con Active Directory. | Licenciamiento costoso por núcleo (core), mejor rendimiento restringido a entornos Windows Server. |

	

	- Selección del Gestor

	Se selecciona PostgreSQL. La capacidad nativa de PostgreSQL para manejar datos estructurados (tablas relacionales) y semiestructurados (JSONB para anexos variables en los expedientes) ofrece la flexibilidad necesaria para el sistema de trámite documentario. Además, su costo cero de licenciamiento optimiza el presupuesto del proyecto, permitiendo destinar recursos a la infraestructura en la nube y la ciberseguridad, cumpliendo con los estándares de interoperabilidad requeridos para interactuar con los otros módulos.

	- Matriz de Permisos y Control de Acceso a la Base de Datos

	La seguridad en bases de datos debe regirse por el principio de mínimo privilegio (RBAC - Role Based Access Control). La siguiente tabla define los permisos transaccionales (CRUD) por cada rol operativo identificado en los flujos del sistema:

	

| **Rol de Usuario** | **Entidades (Tablas) Accesibles** | **Permisos (CRUD) a nivel de BD** | **Restricciones y Reglas de Negocio** |
| --- | --- | --- | --- |
| **Administrador de BD (DBA)** | Todas las tablas del esquema. | CREATE, READ, UPDATE, DELETE, EXECUTE | Acceso irrestricto por consola. No opera el sistema desde el frontend. Encargado de mantenimientos y backups. |
| **Jefe de Oficina** | Expediente, Documento, Movimiento, Hoja_Ruta. | READ, UPDATE (Firma), INSERT (Movimiento) | Solo puede actualizar el estado del documento para estampar su firma digital e insertar la derivación. No puede borrar expedientes. |
| **Auxiliar de Oficina** | Expediente, Documento, Movimiento, Hoja_Ruta, Solicitante. | INSERT,  READ, UPDATE | Registra validaciones iniciales, modifica metadatos con errores materiales y genera la hoja de ruta. No borra registros físicos (solo anulación lógica). |
| **Técnico Administrativo** | Prestacion_Economica, Expediente, Asegurado, Tipo_Subsidio. | INSERT,  READ, UPDATE | Acceso de lectura a historiales clínicos/planillas. Inserta y actualiza cálculos de subsidios. No altera la tabla de Tipos de Subsidio (solo lectura). |
| **Solicitante (Externo)** | Expediente, Documento (propios), Solicitante. | INSERT (al crear trámite), READ | Solo puede insertar a través de la Mesa de Partes Digital y consultar (SELECT) únicamente los registros asociados a su propio ID. |
| **Sistema (Auditoría)** | Auditoria | INSERT,  READ | El disparador (Trigger) de base de datos solo permite insertar registros (logs) sobre quién hizo qué. Ni siquiera el DBA debería tener permiso de DELETE aquí. |

	

	- Metodología de Desarrollo y Adopción de Estándares Internacionales

	El ciclo de vida del desarrollo se regirá por una Metodología Híbrida basada en ASAP (Accelerated SAP) para las configuraciones centrales, integrada con prácticas ágiles para la construcción de los microservicios satelitales (como la Mesa de Partes Digital). Las fases son: Preparación, Blueprint (Diseño), Realización (Desarrollo iterativo), Preparación Final (Testing) y Puesta en Marcha.

	Para potenciar este ciclo de vida y garantizar la calidad empresarial, se integran tres marcos normativos fundamentales:

	- Buenas Prácticas ITIL v4 (Gestión del Servicio)

	ITIL asegura que el software entregado genere valor real al usuario final, pasando de ser solo un "sistema" a un "servicio gestionado".

	- Soporte y Mesa de Ayuda: Se implementará un proceso de Gestión de Incidentes y Gestión de Peticiones de Servicio. Si un ciudadano no puede cargar un PDF o un Auxiliar no puede firmar digitalmente, existirá un flujo estandarizado con Acuerdos de Nivel de Servicio (SLA) para resolver la caída, garantizando la continuidad operativa de la Mesa de Partes Digital.

	- Gestión de Despliegues: Se estandarizan los pases a producción para que las actualizaciones del motor de cálculo de prestaciones no interrumpan la atención diaria.

	- ISO/IEC 27001 (Seguridad de la Información)

	Al procesar resoluciones institucionales y datos financieros de subsidios, la base de datos debe cumplir con el Sistema de Gestión de Seguridad de la Información (SGSI).

	- Confidencialidad e Integridad: Se aplicará encriptación de datos en reposo (Transparent Data Encryption en la BD) para la información económica y el almacenamiento de los certificados de firma digital.

	- Trazabilidad Inalterable: La entidad de AUDITORIA se diseña bajo este estándar, asegurando el No Repudio de las acciones. Cada liquidación económica aprobada dejará un rastro criptográfico auditable.

	- ISO/IEC 29119 (Pruebas de Software)

	Este estándar estructura la estrategia técnica para validar el ERP antes de su salida a producción, mitigando fallos críticos.

	- Pruebas Estáticas: Revisiones formales del Modelo Entidad-Relación y del código fuente antes de la ejecución para evitar redundancias o cuellos de botella en la base de datos.

	- Pruebas Dinámicas basadas en Riesgos: Se priorizará el diseño de casos de prueba (Test Cases) rigurosos para la lógica de interoperabilidad (APIs que traen datos de Talento Humano) y pruebas de unidad y estrés sobre la generación del correlativo automático (concurrencia), asegurando que el sistema resista picos de alta demanda documental.

	- Script para elaborar la base de datos

| -- ============================================================ -- SCRIPT DDL – MODELO RELACIONAL (MR) -- ERP EsSalud La Libertad -- Módulo: Soporte Administrativo y Prestaciones Económicas -- Gestor: PostgreSQL 16 -- Autores: Grupo 1-A  │  NRC 5633 -- Normativa: ISO 27001 · Ley 29733 · DS 016-2024-JUS · Ley 27269 -- ============================================================ -- 1. ESQUEMA DROP SCHEMA IF EXISTS essalud_sii CASCADE; CREATE SCHEMA essalud_sii; SET search_path TO essalud_sii; -- ============================================================ -- 2. TABLAS -- ============================================================ -- 2.1 TIPO_SUBSIDIO (catálogo legal) CREATE TABLE tipo_subsidio (     id_tipo_subsidio          SERIAL          PRIMARY KEY,     codigo                    VARCHAR(10)     NOT NULL UNIQUE,     nombre_subsidio           VARCHAR(100)    NOT NULL,     meses_aporte_requerido    NUMERIC(3,0)    NOT NULL CHECK (meses_aporte_requerido > 0),     porcentaje_calculo        DECIMAL(5,2)    NOT NULL CHECK (porcentaje_calculo BETWEEN 0 AND 100),     estado_vigencia           BOOLEAN         NOT NULL DEFAULT TRUE,     fecha_creacion            TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ); COMMENT ON TABLE tipo_subsidio IS   'Catálogo normativo de tipos de subsidio. Solo el DBA puede modificar.'; -- 2.2 UNIDAD_ORGANICA CREATE TABLE unidad_organica (     id_unidad                 SERIAL          PRIMARY KEY,     codigo_dependencia        VARCHAR(20)     NOT NULL UNIQUE,     nombre_dependencia        VARCHAR(100)    NOT NULL,     nivel_jerarquico          VARCHAR(50),     id_unidad_padre           INTEGER         REFERENCES unidad_organica(id_unidad),     is_active                 BOOLEAN         NOT NULL DEFAULT TRUE,     fecha_creacion            TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ); COMMENT ON TABLE unidad_organica IS   'Dependencias de la Red La Libertad de EsSalud. Soporta jerarquía padre-hijo.'; COMMENT ON COLUMN unidad_organica.id_unidad_padre IS   'Relación reflexiva/recursiva permitida: una unidad puede pertenecer a otra (jerarquía orgánica).'; -- 2.3 USUARIO (personal interno del ERP) CREATE TABLE usuario (     id_usuario                SERIAL          PRIMARY KEY,     dni_ruc                   VARCHAR(15)     NOT NULL UNIQUE,     nombre                    VARCHAR(100)    NOT NULL,     apellidos                 VARCHAR(100)    NOT NULL,     rol                       VARCHAR(30)     NOT NULL                               CHECK (rol IN ('Administrador','Jefe_Oficina',                                              'Auxiliar','Tecnico_Prestaciones')),     email                     VARCHAR(100)    NOT NULL UNIQUE,     id_unidad_organica        INTEGER         REFERENCES unidad_organica(id_unidad),     estado_activo             BOOLEAN         NOT NULL DEFAULT TRUE,     -- ISO 27001 A.9 / DS 016-2024-JUS art. 46: gestión alta-baja     fecha_alta                TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,     fecha_baja                TIMESTAMP,     -- Ley 29733 art. 14.1: base legal del tratamiento (función pública)     base_legal_tratamiento    VARCHAR(150)    DEFAULT 'Función pública – Art. 14.1 Ley 29733',     creado_por                INTEGER         REFERENCES usuario(id_usuario) ); COMMENT ON TABLE usuario IS   'Personal interno con acceso al ERP. Control RBAC según ISO 27001 A.9.'; -- 2.4 SOLICITANTE (actor externo: ciudadano o institución) CREATE TABLE solicitante (     id_solicitante            SERIAL          PRIMARY KEY,     tipo_doc                  VARCHAR(10)     NOT NULL                               CHECK (tipo_doc IN ('DNI','RUC','CE','PASAPORTE')),     nro_doc                   VARCHAR(15)     NOT NULL,     nombre_razon_social       VARCHAR(150)    NOT NULL,     correo_electronico        VARCHAR(100),     telefono                  VARCHAR(20),     -- Ley 29733 art. 5 / DS 016-2024-JUS art. 5: trazabilidad del consentimiento     consentimiento_otorgado   BOOLEAN         NOT NULL DEFAULT FALSE,     fecha_consentimiento      TIMESTAMP,     version_politica_aceptada VARCHAR(10),     finalidad                 VARCHAR(200),     base_legal_tratamiento    VARCHAR(150),     -- Ley 29733 art. 8: retención y supresión     plazo_retencion_anios     INTEGER         DEFAULT 5,     fecha_supresion_programada DATE,     fecha_registro            TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,     UNIQUE (tipo_doc, nro_doc) ); COMMENT ON TABLE solicitante IS   'Personas naturales o jurídicas externas que inician trámites. Requieren consentimiento expreso.'; -- 2.5 ASEGURADO (titular del derecho EsSalud) CREATE TABLE asegurado (     id_asegurado              SERIAL          PRIMARY KEY,     dni                       VARCHAR(8)      NOT NULL UNIQUE,     nombre_completo           VARCHAR(200)    NOT NULL,     condicion_laboral         VARCHAR(50)     NOT NULL,     -- Puede coincidir con un solicitante (relación opcional)     id_solicitante            INTEGER         REFERENCES solicitante(id_solicitante),     -- Datos sensibles de salud – Ley 29733 art. sensible / DS 016-2024-JUS art. III num.6     base_legal_tratamiento    VARCHAR(150)    DEFAULT 'Función pública – Art. 14.1 Ley 29733',     plazo_retencion_anios     INTEGER         DEFAULT 10,     fecha_supresion_programada DATE,     fecha_registro            TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ); COMMENT ON TABLE asegurado IS   'Titular del derecho a prestaciones económicas. Datos de salud = dato sensible (Ley 29733).'; -- 2.6 EXPEDIENTE (núcleo del trámite documentario) CREATE TABLE expediente (     id_expediente             SERIAL          PRIMARY KEY,     numero_correlativo        VARCHAR(20)     NOT NULL UNIQUE,     asunto                    VARCHAR(255)    NOT NULL,     archivo_pdf_url           VARCHAR(500),     fecha_registro            TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,     fecha_vencimiento         TIMESTAMP,     status                    VARCHAR(50)     NOT NULL DEFAULT 'Pendiente_Verificacion'                               CHECK (status IN (                                 'Pendiente_Verificacion','Registrado_Conforme',                                 'Observado','En_Proceso','Atendido','Archivado','Anulado')),     id_solicitante            INTEGER         NOT NULL REFERENCES solicitante(id_solicitante),     id_usuario_creador        INTEGER         REFERENCES usuario(id_usuario),     id_unidad_destino_inicial INTEGER         REFERENCES unidad_organica(id_unidad),     observacion               TEXT,     -- Borrado lógico (ISO 27001 / trazabilidad)     eliminado_logico          BOOLEAN         NOT NULL DEFAULT FALSE,     fecha_eliminacion         TIMESTAMP ); COMMENT ON TABLE expediente IS   'Contenedor lógico del trámite. Nunca se elimina físicamente (borrado lógico).'; -- 2.7 DOCUMENTO (archivos adjuntos al expediente) CREATE TABLE documento (     id_documento              SERIAL          PRIMARY KEY,     id_expediente             INTEGER         NOT NULL REFERENCES expediente(id_expediente),     tipo_doc                  VARCHAR(50)     NOT NULL,     url_archivo               VARCHAR(500)    NOT NULL,     hash_firma                VARCHAR(255),   -- Ley 27269: validez de firma digital     fecha_carga               TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,     tamanio_kb                INTEGER,     estado                    VARCHAR(30)     NOT NULL DEFAULT 'Activo'                               CHECK (estado IN ('Activo','Anulado','Archivado')) ); COMMENT ON TABLE documento IS   'Archivos PDF adjuntos. hash_firma garantiza integridad conforme a Ley 27269.'; -- 2.8 HOJA_RUTA (trazabilidad de derivaciones) --   NOTA sobre la "relación cerrada" del MER: --   id_unidad_origen e id_unidad_destino apuntan ambos a UNIDAD_ORGANICA. --   Esto es una relación DOBLE al mismo destino, NO un bucle incorrecto. --   Se mantiene con el CHECK que impide origen = destino. CREATE TABLE hoja_ruta (     id_hoja_ruta              SERIAL          PRIMARY KEY,     id_expediente             INTEGER         NOT NULL REFERENCES expediente(id_expediente),     id_unidad_origen          INTEGER         NOT NULL REFERENCES unidad_organica(id_unidad),     id_unidad_destino         INTEGER         NOT NULL REFERENCES unidad_organica(id_unidad),     id_usuario_responsable    INTEGER         NOT NULL REFERENCES usuario(id_usuario),     fecha_traslado            TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,     proveido                  TEXT,     estado_movimiento         VARCHAR(30)     NOT NULL DEFAULT 'Recibido'                               CHECK (estado_movimiento IN (                                 'Recibido','En_Proceso','Derivado','Resuelto')),     CONSTRAINT chk_unidades_distintas CHECK (id_unidad_origen <> id_unidad_destino) ); COMMENT ON TABLE hoja_ruta IS   'Registro inmutable de cada derivación. Implementa trazabilidad audit-trail.'; -- 2.9 FIRMA_DIGITAL CREATE TABLE firma_digital (     id_firma                  SERIAL          PRIMARY KEY,     id_expediente             INTEGER         NOT NULL REFERENCES expediente(id_expediente),     id_usuario_firmante       INTEGER         NOT NULL REFERENCES usuario(id_usuario),     certificado_hash          VARCHAR(255)    NOT NULL,     sello_tiempo              TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,     estado_firma              VARCHAR(30)     NOT NULL DEFAULT 'Valida'                               CHECK (estado_firma IN ('Valida','Revocada','Expirada')) ); COMMENT ON TABLE firma_digital IS   'Registro de firmas digitales bajo Ley 27269 y certificados IOFE.'; -- 2.10 PRESTACION_ECONOMICA CREATE TABLE prestacion_economica (     id_prestacion             SERIAL          PRIMARY KEY,     id_expediente             INTEGER         NOT NULL UNIQUE  -- Cardinalidad 1:1                               REFERENCES expediente(id_expediente),     id_asegurado              INTEGER         NOT NULL REFERENCES asegurado(id_asegurado),     id_tipo_subsidio          INTEGER         NOT NULL REFERENCES tipo_subsidio(id_tipo_subsidio),     id_tecnico                INTEGER         NOT NULL REFERENCES usuario(id_usuario),     monto                     DECIMAL(10,2)   NOT NULL CHECK (monto >= 0),     fecha_liquidacion         TIMESTAMP,     estado_validacion         VARCHAR(30)     NOT NULL DEFAULT 'En_Calculo'                               CHECK (estado_validacion IN (                                 'En_Calculo','Liquidado','Rechazado','Pagado')),     motivo_rechazo            TEXT,     fecha_registro            TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP ); COMMENT ON TABLE prestacion_economica IS   'Un expediente activa exactamente una prestación (1:1). Cardinalidad forzada por UNIQUE.'; -- 2.11 AUDITORIA (log de eventos – ISO 27001 A.12 / DS 016-2024-JUS art. 46) CREATE TABLE auditoria (     id_auditoria              BIGSERIAL       PRIMARY KEY,     id_usuario                INTEGER         REFERENCES usuario(id_usuario),     tipo_evento               VARCHAR(30)     NOT NULL                               CHECK (tipo_evento IN (                                 'LOGIN','LOGOUT','INSERT','UPDATE','DELETE',                                 'SELECT_SENSIBLE','EXPORTACION','IMPORTACION',                                 'FIRMA','ERROR_ACCESO')),     tabla_afectada            VARCHAR(100),     registro_afectado_id      INTEGER,     accion_realizada          TEXT            NOT NULL,     fecha_hora                TIMESTAMP       NOT NULL DEFAULT CURRENT_TIMESTAMP,     direccion_ip              VARCHAR(45),    -- Soporta IPv4 e IPv6     sesion_id                 VARCHAR(100),     resultado                 VARCHAR(10)     NOT NULL DEFAULT 'EXITO'                               CHECK (resultado IN ('EXITO','FALLO'))     -- Retención mínima 2 años – DS 016-2024-JUS art. 46     -- DELETE y UPDATE prohibidos por GRANT (ver Sección 3) ); COMMENT ON TABLE auditoria IS   'Log inmutable. Sin UPDATE/DELETE. Retención >= 2 años. Backup WORM.'; -- ============================================================ -- 3. ÍNDICES (rendimiento en consultas frecuentes) -- ============================================================ CREATE INDEX idx_expediente_status        ON expediente(status); CREATE INDEX idx_expediente_solicitante   ON expediente(id_solicitante); CREATE INDEX idx_hoja_ruta_expediente     ON hoja_ruta(id_expediente); CREATE INDEX idx_auditoria_usuario_fecha  ON auditoria(id_usuario, fecha_hora DESC); CREATE INDEX idx_auditoria_tipo_evento    ON auditoria(tipo_evento); CREATE INDEX idx_prestacion_asegurado     ON prestacion_economica(id_asegurado); -- ============================================================ -- 4. TRIGGER DE AUDITORÍA AUTOMÁTICA -- ============================================================ CREATE OR REPLACE FUNCTION fn_auditoria_dml() RETURNS TRIGGER AS $$ BEGIN     INSERT INTO essalud_sii.auditoria         (id_usuario, tipo_evento, tabla_afectada,          registro_afectado_id, accion_realizada,          direccion_ip, sesion_id, resultado)     VALUES (         current_setting('app.current_user_id', TRUE)::INTEGER,         TG_OP,                              -- INSERT / UPDATE / DELETE         TG_TABLE_NAME,         COALESCE(NEW.id_expediente, OLD.id_expediente,                  NEW.id_usuario,   OLD.id_usuario,                  NEW.id_prestacion, OLD.id_prestacion),         format('Operación %s en tabla %s', TG_OP, TG_TABLE_NAME),         current_setting('app.client_ip', TRUE),         current_setting('app.session_id', TRUE),         'EXITO'     );     RETURN NEW; END; $$ LANGUAGE plpgsql SECURITY DEFINER; -- Aplicar trigger a tablas críticas CREATE TRIGGER trg_audit_expediente     AFTER INSERT OR UPDATE OR DELETE ON expediente     FOR EACH ROW EXECUTE FUNCTION fn_auditoria_dml(); CREATE TRIGGER trg_audit_prestacion     AFTER INSERT OR UPDATE ON prestacion_economica     FOR EACH ROW EXECUTE FUNCTION fn_auditoria_dml(); CREATE TRIGGER trg_audit_firma     AFTER INSERT ON firma_digital     FOR EACH ROW EXECUTE FUNCTION fn_auditoria_dml(); -- ============================================================ -- 5. ROLES Y PERMISOS RBAC --    ISO 27001 A.9 – Principio de Mínimo Privilegio --    DS 016-2024-JUS art. 46 – Control de acceso -- ============================================================ -- 5.1 Crear roles base CREATE ROLE rol_dba_essalud; CREATE ROLE rol_jefe_oficina; CREATE ROLE rol_auxiliar_oficina; CREATE ROLE rol_tecnico_prestaciones; CREATE ROLE rol_solicitante_externo; CREATE ROLE rol_sistema_auditoria; -- 5.2 DBA – acceso total (solo consola, nunca desde frontend) GRANT ALL PRIVILEGES ON ALL TABLES     IN SCHEMA essalud_sii TO rol_dba_essalud; GRANT ALL PRIVILEGES ON ALL SEQUENCES  IN SCHEMA essalud_sii TO rol_dba_essalud; GRANT USAGE ON SCHEMA essalud_sii TO rol_dba_essalud; -- 5.3 Jefe de Oficina – firma y supervisión GRANT USAGE ON SCHEMA essalud_sii TO rol_jefe_oficina; GRANT SELECT, UPDATE ON expediente    TO rol_jefe_oficina; GRANT SELECT         ON documento     TO rol_jefe_oficina; GRANT SELECT, INSERT ON hoja_ruta     TO rol_jefe_oficina; GRANT INSERT         ON firma_digital TO rol_jefe_oficina; -- NO tiene acceso a: usuario, auditoria, prestacion_economica, asegurado -- 5.4 Auxiliar de Oficina – registro y derivación GRANT USAGE ON SCHEMA essalud_sii TO rol_auxiliar_oficina; GRANT INSERT, SELECT, UPDATE ON expediente      TO rol_auxiliar_oficina; GRANT INSERT, SELECT, UPDATE ON documento       TO rol_auxiliar_oficina; GRANT INSERT, SELECT, UPDATE ON hoja_ruta       TO rol_auxiliar_oficina; GRANT INSERT, SELECT, UPDATE ON solicitante     TO rol_auxiliar_oficina; -- NO puede DELETE (solo borrado lógico vía UPDATE) -- 5.5 Técnico de Prestaciones Económicas GRANT USAGE ON SCHEMA essalud_sii TO rol_tecnico_prestaciones; GRANT SELECT               ON expediente            TO rol_tecnico_prestaciones; GRANT SELECT               ON asegurado             TO rol_tecnico_prestaciones; GRANT SELECT               ON tipo_subsidio         TO rol_tecnico_prestaciones; GRANT INSERT, SELECT, UPDATE ON prestacion_economica TO rol_tecnico_prestaciones; -- NO modifica tipo_subsidio (catálogo protegido) -- 5.6 Solicitante externo (vía capa de aplicación / API) GRANT USAGE ON SCHEMA essalud_sii TO rol_solicitante_externo; GRANT INSERT         ON solicitante TO rol_solicitante_externo; GRANT INSERT         ON expediente  TO rol_solicitante_externo; GRANT INSERT         ON documento   TO rol_solicitante_externo; GRANT SELECT         ON expediente  TO rol_solicitante_externo; -- filtrado por RLS -- 5.7 Sistema de Auditoría (trigger / cron) GRANT USAGE ON SCHEMA essalud_sii TO rol_sistema_auditoria; GRANT INSERT, SELECT ON auditoria TO rol_sistema_auditoria; -- Sin UPDATE ni DELETE sobre auditoria (inmutabilidad) -- ============================================================ -- 6. ROW LEVEL SECURITY (RLS) – Solicitante solo ve lo suyo -- ============================================================ ALTER TABLE expediente ENABLE ROW LEVEL SECURITY; CREATE POLICY policy_solicitante_propio ON expediente     FOR SELECT     TO rol_solicitante_externo     USING (         id_solicitante = current_setting('app.current_solicitante_id', TRUE)::INTEGER     ); COMMENT ON POLICY policy_solicitante_propio ON expediente IS   'Ley 29733 art. 7 – Proporcionalidad: el solicitante solo accede a sus propios expedientes.'; -- ============================================================ -- 7. USUARIOS DE BD (ejemplos por grupo) -- ============================================================ -- Administrador técnico CREATE USER dba_grupo1a WITH PASSWORD 'SecureP@ss_DBA_2026!' CONNECTION LIMIT 5; GRANT rol_dba_essalud TO dba_grupo1a; -- Jefe de oficina CREATE USER jefe_uo_docgest WITH PASSWORD 'JefeOf!c1na_2026' CONNECTION LIMIT 10; GRANT rol_jefe_oficina TO jefe_uo_docgest; -- Auxiliar de oficina CREATE USER auxiliar_mpd WITH PASSWORD 'Aux1l!arMPD_2026' CONNECTION LIMIT 20; GRANT rol_auxiliar_oficina TO auxiliar_mpd; -- Técnico prestaciones CREATE USER tecnico_pe WITH PASSWORD 'T3cn!coPE_2026' CONNECTION LIMIT 10; GRANT rol_tecnico_prestaciones TO tecnico_pe; -- Sistema auditoría CREATE USER sys_auditoria WITH PASSWORD 'S!stAud!tor!a_2026' CONNECTION LIMIT 5; GRANT rol_sistema_auditoria TO sys_auditoria; -- ============================================================ -- 8. DATOS SEMILLA (catálogo tipo_subsidio) -- ============================================================ INSERT INTO tipo_subsidio (codigo, nombre_subsidio, meses_aporte_requerido, porcentaje_calculo) VALUES     ('SUB-ENF',  'Subsidio por Enfermedad',           3,  66.67),     ('SUB-MAT',  'Subsidio por Maternidad',            3, 100.00),     ('SUB-LAC',  'Subsidio por Lactancia',             3, 100.00),     ('SUB-SEP',  'Subsidio por Sepelio',               1, 100.00),     ('SUB-INC',  'Subsidio por Incapacidad Temporal',  3,  66.67); INSERT INTO unidad_organica (codigo_dependencia, nombre_dependencia, nivel_jerarquico) VALUES     ('RED-LL-001', 'Red La Libertad - Sede Central',      'Red'),     ('RED-LL-002', 'Oficina de Gestión Documentaria',     'Unidad'),     ('RED-LL-003', 'Unidad de Prestaciones Económicas',   'Unidad'),     ('RED-LL-004', 'Unidad de Tesorería y Presupuesto',   'Unidad'),     ('RED-LL-005', 'Oficina de Tecnologías de Información','Unidad'); |
| --- |

		Creación de la base de datos en pgAdmin4

	Figura 18 - DB en pgAdmin4 - PostgreSQL

		Creación de la base de datos en Supabase (nube)

		Figura 19 - DB en Supabase - PostgreSQL

		

	##### PROPUESTA DE MARCO NORMATIVO Y CUMPLIMIENTO LEGAL

		Consideraciones:

	- La consolidación de las bases de datos del proyecto está plenamente alcanzada por la Ley N.° 29733 y su nuevo Reglamento (DS 016-2024-JUS, vigente desde el 30 de marzo de 2025): EsSalud es una entidad pública que trata datos personales (incluidos datos sensibles de salud) y por ello está obligada a inscribir sus bancos de datos en el RNPD, designar un Oficial de Datos Personales, contar con un Documento de Seguridad de fecha cierta y notificar incidentes en 48 horas.

	- El diseño actual (RBAC, transacciones ACID, tabla AUDITORIA, hash_firma) cubre parcialmente las exigencias técnicas de la NTP-ISO/IEC 27001 (de uso obligatorio en el Estado peruano desde la RM 004-2016-PCM) pero presenta brechas relevantes: ausencia de campos de consentimiento y base legal, falta de políticas de retención/supresión, cifrado no acreditado y trazabilidad de auditoría incompleta frente al artículo 46 del DS 016-2024-JUS.

	- Las recomendaciones prioritarias son: añadir campos de consentimiento/finalidad/retención en SOLICITANTE y ASEGURADO, documentar la base legal del tratamiento sin consentimiento (art. 14.1 de la Ley para el ejercicio de funciones públicas), cifrar datos sensibles, reforzar la tabla AUDITORIA con los eventos exigidos, e inscribir el banco de datos consolidado en el RNPD.

	- Decreto Legislativo N.º 1412

		**Conceptos de marcos legales y normativas**

	- **Ley N.° 29733 — Ley de Protección de Datos Personales**

	- Dato personal: Toda información numérica, alfabética, gráfica, fotográfica, acústica o de cualquier otro tipo que identifique o haga identificable a una persona natural.

	- Dato sensible: Dato personal que revela origen racial o étnico, ingresos económicos, opiniones políticas, convicciones religiosas, datos de salud, vida sexual, biométricos o genéticos. Su tratamiento exige protección reforzada y consentimiento expreso.

	- Titular del dato: La persona natural a quien corresponde el dato personal. Es quien ejerce los derechos ARCO sobre su propia información.

	- Banco de datos personales: Conjunto organizado de datos personales, automatizado o no, cualquiera sea la forma o modalidad de su creación, almacenamiento y organización.

	- Responsable del banco de datos: Persona natural, jurídica de derecho privado o entidad pública que determina la finalidad y contenido del tratamiento de datos personales.

	- Encargado del tratamiento: Persona natural o jurídica que trata datos personales por cuenta y bajo instrucciones del responsable, sin que dichos datos formen parte de sus propios bancos de datos.

	- Tratamiento de datos personales: Cualquier operación sobre datos personales: recopilación, registro, organización, almacenamiento, conservación, elaboración, modificación, extracción, consulta, utilización, bloqueo, supresión, comunicación o transferencia.

	- Principio de legalidad (art. 4): Prohíbe la recopilación de datos por medios fraudulentos, desleales o ilícitos. Los datos deben captarse a través de canales oficiales habilitados.

	- Principio de consentimiento (art. 5): El tratamiento de datos personales requiere el consentimiento libre, previo, expreso, inequívoco e informado del titular, salvo las excepciones legales.

	- Consentimiento expreso: Manifestación afirmativa de voluntad, clara y verificable, que el titular otorga antes del tratamiento. Para datos sensibles no puede ser tácito ni implícito.

	- Excepción de función pública (art. 14.1): Permite el tratamiento sin consentimiento cuando los datos son recopilados o tratados para el ejercicio de las funciones propias de las entidades públicas en el ámbito de sus competencias legales.

	- Principio de finalidad (art. 6): Los datos deben recopilarse para una finalidad determinada, explícita y lícita. No pueden usarse para fines distintos a los declarados sin nuevo consentimiento.

	- Principio de proporcionalidad (art. 7): El tratamiento debe ser adecuado, relevante y no excesivo en relación con la finalidad para la que se recopilaron los datos.

	- Principio de calidad (art. 8): Los datos deben ser exactos, completos, actualizados y conservarse solo durante el tiempo necesario para la finalidad que motivó su recopilación.

	- Principio de seguridad (arts. 9 y 16): Obliga al responsable y encargado a adoptar medidas técnicas, organizativas y legales que garanticen la confidencialidad, integridad y disponibilidad de los datos, evitando alteración, pérdida o acceso no autorizado.

	- Principio de disposición de recurso (art. 10): El titular debe contar con vías efectivas para reclamar ante el responsable o la autoridad competente ante vulneraciones a sus derechos.

	- Principio de nivel de protección adecuado (art. 11): Para flujos transfronterizos, el país receptor debe garantizar un nivel de protección equivalente al de la ley peruana.

	- Derechos ARCO: Conjunto de derechos del titular: Acceso (art. 19), Rectificación (art. 20), Cancelación (art. 21) y Oposición (art. 22). Deben atenderse en un plazo máximo de 20 días hábiles.

	- Derecho de acceso (art. 19): El titular puede solicitar información sobre si sus datos son tratados, con qué finalidad, qué datos se tienen y a quiénes han sido comunicados.

	- Derecho de rectificación (art. 20): El titular puede exigir la corrección de datos inexactos, incompletos o desactualizados.

	- Derecho de cancelación (art. 21): El titular puede solicitar la supresión de datos cuando ya no sean necesarios para la finalidad para la que fueron recopilados o cuando el tratamiento sea ilícito.

	- Derecho de oposición (art. 22): El titular puede oponerse al tratamiento de sus datos para finalidades secundarias o cuando exista causa legítima y fundada referida a su situación personal.

	- Flujo transfronterizo de datos (art. 11): Transferencia de datos personales a un destinatario ubicado en un país distinto al de origen, sujeta a garantías de protección equivalente.

	- **D.S. N.° 016-2024-JUS — Reglamento de la Ley 29733**

	- Responsabilidad proactiva (art. IX / Título Preliminar): Principio que exige que el responsable no solo cumpla la normativa, sino que pueda demostrar ese cumplimiento en todo momento mediante documentación, registros y evidencias verificables.

	- Protección desde el diseño: Obligación de incorporar medidas de protección de datos desde la concepción del sistema o proceso, no como añadido posterior. El modelo de datos, la arquitectura y los flujos deben diseñarse con privacidad por defecto.

	- Protección por defecto: Los sistemas deben configurarse de manera que, por defecto, solo se traten los datos estrictamente necesarios para cada finalidad específica, sin intervención activa del usuario para restringir el acceso.

	- Datos biométricos (art. III, num. 6): Datos personales obtenidos a partir de un tratamiento técnico específico relativo a las características físicas, fisiológicas o conductuales de una persona que permiten su identificación única. Incorporados explícitamente como datos sensibles por este Reglamento.

	- Datos genéticos (art. III, num. 6): Datos personales relativos a las características genéticas heredadas o adquiridas de una persona que proporcionan información única sobre su fisiología o estado de salud. Incorporados como datos sensibles por este Reglamento.

	- Oficial de Protección de Datos (OPD) (art. 37): Figura obligatoria para entidades públicas que tratan datos sensibles a gran escala, designada formalmente desde el 1 de diciembre de 2025. Equivale al Data Protection Officer del RGPD europeo. Supervisa el cumplimiento normativo, gestiona los derechos ARCO y coordina la respuesta ante incidentes.

	- Evaluación de Impacto relativa a la Protección de Datos (EIPD) (art. 40): Análisis previo obligatorio cuando el tratamiento implica alto riesgo para los derechos de los titulares, especialmente en tratamiento de datos sensibles a gran escala. Describe los datos tratados, evalúa riesgos, medidas adoptadas y residualidad del riesgo.

	- Registro Nacional de Protección de Datos Personales (RNPD) (art. 42): Registro público administrado por la ANPD donde las entidades deben inscribir sus bancos de datos personales. Desde el 31 de marzo de 2025, la inscripción es gratuita, virtual (plataforma SIPDP) y de aprobación automática con fiscalización posterior.

	- SIPDP: Sistema Informático de Protección de Datos Personales. Plataforma virtual de la ANPD para la inscripción de bancos de datos en el RNPD.

	- Notificación de incidentes de seguridad (art. 34): Obligación de comunicar a la ANPD cualquier brecha de seguridad dentro de las 48 horas posteriores a tomar conocimiento, incluso si el incidente fue subsanado internamente. Si ocurrió en entorno digital, también debe notificarse al Centro Nacional de Seguridad Digital.

	- Centro Nacional de Seguridad Digital (CNSD) (art. 34.5): Entidad a la que deben reportarse los incidentes de seguridad digital conforme al Decreto de Urgencia N.° 007-2020, para su incorporación al Registro Nacional de Incidentes de Seguridad Digital.

	- Documento de Seguridad (art. 47): Documento formal aprobado con fecha cierta que describe las medidas técnicas y organizativas implementadas para proteger los datos personales. Debe incluir inventario de datos, procedimientos de acceso, gestión de incidentes y plan de formación. Toma como referencia la NTP-ISO/IEC 27001.

	- Inventario de datos personales (art. 47.3): Registro detallado de todos los datos personales tratados, los sistemas que los procesan y su clasificación según nivel de sensibilidad. Componente obligatorio del Documento de Seguridad.

	- Portabilidad de datos (art. 76): Derecho del titular a recibir sus datos en un formato estructurado, de uso común y lectura mecánica, para transmitirlos a otro responsable sin impedimento.

	- Gestión de accesos (art. 46): Obligación de controlar el acceso a los sistemas desde el alta hasta la baja del usuario, con identificación, autenticación y verificación periódica de privilegios con intervalo mínimo semestral.

	- Registros de auditoría (art. 46): Logs que registran todas las operaciones sobre datos personales: usuario, acción, registro afectado, timestamp, IP, inicio y cierre de sesión, importaciones y exportaciones. Deben conservarse por mínimo 2 años.

	- Cifrado de datos (art. 52): Obligación de usar mecanismos criptográficos para proteger los datos en transmisión. El Reglamento menciona cifrado, firmas y certificados digitales, y checksum como herramientas válidas.

	- Copias de respaldo (art. 51): Obligación de realizar copias de seguridad con frecuencia mínima semanal, verificando su integridad, y almacenarlas con las mismas medidas de seguridad que los datos originales.

	- Flujo transfronterizo (arts. 18-21): Regulación detallada de la transferencia internacional de datos personales. Solo procede si el país receptor tiene nivel adecuado de protección reconocido por la ANPD o si el exportador otorga garantías adecuadas mediante cláusulas contractuales modelo.

	- Cláusulas contractuales modelo: Mecanismo de garantía para el flujo transfronterizo cuando el país receptor no tiene nivel adecuado de protección reconocido. Son contratos tipo aprobados por la autoridad que vinculan al importador de datos a cumplir estándares equivalentes a la ley peruana.

	- Consentimiento en canales digitales (art. 5): En entornos digitales, el consentimiento debe exteriorizarse mediante una acción concreta que demuestre aceptación (no casillas premarcadas) y debe ser demostrable, con registro técnico de fecha, hora, IP y versión del texto aceptado.

	- **NTP-ISO/IEC 27001 — Gestión de Seguridad de la Información**

	- Sistema de Gestión de Seguridad de la Información (SGSI): Marco estructurado de políticas, procesos, procedimientos y controles que una organización implementa para gestionar los riesgos sobre la seguridad de su información de manera sistemática y continua.

	- Confidencialidad: Propiedad de la información que garantiza que solo las personas autorizadas pueden acceder a ella. Uno de los tres pilares del SGSI junto con integridad y disponibilidad.

	- Integridad: Propiedad que garantiza que la información no ha sido alterada de forma no autorizada. En bases de datos se materializa mediante restricciones referenciales, triggers y registros inmutables.

	- Disponibilidad: Propiedad que garantiza que la información y los sistemas son accesibles y utilizables cuando se necesiten por las personas autorizadas.

	- Control A.8 – Gestión de Activos: Exige un inventario actualizado de todos los activos de información, su clasificación según nivel de sensibilidad y la asignación de un responsable por cada activo.

	- Control A.9 – Control de Acceso: Establece que el acceso a la información debe limitarse según el principio de mínimo privilegio. Abarca la gestión de cuentas de usuario, autenticación, revisión periódica de derechos y segregación de funciones.

	- Principio de mínimo privilegio: Cada usuario, proceso o sistema debe tener únicamente los permisos estrictamente necesarios para cumplir sus funciones, sin accesos adicionales que representen riesgo innecesario.

	- Segregación de funciones: Distribución de tareas críticas entre distintos roles o personas para evitar que una sola persona pueda cometer y ocultar errores o fraudes sin ser detectada.

	- Control A.10 – Criptografía: Establece el uso de controles criptográficos para proteger la confidencialidad, autenticidad e integridad de la información, tanto en tránsito como en reposo.

	- Cifrado en tránsito: Protección criptográfica de los datos mientras se transmiten por redes. Se implementa mediante TLS 1.3, que cifra el canal de comunicación entre el cliente y el servidor.

	- TLS 1.3 (Transport Layer Security versión 1.3): Protocolo criptográfico que establece canales de comunicación seguros entre sistemas. Es el estándar actual para cifrado en tránsito, con mejoras de seguridad y rendimiento respecto a versiones anteriores.

	- Cifrado en reposo: Protección criptográfica de los datos almacenados en discos, bases de datos o sistemas de archivos, de modo que sean ilegibles sin la clave correspondiente aunque se acceda físicamente al medio de almacenamiento.

	- TDE (Transparent Data Encryption): Técnica de cifrado en reposo que opera a nivel del motor de base de datos o del sistema operativo, cifrando automáticamente los archivos físicos de datos sin requerir cambios en la aplicación.

	- AES-256 (Advanced Encryption Standard de 256 bits): Algoritmo de cifrado simétrico considerado estándar de seguridad robusta para protección de datos sensibles en reposo y en tránsito.

	- HSM (Hardware Security Module): Dispositivo físico dedicado a la gestión segura de claves criptográficas, con certificación FIPS 140-2. Protege las claves maestras de cifrado contra extracción o manipulación.

	- Control A.12 – Seguridad Operacional: Cubre los procedimientos para garantizar la operación segura y continua de los sistemas: registros de auditoría, protección contra malware, gestión de vulnerabilidades y copias de respaldo.

	- Logs de auditoría: Registros cronológicos e inmutables de eventos ocurridos en un sistema: accesos, modificaciones, errores y operaciones críticas. Permiten reconstruir lo sucedido ante un incidente.

	- Inmutabilidad de registros: Característica de los logs de auditoría que impide su modificación o eliminación posterior. Se logra restringiendo los permisos de UPDATE y DELETE sobre las tablas de log y replicándolos a sistemas WORM.

	- WORM (Write Once Read Many): Tecnología de almacenamiento que permite escribir datos una sola vez y leerlos múltiples veces, pero impide su modificación o borrado. Garantiza la inmutabilidad de registros de auditoría.

	- Trigger de base de datos: Procedimiento almacenado en el motor que se ejecuta automáticamente ante eventos definidos (INSERT, UPDATE, DELETE) sobre una tabla. Implementado en el motor, no puede ser evadido por la capa de aplicación.

	- Control A.13 – Seguridad en Comunicaciones: Establece mecanismos para proteger la transferencia de información entre sistemas, APIs y redes, incluyendo protección contra ataques de interceptación e inyección.

	- Control A.18 – Cumplimiento: Exige identificar la legislación aplicable, proteger los registros organizacionales, los datos personales y revisar periódicamente la seguridad. Incluye la regulación de controles criptográficos.

	- **Conceptos Técnicos de Base de Datos**

	- Borrado lógico: Técnica que marca un registro como eliminado mediante un campo de estado (estado = ANULADO) sin eliminarlo físicamente de la base de datos. Preserva la trazabilidad y el historial completo para auditorías.

	- Versionado de registros: Mecanismo que genera un nuevo registro ante cada modificación, enlazado al original, manteniendo el historial completo de cambios. Aplicado en la HCE, cada corrección crea un nuevo episodio sin alterar el anterior.

	- Integridad referencial: Conjunto de restricciones (claves foráneas, CHECK, NOT NULL) implementadas en el motor de base de datos que garantizan la consistencia de las relaciones entre tablas, independientemente del canal de acceso.

	- ACID: Propiedades que garantizan la confiabilidad de las transacciones en bases de datos:

	- Atomicidad: La transacción es todo o nada.

	- Consistencia: Los datos pasan de un estado válido a otro.

	- Aislamiento: Las transacciones concurrentes no se interfieren.

	- Durabilidad: Los cambios confirmados persisten ante fallos.

	- pgcrypto: Extensión de PostgreSQL que provee funciones criptográficas a nivel de columna, permitiendo cifrar y descifrar valores específicos dentro de las tablas sin necesidad de cifrado de todo el volumen.

	- Database Masking: Técnica de ocultación de datos sensibles mediante vistas que muestran versiones parciales o enmascaradas de atributos críticos (por ejemplo, DNI como 45***891) para roles que no requieren ver el valor completo.

	- Hash anónimo: Identificador generado mediante función hash criptográfica que permite correlacionar registros entre tablas sin exponer el dato original. Usado en la tabla DISPENSACION para vincular entregas de fármacos sin revelar el diagnóstico clínico.

	- RTO (Recovery Time Objective): Tiempo máximo tolerable que puede estar inoperativo un sistema tras un incidente antes de que el impacto sea inaceptable. Define la velocidad mínima de recuperación requerida.

	- RPO (Recovery Point Objective): Cantidad máxima de datos que una organización puede permitirse perder ante un incidente, medida en tiempo. Un RPO de 15 minutos significa que los backups deben garantizar recuperar el estado del sistema hasta 15 minutos antes del fallo.

	- **Otras Normas Conexas**

	- Ley N.° 27269 – Ley de Firmas y Certificados Digitales: Otorga validez jurídica a la firma digital en el Perú, equiparándola a la firma manuscrita cuando se usa un certificado acreditado bajo IOFE. Relevante para el campo hash_firma en documentos del sistema.

	- Decreto Legislativo N.° 1412 – Ley de Gobierno Digital: Marco legal del gobierno digital peruano. Su reglamento sirve de base para la designación obligatoria del OPD en entidades públicas conforme al art. 37.1 del DS 016-2024-JUS.

	- Decreto de Urgencia N.° 007-2020: Establece el Centro Nacional de Seguridad Digital (CNSD) y el Registro Nacional de Incidentes de Seguridad Digital. Los incidentes ocurridos en entornos digitales deben notificarse al CNSD además de a la ANPD.

	- RGPD (Reglamento General de Protección de Datos): Reglamento europeo de protección de datos (2016/679). Aunque no es vinculante en Perú, el DS 016-2024-JUS adopta figuras análogas (OPD, EIPD, portabilidad, responsabilidad proactiva) y es referencia para evaluar el nivel de protección adecuado de países de la Unión Europea en flujos transfronterizos.

	- Marco Normativo aplicable

	Para el módulo de procesos de soporte administrativo y prestaciones económicas, se inscribe en una jerarquía normativa encabezada por la Constitución Política del Perú, cuyo artículo 2, numeral 6, reconoce el derecho fundamental a que los servicios informáticos no suministren información que afecte la intimidad personal y familiar. De ese mandato deriva la Ley N.° 29733, Ley de Protección de Datos Personales, promulgada el 21 de junio de 2011 y publicada en el Diario Oficial El Peruano el 3 de julio de 2011, norma con rango de ley que constituye el cuerpo sustantivo del régimen. La Ley fija el objeto, las definiciones, los principios rectores, los derechos del titular (ARCO) y las obligaciones de los titulares y encargados de bancos de datos.

	En el segundo nivel se ubica el Decreto Supremo N.° 016-2024-JUS, nuevo Reglamento de la Ley 29733, publicado el 30 de noviembre de 2024 y vigente desde el 30 de marzo de 2025, que derogó el antiguo DS 003-2013-JUS. Como norma reglamentaria, desarrolla operativamente la Ley sin contradecirla: la Ley 29733 "sigue plenamente vigente" y el nuevo Reglamento "solo deroga al reglamento anterior". Conforme al artículo 1 del propio DS 016-2024-JUS, el Reglamento se compone de "un (1) Título Preliminar, tres (3) Títulos, ciento treinta y cinco (135) artículos, seis (6) Disposiciones Complementarias Finales y dos (2) Disposiciones Complementarias Transitorias", e introduce la responsabilidad proactiva, la protección desde el diseño y por defecto, la evaluación de impacto, el Oficial de Datos Personales, la portabilidad y la notificación de incidentes en 48 horas.

	En un tercer plano se sitúa la ISO/IEC 27001, estándar internacional de Sistemas de Gestión de Seguridad de la Información. En el Perú su versión nacional, la NTP-ISO/IEC 27001, es de uso obligatorio para todas las entidades integrantes del Sistema Nacional de Informática en virtud de la Resolución Ministerial N.° 004-2016-PCM (Lima, 8 de enero de 2016), emitida por la PCM a través de la ONGEI como ente rector del Sistema Nacional de Informática, que dispuso: "Apruébese el uso obligatorio de la Norma Técnica Peruana NTP ISO/IEC 27001:2014… Requisitos. 2ª Edición, en todas las entidades integrantes del Sistema Nacional de Informática". Aunque la ISO 27001 es técnicamente una norma voluntaria de gestión, en el contexto peruano adquiere fuerza vinculante para el sector público y, además, el propio DS 016-2024-JUS la incorpora por remisión: su artículo 47 señala que el Documento de Seguridad "puede tomar como referencia los requisitos y controles indicados en la NTP-ISO/IEC 27001 vigente" y su artículo 48 remite a la NTP-ISO/IEC 27001:2022. Así, la jerarquía formal (Ley > Reglamento > norma técnica) se complementa con una articulación funcional en la que la ISO 27001 opera como el estándar técnico que materializa el principio de seguridad de la Ley.

	Como EsSalud es una entidad pública (Seguro Social de Salud), también le resultan aplicables, de forma conexa, la Ley N.° 27269 de Firmas y Certificados Digitales (que otorga validez jurídica a la firma digital, relevante para el campo hash_firma) y el Decreto Legislativo N.° 1412, Ley de Gobierno Digital, cuyo Reglamento sirve de base para la designación obligatoria del Oficial de Datos Personales en entidades públicas (art. 37.1 del DS 016-2024-JUS).

	- Principios de ley 29733 aplicados al proyecto

	- Legalidad (art. 4). Prohíbe la recopilación de datos por medios fraudulentos, desleales o ilícitos. En el proyecto, los datos de ASEGURADO (DNI, nombre, condición laboral) y de SOLICITANTE externo deben capturarse a través de formularios oficiales (p. ej., el Formulario 1040 de prestaciones económicas) y canales legítimos como la Mesa de Partes Digital, garantizando la licitud del origen.

	- Consentimiento (art. 5) y sus limitaciones (art. 14). Es el principio crítico para una entidad pública. El artículo 14.1 de la Ley exime del consentimiento cuando los datos se recopilan o tratan para el ejercicio de las funciones propias de las entidades públicas en el ámbito de sus competencias. EsSalud, al tramitar expedientes y subsidios, actúa bajo esta excepción: no necesita consentimiento del ASEGURADO para procesar su subsidio porque el tratamiento es necesario para el cumplimiento de las competencias asignadas por ley. Sin embargo, esta excepción no es absoluta. Para datos del SOLICITANTE externo (un tercero que no es asegurado, p. ej., quien tramita un sepelio) y para finalidades secundarias (notificaciones, encuestas), sí se requiere consentimiento expreso, previo, informado e inequívoco. El DS 016-2024-JUS (art. 5) precisa que en canales digitales el consentimiento debe exteriorizarse mediante una acción que demuestre aceptación concreta y debe ser demostrable.

	- Finalidad (art. 6). Los datos deben recopilarse para una finalidad determinada, explícita y lícita, y no extenderse a otra distinta. En la consolidación de bases de datos esto es delicado: unir USUARIO, EXPEDIENTE, PRESTACION_ECONOMICA y AUDITORIA en un solo repositorio no debe usarse para fines ajenos al trámite documentario y al pago de prestaciones (p. ej., perfilamiento no autorizado).

	- Proporcionalidad (art. 7). El tratamiento debe ser adecuado, relevante y no excesivo. La entidad SOLICITANTE no debería capturar más campos de los necesarios para identificar y notificar al tramitante.

	- Calidad (art. 8). Los datos deben ser veraces, exactos, actualizados y conservarse solo por el tiempo necesario. Esto exige mecanismos de actualización (sincronización con RENIEC para validar DNI) y, sobre todo, políticas de retención y supresión —hoy ausentes en el diseño.

	- Seguridad (art. 9 y 16). Obliga a adoptar medidas técnicas, organizativas y legales que eviten alteración, pérdida o acceso no autorizado. Aquí se articulan el RBAC, las transacciones ACID, la tabla AUDITORIA y el hash_firma con los artículos 46-52 del DS 016-2024-JUS y los controles de ISO 27001.

	- Disposición de recurso (art. 10). El titular debe contar con vías para reclamar (ARCO). El sistema debe implementar funcionalidades para que ASEGURADO y SOLICITANTE ejerzan acceso, rectificación, cancelación y oposición, con respuesta en plazo de 20 días hábiles.

	- Nivel de protección adecuado (art. 11). Aplica al flujo transfronterizo: si la arquitectura cloud aloja datos fuera del Perú, debe garantizarse protección equiparable.

	- Impacto del Decreto Supremo 016-2024-JUS

	Registro de bancos de datos ante la ANPD. El artículo 42.1 obliga a las entidades públicas que creen, modifiquen o cancelen bancos de datos personales a inscribir dichos actos en el Registro Nacional de Protección de Datos Personales (RNPD). Desde el 31 de marzo de 2025 la inscripción es gratuita, virtual (plataforma SIPDP) y de aprobación automática con fiscalización posterior. La consolidación de múltiples tablas en un repositorio único configura la creación/modificación de un banco de datos que debe declararse, indicando finalidades y categorías de datos (incluidos los sensibles de salud).

	Consentimiento informado en sistemas digitales de trámite documentario. El Reglamento exige consentimiento libre, previo, expreso, informado, inequívoco y demostrable. En auditoría, "tienes que poder probar cuándo, cómo y en qué términos aceptó", lo que se traduce en registros técnicos con fecha, hora, IP y versión del texto aceptado. Para SISGEDO esto implica que, cuando el tratamiento dependa del consentimiento (solicitantes externos, finalidades secundarias), debe registrarse de forma trazable.

	Flujos transfronterizos (arquitectura cloud). Los artículos 18 a 21 establecen que el flujo transfronterizo solo procede si el país receptor tiene nivel adecuado de protección (resolución de la autoridad) o si el exportador otorga garantías adecuadas (cláusulas contractuales modelo). La carga de la prueba recae en el responsable. Si EsSalud usa servidores cloud fuera del Perú, debe documentar estas garantías y poner el flujo en conocimiento de la autoridad.

	Nuevas obligaciones para entidades que consolidan múltiples bases de datos. Destacan: (i) designación obligatoria de un Oficial de Datos Personales por tratarse de entidad pública (art. 37.1.1, en conexión con el Reglamento de la Ley de Gobierno Digital); (ii) Documento de Seguridad aprobado formalmente y con fecha cierta (art. 47); (iii) evaluación de impacto relativa a la protección de datos para tratamientos de alto riesgo (art. 40); (iv) notificación de incidentes a la ANPD —según el art. 34, texto oficial de El Peruano, el responsable "debe notificar a la Autoridad Nacional de Protección de Datos Personales como máximo dentro de las 48 horas posteriores a haber tomado conocimiento o constancia de ello… aun cuando… considere que tal incidente haya sido subsanado o resuelto internamente"— y, conforme al art. 34.5, "en caso de que el incidente… se desarrolle en y/o mediante el entorno digital la notificación se realiza, además de la Autoridad Nacional de Protección de Datos Personales, al Centro Nacional de Seguridad Digital para su incorporación al Registro Nacional de Incidentes de Seguridad Digital conforme… al Decreto de Urgencia Nº 007-2020"; (v) responsabilidad proactiva, que exige documentar todas las decisiones.

	- ISO 27001 como complemento normativo

	El Anexo A de ISO 27001 actúa como el catálogo técnico que operativiza el principio de seguridad. Usando la nomenclatura del Anexo A:2013 indicada en el encargo, los controles se articulan así:

	- A.8 Gestión de Activos. Exige inventario y clasificación de la información. El DS 016-2024-JUS (art. 47.3) ordena elaborar un inventario de datos personales y sistemas, especificando cuáles son sensibles. En el proyecto, debe clasificarse que ASEGURADO y PRESTACION_ECONOMICA contienen datos sensibles de salud, sujetos a protección reforzada.

	- A.9 Control de Acceso. Es el control mejor cubierto por el diseño (RBAC). Se articula con el art. 46 del DS 016-2024-JUS, que exige gestión de accesos desde el alta hasta la baja del usuario, identificación y autenticación, y verificación periódica de privilegios en intervalo mínimo semestral.

	- A.12 Seguridad Operacional. Cubre registros (logging), respaldo y protección contra malware. Se articula con el art. 46 (logs de auditoría conservados por mínimo 2 años) y el art. 51 (copias de respaldo con frecuencia semanal mínima y verificación de integridad). La tabla AUDITORIA debe ampliarse para cumplir el detalle de eventos exigido.

	- A.18 Cumplimiento. Exige identificar la legislación aplicable, proteger registros y datos personales y revisar la seguridad. Es la articulación directa con la Ley 29733 y el DS 016-2024-JUS, e incluye la regulación de controles criptográficos, base del cifrado exigido por el art. 52 para transferencias.

| **Requisito normativo** | **Norma fuente** |
| --- | --- |
| Licitud del origen de los datos | Ley 29733, art. 4 |
| Consentimiento / base legal del tratamiento | Ley 29733, arts. 5 y 14; DS 016-2024-JUS, art. 5 |
| Finalidad determinada en consolidación | Ley 29733, art. 6 |
| Proporcionalidad / minimización | Ley 29733, art. 7 |
| Calidad y retención | Ley 29733, art. 8 |
| Seguridad del tratamiento | Ley 29733, arts. 9 y 16; DS 016-2024-JUS, arts. 46-52; ISO 27001 A.9/A.12 |
| Registros de auditoría (logging) | DS 016-2024-JUS, art. 46; ISO 27001 A.12 |

	

	- Diagramas de actividades

	- Gestión de consentimiento y base legal del tratamiento

	

	- Atención de Derechos ARCO

	

	- Gestión de retención y supresión de datos

	- Notificación de Incidentes de Seguridad (48 horas)

	- Gestión de Accesos RBAC (ISO 27001 A.9)

	

	- Registro de Auditoría Conforme al DS 016-2024-JUS

	

	- Inscripción y Actualización del Banco de Datos en RNPD

	

	

	- Evaluación de Impacto de Protección de Datos (EIPD)

	

	

	

	- Diagramas de secuencia

	- Gestión de Consentimiento y Base Legal del Tratamiento

	

	- Atención de Derechos ARCO

	

	- Gestión de Retención y Supresión de Datos

	

	

	- Notificación de Incidentes de Seguridad (48 horas)

	

	- Gestión de Accesos RBAC (ISO 27001 A.9)

	

	- Registro de Auditoría Conforme al DS 016-2024-JUS

	

	- Inscripción y Actualización del Banco de Datos en RNPD

	

	- Evaluación de Impacto de Protección de Datos (EIPD)

	##### IMPLEMENTACIÓN DE LA METODOLOGÍA UWE BAJO EL ESTÁNDAR UML

	- Introducción a UWE

	UWE (UML-based Web Engineering) es una metodología de ingeniería web basada en el estándar UML que permite modelar sistemas de información accesibles por web de forma sistemática y rigurosa. Se caracteriza por producir cinco modelos complementarios que describen el sistema desde distintas perspectivas: requisitos funcionales, estructura de contenido, estructura de navegación, estructura de presentación y lógica de procesos de negocio.

	En el presente proyecto, UWE se aplica al Módulo de Procesos de Soporte Administrativo y Prestaciones Económicas del ERP de EsSalud — Red La Libertad. Este módulo comprende dos submódulos funcionales: el sistema SISGEDO (Mesa de Partes Digital y gestión documental interna) y el submódulo de Prestaciones Económicas, ambos integrados mediante APIs RESTful con los módulos de Núcleo Asistencial y Talento Humano del ERP institucional.

	- Alcance del Modelado

	El alcance del modelado UWE cubre de forma integral el Módulo de Procesos de Soporte Administrativo y Prestaciones Económicas del ERP institucional de EsSalud - Red La Libertad. Este módulo constituye la capa web del sistema y abarca dos dominios funcionales interrelacionados: el sistema SISGEDO, que gestiona el ciclo de vida completo del trámite documentario desde la recepción en la Mesa de Partes Digital hasta el archivado final; y el submódulo de Prestaciones Económicas, que automatiza la validación de derechos y el cálculo de subsidios (Enfermedad, Maternidad, Lactancia, Sepelio, Incapacidad Temporal) mediante interoperabilidad con los módulos de Núcleo Asistencial y Talento Humano del ERP.

	El modelado excluye deliberadamente los módulos que no forman parte del alcance asignado al Grupo 1-A: Núcleo Asistencial (Gestión de Citas e Historia Clínica), Cadena de Suministro, Gestión Financiera y Talento Humano. Estos módulos aparecen en el Modelo de Proceso únicamente como actores sistémicos externos (API ERP) consultados síncronamente durante el flujo de liquidación, sin que su lógica interna sea modelada en esta sección. De igual forma, la metodología ASAP y el cronograma del proyecto se tratan en secciones previas del documento; la presente sección se circunscribe exclusivamente al modelado UWE de la capa web del módulo asignado.

| Sistema modelado | ERP EsSalud La Libertad — Módulo Soporte Administrativo y Prestaciones Económicas |
| --- | --- |
| Submódulos cubiertos | SISGEDO / Mesa de Partes Digital · Prestaciones Económicas · Gestión de Usuarios |
| Casos de uso | CU-01 al CU-08 (8 casos de uso completos) |
| Actores identificados | Solicitante Externo · Auxiliar de Oficina · Técnico de Prestaciones · Administrador del Sistema · Sistema Externo (API ERP) |
| Modelos UWE | Modelo de Requisitos · Modelo de Contenido · Modelo de Navegación · Modelo de Presentación · Modelo de Proceso |
| Notación | UML 2.x conforme a UWE — estereotipos «content», «navigationClass», «presentationClass», «presentationGroup» |
| Gestor de BD | PostgreSQL 16 (schema essalud_sii) |

	

	- Modelo de Requisitos

	El Modelo de Requisitos UWE traduce los requisitos funcionales del sistema en un diagrama de casos de uso UML extendido. Su propósito es identificar actores, definir los límites del sistema y especificar las relaciones de inclusión y extensión entre funcionalidades, ofreciendo una visión integral de las capacidades del módulo.

	Para el módulo EsSalud se identifican cinco actores y ocho casos de uso principales, organizados en tres paquetes funcionales: SISGEDO/Mesa de Partes Digital (CU-01 a CU-04, CU-07), Módulo de Prestaciones Económicas (CU-05/CU-08), y Módulo de Configuración de Seguridad (CU-06).

	**Actores del Sistema**

| Solicitante (Ciudadano/Institución) | Actor externo que inicia trámites a través del portal público de la Mesa de Partes Digital. No requiere autenticación interna. |
| --- | --- |
| Auxiliar de Oficina | Personal interno encargado de la verificación, validación, modificación y derivación de expedientes dentro del flujo SISGEDO. |
| Técnico de Prestaciones Económicas | Personal especializado que ejecuta la validación de requisitos legales y el cálculo/aprobación de subsidios económicos. |
| Administrador del Sistema | Responsable de la gestión de perfiles de usuario, roles RBAC y auditoría de seguridad del ERP. |
| Sistema Externo (API ERP) | Actor sistémico que representa los módulos satélites del ERP (Núcleo Asistencial y Talento Humano) consultados de forma síncrona durante la liquidación. |

- Requisitos Funcionales

Los siguientes requisitos funcionales se derivan del análisis de la capa web del sistema bajo la metodología UWE. Complementan los RF de la Sección VII del documento (RF-01 al RF-15) con requisitos nuevos originados en el Modelo de Contenido, el Modelo de Navegación, el Modelo de Presentación y el Modelo de Proceso, que describen comportamientos de la interfaz web no contemplados en la especificación funcional base.

| ID | Nombre | Modelo UWE origen | Prioridad |
| --- | --- | --- | --- |
| RF-UWE-01 | Inicio de Sesión y Control de Acceso por Rol | Navegación | Alta |
| RF-UWE-02 | Visualización de Breadcrumb | Navegación | Media |
| RF-UWE-03 | Badge de Estado del Expediente | Presentación / Contenido | Alta |
| RF-UWE-04 | Visor PDF Embebido | Presentación | Alta |
| RF-UWE-05 | Confirmación Explícita de Acciones Críticas | Proceso | Alta |
| RF-UWE-06 | Indicador de Progreso en Llamadas API | Proceso (CU-08) | Alta |
| RF-UWE-07 | Exportación de Reporte de Trazabilidad | Presentación / Contenido | Media |
| RF-UWE-08 | Enmascaramiento de Datos Sensibles | Presentación / Contenido | Alta |
| RF-UWE-09 | Habilitación Condicional del Campo de Monto Manual | Proceso (CU-08 Flujo B) | Alta |
| RF-UWE-10 | Pantalla de Error 403 con Auditoría | Navegación | Alta |

| Identificación del requisito:  RF-UWE-01 |
| --- |
| Nombre del requisito: | Inicio de Sesión y Control de Acceso por Rol |
| Características | El sistema debe autenticar a los usuarios internos mediante credenciales institucionales y habilitar únicamente los nodos de navegación y operaciones correspondientes a su rol RBAC asignado (Auxiliar de Oficina, Técnico de Prestaciones, Administrador del Sistema). |
| Descripción del requisito | El sistema debe presentar una pantalla de inicio de sesión con campos de usuario (DNI institucional) y contraseña. Tras la autenticación exitosa, el sistema debe renderizar el menú de navegación filtrando los nodos según el rol del usuario: el Auxiliar accede a la Bandeja de Verificación y derivación; el Técnico accede a la Cola de Liquidación; el Administrador accede al Panel de Seguridad. El Solicitante externo no requiere autenticación para acceder al portal público de la Mesa de Partes Digital. Todo intento de acceso a un nodo no autorizado mediante URL directa debe ser bloqueado y registrado en la tabla AUDITORIA. |
| Requisito NF | RNF-UWE-05, RNF-01 |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RF-UWE-02 |
| --- |
| Nombre del requisito: | Visualización de Indicador de Ubicación (Breadcrumb) |
| Características | El sistema debe mostrar en todo momento la ruta de navegación activa del usuario dentro de la jerarquía de vistas del módulo, conforme al Modelo de Navegación UWE. |
| Descripción del requisito | Cada pantalla del módulo interno (Auxiliar, Técnico, Administrador) debe mostrar un componente breadcrumb en la parte superior que indique la secuencia de nodos recorridos desde el nodo raíz hasta la vista actual. Ejemplo: Dashboard > Bandeja de Verificación > Detalle Expediente. Cada elemento del breadcrumb debe ser un enlace activo que permita regresar al nodo correspondiente sin pérdida del estado de la sesión. El breadcrumb debe actualizarse dinámicamente en cada transición de nodo de navegación. |
| Requisito NF | RNF-UWE-02, RNF-UWE-01 |
| Prioridad del requisito: | Media |

| Identificación del requisito:  RF-UWE-03 |
| --- |
| Nombre del requisito: | Visualización de Badge de Estado del Expediente |
| Características | El sistema debe representar visualmente el estado actual de cada expediente mediante un componente badge con color diferenciado, en todas las pantallas donde se listen o muestren expedientes. |
| Descripción del requisito | En la Bandeja de Verificación (TablaExpedientes) y en la pantalla de Trazabilidad (CabeceraExpediente), el estado del expediente debe mostrarse como un badge con codificación de color: amarillo para Pendiente_Verificacion, verde para Registrado_Conforme, naranja para Observado, azul para En_Proceso, gris claro para Atendido, gris oscuro para Archivado y rojo para Anulado. El badge debe incluir texto legible además del color, para garantizar accesibilidad. El estado debe actualizarse en tiempo real sin recargar la página completa cuando el Auxiliar ejecute una acción de validación o derivación. |
| Requisito NF | RNF-UWE-01, RNF-UWE-06, RNF-02 |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RF-UWE-04 |
| --- |
| Nombre del requisito: | Visor de Documento PDF Embebido |
| Características | El sistema debe permitir al Auxiliar de Oficina visualizar el documento PDF adjunto al expediente directamente en la pantalla de detalle, sin necesidad de descargarlo a su equipo local. |
| Descripción del requisito | En la pantalla PanelDetalle de la Bandeja de Verificación, el sistema debe renderizar el archivo PDF del expediente en un componente visor embebido (IFrame o visor nativo del navegador) con controles de zoom, desplazamiento de páginas y descarga opcional. El visor debe cargar el documento de forma asíncrona mostrando un indicador de progreso mientras se obtiene el archivo desde el servidor. Si el archivo no está disponible o está corrupto, el sistema debe mostrar el mensaje: 'El documento no pudo cargarse. Contacte al administrador.' El documento no debe ser editable desde el visor. |
| Requisito NF | RNF-UWE-03, RNF-UWE-06, RNF-01 |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RF-UWE-05 |
| --- |
| Nombre del requisito: | Confirmación Explícita de Acciones Críticas |
| Características | El sistema debe solicitar confirmación explícita del usuario antes de ejecutar operaciones irreversibles o de alto impacto dentro del flujo de trabajo del módulo. |
| Descripción del requisito | Las siguientes acciones deben desplegar una ventana de confirmación modal antes de ejecutarse: (1) Derivar Expediente: mostrar la unidad de destino seleccionada y el proveído redactado para confirmación; (2) Anular Expediente: solicitar el motivo de anulación y mostrar advertencia de irreversibilidad; (3) Inhabilitar Cuenta de Usuario: mostrar el nombre del usuario afectado y advertir sobre la revocación inmediata de sesiones; (4) Aprobar Orden de Pago (liquidación): mostrar el monto calculado y el tipo de subsidio para confirmación final. La confirmación debe registrarse en la tabla de AUDITORIA junto con la acción ejecutada. |
| Requisito NF | RNF-UWE-01, RNF-UWE-06, RNF-05 |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RF-UWE-06 |
| --- |
| Nombre del requisito: | Indicador de Progreso en Operaciones con Llamadas API |
| Características | El sistema debe mostrar un indicador de progreso activo durante la ejecución de operaciones que involucren consultas síncronas a los módulos externos del ERP, previniendo el reenvío accidental de solicitudes. |
| Descripción del requisito | Durante el flujo de liquidación de prestaciones económicas (CU-08), al iniciarse las consultas API al Núcleo Asistencial y al módulo de Talento Humano, el sistema debe: (1) deshabilitar el botón 'Calcular' y todos los campos editables del PanelLiquidacion; (2) mostrar un spinner o barra de progreso con el texto 'Validando requisitos... Por favor espere'; (3) mostrar el resultado de cada consulta en el componente ResultadosInterop mediante StatusIndicators (OK / Error) en cuanto se reciba la respuesta de cada API. Si una API no responde dentro del tiempo de espera configurado, el sistema debe mostrar el mensaje de timeout definido en CU-08 Flujo Alterno C y restaurar el estado editable del formulario. |
| Requisito NF | RNF-UWE-03, RNF-UWE-06, RNF-06 |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RF-UWE-07 |
| --- |
| Nombre del requisito: | Exportación de Reporte de Trazabilidad |
| Características | El sistema debe permitir al usuario descargar el historial completo de movimientos de un expediente en formato descargable desde la pantalla de Trazabilidad. |
| Descripción del requisito | En la pantalla TrazabilidadExpediente, el componente AccionesReporte debe ofrecer al menos un formato de exportación: PDF. El reporte exportado debe incluir: número de correlativo, datos del solicitante, asunto del trámite, fecha de registro, estado actual y la línea de tiempo completa de movimientos (fecha, hora, unidad de origen, unidad de destino, usuario responsable y proveído). La generación del reporte debe ejecutarse en el servidor y notificarse al usuario mediante el mecanismo de indicador de progreso definido en RF-UWE-06. El archivo generado debe descargarse automáticamente con el nombre: Trazabilidad_[NroCorrelativo]_[Fecha].pdf. |
| Requisito NF | RNF-UWE-03, RNF-11, RNF-02 |
| Prioridad del requisito: | Media |

| Identificación del requisito:  RF-UWE-08 |
| --- |
| Nombre del requisito: | Enmascaramiento de Datos Sensibles en la Interfaz |
| Características | El sistema debe ocultar parcialmente los datos personales sensibles del Asegurado en la interfaz web para los roles que no requieren visualizar el dato completo, conforme a la Ley N.° 29733 y al principio de minimización de datos. |
| Descripción del requisito | En la pantalla PanelLiquidacion, el campo DNI del asegurado debe mostrarse enmascarado para el Técnico de Prestaciones: se mostrarán los primeros dos y últimos dos dígitos, ocultando los intermedios con asteriscos (ej. 45***891). El nombre completo del asegurado se mostrará íntegro únicamente para el Técnico y el Administrador; el Auxiliar verá solo las iniciales en los listados de bandeja. Ningún rol excepto el Administrador del Sistema podrá ver el campo correo_electronico del Solicitante desde la interfaz web. El enmascaramiento debe aplicarse a nivel de presentación sin alterar los datos almacenados en la base de datos. |
| Requisito NF | RNF-UWE-05, RNF-01, RNF-09 |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RF-UWE-09 |
| --- |
| Nombre del requisito: | Habilitación Condicional del Campo de Modificación Manual de Monto |
| Características | El sistema debe habilitar el campo de modificación manual del monto de subsidio únicamente bajo condiciones excepcionales debidamente justificadas, con controles adicionales de auditoría. |
| Descripción del requisito | En el PanelLiquidacion, el botón 'Modificación Manual de Monto' debe estar deshabilitado por defecto. Solo debe habilitarse cuando el Técnico de Prestaciones seleccione explícitamente la opción de excepción y el sistema registre la solicitud en la tabla de AUDITORIA con estado 'PENDING_APPROVAL'. Al habilitarse, el sistema debe mostrar obligatoriamente el campo TextareaSustentoLegal con un mínimo de 100 caracteres requeridos. El monto modificado manualmente debe quedar diferenciado visualmente del monto calculado automáticamente (ej. con ícono de advertencia) en la pantalla de confirmación y en el reporte de trazabilidad. Esta funcionalidad corresponde al Flujo Alterno B del Modelo de Proceso CU-08. |
| Requisito NF | RNF-UWE-05, RNF-UWE-06, RNF-05, RNF-11 |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RF-UWE-10 |
| --- |
| Nombre del requisito: | Pantalla de Error 403 con Registro de Auditoría |
| Características | El sistema debe mostrar una pantalla de error específica y registrar en auditoría todo intento de acceso a nodos de navegación para los cuales el usuario autenticado no tiene permisos, conforme al Modelo de Navegación UWE. |
| Descripción del requisito | Cuando un usuario autenticado intente acceder directamente mediante URL a un nodo de navegación fuera de su vista autorizada (ej. un Auxiliar intenta acceder al Panel de Liquidación), el sistema debe: (1) interceptar la solicitud antes de renderizar la pantalla; (2) mostrar una pantalla de error 403 con el mensaje 'Acceso denegado: no tiene permisos para acceder a este módulo' y un botón de regreso al Dashboard del usuario; (3) insertar un registro en la tabla AUDITORIA con tipo_evento = 'ERROR_ACCESO', incluyendo la URL solicitada, el ID del usuario, la dirección IP y el timestamp. Esta pantalla no debe revelar información sobre la existencia o contenido del recurso solicitado. |
| Requisito NF | RNF-UWE-05, RNF-01, RNF-09 |
| Prioridad del requisito: | Alta |

- Requisitos No Funcionales

Los siguientes requisitos no funcionales se derivan del análisis de la capa web del sistema bajo la metodología UWE. Complementan los RNFs generales del módulo con requisitos específicos de la interfaz web, la navegación, la usabilidad y la compatibilidad, que son inherentes al enfoque de ingeniería web orientada a modelos.

| ID | Nombre | ISO 25010 | Subcaracterística |
| --- | --- | --- | --- |
| RNF-UWE-01 | Usabilidad de la Interfaz Web | Usabilidad | Capacidad de aprendizaje / Operabilidad |
| RNF-UWE-02 | Consistencia Visual de la Navegación | Usabilidad | Estética / Inteligibilidad |
| RNF-UWE-03 | Tiempo de Carga de Páginas Web | Eficiencia de desempeño | Comportamiento temporal |
| RNF-UWE-04 | Compatibilidad con Navegadores | Compatibilidad | Coexistencia / Interoperabilidad |
| RNF-UWE-05 | Navegabilidad Orientada al Rol (RBAC Web) | Seguridad | Confidencialidad / Control de acceso |
| RNF-UWE-06 | Retroalimentación del Estado del Proceso | Usabilidad | Operabilidad / Protección contra errores |
| RNF-UWE-07 | Integridad de la Sesión Web | Fiabilidad | Madurez / Disponibilidad |
| RNF-UWE-08 | Accesibilidad Web del Portal Público | Usabilidad | Accesibilidad |

	

| Identificación del requisito:  RNF-UWE-01 |
| --- |
| Nombre del requisito: | Usabilidad de la Interfaz Web |
| Características | La interfaz debe seguir la guía de estilos institucional de EsSalud y proporcionar retroalimentación visual inmediata ante cada acción del usuario (validaciones, estados de carga, confirmaciones). |
| Características ISO 25010 | Usabilidad |
| Subcaracterísticas | Capacidad de aprendizaje / Operabilidad |
| Descripción del requisito | El portal de la Mesa de Partes Digital y el módulo interno deben permitir que un usuario sin capacitación previa complete el registro de un expediente en un máximo de 5 minutos. Los mensajes de error deben ser descriptivos, indicar el campo afectado y sugerir la corrección. Los botones de acción crítica (Derivar, Aprobar Liquidación) deben requerir confirmación explícita antes de ejecutarse. |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RNF-UWE-02 |
| --- |
| Nombre del requisito: | Consistencia Visual de la Navegación |
| Características | La estructura de navegación debe ser predecible y consistente en todas las vistas del sistema, independientemente del rol del usuario autenticado. |
| Características ISO 25010 | Usabilidad |
| Subcaracterísticas | Estética de la interfaz / Inteligibilidad |
| Descripción del requisito | Cada pantalla del sistema debe mostrar: (1) un encabezado con el logo institucional de EsSalud y el nombre del módulo activo; (2) un menú lateral o superior con los nodos de navegación habilitados según el rol RBAC del usuario; (3) un indicador de ubicación (breadcrumb) que refleje la posición actual del usuario en la jerarquía de navegación definida en el Modelo de Navegación UWE. La navegación hacia atrás debe ser siempre posible sin pérdida de datos. |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RNF-UWE-03 |
| --- |
| Nombre del requisito: | Tiempo de Carga de Páginas Web |
| Características | Las páginas del sistema deben cargarse dentro de los umbrales de rendimiento percibido establecidos para aplicaciones web institucionales de alta concurrencia. |
| Características ISO 25010 | Eficiencia de desempeño |
| Subcaracterísticas | Comportamiento temporal / Utilización de recursos |
| Descripción del requisito | El tiempo de carga inicial (First Contentful Paint) de cualquier pantalla del sistema no debe superar 2 segundos bajo condiciones de red institucional estándar (LAN 100 Mbps). Las operaciones de búsqueda y filtrado en la Bandeja de Verificación deben retornar resultados en menos de 3 segundos con hasta 500 expedientes activos. La pantalla del Panel de Liquidación, que ejecuta consultas API síncronas al Núcleo Asistencial y Talento Humano, debe mostrar un indicador de progreso activo durante la espera para evitar la percepción de congelamiento. |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RNF-UWE-04 |
| --- |
| Nombre del requisito: | Compatibilidad con Navegadores Web |
| Características | El sistema debe ser funcional y visualmente consistente en los navegadores web utilizados por el personal administrativo y el público de EsSalud — Red La Libertad. |
| Características ISO 25010 | Compatibilidad |
| Subcaracterísticas | Coexistencia / Interoperabilidad |
| Descripción del requisito | La interfaz web del sistema debe ser compatible y completamente funcional en las dos últimas versiones estables de: Google Chrome, Mozilla Firefox y Microsoft Edge. El portal público de la Mesa de Partes Digital (acceso del Solicitante externo) debe además ser accesible desde dispositivos móviles con navegadores equivalentes, garantizando un diseño responsivo que preserve la funcionalidad de carga de archivos PDF en pantallas de al menos 360px de ancho. |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RNF-UWE-05 |
| --- |
| Nombre del requisito: | Navegabilidad Orientada al Rol (RBAC Web) |
| Características | La estructura de navegación expuesta en la interfaz debe reflejar estrictamente los permisos RBAC asignados al usuario autenticado, sin exponer nodos ni funcionalidades a los que no tiene acceso. |
| Características ISO 25010 | Seguridad |
| Subcaracterísticas | Confidencialidad / Control de acceso |
| Descripción del requisito | El menú de navegación y los botones de acción deben renderizarse condicionalmente según el rol del usuario en sesión: el Solicitante externo no debe ver opciones de derivación ni liquidación; el Auxiliar de Oficina no debe ver el Panel de Liquidación; el Técnico de Prestaciones no debe ver la gestión de usuarios. Cualquier intento de acceso directo por URL a un nodo no autorizado debe redirigir a una pantalla de error 403 y registrar el intento en la tabla de AUDITORIA. Este requisito complementa el RNF-09 de la Sección VII. |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RNF-UWE-06 |
| --- |
| Nombre del requisito: | Retroalimentación del Estado del Proceso Web |
| Características | La interfaz debe comunicar de forma visual y en tiempo real el estado de cada operación del proceso de negocio, evitando que el usuario quede sin respuesta durante operaciones de larga duración. |
| Características ISO 25010 | Usabilidad |
| Subcaracterísticas | Operabilidad / Protección contra errores del usuario |
| Descripción del requisito | Durante la ejecución de operaciones que involucren llamadas a servicios externos (validación API en CU-08), carga de archivos (CU-01) o generación de reportes (CU-04), el sistema debe mostrar un indicador de carga activo (spinner o barra de progreso) que impida el reenvío accidental del formulario. Al completarse cualquier operación crítica (registro de expediente, derivación, aprobación de liquidación), el sistema debe mostrar una notificación de confirmación con el identificador del registro afectado (número de correlativo, ID de prestación) visible por al menos 5 segundos. |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RNF-UWE-07 |
| --- |
| Nombre del requisito: | Integridad de la Sesión Web |
| Características | La sesión del usuario autenticado debe mantenerse activa durante el tiempo necesario para completar los flujos de trabajo del módulo, y expirar de forma segura ante inactividad prolongada. |
| Características ISO 25010 | Fiabilidad |
| Subcaracterísticas | Madurez / Disponibilidad |
| Descripción del requisito | La sesión web de usuarios internos (Auxiliar, Técnico, Administrador) debe tener un tiempo de inactividad máximo de 30 minutos antes de expirar automáticamente. Al expirar, el sistema debe redirigir al usuario a la pantalla de inicio de sesión sin pérdida del expediente que estaba visualizando (guardado de estado de navegación). El sistema no debe permitir múltiples sesiones activas simultáneas con las mismas credenciales. Toda expiración de sesión debe registrarse como evento LOGOUT en la tabla de AUDITORIA conforme al RNF-12 de la Sección VII. |
| Prioridad del requisito: | Alta |

| Identificación del requisito:  RNF-UWE-08 |
| --- |
| Nombre del requisito: | Accesibilidad Web del Portal Público |
| Características | El portal público de la Mesa de Partes Digital debe cumplir con estándares mínimos de accesibilidad web para garantizar su uso por ciudadanos con diversidad funcional. |
| Características ISO 25010 | Usabilidad |
| Subcaracterísticas | Accesibilidad |
| Descripción del requisito | El portal público (Vista Solicitante Externo) debe cumplir al menos el nivel AA de las Pautas de Accesibilidad para el Contenido Web (WCAG 2.1), incluyendo: (1) contraste de color mínimo 4.5:1 entre texto y fondo; (2) todos los campos del FormularioRegistro deben tener etiquetas semánticas asociadas (label HTML) para compatibilidad con lectores de pantalla; (3) el componente de carga de archivos PDF debe incluir instrucciones textuales sobre el formato y tamaño máximo aceptado; (4) los mensajes de error de validación deben ser anunciados por tecnologías asistivas mediante roles ARIA. Este requisito es exigible únicamente para el portal público; las interfaces internas del ERP quedan fuera de este alcance. |
| Prioridad del requisito: | Media |

- Modelado UWE (UML-based Web Engineering)

- Modelo de Requisitos (Diagrama de Casos de Uso)

- CU-01: Registrar Expediente en MPD			

- CU-02: Verificar y Validar Expediente

- CU-03: Derivar Expediente

- CU-04: Consultar Estado de Trámite

- CU-05: Calcular Subsidio Económico

- CU-06: Gestionar Perfiles de Usuario

- CU-07: Modificar Datos de Expediente

- CU-08: Liquidar Prestación Económica

- Modelo de Contenido (Content Model-Content Diagram)

- Modelo de Navegación (Navigation Model)

El Modelo de Navegación UWE define la estructura de navegación del sistema desde la perspectiva de cada tipo de usuario. Se compone de nodos de navegación («navigationClass») que representan páginas o vistas del sistema, y de enlaces de navegación («navigationLink») que conectan dichos nodos según el flujo de interacción previsto.

Para el módulo EsSalud se diseñan cuatro vistas de navegación independientes, una por cada actor principal del sistema. Esto refleja el principio de mínimo privilegio: cada actor solo puede navegar hacia los nodos a los que tiene acceso autorizado según su rol RBAC.

- Vista: Solicitante Externo

- Vista: Auxiliar de Oficina

		

- Vista: Técnico Prestaciones Económicas

- Vista: Administrador del Sistema

- Modelo de Presentación (Presentation Model)

El Modelo de Presentación UWE especifica la estructura visual e interactiva de las interfaces del sistema. Utiliza los estereotipos «presentationClass» para representar páginas completas, y «presentationGroup» para los componentes o secciones que las componen (formularios, tablas, paneles, indicadores de estado). Las relaciones de composición (*--) modelan la jerarquía de componentes dentro de cada pantalla.

El modelo no es un wireframe detallado sino una especificación estructural que guía el desarrollo de la interfaz. Define qué elementos deben estar presentes en cada pantalla, sus tipos (InputField, Button, Dropdown, Table, StatusIndicator) y sus restricciones de comportamiento (obligatorio, condicional, enmascarado).

- PD1_RegistrarExpediente

				Descripción:

La clase raíz RegistrarExpedienteMPD agrupa dos componentes principales: el grupo FormularioTramite, que contiene los campos de captura de datos del solicitante (tipo y número de documento mediante selector, nombre o razón social, correo electrónico, asunto del trámite, folios adjuntos y archivo adjunto en formato PDF mediante control de carga ⇧, y unidad orgánica destino mediante selector); y el grupo Acciones, que expone los botones de interacción primaria :EnviarSolicitud y :Cancelar. El grupo Mensajes actúa como contenedor de notificaciones del sistema durante el ciclo de vida del formulario.

El diagrama define además tres estados alternativos de presentación que se activan condicionalmente según el resultado del procesamiento: ErrorValidacion, que muestra el mensaje de error descriptivo, un enlace para volver al formulario y una sección de ayuda contextual; ArchivoInvalido, que informa al usuario sobre el incumplimiento del formato PDF o el peso máximo y ofrece instrucciones de corrección; y Confirmacion, que presenta el número de correlativo asignado, el mensaje de éxito, y las opciones para descargar el cargo de recepción o iniciar un nuevo trámite. La nota al pie especifica que la validación es síncrona y que el cargo de recepción incluye el correlativo, la fecha/hora y la confirmación de envío al correo del solicitante.

- PD2_VerificarDerivar

Descripción

El Presentation Diagram 2 modela la estructura de presentación integrada de los flujos CU-02 (Verificar y Validar Expediente) y CU-03 (Derivar Expediente), los cuales comparten la misma vista de trabajo del Auxiliar de Oficina. La clase raíz ListaExpedientesPendientes organiza tres grupos funcionales: el grupo :FiltrosBusqueda con su selector para filtrar expedientes por criterios como estado o fecha; la colección iterable Expedientes [*], que representa la tabla de resultados con los atributos :NroCorrelativo, :AsuntoTramite, :FechaIngreso, :Estado y el botón de acción :VerDetalle por cada fila; y el grupo AccionesExpediente, que concentra las operaciones disponibles sobre el expediente seleccionado: :ValidarAceptar, :ObservarAnular, :Derivar y :VerHojaRuta. El componente :Mensajes gestiona las notificaciones del sistema en respuesta a cada acción ejecutada.

Cuando el Auxiliar selecciona la acción :Derivar, el diagrama activa el estado de presentación FormularioDerivacion, que contiene el selector para elegir la unidad orgánica destino del catálogo de la Red La Libertad, los campos de texto [ab] para el proveído y las indicaciones técnicas, y los botones :ConfirmarDerivacion y :Cancelar. La nota al pie precisa que la acción ValidarAceptar actualiza el estado del expediente a Registrado/Conforme, y que ObservarAnular desencadena el envío automático de correo al solicitante para su subsanación.

- PD3_ConsultarTramite

				Descripción

El Presentation Diagram 3 modela la estructura de presentación del flujo CU-04: Consultar Estado de Trámite, accesible tanto por el Solicitante externo desde el portal público como por el Auxiliar de Oficina y el Administrador desde el módulo interno. La clase raíz ConsultarEstadoTramite presenta un diseño de búsqueda directa compuesto por el campo de texto [ab] para ingresar el número de expediente y el botón de acción :BuscarExpediente. El grupo ResultadoConsulta organiza la información recuperada en dos niveles: los campos :DatosExpediente y :EstadoActual para la cabecera del trámite, y la colección iterable HistorialMovimientos [*] que despliega la línea de tiempo completa de derivaciones con los atributos :Fecha, :OficinaOrigen, :OficinaDestino, :Usuario y :EstadoPaso por cada movimiento registrado. El componente :Mensajes gestiona las notificaciones contextuales de la vista.

El diagrama define dos estados alternativos: ExpedienteNoEncontrado, que muestra un mensaje de error y un enlace para volver a la búsqueda cuando el correlativo ingresado no existe en la base de datos; y Confirmacion, que presenta un resumen estadístico con :TotalMovimientos y :UltimaActualizacion al completarse la consulta exitosamente. La nota al pie establece que esta pantalla es de solo lectura, sin posibilidad de modificar ningún dato del expediente desde esta vista, conforme al diseño de trazabilidad auditable del sistema.

- Modelo de Proceso (Process Model)

El Modelo de Proceso UWE representa la lógica de negocio de los flujos más complejos del sistema mediante diagramas de actividad UML con swimlanes (carriles). Cada carril corresponde a un actor o componente del sistema que participa en el proceso. Este modelo complementa el Modelo de Navegación al describir no solo hacia dónde navega el usuario sino qué acciones del sistema se desencadenan en cada paso.

- Proceso CU-01: Registrar Expediente en MPD

Descripción del Flujo

El proceso se desarrolla entre tres actores: el Solicitante externo, el Sistema SISGEDO y la Base de Datos. El flujo principal incluye validación síncrona del formulario, generación paralela del correlativo y apertura de hoja de ruta mediante transacción ACID, y registro automático en la tabla de auditoría. El flujo alterno gestiona el ciclo de corrección cuando la validación falla.	

| Actor principal | Solicitante Externo (Ciudadano/Institución) |
| --- | --- |
| Actores del sistema | Sistema SISGEDO · Base de Datos PostgreSQL |
| Precondición | Solicitante con acceso a internet y documento digitalizado en PDF |
| Postcondición | Expediente persistido en estado 'Pendiente_Verificacion'. Correlativo y hoja de ruta generados. Cargo de recepción enviado por correo. |
| Flujo alterno | Validación fallida: ciclo de corrección hasta cumplir todas las restricciones de formato y obligatoriedad |
| Puntos de control ACID | Generación de correlativo y apertura de hoja de ruta se ejecutan en fork paralelo dentro de una única transacción, garantizando atomicidad |

- Proceso CU-08: Liquidar Prestación Económica

Descripción del Flujo

El proceso de liquidación es el más complejo del módulo por involucrar interoperabilidad síncrona con dos módulos externos del ERP (Núcleo Asistencial y Talento Humano) mediante APIs RESTful, además de tres flujos alternos distintos: timeout de conexión, rechazo por incumplimiento de requisitos legales, y modificación manual excepcional por mandato judicial.

| Actor principal | Técnico de Prestaciones Económicas |
| --- | --- |
| Actores del sistema | Sistema ERP Módulo Núcleo Asistencial Módulo Talento Humano Base de Datos |
| Precondición | Expediente verificado en estado 'Conforme'. APIs de módulos satélites operativas. |
| Postcondición (éxito) | Prestación persistida con estado 'Pendiente_Desembolso'. Expediente actualizado a 'Liquidado'. Orden remitida a Tesorería. Trazabilidad ACID inmutable en Auditoría. |
| Flujo alterno A | Timeout API: proceso interrumpido sin modificación de BD. Expediente permanece intacto en cola. |
| Flujo alterno B | Incumplimiento legal (CITT no vigente o aportes insuficientes): resolución denegatoria con estado 'Rechazado'. |
| Flujo alterno C | Modificación manual excepcional: habilitado solo con autorización jerárquica. Requiere sustento legal. Incrementa rigor de bitácora para auditoría posterior. |
| Transacción ACID | La aprobación ejecuta fork paralelo: INSERT Prestacion + UPDATE Expediente + INSERT Auditoría — todo en una sola transacción. COMMIT solo si los tres pasos son exitosos. |

- Modelo de Diagrama de Clases

	

	 Enlace del diagrama: [Diagrama de Clases](https://drive.google.com/file/d/1C89ry4fYYD51wzwyn730KGIk-N3RcPfv/view?usp=sharing)

	##### IMPLEMENTACIÓN DE LA IA EN EL PRODUCTO DE SOFTWARE

	- Implementación de IA en el futuro producto software (Norma ISO/IEC 25059)

	La norma ISO/IEC 25059 extiende el modelo de calidad de la ISO 25010 específicamente para sistemas que incorporan Inteligencia Artificial. En el contexto del sub-módulo SISGEDO, no se busca una IA genérica, sino características de IA Agéntica que aporten control de calidad, automatización de tareas y optimización de flujos.

	Se mapean los atributos de calidad clave de la norma aplicados a la arquitectura:

	- Adaptabilidad del Modelo (Adaptability): Capacidad del agente supervisor (por ejemplo, implementado en plataformas como N8N) para ajustar dinámicamente las rutas de los flujos documentales basándose en el análisis del lenguaje natural de los proveídos de instrucciones recibidos.

	- Explicabilidad (Explainability): El sistema debe registrar en la tabla auditoria o en los metadatos de la tabla documento la justificación lógica de por qué la IA clasificó un archivo bajo cierto tipo_doc (ej. por qué determinó que era un MEMO o un INFORME) o por qué automatizó una derivación específica.

	- Robustez / Capacidad de Manejo de Fallos (Robustness): Ante la recepción de un documento con firmas digitales corruptas o hashes inválidos (hash_firma), el agente inteligente no debe detener el flujo del sistema, sino derivarlo automáticamente a un carril de contingencia en Mesa de Partes.

	- Calidad de Datos en el Sub-módulo (Norma ISO/IEC 25012)

	Para que la automatización a gran escala sea efectiva, la integración requiere una "única fuente de información veraz". Aplicando la norma ISO/IEC 25012 (Modelo de calidad de datos), estructuramos las reglas específicas para tus entidades principales:

	Tabla de Reglas de Calidad de Datos (ISO 25012)

| Entidad / Tabla | Características Inherentes (ISO 25012) | Regla de Negocio / Restricción en EsSalud |
| --- | --- | --- |
| solicitante | Exactitud y Completitud | El nro_doc (DNI/CE) debe ser validado sintácticamente de forma obligatoria (NOT NULL) para evitar el registro de solicitantes huérfanos o duplicados. |
| expediente | Consistencia y Actualización | El campo numero_correlativo debe seguir un formato estandarizado e inmutable (CORR-2026-XXXX). Los estados intermedios del ciclo de vida del trámite deben sincronizarse en tiempo real con la tabla maestra para evitar colisiones en los reportes analíticos. |
| documento | Precisión e Integridad Referencial | Cada registro debe poseer obligatoriamente una llave foránea válida (id_expediente). El campo hash_firma no puede ser nulo si el documento se marca en el estado correspondiente a firmado, asegurando la inmutabilidad y el cumplimiento normativo. |

	

	- BPMN del desarrollo de cada Módulo Asignado

	

	

	

		Descripción del Modelo:

	El proceso comienza en el carril del Analista de Sistemas cuando se recibe la Solicitud formal de automatización SISGEDO. Como primer paso operativo, el analista procede a Modelar el proceso de negocio mediante un diagrama BPMN descriptivo para entender el flujo actual de los trámites. Una vez mapeado, se ejecuta la actividad de Levantar requisitos usando el estándar IEEE 830 con el fin de formalizar las especificaciones funcionales y no funcionales del sistema.

	En este punto, el flujo llega a una primera compuerta de decisión para evaluar si el trámite analizado ¿Requiere reingeniería (BPR)?. Si la respuesta es SÍ, el flujo se desvía de forma alterna hacia la tarea Rediseñar proceso bajo BPR para optimizar la lógica administrativa, regresando inmediatamente después a la fase de modelado descriptivo. Si la respuesta es NO, el flujo avanza en línea recta hacia una segunda compuerta que evalúa si la ¿Arquitectura funcional fue aprobada por EsSalud?. En caso de recibir una respuesta negativa (NO), se activa la tarea Ajustar requisitos para corregir las observaciones y se vuelve a pasar por el levantamiento de requisitos. Si la respuesta es afirmativa (SÍ), el diseño funcional queda validado y el proceso se transfiere al carril del Arquitecto de Software.

	El arquitecto de software inicia su participación con la actividad de Diseñar el esquema relacional del ERP, estructurando la base de datos centralizada. Inmediatamente después, el flujo encuentra una compuerta paralela que divide el trabajo técnico en dos frentes simultáneos: por un lado, se ejecuta la tarea de Desarrollar componentes lógicos y APIs para construir el backend, y por el otro, se procede a Configurar el Agente Supervisor IA en n8n para la orquestación inteligente de los documentos. Ambos frentes se unifican en una compuerta de sincronización paralela una vez terminados, permitiendo avanzar hacia la tarea de Ejecutar scripts de migración e insertar datos de prueba en el sistema.

	Una vez inyectados los datos, el control del proceso se traslada al carril de QA y Automatización, donde se inicia la fase de validación mediante la tarea de Auditar calidad de datos. Posteriormente, una compuerta exclusiva evalúa si el sistema ¿Pasa el control de calidad?. Si se detectan fallos o la respuesta es NO, el flujo se redirige a la actividad Depurar inconsistencias SQL para corregir restricciones de clave foránea o valores nulos, obligando a repetir la auditoría de calidad. Si la respuesta es SÍ, el flujo avanza con seguridad hacia la fase de despliegue, ejecutando la tarea Publicar sub-módulo y conectar Dashboard para habilitar la aplicación en producción y enlazar los indicadores analíticos en tiempo real. Finalmente, el proceso concluye de forma exitosa al alcanzar el evento terminal de Sub-módulo integrado.

	Repositorio: [https://github.com/EsSaludSII-Medisys/erp-essalud-sii](https://github.com/EsSaludSII-Medisys/erp-essalud-sii)

	##### REFERENCIAS BIBLIOGRÁFICAS

EsSalud (2024). Interoperabilidad de sistemas de información en salud (reporte técnico institucional).

EsSalud (2025). Reporte institucional de consultas externas y gestión de citas médicas.

Organización para la Cooperación y el Desarrollo Económicos (2025). OECD Reviews of Health Systems: Peru 2025.

Congreso de la República del Perú. (2011). Ley N.° 29733, Ley de Protección de Datos Personales. Diario Oficial El Peruano. Recuperado de https://www.gob.pe/institucion/congreso-de-la-republica/normas-legales/243470-29733

El Peruano. (2024, 30 de noviembre). Decreto Supremo N.° 016-2024-JUS que aprueba el Reglamento de la Ley N.° 29733, Ley de Protección de Datos Personales. Diario Oficial El Peruano. Recuperado de https://www.gob.pe/institucion/smv/normas-legales/6426760-016-2024-jus

Ministerio de Justicia y Derechos Humanos – Autoridad Nacional de Protección de Datos Personales. (2025). Normativa de protección de datos personales (compendio normativo). Recuperado de https://www.gob.pe/institucion/anpd/colecciones/3482-normativa-de-proteccion-de-datos-personales

Garrigues. (2025, 14 de enero). Perú: Se publica el nuevo Reglamento de la Ley de Protección de Datos Personales. Recuperado de https://www.garrigues.com/es_ES/noticia/peru-publica-nuevo-reglamento-ley-proteccion-datos-personales

Kom Agencia Digital. (2026, 17 de abril). Nuevo Reglamento de Protección de Datos (D.S. 016-2024-JUS): Lo esencial para emprendedores. Recuperado de https://kom.pe/reglamento-ds-016-2024-jus-datos-personales

Quama. (2026, 7 de abril). Guía para implementación de la Certificación ISO 27001: requisitos, auditorías y pasos prácticos. Recuperado de https://quama.pe/blog/guia-para-obtener-la-certificacion-iso-27001-requisitos-auditorias-y-pasos-practicos

Seguridad Cero. (s. f.). Cláusula 4: Contexto de la organización – ISO 27001. Recuperado en 2026 de https://academy.seguridadcero.com.pe/blog/clausula-4-contexto-de-la-organizacion-iso-27001

Umayuq. (s. f.). ISO 27001: Qué es, beneficios y cómo obtener certificación. Recuperado en 2026 de https://umayuq.pe/blog/iso-27001

ISOTools. (s. f.). ISO 27001: Requisitos de seguridad y cumplimiento. Recuperado en 2026 de https://pe.isotools.us/iso-27001-requisitos-seguridad

Ubimia Compliance. (2026, 28 de enero). ISO 27001: Cómo conseguirla y beneficios para empresas. Guía definitiva para proteger tu información. Recuperado de https://compliance.ubimia.com/iso-27001-como-conseguirla-y-beneficios-para-empresas-guia-definitiva-para-proteger-tu-informacion