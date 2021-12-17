<template>
  <div class="flex items-stretch">
    <movie-filters />
    <div>
      <movie-paginate class="w-full flex justify-end" />
      <movies-index />
      <movie-paginate class="w-full flex justify-end" />
    </div>
  </div>
</template>

<script>
import MovieFilters from "../components/MovieFilters.vue";
import MoviesIndex from "../components/MoviesIndex.vue";
import MoviePaginate from "../components/MoviePaginate";
export default {
  components: {
    MoviePaginate,
    MovieFilters,
    MoviesIndex,
  },
};
</script>

<style></style>
