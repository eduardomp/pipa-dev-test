<template>
    <div class="container ">
  
      <div class="row mt-50">
        <div class="col-sm-12">
          <h1 class="titulo">Informações Gerais</h1>
        </div>
        <hr/>
      </div>

      <div class="row mt-50">
        <div class="col-sm-12">
          <h2 class="titulo">Contagem de bandas por país</h2>
        </div>
        <div class="col-sm-12">
          aqui
          <hr>
        </div>
        <hr/>
      </div>

      <div class="row mt-50">
        
        <div class="col-sm-12">
          <h2 class="titulo">Bandas por genero</h2>
        </div>
        
        <div class="col-sm-12">
          <template>
            <b-form-input placeholder="Insira o genero" v-model="genero" list="generos-datalist" debounce="500" @keyup="searchGenero"></b-form-input>

            <datalist id="generos-datalist">
              <option v-for="genero in generos" v-bind:key="genero.value">{{ genero.text }}</option>
            </datalist>

          </template>
          <hr>
        </div>
        
        <div class="col-sm-12">
          <b-table
            ref="table-por-genero"
            striped
            hover
            dark
            small
            :fields="fieldsPorGenero"
            :items="itemsPorGenero"
            :busy="isBusyPorGenero"
            >
              <template v-slot:table-busy>
                <div class="text-center text-danger my-2">
                  <b-spinner class="align-middle"></b-spinner>
                  <strong>Carregando...</strong>
                </div>
              </template>

                <template v-slot:cell(pais)="data">
                  {{ data.item.pais.nome }}
                </template>

          </b-table>
        </div>
        <hr/>
      </div>
      
      <div class="row mt-50">
        <div class="col-sm-12">
          <h2 class="titulo">Bandas por país</h2>
        </div>
        <div class="col-sm-12">
          <template>
            <b-form-input placeholder="Insira o país" v-model="pais" list="paises-datalist" debounce="500" @keyup="searchPais"></b-form-input>

            <datalist id="paises-datalist">
              <option v-for="pais in paises" v-bind:key="pais.value">{{ pais.text }}</option>
            </datalist>

          </template>
          <hr>
        </div>

        <div class="col-sm-12">
          <b-table
            ref="table-por-pais"
            striped
            hover
            dark
            small
            :fields="fieldsPorPais"
            :items="itemsPorPais"
            :busy="isBusyPorPais"
            >
              <template v-slot:table-busy>
                <div class="text-center text-danger my-2">
                  <b-spinner class="align-middle"></b-spinner>
                  <strong>Carregando...</strong>
                </div>
              </template>

                <template v-slot:cell(genero)="data">
                  {{ data.item.genero.nome }}
                </template>

          </b-table>
        </div>
        <hr/>
      </div>
  
    </div>

</template>

<script>
  import axios from 'axios';

  const BASE_URL = `http://${process.env.VUE_APP_API_BASE_URL}:5000`; 
  const GENERO = '/genero';
  const PAIS = '/pais';
  const BANDA = '/banda';

  export default {
   mounted () {
      this.loadGeneros();
      this.loadPaises();
    },
    data() {
      return {
        genero:"",
        pais:"",
        generos:[],
        paises:[],
        itemsPorGenero:[],
        fieldsPorGenero:['codigo','nome','pais'],
        isBusyPorGenero:false,
        itemsPorPais:[],
        fieldsPorPais:['codigo','nome','genero'],
        isBusyPorPais:false
      }
    },
    methods: {
      searchGenero($event) {
          if($event.target.value && $event.target.value.length > 3){
            
            if($event.code === "Enter"){
              this.loadTableGenero();
              return;
            } 

            this.generos = [];

            let term = $event.target.value;
            
            let querystring = `page=1&max_results=30&where={"$or":[{"codigo":"${term}"},{"nome":{"$regex":".*${term}.*","$options":"i"}}]}`;
          
            axios
              .get(`${BASE_URL}${GENERO}?${querystring}`)
              .then(response => {
                response.data._items.forEach(element => {
                  this.generos.push({"value":element._id,"text":element.nome});
                });
              });
          }
      },
      searchPais($event) {
          if($event.target.value && $event.target.value.length > 3){
            
            if($event.code === "Enter"){
              this.loadTablePaises();
              return;
            }
            
            this.paises = [];

            let term = $event.target.value;
            
            let querystring = `page=1&max_results=30&where={"$or":[{"iso":"${term}"},{"nome":{"$regex":".*${term}.*","$options":"i"}}]}`;
          
            axios
              .get(`${BASE_URL}${PAIS}?${querystring}`)
              .then(response => {
                response.data._items.forEach(element => {
                  this.paises.push({"value":element._id,"text":element.nome});
                });
              });
          }
      },
      loadGeneros() {
        axios
        .get(`${BASE_URL}${GENERO}?max_results=1000`)
        .then(response => {
            response.data._items.forEach(element => {
              this.generos.push({"value":element._id,"text":element.nome});  
            });
          })
          .catch(error => {
            console.log(error)
            this.showError(`Erro ao recuperar generos!`)
          })
      },
      loadPaises() {
        axios
        .get(`${BASE_URL}${PAIS}?max_results=1000`)
        .then(response => {
            response.data._items.forEach(element => {
              this.paises.push({"value":element._id,"text":element.nome});  
            });
          })
          .catch(error => {
            console.log(error)
            this.showError(`Erro ao recuperar paises!`)
          })
      },
      loadTablePaises() {
        
        this.isBusyPorPais = true;

        let _pais = this.paises.find(pais => pais.text === this.pais);

        let embedded = `&embedded={"genero":1}`;
        
        let querystring = `&where={"pais":"${_pais.value}"}`

        axios
          .get(`${BASE_URL}${BANDA}?max_results=10${embedded}${querystring}`)
          .then(response => {
            this.itemsPorPais = response.data._items;
          })
          .catch(error => {
            console.log(error)
          })
          .finally(() => {
            this.isBusyPorPais = false;
          })
      },
      loadTableGenero() {
        this.isBusyPorGenero = true;

        let _genero = this.generos.find(genero => genero.text === this.genero);

        let embedded = `&embedded={"pais":1}`;
        
        let querystring = `&where={"genero":"${_genero.value}"}`

        axios
          .get(`${BASE_URL}${BANDA}?max_results=10${embedded}${querystring}`)
          .then(response => {
            this.itemsPorGenero = response.data._items;
          })
          .catch(error => {
            console.log(error)
          })
          .finally(() => {
            this.isBusyPorGenero = false;
          })
      }
    }
  }
</script>

<style>
 .titulo {
  color: orange;
  font-weight: bold;
 }

 hr {
   background-color: whitesmoke;
 }

</style>