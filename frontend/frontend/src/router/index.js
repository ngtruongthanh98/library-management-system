import Vue from "vue";
import VueRouter from "vue-router";
import Shark from "../components/Shark.vue";
import Games from "../components/Games.vue";
import LoginPage from "../views/Login.vue";
import RegisterPage from "../views/Register.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/shark",
    name: "Shark",
    component: Shark,
  },
  {
    path: "/games",
    name: "Games",
    component: Games,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginPage,
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterPage,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
