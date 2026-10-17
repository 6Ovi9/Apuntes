# Formulario y Guía Rápida de Resolución: AEC-1 / EN1 de Estadística (Temas 1 y 2)

## 1. Probabilidad Elemental y Teoremas Fundamentales

### 1.1. Axiomas y Propiedades Básicas de Probabilidad

- **Espacio Muestral ($S$):** Conjunto universal de todos los resultados posibles asociados a un experimento aleatorio.
- **Suceso ($A$):** Cualquier subconjunto medible del espacio muestral $S$ ($A \subseteq S$).
- **Axiomas de Kolmogorov:**
  - **No negatividad:** Para todo suceso $A$, $P(A) \ge 0$.
  - **Certidumbre:** La probabilidad del espacio muestral completo es $P(S) = 1$.
  - **Aditividad contable (sucesos disjuntos):** Si $A$ y $B$ son sucesos mutuamente excluyentes ($A \cap B = \emptyset$), entonces:
    $$P(A \cup B) = P(A) + P(B)$$
- **Propiedades Derivadas Directas:**
  - Probabilidad del suceso contrario (complementario): $P(A^c) = 1 - P(A)$
  - Probabilidad de la unión de dos sucesos no disjuntos: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

### 1.2. Probabilidad Condicionada e Independencia de Sucesos

- **Probabilidad Condicionada:** Evaluada como la probabilidad del suceso $A$ dado que ha ocurrido de forma verificada el suceso $B$ (exigiendo $P(B) > 0$):
  $$P(A|B) = \frac{P(A \cap B)}{P(B)}$$
- **Regla del Producto (Multiplicativa):**
  $$P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$$
- **Condición Necesaria y Suficiente de Independencia:** Dos sucesos $A$ y $B$ son independientes estocásticamente si y solo si la información de uno no altera la probabilidad del otro:
  $$P(A \cap B) = P(A) \cdot P(B) \iff P(A|B) = P(A) \quad (\text{para } P(B) > 0)$$

> **ADVERTENCIA: Diferencia entre Sucesos Disjuntos e Independientes**
>
> - **Sucesos Disjuntos (Mutuamente Excluyentes):** Estructura conjuntista. Ocurre si $A \cap B = \emptyset \implies P(A \cap B) = 0$. Significa que ambos sucesos no pueden ocurrir simultáneamente.
> - **Sucesos Independientes:** Estructura probabilística. Ocurre si $P(A \cap B) = P(A) \cdot P(B) \neq 0$ (salvo sucesos triviales de probabilidad nula).
> - Dos sucesos disjuntos con probabilidades estrictamente positivas ($P(A)>0$, $P(B)>0$) **NUNCA** pueden ser independientes, puesto que $P(A \cap B) = 0 \neq P(A) \cdot P(B)$.

### 1.3. Teorema de la Probabilidad Total (TPT)

El Teorema de la Probabilidad Total permite evaluar la probabilidad global de un suceso $A$ definido sobre un espacio muestral particionado en un sistema completo de sucesos disjuntos $\{C_1, C_2, \dots, C_n\}$ (donde $\bigcup_{i=1}^n C_i = S$ y $C_i \cap C_j = \emptyset$ para $i \neq j$, con $P(C_i) > 0$):

$$P(A) = \sum_{i=1}^{n} P(C_i) \cdot P(A|C_i)$$

**Caso Particular de Dos Particiones ($C$ y $C^c$):**

$$P(A) = P(C) \cdot P(A|C) + P(C^c) \cdot P(A|C^c)$$

**Plantilla Operativa de Resolución Paso a Paso:**

