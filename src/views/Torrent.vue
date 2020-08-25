<template>
  <div>
    <mytitle class="che" title="Torrent檔案" />
    <div class="che info">這個功能可以協助轉換Torrent檔案到<font>Magnet</font>磁力鍵</div>
    <div class="che info">使用<font>Libtorrent</font>庫的<font>Bencode</font>進行轉換</div>

    <upload-bar @getFile="getFile" @startUpload="startUpload" placeholder="請點擊此處或是拖曳檔案至此" />

    <div class="btns">
        <a class="btn btn-primary btn-sm" @click.prevent="startUpload">上傳</a>
    </div>

    <div class="result-div">
      <stillloading v-if="isSending === true" filetype="Torrent檔案" />
      <result-div v-if="isSending === false" :file="myMagnet"></result-div>
    </div>

  </div>
</template>

<script>
import Title from '../components/Title'
import UploadBar from '../components/UploadBar'
import StillLoading from '../components/StillLoading'
import Result from '../components/Result'

export default {
    name: 'Torrent',
    data: () => ({
      userFile: null,
      isSending: null,
      myMagnet: {}
    }),
    components: {
      mytitle: Title,
      'upload-bar': UploadBar,
      stillloading: StillLoading,
      'result-div': Result
    },
    methods: {
      getFile(myfile){
        this.userFile = myfile
      },
      async startUpload(){
        if(this.isSending === null)
          this.isSending = false

        this.isSending = !this.isSending

        if(this.userFile === null){
          this.$dialog({
            title: '錯誤',
            content: '請確實輸入檔案',
            btns: [{label: 'OK', color: '#09f'}]
          })
        }
        else {
          try{
            const fd = new FormData()
            fd.append('file', this.userFile)

            this.myMagnet = (await this.$http.post('/torrent', fd, {
              headers: {'Content-Type': 'multipart/form-data'}
            })).data
          }
          catch(e){
            this.$dialog({
              title: '錯誤',
              content: '伺服器錯誤',
              btns: [{label: 'OK', color: '#09f'}]
            })
          }         
        }    
        this.isSending = !this.isSending
      }
    }
}
</script>

<style scoped>
  font {
    font-family: 'Comic Sans MS';
    margin: 0 1px;
    color: #7c7ee6;
  }

  font::after {
    content: ">";
  }

  font::before {
    content: "<";
  }

  .info {
    font-size: 1.2rem;
  }

  .btns a {
    margin: 0 5px;
  }

  .result-div {
    margin: 10px 0;
  }
</style>