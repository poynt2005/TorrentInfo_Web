<template>
    <div class="barcontent">
        <input type="text" :placeholder="placeholdertext" v-model="magnetlink" ref="inputBar" @keyup.enter="pressEnter">
    </div>
</template>

<script>
export default {
    name: 'InputBar',
    data: () => ({
        magnetlink: ''
    }),
    props: ['placeholdertext', 'getLinkFromChild', 'getMagnet'],
    watch: {
        magnetlink(newVal){
            this.$emit('getLinkFromChild', newVal)
        }
    },
    methods: {
        pressEnter(){
            this.$emit('getMagnet')
        }
    },
    mounted(){
        this.$refs.inputBar.focus()

        this.$parent.$on('clearMagnet', () => {
            this.magnetlink = ''
        })
    }
}
</script>

<style scoped>
    .barcontent {
        margin: 20px 0;
    }

    input {
        width: 70%;
        height: 50px;
        border-radius: 10px;
        border-color: lightblue;
        font-size: 1.5rem;
        font-family: fantasy;
        color: #ff66d9;
        text-align: center;


        animation: mypadding 1.5s;
    }

    


    @keyframes mypadding {
        from { width: 0; }
        to { width: 70%; }
    }
</style>