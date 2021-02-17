#include <iostream>
#include <vector>
#include <assert.h>
#include <cmath>
#include <png++/png.hpp>
#include "mpi.h"
#include "stdio.h"
#include "string.h"
#include <string>
#include <sstream>
#include <chrono>

using namespace std;

typedef vector<double> Array;
typedef vector<Array> Matrix;
typedef vector<Matrix> Image;

Matrix getGaussian(int height, int width, double sigma)
{
    Matrix kernel(height, Array(width));
    double sum = 0.0;
    int i, j;

    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            kernel[i][j] = exp(-(i * i + j * j) / (2 * sigma * sigma)) / (2 * M_PI * sigma * sigma);
            sum += kernel[i][j];
        }
    }

    for (i = 0; i < height; i++)
    {
        for (j = 0; j < width; j++)
        {
            kernel[i][j] /= sum;
        }
    }

    return kernel;
}

// Funcion que nos permite cargar la imagen.
Image loadImage(string filename)
{
    png::image<png::rgb_pixel> image(filename);
    Image imageMatrix(3, Matrix(image.get_height(), Array(image.get_width())));

    int h, w;
    for (h = 0; h < image.get_height(); h++)
    {
        for (w = 0; w < image.get_width(); w++)
        {
            imageMatrix[0][h][w] = image[h][w].red;
            imageMatrix[1][h][w] = image[h][w].green;
            imageMatrix[2][h][w] = image[h][w].blue;
        }
    }

    return imageMatrix;
}

// Funcion que nos permite guardar la Imagen Final.
void saveImage(Image &image, string filename)
{
    assert(image.size() == 3);

    int height = image[0].size();
    int width = image[0][0].size();
    int x, y;

    png::image<png::rgb_pixel> imageFile(width, height);

    for (y = 0; y < height; y++)
    {
        for (x = 0; x < width; x++)
        {
            imageFile[y][x].red = image[0][y][x];
            imageFile[y][x].green = image[1][y][x];
            imageFile[y][x].blue = image[2][y][x];
        }
    }
    imageFile.write(filename);
}

// Funcin que aplica un filtro dado un un tamaño inicial y final. Además, solo devuelve ese trozo calculado.
Image applyFilter(Image &image, Matrix &filter, int initHeight)
{
    assert(image.size() == 3 && filter.size() != 0);

    int heightFinal = image[0].size() + 1 - initHeight;

    int height = image[0].size();
    int width = image[0][0].size();
    int filterHeight = filter.size();
    int filterWidth = filter[0].size();
    int newImageHeight = height - filterHeight;
    int newImageWidth = width - filterWidth;

    Image newImage(3, Matrix(heightFinal, Array(newImageWidth)));

    int x = 0;

    for (int d = 0; d < 3; d++)
    {
        for (int i = initHeight; i < newImageHeight; i++)
        {
            for (int j = 0; j < newImageWidth; j++)
            {
                for (int h = i; h < i + filterHeight; h++)
                {
                    for (int w = j; w < j + filterWidth; w++)
                    {
                        newImage[d][x][j] += filter[h - i][w - j] * image[d][h][w];
                    }
                }
            }
            x++;
        }
        x = 0;
    }
    return newImage;
}

Image applyFilter(Image &image, Matrix &filter){
    assert(image.size()==3 && filter.size()!=0);

    int height = image[0].size();
    int width = image[0][0].size();
    int filterHeight = filter.size();
    int filterWidth = filter[0].size();
    int newImageHeight = height - filterHeight + 1;
    int newImageWidth = width - filterWidth + 1;
    int d,i,j,h,w;

    Image newImage(3, Matrix(newImageHeight, Array(newImageWidth)));

    for (d=0 ; d<3 ; d++) {
        for (i=0 ; i<newImageHeight ; i++) {
            for (j=0 ; j<newImageWidth ; j++) {
                for (h=i ; h<i+filterHeight ; h++) {
                    for (w=j ; w<j+filterWidth ; w++) {
                        newImage[d][i][j] += filter[h-i][w-j]*image[d][h][w];
                    }
                }
            }
        }
    }

    return newImage;
}

// Funcion que nos permite unificar dos imagenes
Image joinImage(Image &image1, Image &image2)
{

    assert(image1.size() == 3);
    assert(image2.size() == 3);

    int height = image1[0].size() + image2[0].size();
    int width = image1[0][0].size();

    Image newImage(3, Matrix(height, Array(width)));

    for (int d = 0; d < 3; d++)
    {
        for (int i = 0; i < height; i++)
        {
            for (int j = 0; j < width; j++)
            {
                if (i < image1[0].size())
                {
                    newImage[d][i][j] += image1[d][i][j];
                }
                else
                {
                    newImage[d][i][j] += image2[d][i - image1[0].size()][j];
                }
            }
        }
    }

    return newImage;
}

