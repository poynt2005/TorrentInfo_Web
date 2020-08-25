<template>
  <div id="app">
    
    <div class="mynav">
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top mynav">
        <a href="/" class="navbar-brand">TorrentInfo</a>
      </nav>
    </div>

    <div class="main">
      <transition 
      mode="out-in"
      tag="div"
      >
        <router-view class="myview" />
      </transition>

      <div class="links">
        <router-link to="/magnet" class="btn btn-primary mybtn">Magnet</router-link>
        <router-link to="/torrent" class="btn btn-primary mybtn">Torrent</router-link>
      </div>
    </div>
  </div>
</template>

<style>
  @font-face { 
    font-family: "Amatic SC";
    src: url("./assets/fonts/AmaticSC-Bold.ttf"); 
   }

  @font-face {
    font-family: "cwTeXKai";
    src: url("./assets/fonts/cwTeXKai-zhonly.ttf");
  }

  html, body {
    padding: 0;
    margin: 0;
    height: 100%;
    overflow: hidden;
  }

  body {
    background-image: url("./assets/bg.jpg");
    background-size: cover;
  }

  #app {
    height: 100%;
    padding: 0;
    margin: 0;
    text-align: center;
  }

  .mynav {
    height: 8%;
  }

  .main {
    height: 92%;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .myview {
    height: 60%;
    width: 100%;

    margin: 30px 0;
  }

  .mybtn {
    margin: 0 20px;
    border-radius: 30px !important;
    font-family: 'Amatic SC', cursive;
    font-size: 1.5rem !important;
    background-color: #8c1aff !important;
    width: 150px;
  }


  .che {
    font-family: 'cwTeXKai';
  }

  .v-enter,
  .v-leave-to {
    opacity: 0;
    transform: scale(1.5,1.5);
  }

  .v-enter-to,
  .v-leave {
    transition: ease 2s;
  }
  
</style>
