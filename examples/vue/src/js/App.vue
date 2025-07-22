<script setup>
import Header from '../components/AppHeader.vue'
import Guides from '../components/AppGuides.vue'
import Footer from '../components/AppFooter.vue'

</script>

<template>
  <div class="container py-4 px-3 mx-auto">
    <Header />

    <h1>ThousandEyes - PoV Visualizer</h1>
    <div class="col-lg-8 px-0">
      <p class="fs-4">Visualize you PoV.</p>
    </div>

    <input type="text"></input>
    <button type="button" class="btn btn-primary me-3" @click="fetchData" >Get your PoV Env</button>
   
    <hr class="col-1 my-5 mx-0">

    <Guides />

    <Footer />
  </div>
</template>