int main(int argc, char **argv)
{
    // int rank, size, tag, rc;
    // MPI_Status status;

    // auto t1 = std::chrono::high_resolution_clock::now();

    // // Inicializa la estructura de comunicación de MPI entre los procesos.
    // rc = MPI_Init(&argc, &argv);
    // // Determina el tamaño del grupo asociado con un comunicador
    // rc = MPI_Comm_size(MPI_COMM_WORLD, &size);
    // // Determina el rango (identificador) del proceso que lo llama dentro del comunicador seleccionado.
    // rc = MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    // tag = 100;

    // // Calculamos los valores del filtro deseado
    // Matrix filter = getGaussian(4, 4, 10.0);

    // int userHeight = atoi(argv[2]);
    // int userWidth = atoi(argv[3]);
    // int newImageHeightNode = userHeight / size;

    // if (rank == 0)
    // {
    //     // Cargamos la iamagen
    //     Image image = loadImage(argv[1]);

    //     if(userHeight != image[0].size() || userWidth != image[0][0].size())
    //     {
    //         cout << "Los tamaños son incorectos. Altura = " << image[0].size() << " Anchura= " << image[0][0].size() << endl;
    //         exit(0);
    //     }

    //     // Calculamos los valores necesarios para poder aplicar el filtrado
    //     int newImageHeightNode = userHeight/size;

    //     // Enviamos la sección de la imagen a todos los procesos
    //     int firstHeight = 0;
    //     int finalHeight = 0;
    //     for(int n = 1; n < size; n++){
    //         finalHeight = newImageHeightNode * n;
    //         for (int j = 0; j < 3; j++){
    //             for (int i = firstHeight; i < finalHeight; i++){
    //                 rc = MPI_Send(&image[j][i][0], userWidth, MPI_DOUBLE, n, tag, MPI_COMM_WORLD);
    //             }
    //         }
    //         firstHeight += newImageHeightNode;
    //     }

    //     // El proceso actual aplica el filtro
    //     Image imageNodo0 = applyFilter(image, filter, finalHeight);

    //     Image finalImage;

    //     // Calculamos los el tamaño de los valores que nos bva a envíar cada proceso
    //     int recvImageHeight = newImageHeightNode - filter.size() + 1;
    //     int newImageWidth = image[0][0].size() - filter[0].size() + 1;

    //     // Recogemos los valores y unificamos la Imagen
    //     for(int n = 1; n < size; n++){
    //         Image newImageNode(3, Matrix(recvImageHeight, Array(newImageWidth)));
    //         for (int j = 0; j < 3; j++){
    //             for (int i = 0; i < recvImageHeight; i++){
    //                 rc = MPI_Recv(&newImageNode[j][i][0], newImageWidth, MPI_DOUBLE, n, tag, MPI_COMM_WORLD, &status);
    //             }
    //         }
    //         if(n == 1)
    //         {
    //             finalImage = newImageNode;
    //         }
    //         else
    //         {
    //             finalImage = joinImage(finalImage,newImageNode);
    //         }
    //     }

    //     // Unimos la Imagen del nodo principal
    //     finalImage = joinImage(finalImage,imageNodo0);

    //     // Guardamos la Imagen

    //     // Generamos el nombre del fichero 
    //     stringstream ss;
    //     ss << argv[4];
    //     string str = ss.str();
    //     string ficheroGuardar = str;

    //     saveImage(finalImage, ficheroGuardar);

    //     auto t2 = std::chrono::high_resolution_clock::now();

	//     auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
	//     std::cout << "Tiempo de ejecucion final: " << (float) (duration / 1000.0) << " sec" << std::endl;
    // }
    // else
    // {
    //     // Creamos la Imagen Vacía
    //     Image newImage(3, Matrix(newImageHeightNode, Array(userWidth)));

    //     // Recibimos la Imagen
    //     for (int j = 0; j < 3; j++){
    //         for (int i = 0; i < newImage[0].size(); i++){
    //             rc = MPI_Recv(&newImage[j][i][0], newImage[0][0].size(), MPI_DOUBLE, 0, tag, MPI_COMM_WORLD, &status);
    //         }
    //     }

    //     // Aplicamos el filtrado
    //     Image finalImage = applyFilter(newImage, filter);

    //     // Reenviamos al nodo 0
    //     for (int j = 0; j < 3; j++){
    //         for (int i = 0; i < finalImage[0].size(); i++){
    //             rc = MPI_Send(&finalImage[j][i][0], finalImage[0][0].size(), MPI_DOUBLE, 0, tag, MPI_COMM_WORLD);
    //         }
    //     }
    // }

    // MPI_Barrier(MPI_COMM_WORLD);
    // // Finaliza la comunicación paralela entre los procesos
    // rc = MPI_Finalize();
    // exit(0);

    cout << "Hello World"<< endl;
    exit(0);
}
