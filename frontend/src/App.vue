<template>
  <div id="app">
    <Menu />
    <Conteudo />
    <Rodape />
  </div>
</template>

<script>
import Menu from './components/layout/Menu'
import Conteudo from './components/layout/Conteudo'
import Rodape from './components/layout/Rodape'

export default {
  name: 'App',
  components: {
    Menu,
    Conteudo,
    Rodape
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
