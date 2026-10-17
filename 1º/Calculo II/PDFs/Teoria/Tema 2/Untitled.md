# Chuleta de Examen: Tema 2 - Derivación (Cálculo II)

Esta guía práctica está diseñada para la resolución rápida de ejercicios. Se omiten demostraciones y límites para centrarse en algoritmos de cálculo y condiciones de aplicación.

--------------------------------------------------------------------------------

### 1. Derivadas Parciales y Operador Gradiente

**Regla de oro:** Para derivar respecto a una variable, trata el resto como constantes.

- **Notación:** \frac{\partial f}{\partial x} = f_x = \partial_x f.
- **El Gradiente (****\nabla f****):** Vector que agrupa las derivadas de primer orden.
    - En \mathbb{R}^2: \nabla f(a, b) = \left( f_x(a, b), f_y(a, b) \right).
    - En \mathbb{R}^n: \nabla f(\vec{a}) = (f_{x_1}(\vec{a}), f_{x_2}(\vec{a}), \dots, f_{x_n}(\vec{a})).

**Derivadas de Segundo Orden (Hessianas):** Existen cuatro combinaciones para f(x, y): f_{xx}, f_{yy}, f_{xy}, f_{yx}.

- **Orden de las cruzadas:** En f_{xy}, se deriva primero respecto a x y luego respecto a y.
- **¡Truco del Experto! (Teorema de Clairaut):** Si f es de clase C^2 (sus segundas parciales son continuas), entonces **f_{xy} = f_{yx}**. Solo calcula una y ahorra tiempo.

--------------------------------------------------------------------------------

### 2. Derivada Direccional (D_{\vec{v}} f) y Crecimiento

**Condición de Diferenciabilidad:** Para usar las fórmulas de esta sección, f debe ser diferenciable.

- **Nota del Tutor:** En el examen, comprueba si f es C^1 (sus derivadas parciales son continuas). Si es C^1, entonces es diferenciable (Teorema 17).

**Cálculo Operativo:**

1. **¡OJO! Vector Unitario:** El vector dirección \vec{v} **DEBE ser unitario** (\|\vec{v}\| = 1). Si no lo es, normaliza: \vec{u} = \frac{\vec{v}}{\|\vec{v}\|}.
2. **Fórmula:** D_{\vec{v}} f(a, b) = \nabla f(a, b) \cdot \vec{v}.

**Tabla de Interpretación y Optimización:**

|   |   |   |   |
|---|---|---|---|
|Valor de D_{\vec{v}} f|Dirección \vec{v}|Comportamiento|Valor (Tasa)|
|**Máximo**|\vec{v} en sentido de \nabla f|Crecimiento más rápido|\|\nabla f\||
|**Mínimo**|\vec{v} en sentido de -\nabla f|Decrecimiento más rápido|-\|\nabla f\||
|**Nulo (****0****)**|\vec{v} \perp \nabla f|Dirección de la curva de nivel|0|
|**> 0**|Ángulo agudo con \nabla f|La función crece|\nabla f \cdot \vec{v}|
|**< 0**|Ángulo obtuso con \nabla f|La función decrece|\nabla f \cdot \vec{v}|

--------------------------------------------------------------------------------

### 3. Geometría del Gradiente: Plano Tangente y Recta Normal

El gradiente \nabla F en un punto P es el **vector normal (****\vec{n}****)** a la superficie de nivel en ese punto.

#### Caso A: Superficie Implícita (F(x, y, z) = 0)

Sea P = (x_0, y_0, z_0).

- **Vector Normal:** \vec{n} = \nabla F(P) = (F_x, F_y, F_z).
- **Plano Tangente:** F_x(P)(x - x_0) + F_y(P)(y - y_0) + F_z(P)(z - z_0) = 0.
- **Recta Normal:** X = P + t\nabla F(P) \implies (x, y, z) = (x_0, y_0, z_0) + t(F_x, F_y, F_z).

#### Caso B: Superficie Explícita (z = f(x, y))

Se puede ver como F(x, y, z) = f(x, y) - z = 0.

- **Vector Normal:** \vec{n} = (f_x(x_0, y_0), f_y(x_0, y_0), -1).
- **Plano Tangente:** z = f(x_0, y_0) + f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0).

--------------------------------------------------------------------------------

### 4. Diferencial Total y Aproximación Lineal

El diferencial dz representa la variación aproximada de la función ante pequeños cambios dx y dy.

- **Fórmula del Diferencial:** dz = f_x(a, b)dx + f_y(a, b)dy.
- **Estimación de valores:** f(x, y) \approx f(a, b) + dz.
    - Donde dx = x - a y dy = y - b.
- **Nota del Tutor:** Úsalo para cálculos de errores o aproximaciones rápidas cuando te mueves del punto (a, b) al (x, y). El error de esta aproximación (Resto de Taylor R_1) tiende a 0 más rápido que la distancia al punto.

--------------------------------------------------------------------------------

### 5. Regla de la Cadena (Multivariable)

Para funciones compuestas donde u = f(x_1, \dots, x_n) y cada x_j depende de variables (t_1, \dots, t_m).

- **Fórmula General:** \frac{\partial u}{\partial t_i} = \sum_{j=1}^{n} \frac{\partial u}{\partial x_j} \frac{\partial x_j}{\partial t_i}.
- **¡Truco del Experto! (Diagrama de Árbol):** Dibuja las dependencias. Para hallar la derivada respecto a t_i, suma todos los caminos que lleguen desde u hasta t_i, multiplicando las derivadas parciales en cada rama.

**Matriz Jacobiana (****JF****):** Para funciones vectoriales F: \mathbb{R}^n \to \mathbb{R}^m (donde hay m funciones y n variables).

- **Estructura:** Matriz de tamaño m \times n. Cada fila i es el gradiente de la función F_i.
- **Dimensiones:** m (filas/funciones) \times n (columnas/variables).

--------------------------------------------------------------------------------

### 6. Derivación Implícita (Teorema de la Función Implícita)

Si F(x, y, z) = 0 define a z como función de (x, y), puedes hallar sus derivadas sin despejar z.

**Condiciones de Existencia:**

1. F(P) = 0.
2. F es de clase C^1 en el entorno de P.
3. **Condición Crítica:** F_z(P) \neq 0.

**Fórmulas de Cálculo Directo:** \frac{\partial z}{\partial x} = -\frac{F_x}{F_z} \quad ; \quad \frac{\partial z}{\partial y} = -\frac{F_y}{F_z}

- **¡OJO! El signo negativo:** Es el error más común en exámenes. No olvides el - delante de la fracción.
- **Gradiente de la función implícita:** \nabla z(x, y) = \left( -\frac{F_x}{F_z}, -\frac{F_y}{F_z} \right).