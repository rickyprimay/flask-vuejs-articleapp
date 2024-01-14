<template>
    <div class="container mt-5">
      <h2> {{ article.title }} </h2>
      <p class="mt-3"> {{ article.body }} </p>
      <h6>Published Date : {{ article.date }}</h6>
      <button class="btn btn-warning mx-3 mt-3">Edit</button>
      <button @click="deleteArticle" class="btn btn-danger mx-3 mt-3">Delete</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        article: {},
      };
    },
    props: {
      id: {
        type: [Number, String],
        required: true,
      },
    },
    methods: {
      getArticles() {
        fetch(`http://127.0.0.1:5001/get/${this.id}/`, {
          method: "get",
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((resp) => resp.json())
          .then((data) => {
            this.article = data;
          })
          .catch((error) => {
            console.log(error);
          });
      },
      deleteArticle() {
        fetch(`http://127.0.0.1:5001/delete/${this.id}/`, {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((resp) => resp.json())
          .then((data) => {
            this.$router.push({
                name:'home'
            })
          })
          .catch((error) => {
            console.log(error);
          });
      },
    },
    created() {
      this.getArticles();
    },
  };
  </script>
  
  <style>
  </style>
  