def obtener_temperatura():
    print("Ingrese las temperaturas diarias en grados Celsius (7 días):")
    temperaturas = []
    
    for dia in range(1, 8):  # 7 días
        while True:
            try:
                temp = float(input(f"Día {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    return temperaturas

def analizar_temperaturas(temperaturas):
    # Cálculo de la temperatura máxima y mínima
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    
    # Cálculo del promedio semanal
    promedio = sum(temperaturas) / len(temperaturas)
    
    # Días con temperatura por encima del promedio
    dias_sobre_promedio = [i + 1 for i, temp in enumerate(temperaturas) if temp > promedio]
    
    # Alertas de temperaturas extremas
    alertas = []
    for i, temp in enumerate(temperaturas):
        if temp > 40:
            alertas.append(f"Día {i + 1}: Temperatura extrema alta ({temp}°C)")
        elif temp < 0:
            alertas.append(f"Día {i + 1}: Temperatura extrema baja ({temp}°C)")
    
    # Resultados
    print("\nResultados del análisis:")
    print(f"Temperatura máxima: {temp_max}°C")
    print(f"Temperatura mínima: {temp_min}°C")
    print(f"Promedio semanal: {promedio:.2f}°C")
    print(f"Días con temperatura por encima del promedio: {dias_sobre_promedio if dias_sobre_promedio else 'Ninguno'}")
    if alertas:
        print("\nAlertas de temperaturas extremas:")
        for alerta in alertas:
            print(alerta)
    else:
        print("\nNo hubo temperaturas extremas.")

# Programa principal
if __name__ == "__main__":
    temperaturas = obtener_temperatura()
    analizar_temperaturas(temperaturas)