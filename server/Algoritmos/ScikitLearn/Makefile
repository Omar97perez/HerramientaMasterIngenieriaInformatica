runTomeCanoUser1:
	python3 Programa.py ./Data/TomeCano1.csv 1 
runTomeCanoUser2:
	python3 Programa.py ./Data/TomeCano2.csv 1 
runTomeCanoUser3:
	python3 Programa.py ./Data/TomeCano3.csv 1 
runTomeCanoServerBR:
	python3 Programa.py ./Data/TomeCano.csv 0 1 1 12 ./FinalImage_BR.png
runTomeCanoServerDTR:
	python3 Programa.py ./Data/TomeCano.csv 0 6 1 12 ./FinalImage_DTR.png
runTomeCanoServerMS:
	python3 Programa.py ./Data/TomeCano.csv 0 3 4 6 ./FinalImage_MS.png
all:
	ls
run:
	python3 Programa.py $(file) 0 $(tipoGrafica) $(columnaSeleccionadaInicial) $(columnaSeleccionada) $(fileExit)