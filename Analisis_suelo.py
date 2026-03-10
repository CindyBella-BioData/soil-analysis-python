
# Programa de análisis básico de suelo

ph = float(input("Ingrese el pH del suelo: "))
humedad = float(input("Ingrese el porcentaje de humedad del suelo: "))
nitrogeno = float(input("Ingrese nivel de nitrógeno (0-100): "))

print("\n--- RESULTADO DEL ANÁLISIS ---")

if ph < 5.5:
    print("Suelo ácido. Se recomienda aplicar cal agrícola.")
elif ph > 7.5:
    print("Suelo alcalino. Se recomienda materia orgánica.")
else:
    print("El pH del suelo es adecuado.")

if humedad < 30:
    print("El suelo está seco. Se recomienda riego.")
elif humedad > 70:
    print("Exceso de humedad. Revisar drenaje.")
else:
    print("Humedad del suelo adecuada.")

if nitrogeno < 40:
    print("Bajo nivel de nitrógeno. Se recomienda fertilización.")
else:
    print("Nivel de nitrógeno adecuado.")