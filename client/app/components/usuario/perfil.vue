<template>
  <div>
    <!--/ Intro Single star /-->
    <section class="intro-single">
      <div class="container">
        <div class="row">
          <div class="col-md-12 col-lg-8">
            <div class="title-single-box">
              <h1 class="title-single">{{getName}}</h1>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!--/ Intro Single End /-->

    <!--/ Agent Single Star /-->
    <section class="agent-single">
      <div class="container">
        <div class="row">
          <div class="col-sm-12">
            <div class="row">
              <div class="col-md-6">
                <div class="agent-avatar-box">
                  <img src="img/ComingSoon.png" alt="" class="agent-avatar img-fluid">
                </div>
              </div>
              <div class="col-md-5 section-md-t3">
                <div class="agent-info-box">
                  <div class="agent-title">
                    <div class="title-box-d">
                      <h3 class="title-d">{{getName}}
                        <br> {{getSurname}}</h3>
                    </div>
                  </div>
                  <div class="agent-content mb-3">
                    <p class="content-d">{{getParagraph}}</p>
                    <div class="info-agents">
                      <p>
                        <strong>Teléfono: </strong>
                        <span>{{getTelephone}}</span>
                      </p>
                      <p>
                        <strong>Email: </strong>
                        <span>{{getEmail}}</span>
                      </p>
                      <p>
                        <strong>Fecha de Nacimiento: </strong>
                        <span>{{getBirthdate}}</span>
                      </p>
                    </div>
                  </div>
                  <div class="socials-footer">
                    <ul class="list-inline">
                      <li class="list-inline-item">
                        <a href="#" class="link-one">
                          <i class="fab fa-facebook" aria-hidden="true"></i>
                        </a>
                      </li>
                      <li class="list-inline-item">
                        <a href="#" class="link-one">
                          <i class="fab fa-twitter" aria-hidden="true"></i>
                        </a>
                      </li>
                      <li class="list-inline-item">
                        <a href="#" class="link-one">
                          <i class="fab fa-instagram" aria-hidden="true"></i>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!--/ Agent Single End /-->
  </div>
</template>

<script>
export default {
  name: 'ModUsuario',
  data() {
    return {
      name: '',
      surname: '',
      email: '',
      password: '',
      birthdate: '',
      genre: '',
      Productos: [],
      ProductosPaginacion: [],
      Paginacion: [],
      tipo: '',
      numeropagina: 1,
      tampagina: '6',
      numero: '',
    }
  },
  created() {
    this.getProductos(this.$store.getters.email);
    this.NumPaginas();
  },
  methods: {
    getProductos(email) {
      fetch('/api/CosasDeClase/Producto/')
        .then(res => res.json())
        .then(data => {
          this.Paginacion = data.filter(data =>  data.anunciante == email);
          this.Productos = this.Paginacion.slice(0,this.tampagina);
        });
    },
    addToPrev(invId) {
      this.$store.dispatch('addToPrev', invId);
    },
    NumPaginas() {
      this.numero = Math.ceil(this.ProductosPaginacion.length/this.tampagina);
      return this.numero;
    },
    resetpag() {
      this.numeropagina = 1;
    },
    cambiosiguiente() {
      if(this.numeropagina < this.numero ){
          this.numeropagina = this.numeropagina + 1;
      }
    },
    cambioanterior() {
      if(this.numeropagina > 1 ){
          this.numeropagina = this.numeropagina - 1;
      }
    },
    cambioprimera() {
          this.numeropagina = 1;
    },
    cambioultima() {
          this.numeropagina = this.numero;
    },
    pagination(numpag) {
      this.numeropagina = numpag;
      var x;
      x = this.tampagina * numpag;
      numpag = numpag - 1;
      numpag = numpag * this.tampagina;
      this.Productos = this.Paginacion.slice(numpag,x);
    },
    buscador_pagination(vector) {
      var numpag,x;
      numpag = this.numeropagina
      x = this.tampagina * numpag;
      numpag = numpag - 1;
      numpag = numpag * this.tampagina;
      this.Productos = vector.slice(numpag,x);
    }
  },
  computed:  {
    buscarProducto() {
      this.ProductosPaginacion = this.Paginacion.filter(Producto => Producto.tipo.includes(this.tipo));
      this.buscador_pagination(this.ProductosPaginacion);
    },
    getName() {
      return this.$store.getters.name
    },
    getSurname() {
      return this.$store.getters.surname
    },
    getBirthdate() {
      return this.$store.getters.birthdate
    },
    getParagraph() {
      return this.$store.getters.paragraph
    },
    getImage() {
      return this.$store.getters.image
    },
    getTelephone() {
      return this.$store.getters.telephone
    },
    getGenre() {
      return this.$store.getters.genre
    },
    getEmail() {
      return this.$store.getters.email
    }
  }
}
</script>
