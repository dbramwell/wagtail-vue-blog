<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <HelloWorld v-bind:msg="message" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import axios from "axios";

export default {
  name: "Home",
  components: {
    HelloWorld
  },
  data: () => ({
    message: "VUE MAN",
    pages: null
  }),
  mounted () {
    axios.get(process.env.VUE_APP_API_ENDPOINT + "pages/")
    .then(response => this.pages = response)
  }
};
</script>
