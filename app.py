from librodiario import LibroDiario

def main():
    libro = LibroDiario()

    print(" Cargando transacciones desde archivo CSV...\n")
    libro.cargar_transacciones_desde_archivo("transacciones.csv")

    print("Calculando resumen contable...\n")
    resumen = libro.calcular_resumen()
    print(f"Ingresos totales: ${resumen['ingresos']:.2f}")
    print(f"Egresos totales: ${resumen['egresos']:.2f}\n")

    print("Exportando resumen a archivo 'resumen.txt'...\n")
    libro.exportar_resumen("resumen.txt")

    print("Proceso completado. Revisa el archivo 'log_contable.log' para los registros.")
    print("También puedes verificar el archivo 'resumen.txt' para el total de ingresos y egresos.\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        from datetime import datetime
        import logging
        logging.basicConfig(filename='log_contable.log', level=logging.ERROR)
        logging.error(f"Error no controlado en la app: {e}")
        print("Ocurrió un error inesperado. Revisa 'log_contable.log' para más detalles.")