1. **Identificar la partición del espacio muestral:** Definir las condiciones previas y exhaustivas del sistema (ejemplo: adjudicación de contrato de defensa $C$ con $P(C) = 0.30$ frente a $C^c$ con $P(C^c) = 0.70$; o clasificación del origen de un componente entre Tipo A con $P(A) = 0.60$ y Tipo B con $P(B) = 0.40$; o bien percepción de complemento salarial $V=1$ con $P(V=1)=0.70$ frente a $V=0$ con $P(V=0)=0.30$).
2. **Identificar el suceso condicionado global de interés ($A$):** Formular rigurosamente el evento terminal observado (ejemplo: $A \equiv \text{"Beneficios excede 40M€"}$, $A \equiv \text{"Fallo del sistema por temperatura } T > 90\,^\circ\text{C"}$, o bien $A \equiv \text{"Ingreso salarial superior a 45.000€"}$).
3. **Calcular las probabilidades condicionadas $P(A|C_i)$ mediante variables continuas o discretas:** En los problemas de examen tipo AEC-1 / EN1, los pesos ponderados $P(A|C_i)$ se obtienen frecuentemente a partir de distribuciones continuas (tales como la Normal $N(\mu, \sigma)$ o la Exponencial):
   - **Caso 1 (Normal en contratos):** Si bajo $C$ el beneficio es $X \sim N(50, 10)$, entonces $P(X > 40 | C) = P\left(Z > \frac{40-50}{10}\right) = P(Z > -1) = 0.8413$. Si bajo $C^c$ el beneficio es $X \sim N(30, 6)$, entonces $P(X > 40 | C^c) = P\left(Z > \frac{40-30}{6}\right) = P(Z > 1.67) = 0.0475$.
   - **Caso 2 (Normal en salarios combinados):** Si $X_1 \sim N(40, 5)$ representa el salario base y $X_2 \sim N(10, 2)$ el complemento por objetivo de ventas ($V=1$), al lograr el objetivo el salario total es $Y = X_1 + X_2 \sim N(40+10, \sqrt{5^2+2^2}) = N(50, \sqrt{29}) \approx N(50, 5.385)$. Así, $P(Y > 45 | V=1) = P\left(Z > \frac{45-50}{5.385}\right) = P(Z > -0.928) \approx 0.8212$. Si no se alcanza el objetivo ($V=0$), el ingreso es solo $X_1 \sim N(40, 5)$, dando $P(X_1 > 45 | V=0) = P(Z > 1) = 0.1587$.
   - **Caso 3 (Temperaturas límite en componentes A/B):** Para componentes A con $X_A \sim N(63, 14)$, $P(X_A > 90) = P\left(Z > \frac{90-63}{14}\right) = P(Z > 1.93) = 0.0268$. Para componentes B con $X_B \sim N(70, 14)$, $P(X_B > 90) = P\left(Z > \frac{90-70}{14}\right) = P(Z > 1.43) = 0.0764$.
4. **Sustituir y ponderar en la fórmula del TPT:** $P(A) = \sum_{i=1}^n P(C_i) \cdot P(A|C_i)$
   (Ejemplo salarial: $P(Y > 45) = 0.30 \cdot 0.1587 + 0.70 \cdot 0.8212 = 0.04761 + 0.57484 = 0.62245$).

### 1.4. Teorema de Bayes

El Teorema de Bayes permite actualizar la probabilidad a priori de un suceso de la partición $C_i$ tras constatar la ocurrencia del suceso de causa o efecto global $A$.

$$P(C_i|A) = \frac{P(C_i) \cdot P(A|C_i)}{\sum_{j=1}^{n} P(C_j) \cdot P(A|C_j)} = \frac{P(C_i) \cdot P(A|C_i)}{P(A)}$$

- **Probabilidad a priori $P(C_i)$:** Probabilidad asignada a la hipótesis $C_i$ antes de observar la prueba $A$.
- **Probabilidad a posteriori $P(C_i|A)$:** Probabilidad condicionada e informada de $C_i$ una vez verificado el suceso $A$.

**Instrucción Operativa de Cálculo:**

1. Identificar de forma unívoca el suceso global observado $A$ expuesto en la condición del problema.
2. Calcular el valor del denominador $P(A)$ ejecutando la plantilla del Teorema de la Probabilidad Total (sección 1.3).
3. Obtener la probabilidad del camino conjunto específico del numerador: $P(C_i \cap A) = P(C_i) \cdot P(A|C_i)$.
4. Efectuar el cociente entre el numerador de la trayectoria específica y el denominador global obtenido del TPT.

---

## 2. Análisis de Fiabilidad de Sistemas y Distribución Exponencial

### 2.1. Función de Fiabilidad $R(t)$, $F(t)$ y $f(t)$

Sea $T \ge 0$ la variable aleatoria continua que representa el tiempo hasta la avería (tiempo de vida) de un sistema o componente en el dominio temporal $t \ge 0$:

