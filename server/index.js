require('rootpath')()
const express = require('express')
const morgan = require('morgan')
const mongoose = require('mongoose')
const cors = require('cors')
const bodyParser = require('body-parser')
const path = require('path');
const multer = require('multer');
let fs = require('fs');
var request = require('request');
const axios = require('axios')

const app = express();
app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())
app.use(cors())

function executeMake(nameMethod) {
  require('child_process').execSync("sudo make -C ./Algoritmos/" + nameMethod + " all");
}

// Permite Subir Imagenes
let storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, './Archivos')
  },
  filename: (req, file, cb) => {
    cb(null, file.fieldname + '-' + Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({ storage });

//Conexión con la base de datos, cuando se despliegue en servidor  se tendrá que cambiar la dirección
mongoose.connect('mongodb://omar:antonio1997@cluster0-shard-00-00-svm5b.mongodb.net:27017,cluster0-shard-00-01-svm5b.mongodb.net:27017,cluster0-shard-00-02-svm5b.mongodb.net:27017/TrabajoFinalCN?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true')
  .then(db => console.log('DB conectada')) //Imprimir DB conectada en caso de que todo vaya bien
  .catch(err => console.error(err)); //Imprime error si no se puedo conectar

//Ajustes
//Si el servidor tiene puerto lo coge sino pone el puerto 3000
app.set('port', process.env.PORT || 3000);

//Sever escucha en el puerto x te lo muestra por pantalla
app.listen(app.get('port'), () => {
  console.log('Server on port', app.get('port'));
});

// Permite Ejecutar Métodos 
app.post('/api/Execute/Algorithm/:name/:Elements', upload.single('file'), (req, res) => {

  var elementsUrl = req.params.Elements.split("-");

  if (req.file) {
    var fileExit = req.file.filename.split(".");
  }

  fs.readFile("./Metodos.json", 'utf-8', (err2, data) => {
    var methods = JSON.parse(data);
    var element = methods['Methods'].findIndex(method => method.Name === req.params.name);
    var method = methods['Methods'][element];
    //executeMake(method["Name"]);
    var elements = method["Elements"];
    var stringFinal = "";

    if (elementsUrl.length != 1) {
      for (x = 0; x < elementsUrl.length; x++) {
        stringFinal += " " + elements[x]["Name"] + "=" + elementsUrl[x];
      }
    }

    
    console.log("make -C ./Algoritmos/" + req.params.name + " file=../../Archivos/" + req.file.filename + " fileExit=../../Archivos/" + fileExit[0] + ".png " + stringFinal + " run")
    var start = Date.now();
    const exec = require('child_process').exec;
    exec("make -C ./Algoritmos/" + req.params.name + " file=../../Archivos/" + req.file.filename + " fileExit=../../Archivos/" + fileExit[0] + ".png " + stringFinal + " run", (err, stdout, stderr) => {
      var final = (Date.now() - start) / 1000;
      res.send([req.file.filename, String(final).replace(".",",")]);
    });

  });
});

// Permite recoger Imágenes 
app.get('/api/Get/file/:name', (req, res) => {
  res.sendFile('./Archivos/' + req.params.name, { root: __dirname });
});

// Permite devolver El archivo con todos los Métodos
app.get('/api/Get/Methods', function (req, res) {
  res.sendFile('./Metodos.json', { root: __dirname });
});

//Middlewares
  //Sirve para imprimir las peticiones Get de la consola
  app.use(morgan('dev'));
  //Body-parser viene integrado con express (sirve para trabajar con los json)
  app.use(express.json());

  //Ficheros estáticos, coge el index.html dentro de public
  app.use(express.static(__dirname + '/public'));

  // Permite devolver El archivo con todos los Métodos
  app.get('/api/Get/AlgoritmosImagenes/Methods', function(req, res) {
    res.sendFile('./MetodosImagenes.json', { root: __dirname });
  });
  
  // Permite Ejecutar Métodos 
  app.post('/api/Execute/Method/AlgorithmImages/:name/:Elements', upload.single('file'), (req, res) => {
    
    var elementsUrl = req.params.Elements.split("-");
    var fileExit = req.file.filename.split(".");

    fs.readFile("./MetodosImagenes.json", 'utf-8', (err2, data) => {
      var methods = JSON.parse(data);
      var element = methods['Methods'].findIndex(method => method.Name === req.params.name);
      var method = methods['Methods'][element];
      executeMake(method["Name"]);	
      var elements = method["Elements"];
      var stringFinal = "";

      if (elementsUrl.length != 1){
        for(x =0; x < elementsUrl.length; x++){
          stringFinal += " " + elements[x]["Name"] + "=" + elementsUrl[x];
        }	
      }

      var start = Date.now();
      console.log("make -C ./Algoritmos/" + req.params.name + " file=../../Archivos/"+ req.file.filename + " fileExit=../../Archivos/" + fileExit[0] + ".png " + stringFinal + " run");
      const exec = require('child_process').exec;
      exec("make -C ./Algoritmos/" + req.params.name + " file=../../Archivos/"+ req.file.filename + " fileExit=../../Archivos/" + fileExit[0] + ".png " + stringFinal + " run", (err, stdout, stderr) => {
        var final = (Date.now() - start) / 1000;
        res.send([req.file.filename, String(final).replace(".",",")]);
      });
    });	
  });