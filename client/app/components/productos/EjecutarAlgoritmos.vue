<template>
  <div>
    <section class="intro-single">
      <div class="container">
        <div class="row">
          <div class="col-md-12 col-lg-8">
            <div class="title-single-box">
              <h1 class="title-single">Algoritmos</h1>
            </div>
          </div>
        </div>

        <div class="card-deck mt-5">
          <div class="card" style="border: 1px solid #343a40!important">
            <img class="card-img-top" src="/img/ScikitLearn.png" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title">Scikit Learn</h5>
              <p class="card-text">Use la librería de Scikit Learn en la nube.</p>
              <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <router-link :to="{ name: 'ScikitLearn' }" >
                    <button class="btn btn-dark">Acceder</button>
                  </router-link>
              </div>
            </div>
          </div>
          <div class="card" style="border: 1px solid #343a40!important">
            <img class="card-img-top" src="/img/OpenMP.jpg" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title">OpenMP</h5>
              <p class="card-text">Use la librería de Scikit Learn junto con OpenMP en la nube.</p>
              <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <router-link :to="{ name: 'OpenMP' }" >
                    <button class="btn btn-dark">Acceder</button>
                  </router-link>
              </div>
            </div>
          </div>
          <div class="card" style="border: 1px solid #343a40!important">
            <img class="card-img-top" src="/img/Spark.jpeg" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title">Spark</h5>
              <p class="card-text">Use Spark estadístico en la nube.</p>
              <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <router-link :to="{ name: 'Spark' }" >
                    <button class="btn btn-dark">Acceder</button>
                  </router-link>
              </div>
            </div>
          </div>
        </div>
        
      </div>
    </section>


  </div>
</template>


<script>
</script>