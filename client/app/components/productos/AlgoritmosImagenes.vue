<template>
  <div>
      <!-- Modal Métodos -->
      <div class="modal fade" id="ModalEjecutarMetodo" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
          <div class="modal-content">
              <div class="modal-header">
              <h3 class="modal-title" id="TitleMethod"></h3>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
              </button>
              </div>
              <div class="modal-body" align="center">
                  <form id="ModalMetodo"></form>
                  <form class="mt-3" align="left">
                      <label class="font-weight-bold">Archivo</label>
                  </form>
                  <input type="file" id="fileExecuteMethod">
              </div>
                  <div class="modal-footer">
                  <button type="button" class="btn btn-dark" @click="DescargarFicheroPrueba()">Descargar Archivo Prueba</button>
                  <button type="button" class="btn btn-primary" data-dismiss="modal" @click="EjecutarAlgoritmo()">Enviar</button>
                  <button type="button" class="btn btn-danger" data-dismiss="modal">Cerrar</button>
              </div>
          </div>
          </div>
      </div>

      <!-- Modal Cargar Imagen -->
      <div class="modal fade bd-example-modal-lg" id="ModalCargaImagen" role="dialog" aria-labelledby="exampleModalLabel">
          <div class="modal-dialog modal-lg" role="document">
              <div class="modal-content">
                  <div class="modal-header">
                      <h3 class="modal-title" id="exampleModalLabel">Visualizar Imagen</h3>
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                      </button>
                  </div>
                  <div class="modal-body" >
                      <div class="d-flex justify-content-center">
                          <div class="spinner-border" role="status">
                              <span class="sr-only">Loading...</span>
                          </div>
                      </div>
                  </div>
                  <div class="modal-footer">
                      <button type="button" class="btn btn-danger" data-dismiss="modal">Cerrar</button>
                  </div>
              </div>
          </div>
      </div>

      <!-- Modal Ver Imágenes -->
      <div class="modal fade bd-example-modal-lg" id="ModalVerImagen" role="dialog" aria-labelledby="exampleModalLabel">
          <div class="modal-dialog modal-lg" role="document">
              <div class="modal-content">
                  <div class="modal-header">
                      <h3 class="modal-title" id="exampleModalLabel">Visualizar Imagen</h3>
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                      </button>
                  </div>
                  <div class="modal-body" align="center">
                      <h4 id="TimeEjecution"></h4>
                      <img class="img-fluid mt-3" id="myimage"/>
                  </div>
                  <div class="modal-footer">
                      <button type="button" class="btn btn-primary" id="prueba" rel="myimage" @click="DescargarImagen()">Descargar</button>
                      <button type="button" class="btn btn-danger" data-dismiss="modal">Cerrar</button>
                  </div>
              </div>
          </div>
      </div>
      

    <section class="intro-single">
      <div class="container">
        <div class="row">
          <div class="col-md-12 col-lg-8">
            <div class="title-single-box">
              <h1 class="title-single">Algoritmos</h1>
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="container">
      <form class="form-a">
        <div class="row">
          <div class="col-md-12 mb-2">
            <div class="form-group">
              <label for="Type">¿Qué buscas?</label>
              <input type="text" class="form-control form-control-lg form-control-a" placeholder="Introduzca el nombre del algoritmo a buscar" v-model="busqueda" name="buscar" value="buscar" @keyup="buscarProducto()" @click="pagination(1)">
            </div>
          </div>
        </div>
      </form>
    </div>

    <section class="property-grid grid">
      <div class="container">
          <div id="method" class="mt-5 row text-center" align="center">
            <div  v-for="Producto of Productos" class="col-lg-3 col-s-6 card border-dark mb-4 box-shadow ml-5">
                <div class="card-header">
                  <h4 class="my-0 font-weight-normal">{{Producto.Name}}</h4>
                </div>
                <div class="card-body">
                  <p>{{Producto.Description}}</p>
                  <button type="button" data-toggle="modal" data-target="#ModalEjecutarMetodo" class="btn btn-lg btn-block btn-dark" @click="CargarFormulario(Producto.Name)">Ejecutar</button>
                </div>
            </div>

          </div>


        <div class="row">
          <div class="col-sm-12">
            <nav class="pagination-a">
              <ul class="pagination justify-content-end">
                <li class="page-item" @click="pagination(1)">
                  <p class="page-link tipo-1" href="#" tabindex="-1">
                    <span class="ion-ios-arrow-back"></span>
                    <span class="ion-ios-arrow-back"></span>
                  </p>
                </li>
                <li class="page-item" @click="cambioanterior">
                  <p class="page-link tipo-1" href="#" tabindex="-1">
                    <span class="ion-ios-arrow-back"></span>
                  </p>
                </li>
                <div v-for="Num in NumPaginas()" >
                  <li  class="page-item">
                      <p class="page-link tipo-1" @click="pagination(Num)">{{Num}}</p>
                  </li>
                </div>
                <li class="page-item" @click="cambiosiguiente">
                  <p class="page-link tipo-1" href="#">
                    <span class="ion-ios-arrow-forward"></span>
                  </p>
                </li>
                <li class="page-item" @click="cambioultima">
                  <p class="page-link tipo-1" href="#">
                    <span class="ion-ios-arrow-forward"></span>
                    <span class="ion-ios-arrow-forward"></span>
                  </p>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>


