## Outra api simples para downloads do YouTube 
### Agora usando a lib em python [yt-dlp](https://github.com/yt-dlp/yt-dlp)

Por conta do projeto [ytdl-core](https://github.com/fent/node-ytdl-core) em nodejs não estar com um desenvolvimento ativo, alguns erros começaram a surgir, prejudicando meu outro projeto: [ytdl-simple-api](https://github.com/erickythierry/ytdl-simple-api)

Irei focar nesse aqui por enquanto até a lib em nodejs voltar a funcionar (se voltar :/)

Esse projeto aqui será BEM mais simples, apenas uma API básica para download de video e audio do youtube

## Docker
Projeto adaptado para docker, inclusive já tem uma imagem pública no docker hub
[aqui](https://hub.docker.com/repository/docker/rickhdamas/ytdlp-api/)

## HowTo
- Clone esse repositório
- Instale as dependências com `pip install -r requirements.txt`
- Execute `python main.py` (ou `python3 main.py` no linux)

- Os endpoints são:
     - http://localhost:5000/download/audio para o áudio bruto (webm)
     - http://localhost:5000/download/video para o vídeo bruto (webm ou mp4)

## Exemplo com Curl
- curl -X POST -H "Content-Type: application/json" -d '{"url": **"LINK_VIDEO"**}' http://localhost:5000/download/audio⁠ -O
- curl -X POST -H "Content-Type: application/json" -d '{"url": **"LINK_VIDEO"**}' http://localhost:5000/download/video⁠ -O