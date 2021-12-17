<template>
  <div>
    <div v-for="movie in movies" :key="movie._id">
      <movie-card :movie="movie"></movie-card>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import MovieCard from "./MovieCard";

export default {
  components: { MovieCard },
  data() {
    return {};
  },
  computed: mapState({
    filters: (state) => state.movie_filters,
    movies: (state) => state.movies,
    movie_pages: (state) => state.movie_pages,
  }),
  methods: {
    ...mapActions(["GET_MOVIES_PAGINATED"]),
  },
  watch: {
    filters: async function () {
      await this.GET_MOVIES_PAGINATED({
        filters: this.filters,
        page_nb: 1,
      });
    },
  },
  async created() {
    await this.GET_MOVIES_PAGINATED({ filters: this.filters, page_nb: 1 });
  },
};
</script>
