<template>
  <div class="container mt-4">
    <form @submit.prevent="insertArticle">
      <input
        type="text"
        class="form-control"
        placeholder="please enter your title"
        v-model="title"
      />
      <br />
      <textarea
        rows="10"
        class="form-control"
        placeholder="please enter detail article"
        v-model="body"
      ></textarea>
      <button class="btn btn-success mt-4">Publish Article</button>
    </form>
    <div class="alert alert-warning alert-dismissibile fade show mt-5" role="alert" v-if="error">
        <strong>{{ error }}</strong>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      title: null,
      body: null,
      error: null,
    };
  },
  methods: {
    insertArticle() {
      if (!this.title || !this.body) {
        this.error = "please fill all field";
      } else {
        fetch("http://127.0.0.1:5001/add", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            title:this.title,
            body:this.body
          })
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
      }
    },
  },
};
</script>

<style>
</style>