<template>
    <div class="che">
        <div class="spinner-border" role="status"></div>
        目前Server正在處理 {{ filetype }} 請稍後...
    </div>
</template>

<script>
export default {
    name: 'StillLoading',
    props: ['filetype']
}
</script>

<style scoped>
</style>