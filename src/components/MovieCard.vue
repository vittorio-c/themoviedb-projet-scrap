<template>
  <div class="flex m-4">
    <aside class="movie__infos w-1/2">
      <h3 class="text-2xl text-left">
        <a href="/">{{ movie.title }}</a>
      </h3>
      <ul class="text-left">
        <li>
          Année : <span class="font-bold">{{ movie.release_year }}</span>
        </li>
        <li v-if="movie.director">
          Réalisateur : <span class="font-bold">{{ movie.director }}</span>
        </li>
        <li v-if="movie.budget > 0">
          Budget :
          <span class="font-bold">{{ formatCurrency(movie.budget) }}</span>
        </li>
        <li v-if="movie.revenues > 0">
          Chiffre d'affaire réalisé :
          <span class="font-bold">{{ formatCurrency(movie.revenues) }}</span>
        </li>
        <li v-if="movie.profit > 0">
          Bénéfices :
          <span class="font-bold">{{ formatCurrency(movie.profit) }}</span>
        </li>
      </ul>
      <div v-if="movie.artists.length > 0" class="text-left">
        <span>Artistes : </span>
        <span v-for="artist in movie.artists" :key="artist._id">
          <span class="font-bold">{{ artist.name }}</span> ({{ artist.role }})
        </span>
      </div>
    </aside>
    <div class="movie_image w-1/2">
      <img :src="movie.picture_url" alt="movie_image" />
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieCard",
  props: ["movie"],
  methods: {
    formatCurrency(price) {
      // Create our number formatter.
      var formatter = new Intl.NumberFormat("fr-FR", {
        style: "currency",
        currency: "EUR",

        // These options are needed to round to whole numbers if that's what you want.
        //minimumFractionDigits: 0, // (this suffices for whole numbers, but will print 2500.10 as $2,500.1)
        //maximumFractionDigits: 0, // (causes 2500.99 to be printed as $2,501)
      });

      return formatter.format(price);
    },
  },
};
</script>

<style scoped></style>
