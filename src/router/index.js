import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Ping from "../views/Ping.vue";
import Movies from "../views/Movies";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/ping",
    name: "Ping",
    component: Ping,
  },
  {
    path: "/movies",
    name: "Movies",
    component: Movies,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
