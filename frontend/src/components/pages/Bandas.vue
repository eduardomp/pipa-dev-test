<template>
  <div class="container ">
    
    <div class="row mt-50">
      <div class="col-sm">
        <h1>Bandas</h1>
      </div>
      <div class="col-sm d-flex justify-content-end">
        <b-button size="lg" variant="dark" @click="addNew">Adicionar Nova Banda</b-button>
      </div>
    </div>

    <div class="row mt-50">

       <div class="col-sm-6 d-flex justify-content-start">
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
              placeholder="Busque por... "
              @keyup="handleSearch"
            ></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!filter" @click="clearSearch">Limpar</b-button>
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
        id="modal-crud"
        title="Banda"
        header-bg-variant="dark"
        body-bg-variant="dark"
        footer-bg-variant="dark"
        header-text-variant="light"
        body-text-variant="light"
        @ok="salvar"
        @cancel="excluir"
        @hide="handleHideModal"
        >
      
          <form id="form-crud">
            <input id="nome" type="text" v-model="nome" placeholder="Insira o nome da banda..."/> 
          </form>
      
        <template v-slot:modal-footer="{ ok, cancel, close }">
          <b-button size="sm" variant="success" @click="ok">
            Salvar
          </b-button>
          <b-button size="sm" variant="danger" @click="cancel">
            Excluir
          </b-button>
          <b-button size="sm" variant="secondary" @click="close">
            Cancelar
          </b-button>
        </template>
      </b-modal>
    </div>

  </div>
</template>

<script>
 import axios from 'axios';

 const API_URL = 'http://localhost:5000/banda'; 

 export default {
    mounted () {
      this.getItemsByPageNumber(1);
    },
    data() {
      return {
        fields:['codigo','nome','genero','pais'],
        items: [],
        filter: '',
        isBusy: false,
        nome:"",
        selected: [{"nome":"","genero":"","pais":""}],
        currentPage: 1,
        totalItems: 0,
        paginationDisabled: false 
      }
    },
    methods: {
      getItems(queryString) {
        this.isBusy = true;

        axios
          .get(`${API_URL}?max_results=10&${queryString}`)
          .then(response => {
            this.items = response.data._items;
            this.totalItems = response.data._meta.total;
          })
          .catch(error => {
            console.log(error)
            this.showError(`Erro ao recuperar bandas!`)
          })
          .finally(() => {
            this.isBusy = false;
            (this.items.length === 0)? this.paginationDisabled = true : this.paginationDisabled = false;
          })
      },
      getItemsByPageNumber(page) {
        this.getItems(`page=${page}`);
        this.currentPage = page;
      },
      clearSearch() {
        this.filter = '';
        this.getItemsByPageNumber(1);  
      },
      handleSearch($event) {
        if($event.code === "Enter"){
          
          if($event.target.value){
            
            let term = $event.target.value;
            
            let querystring = `page=1&max_results=10&where={"$or":[{"codigo":"${term}"},{"nome":{"$regex":".*${term}.*","$options":"i"}}]}`;
          
            this.getItems(querystring);
         
            return;
          }
         
         this.getItemsByPageNumber(1);

        }
      },
      handleSelectItem(item) {
        if(item && item.length > 0){
          this.selected = item;
          this.nome = this.selected[0]?.nome;
          this.genero = this.selected[0]?.genero;
          this.pais = this.selected[0]?.pais;
          this.showModal();
        }
      },
      handleHideModal() {
        this.$refs.table.clearSelected();
      },
      addNew(){
        this.nome = "";
        this.genero = "";
        this.pais =  "";
        this.selected = [];
        this.showModal();
      },
      showModal() {
        this.$bvModal.show("modal-crud");
      },
      salvar(){
        if(this.selected && this.selected.length > 0 && this.selected[0].codigo){
          axios
          .patch(`${API_URL}/${this.selected[0]._id}`,{"nome":this.nome,"genero":this.genero,"pais":this.pais},{headers:{"If-Match":this.selected[0]._etag}})
          .then(response => {
            console.log(response);
            this.showSuccess(`Banda atualizada!`);
          })
          .catch(error => {
            console.log(error)
            this.showError(`Erro ao atualizar!`);
          })
          .finally(() => {
            this.getItemsByPageNumber(1);
          })
 
          return;
        }
        
        axios
          .post(`${API_URL}`,{"nome":this.nome,"genero":this.genero,"pais":this.pais})
          .then(response => {
            console.log(response);
            this.showSuccess(`Banda ${this.nome} cadastrada!`);
          })
          .catch(error => {
            console.log(error)
            this.showError(`Erro ao cadastrar ${this.nome}`);
          })
          .finally(() => {
            this.getItemsByPageNumber(1);
          })

      },
      excluir(){
        axios
          .delete(`${API_URL}/${this.selected[0]._id}`,{headers:{"If-Match":this.selected[0]._etag}})
          .then(response => {
            console.log(response);
            this.showSuccess(`Banda ${this.selected[0].nome} excluida!`);
          })
          .catch(error => {
            console.log(error);
            this.showError(`Erro ao excluir ${this.selected[0].nome}`);
          })
          .finally(() => {
            this.getItemsByPageNumber(1);
          })
      },
      changePage(page) {
        this.getItemsByPageNumber(page);
      },
      showError(msg) {
         this.$bvToast.toast(`${msg}`, {
          title: 'Erro',
          autoHideDelay: 4000,
          variant: 'danger'
        });
      },
      showSuccess(msg) {
        this.$bvToast.toast(`${msg}`, {
          title: 'Sucesso',
          autoHideDelay: 4000,
          variant: 'success'
        })
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

  #form-crud input {
    width: 100%;
  }
  
</style>