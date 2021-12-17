import { createStore } from "vuex";
import api from "../api";

export default createStore({
  state: {
    movie_filters: {},
    movie_pages: {},
    movies: {},
  },
  mutations: {
    set_movie_filters(state, filter) {
      state.movie_filters = filter;
    },
    set_movies(state, movies) {
      state.movies = movies;
    },
    set_movie_pages(state, pages) {
      state.movie_pages = pages;
    },
  },
  actions: {
    GET_MOVIES_PAGINATED({ commit }, { filters, page_nb }) {
      return api
        .getMoviesPaginated(filters, page_nb)
        .then((response) => {
          commit("set_movies", response.data.data);
          commit("set_movie_pages", response.data._embed);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  modules: {},
});
