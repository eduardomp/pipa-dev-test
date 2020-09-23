<template>
  <div class="container ">
    
    <div class="row mt-50">
      <div class="col-sm">
        <h1>Generos</h1>
      </div>
      <div class="col-sm d-flex justify-content-end">
        <b-button size="lg" variant="dark" @click="showModal">Adicionar Novo</b-button>
      </div>
    </div>

    <div class="row mt-50">
      <div class="col-sm">
        <b-table 
          striped
          hover
          dark
          small
          :items="items"
          >
        </b-table>
      </div>
    </div>

    <div class="row mt-10">
      <div class="col-sm d-flex justify-content-end">
        <b-pagination
          v-model="currentPage"
          total-rows="20"
          per-page="10"
          align="fill"
          size="sm"
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
        footer-text-variant="light"
        @ok="salvar"
        @cancel="excluir"
        @hide="cancelar"
        >
      
        <p>Conteudo da modal...</p>
      
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
 export default {
    data() {
      return {
        items: [
          { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' },
          { age: 40, first_name: 'Dickerson', last_name: 'Madonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' },
        ],
        currentPage: 1
      }
    },
    methods: {
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
        this.$refs['modal-crud'].hide()
      }
    }
  }
</script>

<style>
  .mt-50 {
    margin-top:50px;
  }
</style>salvar