| Función  | Denominación Matemática               | Definición y Relación Directa                         |
| -------- | ------------------------------------- | ----------------------------------------------------- |
| $R_T(t)$ | Función de Fiabilidad / Supervivencia | $R_T(t) = P(T > t)$                                   |
| $F_T(t)$ | Función de Distribución Acumulada     | $F_T(t) = P(T \le t) = 1 - R_T(t)$                    |
| $f_T(t)$ | Función de Densidad de Probabilidad   | $f_T(t) = \frac{d F_T(t)}{dt} = -\frac{d R_T(t)}{dt}$ |

### 2.2. Sistemas con Componentes en Serie

Un sistema en serie constituido por $n$ componentes independientes se mantiene operativo si y solo si todos y cada uno de sus componentes individuales sobreviven al instante $t$.

$$\text{Funcionamiento global del sistema: } (T > t) \iff \bigcap_{i=1}^{n} (T_i > t)$$

**Expresión General de Fiabilidad:**

Por independencia estocástica de las variables aleatorias de tiempo de vida $T_i$:

$$R_{sistema}(t) = P\left(\bigcap_{i=1}^{n} \{T_i > t\}\right) = \prod_{i=1}^{n} P(T_i > t) = \prod_{i=1}^{n} R_i(t)$$

**Caso de Componentes Exponenciales Independientes $T_i \sim \exp(\lambda_i)$:**

Para componentes exponenciales con tasa de fallo $\lambda_i$, se cumple que $R_i(t) = e^{-\lambda_i t}$:

$$R_{sistema}(t) = \prod_{i=1}^{n} e^{-\lambda_i t} = e^{-\left(\sum_{i=1}^{n} \lambda_i\right) t}, \quad t > 0$$

- **Teorema de Suma de Tasas:** El tiempo de vida global de una arquitectura en serie formada por componentes exponenciales independientes sigue rigurosamente una distribución exponencial cuya tasa equivalente es la suma de las tasas de fallo individuales:
  $$T_{sistema} \sim \exp\left(\sum_{i=1}^{n} \lambda_i\right)$$

### 2.3. Sistemas con Componentes en Paralelo

Un sistema en paralelo de $n$ componentes opera de manera satisfactoria si al menos uno de los componentes sobrevive al instante $t$.

$$\text{Funcionamiento global del sistema: } (T > t) \iff \bigcup_{i=1}^{n} (T_i > t)$$

**Deducción Formal para Dos Componentes Independientes A y B:**

Utilizando la probabilidad de la unión de sucesos no disjuntos:

$$R_T(t) = P((T_A > t) \cup (T_B > t)) = P(T_A > t) + P(T_B > t) - P(T_A > t) \cdot P(T_B > t)$$

Sustituyendo los componentes exponenciales $T_A \sim \exp(\lambda_A)$ y $T_B \sim \exp(\lambda_B)$:

$$R_T(t) = e^{-\lambda_A t} + e^{-\lambda_B t} - e^{-(\lambda_A + \lambda_B)t}, \quad t > 0$$

**Obtención Formal de $F_T(t)$ y $f_T(t)$:**

- **Distribución Acumulada de Averías:**
  $$F_T(t) = 1 - R_T(t) = 1 - e^{-\lambda_A t} - e^{-\lambda_B t} + e^{-(\lambda_A + \lambda_B)t}, \quad t > 0$$
- **Función de Densidad de Probabilidad (derivando respecto a $t$):**
  $$f_T(t) = \frac{d F_T(t)}{dt} = \lambda_A e^{-\lambda_A t} + \lambda_B e^{-\lambda_B t} - (\lambda_A + \lambda_B) e^{-(\lambda_A + \lambda_B)t}, \quad t > 0$$

### 2.4. Cálculo del Tiempo Medio Esperado $E[T]$

**Método 1: Integración Directa de la Función de Fiabilidad (Método Óptimo)**

Para cualquier variable aleatoria continua no negativa $T \ge 0$:

$$E[T] = \int_{0}^{\infty} R_T(t) \, dt$$

**Método 2: Integral de la Densidad Completando la 2-Erlang**

Efectuando la definición estándar de la esperanza $E[T] = \int_{0}^{\infty} t \cdot f_T(t) \, dt$, se aplica la propiedad de integración demostrada en las pruebas de examen basada en la densidad de una 2-Erlang:

$$\int_{0}^{\infty} \lambda^2 x e^{-\lambda x} \, dx = 1 \implies \int_{0}^{\infty} x e^{-\lambda x} \, dx = \frac{1}{\lambda^2}$$

