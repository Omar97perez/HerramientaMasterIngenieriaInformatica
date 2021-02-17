#include <iostream>
#include <vector>
#include <assert.h>
#include <cmath>
#include <png++/png.hpp>
#include "stdio.h"
#include "string.h"
#include <string>
#include <sstream>
#include <chrono>
#include <omp.h>

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
Image applyFilter(Image &image, Matrix &filter, int numThreads)
{
    assert(image.size() == 3 && filter.size() != 0);

    int height = image[0].size();
    int width = image[0][0].size();
    int filterHeight = filter.size();
    int filterWidth = filter[0].size();
    int newImageHeight = height - filterHeight + 1;
    int newImageWidth = width - filterWidth + 1;

    Image newImage(3, Matrix(newImageHeight, Array(newImageWidth)));

    int x = 0;
    const int a = 1;
    const int b = 3;

    for (int d = 0; d < 3; d++)
    {
        #pragma omp parallel for num_threads(numThreads)
        for (int i = 0; i < newImageHeight; i++)
        {
            for (int j = 0; j < newImageWidth; j++)
            {
                for (int h = i; h < i + filterHeight; h++)
                {
                    for (int w = j; w < j + filterWidth; w++)
                    {
                        newImage[d][i][j] += filter[h - i][w - j] * image[d][h][w];
                    }
                }
            }
        }
    }

    return newImage;
}

int main(int argc, char **argv)
{
    // int rank, size, tag, rc;
    // char message[20];

    // auto t1 = std::chrono::high_resolution_clock::now();

    // // Calculamos los valores del filtro deseado
    // Matrix filter = getGaussian(10, 10, 50.0);

    // // Cargamos la iamagen
    // Image image = loadImage(argv[1]);

    // // Calculamos los valores necesarios para poder aplicart el filtrado
    // int height = image[0].size();
    // int width = image[0][0].size();
    // int filterHeight = filter.size();
    // int filterWidth = filter[0].size();
    // //Mostramos los valores del filtrado
    // cout << endl;
    // cout << "--- Información de la Imagen---" << endl;
    // cout << "height: " << height << endl;
    // cout << "width: " << width << endl;
    // cout << "filterHeight: " << filterHeight << endl;
    // cout << "filterWidth: " << filterWidth << endl;
    // cout << endl;

    // cout << "Cargando..." << endl;
	
    // // Generamos el nombre del fichero 
    // stringstream ss;
    // ss << argv[3];
    // string str = ss.str();
    // string ficheroGuardar = str;

    // Image newImage = applyFilter(image, filter, atoi(argv[2]));
    // saveImage(newImage, ficheroGuardar);

    // auto t2 = std::chrono::high_resolution_clock::now();

    // auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(t2 - t1).count();
    // std::cout << "Tiempo de ejecucion: " << (float) (duration / 1000.0) << " sec" << std::endl;


    std::cout << "Hello World:" << std::endl;
}
