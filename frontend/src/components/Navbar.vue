<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary fixed-top">
      <div class="container">
        <router-link class="navbar-brand text-style" to="/">Article App</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item mr-2">
                  <router-link class="btn btn-primary mx-3" aria-current="page" to="/">Home</router-link>
                </li>
                <li class="nav-item">
                  <router-link class="btn btn-success" to="/create">Create</router-link>
                </li>
              </ul>              
        </div>
      </div>
    </nav>
  </template>
  
  <script>
  export default {
  
  }
  </script>
  
  <style>
    .text-style{
        font-size: 30px !important;
        color: brown !important;
    }
  </style>
  