**Demostración y Desarrollo Algebraico con Factores Ponderados:**

Para un sistema de 2 componentes idénticos en paralelo con $T_A, T_B \sim \exp(1)$, donde $R_T(t) = 2e^{-t} - e^{-2t}$ y $f_T(t) = 2e^{-t} - 2e^{-2t}$:

$$E[T] = \int_{0}^{\infty} t \cdot \left(2e^{-t} - 2e^{-2t}\right) dt = 2 \int_{0}^{\infty} t e^{-t} \, dt - \int_{0}^{\infty} 2 t e^{-2t} \, dt$$

Para resolver la segunda integral $\int_{0}^{\infty} 2 t e^{-2t} \, dt$, multiplicamos y dividimos por el parámetro de escala 2 para completar el núcleo exacto de la densidad 2-Erlang con $\lambda = 2$:

$$\int_{0}^{\infty} 2 t e^{-2t} \, dt = \frac{1}{2} \int_{0}^{\infty} 2^2 t e^{-2t} \, dt = \frac{1}{2} \cdot (1) = \frac{1}{2}$$

Sustituyendo ambos términos:

$$E[T] = 2 \cdot (1) - \frac{1}{2} \cdot (1) = 2 - \frac{1}{2} = \frac{3}{2} \text{ años}$$

### 2.5. La Distribución Exponencial y la Propiedad de Falta de Memoria

Si $T \sim \exp(\lambda)$, donde $\lambda > 0$ representa la tasa media constante de averías o eventos por unidad de tiempo:

- **Función de densidad de probabilidad:** $f(t) = \lambda e^{-\lambda t}, \quad t > 0$
- **Función de distribución acumulada:** $F(t) = 1 - e^{-\lambda t}, \quad t > 0$
- **Función de fiabilidad:** $R(t) = e^{-\lambda t}, \quad t > 0$
- **Esperanza Matemática y Varianza:** $E[T] = \frac{1}{\lambda}, \quad V[T] = \frac{1}{\lambda^2}$
- **Propiedad de Falta de Memoria (Loss of Memory):** La probabilidad condicional de que el componente sobreviva $t$ unidades de tiempo adicionales dado que ha sobrevivido un tiempo $s$ no depende del tiempo transcurrido $s$:
  $$P(T > t + s \mid T > s) = \frac{P(T > t + s)}{P(T > s)} = \frac{e^{-\lambda(t+s)}}{e^{-\lambda s}} = e^{-\lambda t} = P(T > t)$$

---

## 3. Distribuciones Discretas de Probabilidad

### 3. Distribuciones Discretas de Probabilidad

### 3.1. Distribución Binomial 𝑋 ∼𝐵(𝑛,𝑝)

Modela el número total de éxitos 𝑋 registrados al ejecutar 𝑛 ensayos independientes e idénticos de Bernoulli, con una probabilidad constante de éxito 𝑝 en cada ensayo (y probabilidad de fracaso 𝑞 =1 −𝑝).

- **Soporte de la v.a.:** 𝑥 ∈𝑆𝑋 ={0,1,2,…,𝑛}
- **Función de masa de probabilidad (FMP):**  
    𝑃(𝑋=𝑘)=(𝑛𝑘)𝑝𝑘(1−𝑝)𝑛−𝑘=𝑛!𝑘!(𝑛−𝑘)!𝑝𝑘(1−𝑝)𝑛−𝑘
- **Esperanza Matemática:** 𝐸[𝑋] =𝑛𝑝
- **Varianza:** 𝑉[𝑋] =𝑛𝑝(1 −𝑝)

#### Aproximación a la Normal

Si se cumplen las condiciones 𝑛 ≥30, 𝑛𝑝 ≥5 y 𝑛𝑞 ≥5, la variable discreta se puede aproximar a una variable continua Normal 𝑋′ ∼𝑁(𝜇,𝜎):

- **Nuevos parámetros:** 𝜇 =𝑛𝑝 y 𝜎 =√𝑛𝑝𝑞.

**Corrección por continuidad (Yates):** Al pasar de discreta a continua, se ajusta el valor en 0,5 para "ensanchar" el número y cubrir el hueco decimal:

