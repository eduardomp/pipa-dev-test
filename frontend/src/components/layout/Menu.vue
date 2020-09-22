<template>
  <div id="menu">
    <b-navbar type="dark" variant="dark" sticky=true fixed="top">
      <b-navbar-nav align='right'>
        <b-navbar-brand>PipaDevTest</b-navbar-brand>    
        <b-nav-item href="#/">Info</b-nav-item>        
        <b-nav-item href="#/bandas">Bandas</b-nav-item>
        <b-nav-item href="#/generos">Generos</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
  export default {
  }
</script>

<style>
  #menu {
   color: #EB5E28; 
   border-bottom: 0.1em solid whitesmoke; 
  }
</style>