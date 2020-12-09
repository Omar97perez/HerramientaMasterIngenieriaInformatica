<template>
  <div>
    <section class="intro-single">
      <div class="container">
        <div class="row">
          <div class="col-md-12 col-lg-8">
            <div class="title-single-box">
              <h1 class="title-single">Investigaciones</h1>
            </div>
          </div>
        </div>

        <div class="row mt-5">
          <div class="card col-md-4 col-s-12" style="border: 1px solid #343a40!important">
            <img class="card-img-top" src="/img/futbol.jpeg" alt="Card image cap">
            <div class="card-body">
              <h5 class="card-title">Previsión de fútbol</h5>
              <p class="card-text">Investigación sobre la posible previsión de la posición de un equipo sabiendo algunos partidos jugados.</p>
              <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <router-link :to="{ name: 'InvestigacionFutbol' }" >
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