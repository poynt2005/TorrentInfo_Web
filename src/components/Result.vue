<template>
    <div class="che result-div">
        <div v-if="file.filetype === 'magnet'">
            <div v-if="file.isExists">
                下載的檔案名稱為 
                <a href="" @click.prevent="downloadfile">{{ file.filename }}</a>
                (點擊即可下載)
            </div>
            <div v-else>
                伺服器超時，應是Magnet鏈結太舊，<font style="color:red">無法從DHT獲得Torrent檔案</font>
            </div>
        </div>
        <div v-else>
            <div>
                Magnet連結為:
                <a :href="file.magnet">這裡</a>
                (右鍵複製)
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Result',
    props: ['file'],
    methods: {
        async downloadfile(){
            try{
                const { downloadLink } = this.file

                console.log(downloadLink)
                const rst = await this.axios({
                    url: downloadLink,
                    method: 'GET',
                    responseType: 'blob'
                })
                const a = document.createElement('a')
                a.download = this.file.filename
                a.href = URL.createObjectURL(new Blob([rst.data]))
                a.click()
            }
            catch(e){
                console.log('Error Download')
            }
        }
    }
}
</script>

<style scoped>
    .result-div {
        font-size: 1.2rem;
    }
</style>