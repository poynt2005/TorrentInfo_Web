const http = require('http')
const fs = require('fs')

const server = http.createServer((req, res) => {

    res.setHeader('Access-Control-Allow-Origin', '*')
	res.setHeader('Access-Control-Request-Method', '*')
    res.setHeader('Access-Control-Allow-Headers', '*')
    
    if(req.url == '/magnet' ){
        res.writeHead(200, {'Content-Type': 'application/json'})

        res.write(JSON.stringify({ filetype: 'magnet', filename: 'ubuntu.torrent', downloadLink: '/file/mm.torrent', isExists: true}))
        res.end()
        return
    }
    else if(req.url == '/torrent'){
        res.writeHead(200, {'Content-Type': 'application/json'})
        res.write(JSON.stringify({ filetype: 'torrent', magnet: 'magnet:?xt=urn:btih:ae9ccffe9925bc31d3116e5f5edf8db1ca137016'}))
        res.end()
        return
    }
    else if(req.url == '/file/mm.torrent'){
        res.writeHead(200, {'Content-Type': 'application/octet-stream'})
        res.write(fs.readFileSync('./ubuntu.torrent'))
        res.end()
        return

    }

})

server.listen(3250, () => {
    console.log('Test server is listening on port 3250')
})

