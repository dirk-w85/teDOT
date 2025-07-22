import TeInput from './components/teInput.vue'

const app = Vue.createApp({
    data() {
      return {
        title: "teDOT UI",
        data: null,
        showDiag1: true
      }
    },
    methods: {
        async fetchData() {
          const response = await fetch("https://api.chucknorris.io/jokes/random");
          this.data = await response.json();
          //alert(`Data: ${this.data.value}`)
        }
    }
  });

app.component('teInput', TeInput)
app.mount('#app')