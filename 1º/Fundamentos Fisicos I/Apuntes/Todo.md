## 1. Mecánica: Cinemática, Dinámica y Momento

| **Concepto**                | **Fórmula**                                                                                                            | **Notas**                                                                                    |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Velocidad y Aceleración** | $\vec{v}(t) = \frac{d\vec{r}}{dt}$<br><br>  <br>  <br><br>$\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}$ | $\vec{v}$ es siempre tangente a la trayectoria.                                              |
| **Componentes intrínsecas** | $\vec{a}(t) = \frac{dv}{dt}\hat{u}_t + \frac{v^2}{\rho}\hat{u}_n$                                                      | $\hat{u}_n$ apunta hacia el centro de curvatura y $\rho$ es el radio de curvatura.           |
| **Momento Lineal**          | $\vec{p} = m\vec{v}$                                                                                                   | Se conserva en sistemas aislados.                                                            |
| **2ª Ley de Newton**        | $\vec{F} = \frac{d\vec{p}}{dt}$ o $\vec{F} = m\vec{a}$                                                                 | La forma $\vec{F} = m\vec{a}$ solo es válida si la masa es constante.                        |
| **Momento Angular**         | $\vec{L} = \vec{r} \times \vec{p}$                                                                                     | No es nulo si la partícula gira respecto al origen elegido.                                  |
| **Cambio de Mom. Angular**  | $\vec{\tau} = \vec{r} \times \vec{F} = \frac{d\vec{L}}{dt}$                                                            | Si $\vec{\tau} = \vec{0}$, el momento angular es constante y el objeto se mueve en un plano. |
| **Centro de Masas (CM)**    | $\vec{r}_{CM} = \frac{1}{M}\sum m_i\vec{r}_i$<br><br>  <br>  <br><br>$\vec{v}_{CM} = \frac{1}{M}\sum m_i\vec{v}_i$     | Concentra el movimiento de un sistema de partículas de masa total $M$.                       |

---

## 2. Trabajo, Energía y Colisiones

|**Concepto**|**Fórmula**|**Notas**|
|---|---|---|
|**Energía Cinética** ($E_{cin}$)|$E_{cin} = \frac{1}{2}mv^2 = \frac{\vec{p} \cdot \vec{p}}{2m}$|Es una magnitud escalar.|
|**Trabajo** ($W$)|$W = \int_1^2 \vec{F} \cdot d\vec{r} = \Delta E_{cin}$|El trabajo de la fuerza neta equivale al cambio en la energía cinética.|
|**Fuerzas Conservativas**|$\vec{F} = -\nabla U \implies W_{cons} = -\Delta U$|El trabajo no depende de la trayectoria.<br><br>  <br><br>_Ej: Fuerza elástica_ $U = \frac{1}{2}kx^2$.|
|**Energía Mecánica** ($E_m$)|$E_m = E_{cin} + U$|Suma de energía cinética y potencial.|
|**Fuerzas No Conservativas**|$\Delta E_m = W_{no-cons}$|Si no hay fuerzas no conservativas (ej. rozamiento), $\Delta E_m = 0$.|

> [!info] Casos de Estudio: Colisiones
> 
> - **Colisión Elástica:** Se conserva el momento lineal ($\vec{p}_{antes} = \vec{p}_{despues}$) y la energía mecánica ($E_{m\_antes} = E_{m\_despues}$).
>     
> - **Colisión Inelástica:** Se conserva el momento lineal, pero NO la energía mecánica (parte de la energía deforma el sistema o se disipa como calor).
>     

---

## 3. Electrostática

|**Concepto**|**Fórmula**|**Notas**|
|---|---|---|
|**Ley de Coulomb**|$\vec{F}_{1\to2} = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r_{12}^2}\hat{u}_{12}$|Fuerza ejercida por $q_1$ sobre $q_2$.|
|**Campo Eléctrico puntual**|$\vec{E}(\vec{r}) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat{u}_r$|Campo generado por una carga $q$ a una distancia $r$.|
|**Potencial Eléctrico** ($V$)|$V(\vec{r}) = \frac{1}{4\pi\varepsilon_0}\frac{q}{|\vec{r}-\vec{r}'|
|**Flujo Eléctrico** ($\Phi$)|$\Phi = \iint_S \vec{E} \cdot d\vec{S}$|Representa cuántas líneas de campo atraviesan una superficie $S$.|

> [!tip] Casos de Estudio: Distribuciones de carga y Ley de Gauss
> 
> **Densidades de carga a usar:**
> 
> - Lineal: $dq = \lambda dl$
>     
> - Superficial: $dq = \sigma dA$
>     
> - Volumétrica: $dq = \rho dV$
>     
> 
> **Aplicación de la Ley de Gauss** ($\Phi = \frac{q_{encerrada}}{\varepsilon_0}$) para sacar el Campo Eléctrico:
> 
> ![Gaussian surface for electric field, AI generated](https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcTdqVgwnvZ02ecqauKFbEb1x9q8cADRcgD6qvSegyoTsUeJXsxkSbBfMF8XNN0iaDbpG1i5isHsB8F44FlfYuyAQDOpBBrePFQJcAuk63RWtA0r94k)
> 
> Shutterstock
> 
> Explore

> 1. Identifica la simetría de la distribución de carga (esférica, cilíndrica, plana).
>     
> 2. Elige una superficie de Gauss cerrada donde el campo eléctrico sea constante en módulo (para poder sacarlo de la integral: $\oint \vec{E} \cdot d\vec{S} = E \oint dS$).
>     
> 3. Calcula el lado izquierdo de la ecuación evaluando el área de tu superficie imaginaria.
>     
> 4. Calcula el lado derecho sumando o integrando la carga total interior ($q_{encerrada}$).
>     
> 5. Despeja $E$.
>