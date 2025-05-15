# Análisis de valoración de YPF

Este repositorio contiene un análisis detallado de valoración de YPF.

## Objetivo
**Evaluar la performance operativa y financiera de YPF, con énfasis en Vaca Muerta (shale oil/gas):**
1. Evaluar las operaciones de producción (upstream) y refinación/ventas (downstream).
2. Analizar costos de extracción y su competitividad frente a empresas que utilizan fracking.
3. Estudiar el precio del petróleo y su impacto en los ingresos.
4. Revisar inversiones futuras (CAPEX) y su sostenibilidad financiera.
5. Identificar patrones, tendencias, correlaciones y anomalías en datos financieros y operativos.

## Alcance del Análisis
### 1. Análisis Operativo
- **Producción de petróleo, gas y derivados (upstream):**
  - Volúmenes actuales de producción.
  - Proyección de producción a 5 y 10 años (crecimiento o declive).
- **Refinación y comercialización (downstream):**
  - Desempeño de refinación y ventas de combustibles.
  - Tendencias en márgenes y demanda de mercado.
### 2. Costos de Extracción
- **Costos de extracción (lifting costs):**
  - Evolución histórica de los costos en operaciones upstream.
  - Proyección de costos futuros y posibles reducciones (tecnología, eficiencia).
- **Comparación con competidores:**
  - Análisis de costos de extracción de empresas que utilizan fracking.
  - Evaluación de la competitividad de YPF en el sector.
### 3. Precio del Petróleo
- Análisis del precio medio histórico del petróleo.
- Evaluación de tendencias: ¿existe una media estable, o tiende a subir/bajar?
- Implicaciones para los ingresos y la planificación estratégica de YPF.
### 4. Inversiones y Sostenibilidad Financiera
- **Inversiones futuras (CAPEX):**
  - Revisión de planes de inversión en upstream, downstream y proyectos estratégicos.
  - Relación entre CAPEX y sostenibilidad financiera (flujo de caja, deuda).
- **Sostenibilidad:**
  - Evaluación de la capacidad de YPF para financiar inversiones sin comprometer su estabilidad financiera.
### 5. Análisis de Datos
- Identificación de patrones, tendencias y correlaciones en datos financieros y operativos.
- Detección de posibles anomalías que requieran atención.
- Generación de insights accionables para optimizar estrategias de inversión o decisiones operativas

## Descripción de la metodología a seguir:
- `Preprocesamiento de datos.`
- `Análisis exploratorio (EDA).`
- `Diseño de tablero de control.`
- `Conclusiones y recomendaciones.`

### 1. Preprocesamiento de datos:
  * 1.1. Selección de columnas relevantes (ingresos, EBITDA, producción de petróleo/gas, costos operativos, CAPEX, deuda, etc.).
  * 1.2. Limpieza de datos (valores nulos, duplicados, formateo).
### 2. Análisis exploratorio (EDA):
  * 2.1. Análisis univariado: distribución de variables clave (producción, costos, ingresos).
  * 2.2. Análisis bivariado: relaciones entre variables (e.g., producción vs. costos, CAPEX vs. EBITDA).
  * 2.3. Análisis multivariado: correlaciones y patrones entre múltiples variables.
  * 2.4. Detección de outliers (e.g., picos en costos de extracción o caídas en producción).
  * 2.5. Análisis de tendencias: evolución temporal de producción, costos e inversiones.
  * 2.6. Identificación de patrones (e.g., relación entre inversión en Vaca Muerta y aumento de producción shale).
  * 2.7. Segmentación (e.g., upstream vs. downstream en términos de rentabilidad).
  * 2.8. Correlaciones (e.g., impacto del precio del petróleo en ingresos downstream).
### 3. Diseño de tablero de control:
  * 3.1. Gráficos para tendencias, correlaciones y outliers.
  * 3.2. Tablero de control (usando Plotly o Matplotlib para decisiones estratégicas).
### 4. Conclusiones y recomendaciones:
  * Insights sobre la sostenibilidad de YPF, eficiencia operativa y oportunidades de crecimiento.

