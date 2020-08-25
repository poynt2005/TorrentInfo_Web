<template>
    <div class="upload-bar che">
        <label for="userinput" 
            @dragover.prevent="fileDragOver" 
            @dragleave.prevent="fileDragLeave"
            @drop.prevent="fileDrop"
        >
            {{ childPlaceholder }} 
        </label>
        <input type="file" @change="changeFile" id="userinput">
    </div>
</template>

<script>
export default {
    name: 'InputBar',
    props: ['placeholder', 'getFile', 'startUpload'],
    data: () => ({
        childPlaceholder: ''
    }),
    methods: {
        changeFile(el){
            const files = el.target.files || el.dataTransfer.files

            if(files.length === 0)
                return

            this.childPlaceholder = files[0].name

            this.$emit('getFile', files[0])
        },
        fileDragOver(){
            this.childPlaceholder = '在此放置'
        },
        fileDragLeave(){
            this.childPlaceholder = this.placeholder
        },
        fileDrop(e){
            this.childPlaceholder = this.placeholder

            const files = e.dataTransfer.files

            if(files.length === 0)
                return

            this.childPlaceholder = files[0].name

            this.$emit('getFile', files[0])
        }
    },
    created(){
        this.childPlaceholder = this.placeholder
    }

}
</script>

<style scoped>
    @font-face {
        font-family: myche;
        unicode-range: U+4E00-9FFF;
        src: url("../assets/fonts/cwTeXKai-zhonly.ttf")
    }

    .upload-bar {
        margin: 20px 0;
    }

    input {
        display: none;
    }

    label {
        border-style: solid;
        width: 60%;
        height: 50px;
        border-width: 1px;
        font-size: 30px;
        color:  #9933ff;
        background-color: #DCD9D4;
        background-image: linear-gradient(to bottom, rgba(255,255,255,0.50) 0%, rgba(0,0,0,0.50) 100%), radial-gradient(at 50% 0%, rgba(255,255,255,0.10) 0%, rgba(0,0,0,0.50) 50%);
        background-blend-mode: soft-light,screen;
        overflow: hidden;
        font-family: myche, fantasy;
    }
</style>