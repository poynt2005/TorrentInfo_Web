<template>
    <div>
        <div v-ctitle="title"></div>
        <div class="mytitle"> {{ title }} </div>
    </div>
</template>

<script>
export default {
    name: 'Title',
    props: ['title']
}
</script>

<style scoped>
    .mytitle {
        font-size: 3rem;
    }  
</style>