<script>
import axios from 'axios';
class Buscador {
  constructor(busqueda = '',tipo = '',ciudad = '') {
    this.busqueda = busqueda;
  }
}
export default {
  name: 'clases',
  data() {
    return {
      Productos: [],
      Buscador: new Buscador(),
      busqueda: '',
      ProductosPaginacion: [],
      Paginacion: [],
      ciudad: '',
      numeropagina: 1,
      tampagina: '6',
      numero: '',
      tipo:'clases',
      titleMethod:''
    }
  },
  created() {
    this.getProductos();
    this.NumPaginas();
  },
  methods: {
    getProductos() {
      fetch('http://localhost:3000/api/Get/AlgoritmosImagenes/Methods')
        .then(res => res.json())
        .then(data => {
          this.Paginacion = data["Methods"];
          console.log(this.Paginacion)
          this.Productos = this.Paginacion.slice(0,this.tampagina);
        });
    },
    addToPrev(invId) {
      this.$store.dispatch('addToPrev', invId);
    },
    NumPaginas() {
      this.numero = Math.ceil(this.Paginacion.length/this.tampagina);
      return this.numero;
    },
    cambiosiguiente() {
      if(this.numeropagina < this.numero ){
        this.pagination(this.numeropagina + 1);
      }
    },
    cambioanterior() {
      if(this.numeropagina > 1 ){
        this.pagination(this.numeropagina - 1);
      }
    },
    cambioultima() {
      console.log(this.numero );
      this.pagination(this.numero);
    },
    pagination(numpag) {
      this.numeropagina = numpag
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
    },
    buscarProducto() {
      this.ProductosPaginacion = this.Paginacion.filter(Producto => Producto.Name.toUpperCase().includes(this.busqueda.toUpperCase()));
      this.buscador_pagination(this.ProductosPaginacion);
    },
    CargarFormulario(title){
      this.titleMethod = title;
      var position = this.Paginacion.findIndex(method => method.Name === title);
      document.getElementById('TitleMethod').innerHTML = this.Paginacion[position].Name;
      document.getElementById('ModalMetodo').innerHTML = "";
      for (var x=0;x<(Object.keys(this.Paginacion[position].Elements).length);x++) { 
          document.getElementById('ModalMetodo').innerHTML += '<div class="mt-3 form-group" align="left"><label class="font-weight-bold" for="exampleInputEmail1">'+ this.Paginacion[position].Elements[x].Name + "2" + '</label><div class="input-group mb-3"><input type="text" name="' + this.Paginacion[position].Elements[x].Name + '" id="' + this.Paginacion[position].Elements[x].Name + "2" + '" value="' + this.Paginacion[position].Elements[x].value + '" class="form-control"> <div class="input-group-append"><button class="btn btn-outline-primary" type="button" data-toggle="collapse" href="#'+ this.Paginacion[position].Elements[x].Name +'" role="button" aria-expanded="false" aria-controls="collapseExample"><i class="fa fa-question-circle" aria-hidden="true"></i></button></div></div><small id="emailHelp" class="form-text text-muted">'+ this.Paginacion[position].Elements[x].DescriptionShort +'</small></div> <div class="collapse" id="' + this.Paginacion[position].Elements[x].Name +'"><div class="card card-body">'+ this.Paginacion[position].Elements[x].DescriptionLong +'</div></div>';
      }
    },
    Endrefresh()
    {
        document.getElementById("loading").className = "";
        location.reload(true);
    },
    EjecutarAlgoritmo(){
      $("#ModalCargaImagen").modal();
      var position = this.Paginacion.findIndex(method => method.Name === this.titleMethod);
      var elements = "";
      for (var x=0;x<(Object.keys(this.Paginacion[position].Elements).length);x++) { 
          if(x != 0){
              elements +=  "-";
          }
          elements += document.getElementById(this.Paginacion[position].Elements[x]["Name"] + "2").value;
      }

      var urlPostMetodo = "";

      if(elements == ""){
          urlPostMetodo = 'http://localhost:3000/api/Execute/Method/AlgorithmImages/' + this.titleMethod + '/' + "no";
      }
      else{
          urlPostMetodo = 'http://localhost:3000/api/Execute/Method/AlgorithmImages/' + this.titleMethod + '/' + elements;
      }
      var formData = new FormData();
      formData.append("file", document.getElementById("fileExecuteMethod").files[0]);

      $.ajax({
          url: urlPostMetodo,
          type: "POST",
          data: formData,
          processData: false,
          contentType: false,
          success: function(response) {
            console.log()
              $("#ModalCargaImagen").modal('hide');
              $('body').removeClass('modal-open');
              $('.modal-backdrop').remove();
              var responseImage = response[0].split(".");
              document.getElementById('myimage').src = 'http://localhost:3000/api/Get/file/' + responseImage[0] + ".png";
              document.getElementById('TimeEjecution').innerHTML =  "Tiempo de ejecución: " + response[1] + " segundos";
              
              $('body').removeClass('ModalCargaImagen');
              $("#ModalVerImagen").modal();
          },
          error: function(jqXHR, textStatus, errorMessage) {
              console.log(errorMessage); 
          }
      });
    },
    DescargarImagen() {
        var nameHC = document.getElementById('myimage');
        var link = document.createElement("a");
        link.download = "image.png";
        link.href = nameHC.src;
        link.click();
    },
    DescargarFicheroPrueba() 
    {
      var link = document.createElement("a");
      var position = this.Paginacion.findIndex(method => method.Name === this.titleMethod);
      link.download = this.Paginacion[position].file;
      link.href = "http://localhost:3000/api/Get/file/" + this.Paginacion[position].file;
      link.click();
    }
  },
};
</script>