# ================================================================
# Simulación de políticas de reemplazo de cajetines
# Ejercicio M:3, U:7, O:7
# ================================================================
# Este programa simula mediante Monte Carlo dos políticas de mantenimiento:
#   - Política A: reemplazar únicamente el cajetín que falle.
#   - Política B: cuando falla un cajetín, se reemplazan los tres al mismo tiempo.
#
# Con los resultados se estiman:
#   a) El costo promedio de cada política.
#   b) El tiempo empleado en el cambio de cajetines.
#   c) El tiempo de retardo (promedio).
#   d) El tiempo de inactividad del centro mecánico.
#
# Autor: Dominic De Freitas
# ================================================================

import numpy as np
import random

# Para que los resultados sean reproducibles
random.seed(0)
np.random.seed(0)

# ------------------------------------------------
# Distribución de vidas de los cajetines (en horas)
# ------------------------------------------------
lifetimes = np.array([1000,1100,1200,1300,1400,1500,1600,1700,1800,1900])
p_life = np.array([0.10,0.14,0.24,0.14,0.12,0.10,0.06,0.05,0.03,0.02])

# ------------------------------------------------
# Distribución del tiempo de retardo (en minutos)
# ------------------------------------------------
delays = np.array([4,6,8])
p_delay = np.array([0.3,0.6,0.1])

# ------------------------------------------------
# Costos y tiempos
# ------------------------------------------------
cost_downtime_per_min = 5.0   # UM por minuto de inactividad
tech_cost_per_hour = 25.0     # UM por hora del técnico
price_cajetin = 20.0          # UM por cada cajetín nuevo

# Tiempo de reemplazo según cuántos cajetines se cambien (en minutos)
replace_time_for = {1:20, 2:30, 3:40}

# ------------------------------------------------
# Funciones auxiliares para muestreo
# ------------------------------------------------
def sample_life():
    """Devuelve una vida útil aleatoria de acuerdo a la distribución dada"""
    return np.random.choice(lifetimes, p=p_life)

def sample_delay():
    """Devuelve un retardo aleatorio de acuerdo a la distribución dada"""
    return np.random.choice(delays, p=p_delay)

# ------------------------------------------------
# Función principal de simulación
# ------------------------------------------------
def simulate_policy(replace_all=False, n_events=20000):
    """
    Simula el comportamiento del sistema bajo una política de reemplazo.
    replace_all = False -> Política A (solo el cajetín fallado).
    replace_all = True  -> Política B (se reemplazan los tres).
    n_events: número de fallas a simular.
    """
    # Se inicializan tres cajetines con vidas aleatorias
    lives = [sample_life() for _ in range(3)]

    # Variables acumuladas
    total_operational_time = 0.0   # en horas
    total_downtime_minutes = 0.0
    total_cost = 0.0
    total_tech_time_minutes = 0.0
    counts = 0

    # Simulación evento por evento (cada evento es una falla)
    for ev in range(n_events):
        # Se determina el tiempo hasta la próxima falla (mínima vida restante)
        t_next = min(lives)
        idx_fail = int(np.argmin(lives))

        # Se acumula tiempo operativo
        total_operational_time += t_next

        # Se actualizan las vidas restantes de los tres cajetines
        lives = [lv - t_next for lv in lives]

        # Cuando ocurre la falla, se genera un retardo (en minutos)
        delay_min = sample_delay()

        if replace_all:
            # Política B: se reemplazan los 3 cajetines
            repl_time = replace_time_for[3]
            downtime = delay_min + repl_time

            # Costos
            downtime_cost = cost_downtime_per_min * downtime
            tech_cost = tech_cost_per_hour * (repl_time/60.0)
            parts_cost = price_cajetin * 3

            # Luego de reemplazar, los tres cajetines son nuevos
            lives = [sample_life() for _ in range(3)]
        else:
            # Política A: solo se cambia el cajetín que falló
            repl_time = replace_time_for[1]
            downtime = delay_min + repl_time

            downtime_cost = cost_downtime_per_min * downtime
            tech_cost = tech_cost_per_hour * (repl_time/60.0)
            parts_cost = price_cajetin

            # Solo el cajetín fallado se reinicia
            lives[idx_fail] = sample_life()

        # Se acumulan los valores de esta intervención
        total_downtime_minutes += downtime
        total_tech_time_minutes += repl_time
        total_cost += (downtime_cost + tech_cost + parts_cost)
        counts += 1

    # Métricas de salida
    total_operational_minutes = total_operational_time * 60.0
    cost_per_operational_hour = total_cost / total_operational_time if total_operational_time > 0 else float('inf')
    inactive_fraction = total_downtime_minutes / (total_operational_minutes + total_downtime_minutes)

    return {
        'replace_all': replace_all,
        'n_events': counts,
        'avg_cost_per_event': total_cost / counts,
        'avg_downtime_per_event_min': total_downtime_minutes / counts,
        'avg_tech_time_per_event_min': total_tech_time_minutes / counts,
        'cost_per_operational_hour': cost_per_operational_hour,
        'inactive_fraction': inactive_fraction
    }

# ------------------------------------------------
# Programa principal
# ------------------------------------------------
if __name__ == "__main__":
    # Se simulan 20 000 eventos para cada política
    res_A = simulate_policy(replace_all=False, n_events=20000)
    res_B = simulate_policy(replace_all=True, n_events=20000)

    print("Resultados Política A (reemplazo de 1 cajetín):")
    for k,v in res_A.items():
        print(f"  {k}: {v}")

    print("\nResultados Política B (reemplazo de 3 cajetines):")
    for k,v in res_B.items():
        print(f"  {k}: {v}")
