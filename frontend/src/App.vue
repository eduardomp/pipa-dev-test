<template>
  <div id="app">
    <Menu />
    <Conteudo />
  </div>
</template>

<script>
import Menu from './components/layout/Menu'
import Conteudo from './components/layout/Conteudo'

export default {
  name: 'App',
  components: {
    Menu,
    Conteudo,
  }
}
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #EB5E28;
    background: url('~@/assets/background_pipa_dev_test.jpg') no-repeat center center fixed;
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
  }
</style>