- **Exacto:** 𝑃(𝑋 =𝑘) ⟶𝑃(𝑘 −0,5 ≤𝑋′ ≤𝑘 +0,5)
- **Incluye el borde (≤, ≥):**
    - 𝑃(𝑋 ≤𝑘) ⟶𝑃(𝑋′ ≤𝑘 +0,5)
    - 𝑃(𝑋 ≥𝑘) ⟶𝑃(𝑋′ ≥𝑘 −0,5)
- **Excluye el borde (<, >):**
    - 𝑃(𝑋 <𝑘) ⟶𝑃(𝑋′ ≤𝑘 −0,5)
    - 𝑃(𝑋 >𝑘) ⟶𝑃(𝑋′ ≥𝑘 +0,5)

### 3.2. Distribución Geométrica: Comparativa Versión 1 vs. Versión 2

Para prevenir errores habituales en las entregas EN1 y pruebas AEC-1, se detalla la parametrización exacta de las dos versiones formales de la distribución Geométrica:

| Característica | Geométrica Versión 1 | Geométrica Versión 2 |
|---|---|---|
| **Definición de la v.a. $Y$** | Número de ensayos necesarios **HASTA** obtener el 1.er éxito/evento de parada | Número de fracasos ocurridos **ANTES** de observar el 1.er éxito/evento de parada |
| **Parámetro del evento de parada** | $p$ (probabilidad de éxito por ensayo) | $p_{stop} = \theta$ (probabilidad de fallo o parada) |
| **Probabilidad de continuación** | $1-p$ | $1-\theta = p_{success}$ |
| **Soporte ($S_Y$)** | $y \in \{1, 2, 3, \dots\}$ | $y \in \{0, 1, 2, \dots\}$ |
| **Función de Masa $P(Y = y)$** | $P(Y = y) = p (1-p)^{y-1}$ | $P(Y = y) = \theta (1-\theta)^y$ |
| **Esperanza $E[Y]$** | $E[Y] = \frac{1}{p}$ | $E[Y] = \frac{1-\theta}{\theta}$ |
| **Varianza $V[Y]$** | $V[Y] = \frac{1-p}{p^2}$ | $V[Y] = \frac{1-\theta}{\theta^2}$ |

**Identificación Operativa en Problemas de Telecomunicaciones (Versión 2):**

En problemas de lectura de memoria RAM de 16 bits (ENTREGABLES_TelEst):

1. **Paso 1:** Se calcula la probabilidad de que una palabra sea errónea mediante una Binomial $X \sim B(n=16, p=0.02)$, obteniendo la probabilidad de detención/parada $\theta = P(X \ge 2) = 1 - P(X=0) - P(X=1) \approx 0.03986$.
2. **Paso 2:** La variable $Y \equiv \text{"Número de palabras enviadas a pantalla seguidas ANTES del primer fallo"}$ sigue una Geométrica Versión 2 con $Y \sim \text{Geométrica}(\theta = 0.03986)$.
3. **Paso 3:** La probabilidad de enviar entre $a=8$ y $b=10$ palabras consecutivas es la suma sobre el intervalo:
   $$P(8 \le Y \le 10) = \sum_{y=8}^{10} \theta(1-\theta)^y = 0.03986 \cdot (1-0.03986)^8 + 0.03986 \cdot (1-0.03986)^9 + 0.03986 \cdot (1-0.03986)^{10} \approx 0.08297$$

### 3.3. Distribución de Poisson $X \sim \text{Poisson}(\lambda)$ y su Enlace Temporal

Modela el recuento de eventos raros $X$ que ocurren en un intervalo continuo de tiempo o dimensión espacial.

- **Soporte de la v.a.:** $x \in S_X = \{0, 1, 2, \dots\}$
- **Función de masa de probabilidad:**
  $$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}$$
