<template>
  <div class="container mt-4">
    <form @submit.prevent="updateArticle">
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
      <button class="btn btn-warning mt-4">Edit Article</button>
    </form>
    <div
      class="alert alert-warning alert-dismissibile fade show mt-5"
      role="alert"
      v-if="error"
    >
      <strong>{{ error }}</strong>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    id: {
      type: [Number, String],
      required: true,
    },
  },
  data() {
    return {
      title: null,
      body: null,
      error: null,
    };
  },
  methods: {
    updateArticle() {
      if (!this.title || !this.body) {
        this.error = "please fill all field";
      } else {
        fetch(`http://127.0.0.1:5001/update/${this.id}/`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            title: this.title,
            body: this.body,
          }),
        })
          .then((resp) => resp.json())
          .then((data) => {
            this.$router.push({
              name: "home",
            });
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
  },

  beforeRouteEnter(to, from, next) {
    if (to.params.id !== undefined) {
      fetch(`http://127.0.0.1:5001/get/${to.params.id}/`, {
        method: "get",
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((resp) => resp.json())
        .then((data) => {
          return next((vm) => ((vm.title = data.title), (vm.body = data.body)));
        })
        .catch((error) => {
          console.log(error);
        });
    } else {
      return next();
    }
  },
};
</script>

<style>
</style>