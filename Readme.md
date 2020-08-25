# TorrentInfo Web

## 介紹
這個是把3年前的小網頁項目重新拿來寫  
當初是剛剛學html，啥都不會的情況下應寫出來的，寫的很爛(~~不過看看三年後的自己好像也沒什麼長進的樣子~~)  
最近學了vue，想說必須找個東西來練習一下，就把這個小項目在拿出來搞搞  
學了東西不操作不使用基本上馬上就會忘了

## 用途
有兩個功能
1. 磁力鍵轉成Torrent檔案
2. Torrent檔案轉成磁力鍵

## 套件
前端: Vue 2 (Vue 3目前好像還在Preview階段)  
後端: python 2 & flask  

後端有用上python-libtorrent binding函式庫，  
用來轉換磁力鍵和torrent檔案  
因為這個函式庫不支援python 3(要自己編譯)，
所以就用Python 2

## 使用

1. 使用Docker  
    ### __*(需要安裝Docker)*__ 
    ```
    git clone https://github.com/poynt2005/TorrentInfo_Web.git
    cd TorrentInfo_Web
    docker build -t <名字> .
    docker run -p 8080:8080 -p 6881:6881 -d <名字>
    ```
2. 不使用Docker  
    需安裝 node, npm, python 2, python-libtorrent  
    
    (python-libtorrent在Windows下有安裝程式能直接裝，
    ubuntu下可以用sudo apt-get install python-libtorrent安裝)  

    ```
    git clone https://github.com/poynt2005/TorrentInfo_Web.git
    cd TorrentInfo_Web
    npm i
    npm run build
    python app.py
    ```
之後瀏覽器打開localhost:8080就能看到網頁了