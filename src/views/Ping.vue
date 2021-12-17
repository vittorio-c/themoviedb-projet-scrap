<template>
  <div>
    <button>Ping this !</button>
    <button @click.prevent="getMovieList">Get movie list</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Ping",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getMessage() {
      const path = "http://localhost:5000/ping";
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getMovieList() {
      const path = "http://localhost:5000/api/movies";
      axios
        .get(path)
        .then((res) => {
          // this.msg = res.data;
          console.log(res.data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
