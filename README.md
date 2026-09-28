# Optimización de Bases de Datos OLTP

En un entorno de banca digital, la gestión de transacciones en tiempo real es crítica. Tu tarea es diseñar y optimizar una base de datos OLTP para manejar transacciones financieras con alta consistencia y disponibilidad. Debes considerar la configuración del sistema, el diseño del esquema, la indexación adecuada, la gestión de transacciones y el monitoreo del rendimiento. Los actores involucrados incluyen el sistema de procesamiento de transacciones, el motor de reglas de negocio y el sistema de auditoría. La base de datos debe soportar un throughput de 5 000 transacciones por segundo con una latencia máxima de 50ms.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | implementacion-bases-de-datos-oltp |
| **Nivel** | senior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 20 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Configuración Inicial

**Objetivo:** Establecer la configuración básica de la base de datos para soportar transacciones financieras.

**Tiempo estimado:** 5 horas

**Instrucciones:**

- Identifica las métricas clave de rendimiento para la base de datos (throughput, latencia, disponibilidad).
- Establece la configuración inicial de la base de datos para asegurar un throughput de 5 000 transacciones por segundo con una latencia máxima de 50ms.

**Entregable:** Configuración inicial de la base de datos documentada.

<details>
<summary>Pistas de conocimiento</summary>

- Considera las implicaciones de la configuración en el rendimiento y la escalabilidad.
- Evalúa diferentes configuraciones para identificar la que mejor se ajusta a los requisitos de rendimiento.

</details>

### Fase 2: Diseño del Esquema

**Objetivo:** Diseñar un esquema de base de datos que soporte las transacciones financieras con alta consistencia y disponibilidad.

**Tiempo estimado:** 5 horas

**Instrucciones:**

- Identifica las tablas y relaciones necesarias para soportar las transacciones financieras.
- Diseña el esquema de la base de datos para asegurar la consistencia y la disponibilidad de los datos.

**Entregable:** Esquema de base de datos diseñado y documentado.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la normalización y la desnormalización en tu diseño.
- Evalúa diferentes estrategias de indexación para mejorar el rendimiento.

</details>

### Fase 3: Gestión de Transacciones

**Objetivo:** Implementar la gestión de transacciones para asegurar la integridad de los datos y la consistencia.

**Tiempo estimado:** 5 horas

**Instrucciones:**

- Diseña las transacciones necesarias para soportar las operaciones financieras.
- Implementa mecanismos de control de concurrencia para asegurar la integridad de los datos.

**Entregable:** Gestión de transacciones implementada y documentada.

<details>
<summary>Pistas de conocimiento</summary>

- Considera los diferentes niveles de aislamiento de transacciones.
- Evalúa diferentes estrategias de control de concurrencia para identificar la que mejor se ajusta a los requisitos de integridad y consistencia.

</details>

### Fase 4: Monitoreo de Rendimiento

**Objetivo:** Implementar un sistema de monitoreo para evaluar el rendimiento de la base de datos y identificar áreas de mejora.

**Tiempo estimado:** 5 horas

**Instrucciones:**

- Identifica las métricas clave de rendimiento para monitorear la base de datos.
- Implementa un sistema de monitoreo para evaluar el rendimiento y identificar áreas de mejora.

**Entregable:** Sistema de monitoreo implementado y documentado.

<details>
<summary>Pistas de conocimiento</summary>

- Considera la frecuencia de monitoreo y las herramientas disponibles para la evaluación del rendimiento.
- Evalúa diferentes estrategias de monitoreo para identificar la que mejor se ajusta a los requisitos de rendimiento y escalabilidad.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una base de datos OLTP y cuáles son sus características principales?
- **paraQueSirve**: ¿Para qué sirve la gestión de transacciones en una base de datos OLTP?
- **comoSeUsa**: ¿Cómo se usa el monitoreo de rendimiento para optimizar una base de datos OLTP?
- **queDecisionesImplica**: ¿Qué decisiones implica el diseño del esquema de una base de datos OLTP?

## Criterios de Evaluacion

- Configuración inicial de la base de datos documentada.
- Esquema de base de datos diseñado y documentado.
- Gestión de transacciones implementada y documentada.
- Sistema de monitoreo implementado y documentado.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
pip install -r requirements.txt && pytest -q
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
