<template>
  <div>
    <mytitle class="che" title="磁力鍵"></mytitle>
    <div class="che info">這個功能可以協助轉換磁力鍵到<font>Torrent</font>檔案</div>
    <div class="che info">使用<font>Libtorrent</font>庫搜尋<font>DHT</font>網路進行轉換</div>
    <div class="che info warning">注意: 若磁力鍵年代久遠，則會尋找失敗</div>

    <mybar placeholdertext="請輸入磁力鍵結" @getLinkFromChild="getLinkFromChild" @getMagnet="getMagnet"/>
    
    <div class="btns">
      <a class="btn btn-primary btn-sm" @click.prevent="getMagnet">確認</a>
      <a class="btn btn-danger btn-sm" @click.prevent="clearMagnet">清除</a>
    </div>

    <div class="result-div">
      <stillloading v-if="isSending === true" filetype="Magnet鍵結" />
      <result-div v-if="isSending === false" :file="myFile" ></result-div>
    </div>
  </div>
</template>

<script>
  import Title from '../components/Title'
  import InputBar from '../components/InputBar'
  import StillLoading from '../components/StillLoading'
  import Result from '../components/Result'

  export default {
    name: 'Magnet',
    data: () => {
      return {
        magnetlink: '',
        isSending: null,
        myFile: {}
      }
    },
    methods: {
      getLinkFromChild(val){
        this.magnetlink = val
      },
      async getMagnet(){
        if(this.isSending)
          return

        if(/^magnet:\?xt=urn:[a-z0-9]+:[a-z0-9]{32,40}.+$/i.test(this.magnetlink)){
          if(this.isSending === null)
            this.isSending = false

          this.isSending = !this.isSending  
          try{
            this.myFile = (await this.$http.post('/magnet', {
              link: this.magnetlink
            })).data
            this.isSending = !this.isSending
          }
          catch(e){
            this.isSending = !this.isSending
            this.$dialog({
              title: '錯誤',
              content: '與伺服器溝通發生錯誤',
              btns: [{label: 'OK', color: '#09f'}]
            })
          }
        }
        else{
          this.$dialog({
            title: '錯誤',
            content: '請輸入正確的磁力鍵',
            btns: [{label: 'OK', color: '#09f'}]
          })
        }
      },
      clearMagnet(){
        this.$emit('clearMagnet')
      }
    },
    components: {
      mytitle: Title,
      mybar: InputBar,
      stillloading: StillLoading,
      'result-div': Result
    }
  }
</script>

<style scoped>
  .info {
    font-size: 1.2rem;
  }

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

  .warning {
    color: red;
    font-style: italic;
  }

  .btns a {
    margin: 0 5px;
  }

  .result-div {
    margin: 10px 0;
  }
</style>