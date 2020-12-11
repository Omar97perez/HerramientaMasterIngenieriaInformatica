all: 
	mpic++ -o mpi_Final_version main_final_version.cpp -lpng

run:
	mpiexec  -np 4 ./mpi_Final_version $(file) $(height) $(width) $(fileExit) 
