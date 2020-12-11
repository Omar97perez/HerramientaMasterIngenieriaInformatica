all: 
	mpic++ -o mpi_Final_version main_final_version.cpp -lpng

run:
	mpiexec --allow-run-as-root -np 4 ./mpi_Final_version $(file) $(height) $(width) $(fileExit) 