- **Esperanza Matemática y Varianza:** $E[X] = \lambda, \quad V[X] = \lambda$
- **Escalabilidad Temporal de Parámetros:** Si la tasa base es $\lambda_{base}$ por unidad de tiempo, para un intervalo continuo de duración $t$, el parámetro ajustado es:
  $$\lambda' = \lambda_{base} \cdot t$$
  (Ejemplo de servidor web: Con $\lambda_{base} = 8$ bloqueos diarios en 24 horas $\implies \lambda = \frac{8}{24} = \frac{1}{3}$ bloqueos/hora. Para una ventana de $t = 4$ horas, $\lambda' = \frac{1}{3} \cdot 4 = \frac{4}{3}$).

**Enlace Dual con el Tiempo entre Eventos ($n$-Erlang):**

Dado un proceso continuo de Poisson con tasa $\lambda$ por unidad de tiempo, existe una equivalencia fundamental entre el recuento $N(t)$ y los tiempos de llegada:

- El tiempo entre dos eventos consecutivos sigue una distribución Exponencial $T_1 \sim \exp(\lambda)$ con $E[T_1] = \frac{1}{\lambda}$.
- El tiempo transcurrido $T_n$ hasta que se registra exactamente el $n$-ésimo evento sigue una distribución $n$-Erlang de parámetro $\lambda$ ($T_n \sim n\text{-Erlang}(\lambda)$).
- **Esperanza del $n$-ésimo evento:** $E[T_n] = \frac{n}{\lambda}$
  (Ejemplo del servidor web de EN2: Para hallar el instante en que ocurre el 4.º bloqueo de servidor con tasa $\lambda = 1/3$ bloqueos/hora, la variable es $T_4 \sim 4\text{-Erlang}(1/3)$, resultando una hora esperada de $E[T_4] = \frac{4}{1/3} = 12\text{ horas}$, con varianza $V[T_4] = \frac{n}{\lambda^2} = \frac{4}{(1/3)^2} = 36 \implies \sigma_{T_4} = 6\text{ horas}$).

---

## 4. Distribución Continua Normal $N(\mu, \sigma)$

### 4.1. Definición y Tipificación Z

Sea $X$ una variable aleatoria continua gaussiana parametrizada por su media $\mu$ y su desviación típica $\sigma > 0$ (con varianza $\sigma^2$): $X \sim N(\mu, \sigma)$.

- **Transformación Integrada de Tipificación:**
  $$Z = \frac{X - \mu}{\sigma} \sim N(0,1)$$
- **Cálculo de Probabilidad en Intervalos Generales:**
  $$P(a < X < b) = P\left(\frac{a - \mu}{\sigma} < Z < \frac{b - \mu}{\sigma}\right)$$

### 4.2. Uso de Tablas de la Normal $N(0,1)$ y Propiedades de Simetría

Las tablas formales proporcionan la cola superior $P(Z > z)$ o la función acumulada de la distribución $P(Z \le z)$.

1. **Cola Superior Directa:** $P(Z > z)$
2. **Propiedad de Simetría Espejo:** $P(Z < -z) = P(Z > z)$
3. **Probabilidad del Complementario:** $P(Z \le z) = 1 - P(Z > z)$
4. **Transformación de Cola Negativa a Positiva:** $P(Z > -z) = 1 - P(Z > z)$
5. **Valores Críticos de Cola Frecuentes:**
   - Para una cola del 5% superior ($P(Z > z_{\alpha/2}) = 0.05$): $z_{0.05} \approx 1.645$ (ó 1.64 / 1.65).
   - Para $P(Z > 1) \approx 0.1587 \implies P(Z \le 1) \approx 0.8413$.

### 4.3. Propiedades Avanzadas de la Normal

#### Combinación Lineal y Suma de Variables Normales Independientes

Si $X_1 \sim N(\mu_1, \sigma_1)$ y $X_2 \sim N(\mu_2, \sigma_2)$ son variables aleatorias independientes:

$$Y = X_1 + X_2 \sim N(\mu_Y, \, \sigma_Y)$$

Donde los parámetros de la variable suma $Y$ son:

- **Media de la suma:** $\mu_Y = \mu_1 + \mu_2$
- **Varianza de la suma:** $\sigma_Y^2 = \sigma_1^2 + \sigma_2^2$
- **Desviación Típica de la suma:** $\sigma_Y = \sqrt{\sigma_1^2 + \sigma_2^2}$

> **Cuidado Operativo en Exámenes:** No deben sumarse directamente las desviaciones típicas.
>
> **Ejemplo cuantitativo (Práctica 3):** Si el salario base es $X_1 \sim N(40, 5)$ y el complemento es $X_2 \sim N(10, 2)$:
>
> - $\mu_Y = 40 + 10 = 50$
> - $\sigma_Y^2 = 5^2 + 2^2 = 25 + 4 = 29 \implies \sigma_Y = \sqrt{29} \approx 5.385$
>
> Por lo tanto, $Y \sim N(50, \, 5.385)$.

#### Intervalo de Predicción Simétrico del $(1-\alpha)\cdot 100\%$

Para una variable $X \sim N(\mu, \sigma)$, el intervalo simétrico de predicción $I = [L_1, L_2]$ centrado en la media $\mu$ que encierra una probabilidad contenida de $1-\alpha$ verifica:

$$P(L_1 < X < L_2) = 1 - \alpha \iff P(X > L_2) = \frac{\alpha}{2} \quad \text{y} \quad P(X < L_1) = \frac{\alpha}{2}$$

Expresiones explícitas de los límites:

$$L_1 = \mu - z_{\alpha/2} \cdot \sigma, \quad L_2 = \mu + z_{\alpha/2} \cdot \sigma$$

**Ejemplo (Intervalo de predicción del 90% para salario base $X_1 \sim N(40, 5)$):**

- $\alpha = 0.10 \implies \alpha/2 = 0.05 \implies z_{0.05} = 1.645$
- $L_1 = 40 - 1.645 \cdot (5) = 40 - 8.225 = 31.775 \approx 31.8$
- $L_2 = 40 + 1.645 \cdot (5) = 40 + 8.225 = 48.225 \approx 48.2$
- Intervalo resultante: $I = [31.8, \, 48.2]$ (miles de euros).

---

## 5. Guía Rápida de Decisión: Tabla Comparativa según el Enunciado

| Pregunta / Palabra clave en el enunciado | Distribución a aplicar | Parámetros a identificar | Fórmula / Operación principal |
|---|---|---|---|
| "Número de éxitos/errores en $n$ ensayos/bits independientes" | Binomial | $n$ (número de ensayos), $p$ (prob. de éxito/error por ensayo) | $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$ |
| "Número de palabras/ensayos correctos enviados ANTES del primer fallo" | Geométrica (v2) | $\theta = p_{stop}$ (probabilidad de fallo o parada) | $P(Y = y) = \theta(1-\theta)^y$ <br> $P(a \le Y \le b) = \sum_{y=a}^b \theta(1-\theta)^y$ |
| "Número de eventos/llegadas/bloqueos por unidad de tiempo o espacio" | Poisson | $\lambda'$ (tasa media ajustada al intervalo $t$: $\lambda' = \lambda_{base} \cdot t$) | $P(X = k) = \frac{e^{-\lambda'} (\lambda')^k}{k!}$ |
| "Tiempo transcurrido HASTA el $n$-ésimo evento de un proceso de Poisson" | $n$-Erlang | $n$ (orden del evento), $\lambda$ (tasa del proceso) | $T_n \sim n\text{-Erlang}(\lambda) \implies E[T_n] = \frac{n}{\lambda}, \, V[T_n] = \frac{n}{\lambda^2}$ |
| "Tiempo hasta la primera avería / tiempo entre dos accesos" | Exponencial | $\lambda$ (tasa media de averías por unidad de tiempo) | $R(t) = e^{-\lambda t}, \quad f(t) = \lambda e^{-\lambda t}, \quad E[T] = \frac{1}{\lambda}$ |
| "Comportamiento de sistema con componentes A, B en SERIE" | Serie (Exponencial) | $\lambda_A, \lambda_B$ de cada componente | $R_S(t) = e^{-(\lambda_A + \lambda_B)t} \implies T \sim \exp(\lambda_A + \lambda_B)$ |
| "Comportamiento de sistema con componentes A, B en PARALELO" | Paralelo (Fiabilidad) | $\lambda_A, \lambda_B$ de cada componente | $R_P(t) = e^{-\lambda_A t} + e^{-\lambda_B t} - e^{-(\lambda_A + \lambda_B)t}$ <br> $E[T] = \int_0^\infty R_P(t) dt$ |
| "Variable continua con media $\mu$, desviación $\sigma$, salarios, temperaturas" | Normal | $\mu$ (media), $\sigma$ (desviación típica) | Tipificar $Z = \frac{X - \mu}{\sigma}$ y buscar en tabla $N(0,1)$ |
| "Suma de dos variables normales independientes $X_1 + X_2$" | Suma de Normales | $\mu_Y = \mu_1 + \mu_2$, $\sigma_Y = \sqrt{\sigma_1^2 + \sigma_2^2}$ | $Y \sim N(\mu_Y, \sigma_Y) \implies Z = \frac{Y - \mu_Y}{\sigma_Y}$ |
