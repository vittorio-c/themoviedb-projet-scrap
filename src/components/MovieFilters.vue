<template>
  <div class="h-full p-4 text-left w-72">
    <div class="m-4">
      <p>Classer par :</p>
      <div>
        <div>
          <input type="radio" id="budget" value="budget" v-model="sorts" />
          <label for="budget">Budget</label>
        </div>

        <div>
          <input type="radio" id="revenues" value="revenues" v-model="sorts" />
          <label for="revenues">Revenus</label>
        </div>

        <div>
          <input type="radio" id="profit" value="profit" v-model="sorts" />
          <label for="profit">Bénéfices</label>
        </div>

        <div>
          <input
            type="radio"
            id="release_year"
            v-model="sorts"
            value="release_year"
          />
          <label for="release_year">Année de parution</label>
        </div>
      </div>
    </div>
    <div class="m-4">
      <p>En ordre :</p>
      <div>
        <input type="radio" id="asc" name="order" value="1" v-model="order" />
        <label for="asc">Ascendant</label>
      </div>
      <div>
        <input type="radio" id="desc" name="order" value="-1" v-model="order" />
        <label for="desc">Descendant</label>
      </div>
      <div>
        <input id="page" name="page" type="hidden" value="1" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from "vuex";

export default {
  data() {
    return {
      sorts: "release_year",
      order: "-1",
    };
  },
  methods: {
    ...mapMutations(["set_movie_filters"]),
  },
  computed: {
    filters() {
      return { sorts: this.sorts, order: this.order };
    },
  },
  watch: {
    sorts: function () {
      this.set_movie_filters(this.filters);
    },
    order: function () {
      this.set_movie_filters(this.filters);
    },
  },
  created() {
    this.set_movie_filters(this.filters);
  },
};
</script>

<style></style>
