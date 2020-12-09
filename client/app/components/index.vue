Productos_clases<template>
  <div>

      <section class="intro-single">
        <div class="intro-carousel">
          <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
            <ol class="carousel-indicators">
              <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
              <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
              <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
            </ol>
            <div class="carousel-inner">
              <div class="carousel-item active">
                <img class="d-block w-100" src="img/slide-1.jpg" alt="First slide">
              </div>
              <div class="carousel-item">
                <img class="d-block w-100" src="img/slide-2.jpg" alt="Second slide">
              </div>
              <div class="carousel-item">
                <img class="d-block w-100" src="img/slide-3.jpg" alt="Third slide">
              </div>
            </div>
            <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="sr-only">Previous</span>
            </a>
            <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="sr-only">Next</span>
            </a>
          </div>
        </div>
      </section>

        <section class="section-services section-t8">
          <div class="container">
            <div class="row">
              <div class="col-md-12">
                <div class="title-wrap d-flex justify-content-between">
                  <div class="title-box">
                    <h2 class="title-a">Nuestros servicios</h2>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-4">
                <div class="card-box-c foo">
                  <div class="card-header-c d-flex">
                    <div class="card-box-ico">
                      <span class="far fa-hand-point-up"></span>                    
                    </div>
                    <div class="card-title-c align-self-center">
                      <h2 class="title-c">Selecciona</h2>
                    </div>
                  </div>
                  <div class="card-body-c">
                    <p class="content-c">
                      Seleccione el modo y el algoritmo a ejecutar.
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card-box-c foo">
                  <div class="card-header-c d-flex">
                    <div class="card-box-ico">
                      <span class="fa fa-clock-o"></span>
                    </div>
                    <div class="card-title-c align-self-center">
                      <h2 class="title-c">Ejecuta</h2>
                    </div>
                  </div>
                  <div class="card-body-c">
                    <p class="content-c">
                      Ejecuta tu algoritmo agregando los parámetros necesarios.
                    </p>
                  </div>
                </div>
              </div>
              <div class="col-md-4">
                <div class="card-box-c foo">
                  <div class="card-header-c d-flex">
                    <div class="card-box-ico">
                      <span class="fa fa-eye"></span>
                    </div>
                    <div class="card-title-c align-self-center">
                      <h2 class="title-c">Observa</h2>
                    </div>
                  </div>
                  <div class="card-body-c">
                    <p class="content-c">
                      Observa el resultado de forma muy sencilla.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section class="section-news section-t8">
          <div class="container">
            <div class="row">
              <div class="col-md-12">
                <div class="title-wrap d-flex justify-content-between">
                  <div class="title-box">
                    <h2 class="title-a">Algoritmos</h2>
                  </div>
                  <div class="title-link" style="color:black!important">
                    <router-link :to="{ name: 'ejecutarAlgoritmo' }" style="color:black!important" >
                      <p >Resto de opciones <span class="ion-ios-arrow-forward"></span></p>
                    </router-link>
                  </div>
                </div>
              </div>
            </div>

              <div class="card-deck">
                <div class="card" style="border: 1px solid #343a40!important">
                  <img class="card-img-top" src="/img/ScikitLearn.png" alt="Card image cap">
                  <div class="card-body">
                    <h5 class="card-title">Scikit Learn</h5>
                    <p class="card-text">Use la librería de Scikit Learn en la nube.</p>
                    <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                      <button class="btn btn-dark">Acceder</button>
                    </div>
                  </div>
                </div>
                <div class="card" style="border: 1px solid #343a40!important">
                  <img class="card-img-top" src="/img/OpenMP.jpg" alt="Card image cap">
                  <div class="card-body">
                    <h5 class="card-title">OpenMP</h5>
                    <p class="card-text">Use la librería de Scikit Learn hybto con OpenMP en la nube.</p>
                    <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                      <button class="btn btn-dark">Acceder</button>
                    </div>
                  </div>
                </div>
                <div class="card" style="border: 1px solid #343a40!important">
                  <img class="card-img-top" src="/img/Spark.jpeg" alt="Card image cap">
                  <div class="card-body">
                    <h5 class="card-title">Spark</h5>
                    <p class="card-text">Use Spark estadísctico en la nube.</p>
                    <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                      <button class="btn btn-dark">Acceder</button>
                    </div>
                  </div>
                </div>
              </div>
          </div>
        </section>
  </div>

</template>

<script></script>