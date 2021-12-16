import axios from "axios";

const base_url = "http://localhost:5000/api";

export default {
  getMoviesPaginated({ sorts, order }, page) {
    let url_params = "/movies?page=" + page;
    url_params += "&sorts[]=" + sorts;
    url_params += "&order=" + order;

    return axios.get(base_url + url_params);
  },
};
