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
              <h1 class="title-single">OpenMp</h1>
            </div>
          </div>
        </div>

        <div class="mt-5" align="center">
          <h2><strong>Clasificación</strong></h2>
        </div>

        <div class="row ">

          <div class="col-md-4 col-s-12 mt-5">
            <div class="card " style="border: 1px solid #343a40!important">
              <img class="card-img-top" src="/img/DesicionTreeRegression.png" alt="Card image cap">
              <div class="card-body">
                <h5 class="card-title">Árbol de decisión</h5>
                <p class="card-text">Use el clasificador  denominado "Árbol de decisión" para sus datos.</p>
                <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Decision Tree Regression',2)">Acceder</button>
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-4 col-s-12 mt-5">
            <div class="card" style="border: 1px solid #343a40!important">
              <img class="card-img-top" src="/img/ClasificadorBayesiano.jpeg" alt="Card image cap">
              <div class="card-body">
                <h5 class="card-title">Clasificación Bayesiana</h5>
                <p class="card-text">Use el clasificador Bayesiano para sus datos.</p>
                <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Clasificación Bayesiana',1)">Acceder</button>
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-4 col-s-12 mt-5">
            <div class="card" style="border: 1px solid #343a40!important">
              <img class="card-img-top" src="/img/GaussianProcessClassifier.png" alt="Card image cap">
              <div class="card-body">
                <h5 class="card-title">Clasificador Gausiano</h5>
                <p class="card-text">Use el clasificador Gausiano para sus datos.</p>
                <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Clasificación Bayesiana',12)">Acceder</button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="mt-5" align="center">
          <h2><strong>Regresión</strong></h2>
        </div>

        <div class="row mb-5">
          <div class="col-md-4 col-s-12 mt-5">
              <div class="card" style="border: 1px solid #343a40!important">
                <img class="card-img-top" src="/img/RegresionLinear.jpg" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">Regresión Lineal</h5>
                  <p class="card-text">Use una regresión basada en Regresión Lineal para sus datos.</p>
                  <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                    <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Regresión Lineal',4)">Acceder</button>
                  </div>
                </div>
              </div>
          </div>



          <div class="col-md-4 col-s-12 mt-5">
            <div class="card" style="border: 1px solid #343a40!important">
              <img class="card-img-top" src="/img/RandomForestRegressor.png" alt="Card image cap">
              <div class="card-body">
                <h5 class="card-title">Random Forest Regressor</h5>
                <p class="card-text">Use una regresión basada en "Random Forest Regressor" para sus datos.</p>
                <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Random Forest Regressor',5)">Acceder</button>
                </div>
              </div>
            </div>
          </div>



          <div class="col-md-4 col-s-12 mt-5">
            <div class="card" style="border: 1px solid #343a40!important">
              <img class="card-img-top" src="/img/RedNeuronal.jpg" alt="Card image cap">
              <div class="card-body">
                <h5 class="card-title">Red Neuronal</h5>
                <p class="card-text">Use una regresión basada en  una Red Neural para sus datos.</p>
                <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Red Neural',6)">Acceder</button>
                </div>
              </div>
            </div>
          </div>

        </div>

        <div class="mt-5" align="center">
          <h2><strong>Clustering</strong></h2>
        </div>

        <div class="row mb-5">
          <div class="col-md-4 col-s-12 mt-5">
            <div class="card" style="border: 1px solid #343a40!important">
              <img class="card-img-top" src="/img/Mean-Shift.png" alt="Card image cap">
              <div class="card-body">
                <h5 class="card-title">Mean Shift</h5>
                <p class="card-text">Use el algoritmo e clustering denominado "Mean Shift" para sus datos.</p>
                <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Mean Shift',3)">Acceder</button>
                </div>
              </div>
            </div>
          </div>
            <div class="col-md-4 col-s-12 mt-5">
              <div class="card" style="border: 1px solid #343a40!important">
                <img class="card-img-top" src="/img/AgglomerativeClustering.png" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">Agglomerative Clustering</h5>
                  <p class="card-text">Use el algoritmo e clustering denominado "Agglomerative Clustering" para sus datos.</p>
                  <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                    <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Agglomerative Clustering',9)">Acceder</button>
                  </div>
                </div>
              </div>
            </div>

            <div class="col-md-4 col-s-12 mt-5">
              <div class="card" style="border: 1px solid #343a40!important">
                <img class="card-img-top" src="/img/DBSCAN.png" alt="Card image cap">
                <div class="card-body">
                  <h5 class="card-title">DBSCAN</h5>
                  <p class="card-text">Use el algoritmo e clustering denominado "DBSCAN" para sus datos.</p>
                  <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                    <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'DBSCAN',11)">Acceder</button>
                  </div>
                </div>
              </div>
            </div>
        </div>

        <div class="mt-5" align="center">
          <h2><strong>Comparativas</strong></h2>
        </div>

        <div class="row">
          <div class="col-md-4 col-s-12 mt-5">
            <div class="card" style="border: 1px solid #343a40!important">
              <img class="card-img-top" src="/img/Clasificcation.png" alt="Card image cap">
              <div class="card-body">
                <h5 class="card-title">Clasificaciones</h5>
                <p class="card-text">Ejecute una comparativa entre los algoritmos de Clasificación y seleccione el que mejor se adapte a sus datos.</p>
                <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Comparaciones Clasificaciones',8)">Acceder</button>
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-4 col-s-12 mt-5">
            <div class="card" style="border: 1px solid #343a40!important">
              <img class="card-img-top" src="/img/ComparativeRegressions.png" alt="Card image cap">
              <div class="card-body">
                <h5 class="card-title">Regresiones</h5>
                <p class="card-text">Ejecute una comparativa entre los algoritmos de Regresión y seleccione el que mejor se adapte a sus datos.</p>
                <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Comparaciones Regresiones',7)">Acceder</button>
                </div>
              </div>
            </div>
          </div>

          <div class="col-md-4 col-s-12 mt-5">
            <div class="card" style="border: 1px solid #343a40!important">
              <img class="card-img-top" src="/img/ComparacionClustering.png" alt="Card image cap">
              <div class="card-body">
                <h5 class="card-title">Clustering</h5>
                <p class="card-text">Ejecute una comparativa entre los algoritmos de Clustering y seleccione el que mejor se adapte a sus datos.</p>
                <div class="card-footer mt-2" align="center" style="position: relative!important; border-top: 1px solid  #343a40!important;">
                  <button class="btn btn-dark" data-toggle="modal" data-target="#ModalEjecutarMetodo" @click="CargarFormulario('Joblib', 'Comparaciones Clustering',10)">Acceder</button>
                </div>
              </div>
            </div>
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
      ciudad: '',
      tipo:'clases',
      titleMethod:'',
      Paginacion: [],
      elemento:''
    }
  },
  created() {
    this.getProductos();
  },
  methods: {
    getProductos() {
      fetch('/api/Get/Methods')
        .then(res => res.json())
        .then(data => {
          this.Paginacion = data["Methods"];
          this.Productos = this.Paginacion.slice(0,this.tampagina);
        });
    },
    CargarFormulario(title, titleModal, elemento){
      this.elemento = elemento;
      this.titleMethod = title;
      var position = this.Paginacion.findIndex(method => method.Name === title);
      document.getElementById('TitleMethod').innerHTML = titleModal;
      document.getElementById('ModalMetodo').innerHTML = "";
      for (var x=1;x<(Object.keys(this.Paginacion[position].Elements).length);x++) { 
          document.getElementById('ModalMetodo').innerHTML += '<div class="mt-3 form-group" align="left"><label class="font-weight-bold" for="exampleInputEmail1">'+ this.Paginacion[position].Elements[x].NameInput + '</label><div class="input-group mb-3"><input type="text" name="' + this.Paginacion[position].Elements[x].Name + '" id="' + this.Paginacion[position].Elements[x].Name + "2" + '" value="' + this.Paginacion[position].Elements[x].value + '" class="form-control"> <div class="input-group-append"><button class="btn btn-outline-primary" type="button" data-toggle="collapse" href="#'+ this.Paginacion[position].Elements[x].Name +'" role="button" aria-expanded="false" aria-controls="collapseExample"><i class="fa fa-question-circle" aria-hidden="true"></i></button></div></div><small id="emailHelp" class="form-text text-muted">'+ this.Paginacion[position].Elements[x].DescriptionShort +'</small></div> <div class="collapse" id="' + this.Paginacion[position].Elements[x].Name +'"><div class="card card-body">'+ this.Paginacion[position].Elements[x].DescriptionLong +'</div></div>';
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
      elements += this.elemento;

      for (var x=1;x<(Object.keys(this.Paginacion[position].Elements).length);x++) { 
          elements +=  "-";
          elements += document.getElementById(this.Paginacion[position].Elements[x]["Name"] + "2").value;
      }

      var urlPostMetodo = "";

      if(elements == ""){
          urlPostMetodo = '/api/Execute/Algorithm/' + this.titleMethod + '/' + "no";
      }
      else{
          urlPostMetodo = '/api/Execute/Algorithm/' + this.titleMethod + '/' + elements;
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
              $("#ModalCargaImagen").modal('hide');
              $('body').removeClass('modal-open');
              $('.modal-backdrop').remove();
              response = response.split(".");
              document.getElementById('myimage').src = '/api/Get/file/' + response[0] + ".png";
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
      link.href = "/api/Get/file/" + this.Paginacion[position].file;
      link.click();
    }
  },
};
</script>