#-*- coding: utf-8 -*-

def read_value_from_dat_file(file_path):
    with open(file_path, 'r') as file:
        # Leer todas las líneas del archivo .dat
        lines = file.readlines()
        
        # Obtener el valor de la fila 4 y columna 5 (ten en cuenta que Python usa índices base 0)
        value = float(lines[5].split()[4])
        
    return value

def main():
    output_file = "output.dat"

    # Lista de archivos a procesar
    file_names = ["wallHeatFlux_2.dat", "wallHeatFlux_4.dat", "wallHeatFlux_6.dat",
                  "wallHeatFlux_8.dat", "wallHeatFlux_10.dat", "wallHeatFlux_12.dat",
                  "wallHeatFlux_14.dat", "wallHeatFlux_16.dat","wallHeatFlux_18.dat",
                  "wallHeatFlux_20.dat", "wallHeatFlux_22.dat", "wallHeatFlux_24.dat",
                  "wallHeatFlux_26.dat", "wallHeatFlux_28.dat","wallHeatFlux_30.dat",
                  "wallHeatFlux_32.dat", "wallHeatFlux_34.dat","wallHeatFlux_36.dat",
                  "wallHeatFlux_38.dat", "wallHeatFlux_40.dat","wallHeatFlux_42.dat",
                  "wallHeatFlux_44.dat", "wallHeatFlux_46.dat","wallHeatFlux_48.dat",
                  "wallHeatFlux_50.dat", "wallHeatFlux_52.dat","wallHeatFlux_54.dat",
                  "wallHeatFlux_56.dat", "wallHeatFlux_58.dat","wallHeatFlux_60.dat",
                  "wallHeatFlux_62.dat", "wallHeatFlux_64.dat","wallHeatFlux_66.dat",
                  "wallHeatFlux_68.dat", "wallHeatFlux_70.dat","wallHeatFlux_72.dat",
                  "wallHeatFlux_74.dat", "wallHeatFlux_76.dat","wallHeatFlux_78.dat",
                  "wallHeatFlux_80.dat", "wallHeatFlux_82.dat","wallHeatFlux_84.dat",
                  "wallHeatFlux_86.dat", "wallHeatFlux_88.dat","wallHeatFlux_90.dat",
                  "wallHeatFlux_92.dat", "wallHeatFlux_94.dat","wallHeatFlux_96.dat",
                  "wallHeatFlux_98.dat", "wallHeatFlux_100.dat"]

    # Ruta de la carpeta contenedora de los archivos .dat
    folder_path = "postProcessing/metal/wallHeatFlux/0/"

    with open(output_file, 'w') as output:
        # Escribir la primera fila con los números de los archivos
        output.write("2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100\n")

        for file_name in file_names:
            # Construir la ruta completa al archivo
            file_path = folder_path + file_name

            # Leer el valor del archivo .dat actual
            value = read_value_from_dat_file(file_path)

            # Escribir el valor en el archivo de salida
            output.write(f"{value} ")

    print("Proceso completado. Los valores han sido guardados en 'output.dat'.")

if __name__ == "__main__":
     main()
