<template>
  <div class="">
    <button
      type="button"
      class="p-4 cursor-pointer"
      v-if="movie_pages.previous"
      @click.prevent="paginate(-1)"
    >
      Précédent
    </button>
    <button
      type="button"
      class="p-4 cursor-pointer"
      v-if="movie_pages.next"
      @click.prevent="paginate(1)"
    >
      Suivant
    </button>
  </div>
</template>

<script>
import { mapActions, mapState } from "vuex";

export default {
  name: "MoviePaginate",
  computed: {
    ...mapState({
      filters: (state) => state.movie_filters,
      movie_pages: (state) => state.movie_pages,
    }),
  },
  methods: {
    ...mapActions(["GET_MOVIES_PAGINATED"]),

    async paginate(direction) {
      await this.GET_MOVIES_PAGINATED({
        filters: this.filters,
        page_nb: +this.movie_pages.current + direction,
      });
    },
  },
};
</script>

<style scoped></style>
