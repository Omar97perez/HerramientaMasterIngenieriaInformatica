runTomeCanoUser:
	python3 main.py ./Datos/TomeCano.csv 1
runTomeCanoServer:
	python3 main.py ./Datos/TomeCano.csv 0 1 0 12 1,1,2010,1.00,12.00,5.00,31.00,56.00,0.4,2.00,3.00,2.00 ./Datos/ 
runResultadosSinEspaciosServer:
	python3 main.py ./Datos/final.csv 0 1 2 32 32 1,0,1,0,0,0,0,2,0,0,2,0,0,2,0,2,0,0,2,1,0,2,1,0,0,0,0,0,0,1 ./Datos/
runResultadosSinEspaciosServer10Partidos:
	python3 main.py ./Datos/final.csv 0 1 2 12 32 1,0,1,0,0,0,0,2,0,0 ./Datos/
all:
	ls
run:
	python3 main.py $(file) 0 $(tipoGrafica) $(columnaSeleccionadaInicial) $(columnaSeleccionadaFinal) $(columnaSeleccionada) $(datos) $(fileExit)