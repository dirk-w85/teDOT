//import { createApp } from 'vue'
//import TeInput from '../components/teInput.vue'
//import App from './App.vue'

const App = Vue.createApp({
    data() {
      return {
        title: "teDOT UI",
        data: null,
        webhook: null,
        showDiag1: true,
        inputAGT: null
      }
    },
    methods: {
        async fetchData() {
          const response = await fetch("https://api.chucknorris.io/jokes/random");
          this.data = await response.json();
          //alert(`Data: ${this.data.value}`)
          alert(`AGT: ${this.inputAGT}`)

          //response = await fetch("https://webhook.site/7c9508bf-1e63-4b69-84dc-48498d4d9d49"), {
          //  method: 'GET',
          //  headers: {
          //      'X-AGT': this.inputAGT
          //  }
          //};
          //this.webhook = await response.json();
          //alert(`Webhook: ${this.webhook}`)
        },
        async fetchTeLabels() {
          const response = await fetch('https://api.thousandeyes.com/v7/tags');
          this.webhook = await response.json();
          alert(`Webhook: ${this.webhook}`)
        }
    }
  });

App.mount('#app')

