<template>
  <div class="container ">
    
    <div class="row mt-50">
      <div class="col-sm">
        <h1>Generos</h1>
      </div>
      <div class="col-sm d-flex justify-content-end">
        <b-button size="lg" variant="dark" @click="addNew">Adicionar Novo Genero</b-button>
      </div>
    </div>

    <div class="row mt-50">

       <div class="col-sm d-flex justify-content-start">
        <b-form-group
          label=""
          label-cols-sm="0"
          label-size="sm"
          label-for="filterInput"
          class="mb-0"
        >
          <b-input-group size="sm">
            <b-form-input
              v-model="filter"
              type="search"
              id="filterInput"
              placeholder="Procurar por..."
              :formatter="searchFormatter"
            ></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="filter = ''">Limpar</b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
       </div>


      <div class="col-sm-12 mt-10">
        <b-table
          ref="table"
          striped
          hover
          dark
          small
          :fields="fields"
          :items="items"
          :busy="isBusy"
          :filter="filter"
          selectable 
          select-mode="single"
          @row-selected="handleSelectItem"
          >
            <template v-slot:table-busy>
              <div class="text-center text-danger my-2">
                <b-spinner class="align-middle"></b-spinner>
                <strong>Carregando...</strong>
              </div>
            </template>
        </b-table>
      </div>
    </div>

    <div class="row mt-10">
      <div class="col-sm d-flex justify-content-end">
        <b-pagination
          v-model="currentPage"
          :total-rows="totalItems"
          per-page="10"
          align="fill"
          size="sm"
          @change="changePage"
          :disabled="paginationDisabled"
        ></b-pagination>
      </div>
    </div>

    <div>
      <b-modal 
        ref="modal-crud"
        title="Genero"
        header-bg-variant="dark"
        body-bg-variant="dark"
        footer-bg-variant="dark"
        header-text-variant="light"
        body-text-variant="light"
        @cancel="excluir"
        @hide="cancelar"
        >
      
        <p>{{ (selected.length > 0)? selected[0].first_name:''}}</p>
      
        <template v-slot:modal-footer="{ ok, cancel, hide }">
          <b-button size="sm" variant="success" @click="ok()">
            Salvar
          </b-button>
          <b-button size="sm" variant="danger" @click="cancel()">
            Excluir
          </b-button>
          <b-button size="sm" variant="secondary" @click="hide()">
            Cancelar
          </b-button>
        </template>
      </b-modal>
    </div>

  </div>
</template>

<script>
 import axios from 'axios';

 const API_URL = 'http://localhost:5000/genero'; 

 export default {
    mounted () {
      
      this.isBusy = true;

      axios
      .get(`${API_URL}?max_results=10&page=1`)
      .then(response => {
        this.items = response.data._items
      })
      .catch(error => {
        console.log(error)
      })
      .finally(() => this.isBusy = false)
    },
    data() {
      return {
        fields:['codigo','nome'],
        items: [],
        filter: '',
        isBusy: false,
        selected: [],
        currentPage: 1,
        totalItems: 20,
        paginationDisabled: false 
      }
    },
    methods: {
      searchFormatter(value) {
        console.log("valor da busca",value);
        return value;
      },
      handleSelectItem(item) {
        this.selected = item;
        this.showModal();
      },
      addNew(){
        this.selected = [];
        this.showModal();
      },
      showModal() {
        this.$refs['modal-crud'].show()
      },
      hideModal() {
        this.$refs['modal-crud'].hide()
      },
      salvar(){
        console.log('salvar...');
      },
      excluir(){
        console.log('excluir...');
      },
      cancelar(){
        console.log('cancelar...');
        this.hideModal();
      },
      changePage(page) {
        console.log('Page selected:',page);
      }
    }
  }
</script>

<style>
  .mt-50 {
    margin-top:50px;
  }

  .mt-10 {
    margin-top:10px;
  }
</style>