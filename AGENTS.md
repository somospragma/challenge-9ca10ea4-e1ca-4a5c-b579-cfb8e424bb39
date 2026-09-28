# AGENTS.md

Instrucciones para el agente de IA que abra este repositorio (Claude Code, Cursor, Codex, Copilot, Gemini). Se cargan solas: no hay que pegar nada en ningun chat.

## Que es este repositorio

Es el codigo base de un reto de aprendizaje de Pragma: **Optimización de Bases de Datos OLTP**.

| | |
|---|---|
| Tema | implementacion-bases-de-datos-oltp |
| Nivel | senior-l2 |
| Chapter | Ciencia de Datos — Ingeniero de Datos |
| Especialidad | Ingeniero de datos |
| Stack | Python 3.13 / Apache Airflow 2.10 |
| Patron arquitectonico | ETL con orquestación, particionado y calidad de datos |
| Tiempo estimado | 20 horas |

## Receta del stack

Esqueleto obligatorio:

- `pyproject.toml o requirements.txt en la raiz`
- `dags/ con el DAG de Airflow o el orquestador equivalente`
- `src/extract con los lectores de origen`
- `src/transform con las transformaciones y las reglas de calidad`
- `src/load con los escritores de destino`
- `tests/ con casos de validacion de resultados esperados`
- `conf/ con la configuracion por ambiente`

Dependencias:

- apache-airflow 2.10.0
- psycopg2-binary 2.9.9
- pandas 2.2.1
- pytest 8.1.1
- prometheus-client 0.20.0
- python-dotenv 1.0.1
- SQLAlchemy 2.0.29

## Tu tarea

Dejar este proyecto en estado **verificable**: que el comando de verificacion corra sin errores. Escribi los archivos en disco, en este repositorio. No generes ZIPs ni archivos adjuntos.

En orden:

1. Corre `pip install -r requirements.txt && pytest -q` y mira que falla.
2. Completa lo que falte de la lista de abajo: manifiesto de dependencias, punto de entrada, capa de interfaz y las capas del patron declarado.
3. Arregla SOLO los errores que impiden compilar o arrancar.
4. Volve a correr `pip install -r requirements.txt && pytest -q` hasta que pase.
5. Pará ahí.

## Regla dura: las fases son trabajo del humano

**PROHIBIDO implementar los entregables de las fases.** El valor del reto esta en que la persona los resuelva. Tu trabajo es que tenga un proyecto que arranca; el hueco pedagogico se queda como esta.

No resuelvas nada de esto:

- **Fase 1 — Configuración Inicial**: Configuración inicial de la base de datos documentada.
- **Fase 2 — Diseño del Esquema**: Esquema de base de datos diseñado y documentado.
- **Fase 3 — Gestión de Transacciones**: Gestión de transacciones implementada y documentada.
- **Fase 4 — Monitoreo de Rendimiento**: Sistema de monitoreo implementado y documentado.

Distincion operativa:

- **Arreglar** (si): import faltante, tipo que no existe, dependencia sin declarar, error de sintaxis, archivo referenciado que no existe.
- **No tocar** (no): logica de negocio incompleta, validaciones ausentes, secretos hardcodeados, APIs deprecadas que funcionan, concurrencia insegura, patrones mejorables. Eso es lo que la persona tiene que encontrar.

## Lo que falta y tenes que completar

### 1. Archivos que la arquitectura declara (6 de 11)

La propuesta arquitectonica del reto los lista y no llegaron al repo. Crealos con implementacion real, respetando la capa en la que viven:

- [ ] `dags/oltp_etl_pipeline.py`
- [ ] `src/extract/transaction_reader.py`
- [ ] `src/transform/transaction_processor.py`
- [ ] `sql/schema.sql`
- [ ] `sql/transactions.sql`
- [ ] `tests/test_transaction_processor.py`

### 2. Referencias colgando (2)

Salieron de un analisis estatico del codigo que SI esta en el repo. Cada una rompe la compilacion:

- [ ] `requirements.txt` — `airflow-prometheus-exporter@0.2.0`
      airflow-prometheus-exporter declara la version 0.2.0, pero PyPI respondio que esa version no existe. Es una version inventada: reemplazala por una version publicada real, o si no se conoce con certeza, usa el mecanismo centralizado del ecosistema (BOM/parent/platform/version catalog) y no declares una version individual.
- [ ] `requirements.txt` — `decouple@1.7`
      decouple declara la version 1.7, pero PyPI respondio que esa version no existe. Es una version inventada: reemplazala por una version publicada real, o si no se conoce con certeza, usa el mecanismo centralizado del ecosistema (BOM/parent/platform/version catalog) y no declares una version individual.

### Presentes (5)

- `requirements.txt`
- `src/load/transaction_writer.py`
- `src/monitoring/performance_tracker.py`
- `conf/config.json`
- `README.md`

### Capas del patron declarado

Cada una tiene que existir como directorio real con al menos un archivo. Codigo plano en la raiz no satisface el patron.

- `dags`
- `src/extract`
- `src/transform`
- `src/load`
- `src/monitoring`
- `tests`
- `conf`
- `sql`

## Verificacion

```bash
pip install -r requirements.txt && pytest -q
```

Ese comando pasando es la definicion de "terminado" para vos.

## Convenciones que tenes que respetar

- Un solo ecosistema: no declares librerias de otro lenguaje ni mezcles gestores de paquetes.
- Toda libreria que uses tiene que estar declarada en el manifiesto de dependencias.
- Todo import declarado tiene que usarse; todo tipo usado tiene que existir o venir de una dependencia declarada.
- El patron es **ETL con orquestación, particionado y calidad de datos**: los contratos (interfaces, puertos) los define la capa interna y los implementa la externa, nunca al revés.
- Los archivos que crees llevan implementacion real, no stubs: sin `TODO`, sin cuerpos vacios, sin `// getters y setters`.

## Contexto del candidato

Sirve para calibrar el nivel del codigo, no para resolver las fases.

- Perfil: Chapter Ciencia de Datos, Especialidad Ingeniero de Datos, Seniority Senior
- Brecha que el reto ataca: Implementa bases de datos OLTP. El objetivo es que el candidato domine la implementación y optimización de bases de datos orientadas a transacciones en línea, incluida la configuración, diseño de esquemas, indexación, gestión de transacciones y monitoreo de rendimiento.
- Mision: Candidato con experiencia como Senior en ingeniería de datos.

---

*Generado por Challenge Generator — Pragma. `README.md` tiene el enunciado completo del reto para la persona. `PROMPT_MEJORA.md` es la variante para pegar en un chat, si se prefiere ese flujo.*
