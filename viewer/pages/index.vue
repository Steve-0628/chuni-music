<script setup lang="ts" ssr="false">

let chunirec_token = ""
if(!chunirec_token){
    // alert("oi")
}
const musics = {}

let category = ref("")
let categories = ref([])

onMounted(async () => {
    chunirec_token = localStorage.chunirec_token
    if(!chunirec_token){
        alert("chunirec_tokenがありません。chunirec_tokenを設定してください。")
        chunirec_token = prompt("ここにchunirecで取得したトークンをペースト")
        localStorage.chunirec_token = chunirec_token
    }

    const chunirec_region = "jp2"
    const chunirec_url = new URL("https://api.chunirec.net/2.0/music/showall.json")
    chunirec_url.searchParams.append("region", chunirec_region)
    chunirec_url.searchParams.append("token", chunirec_token)
    const chunirec_data = await fetch(chunirec_url.href).then(chunirec => chunirec.json())

    const sega = (await useFetch("/api/all")).data.value
    // console.log(sega)
    const sega_data = await JSON.parse(sega)
    const sega_parsed = {}
    sega_data.forEach(item => {
        sega_parsed[item["title"]] = item["image"]
    });


    chunirec_data.forEach(music => {
        let {genre} = music["meta"]
        // categories_set.add(gener)
        if(sega_parsed[music["meta"]["title"]]){
            music["image"] = sega_parsed[music["meta"]["title"]]
        }
        musics[genre] ||= []
        musics[genre].push(music)
    })
    categories.value = Object.keys(musics)//Array.from(categories_set)

    category.value = categories[0]
})


</script>
<script>
</script>

<style>
body {
    padding: 0;
    margin:0;
}
.app {
    background-color: yellow;
}
.geners {
    height: 20vh;
    width: 100%;
    display: flex;
    align-items: center;
}
.gener_container {
    width: 100%;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}
.gener {
    background-color: white;
}
.gener button {
    font-size: 1.5rem;
    border-radius: 0;
    border: none;
    padding: .8rem;
    background-color: lightgray;
}
.gener button:hover {
    background-color: gray;
}

.musics {
    height: 80vh;
    overflow:hidden;
    display: flex;
    align-items: center;
}
.music_container {
    display: flex;
    justify-content: space-between;
    overflow-x: auto;
    margin-bottom: 10vmin;
}
.music {
    height: 55vmin;
    width: 40vmin;
    flex-shrink: 0;
    background-color: white;
    margin-left: 5vmin;
    margin-right:5vmin;
}
.music_top {
    height: 40vmin;
    background-color: beige;
}
.music_top_container {
    display:flex;
    flex-direction: column;
    justify-content: space-between;
    height:100%;
}
.music_top_img_container {
    display:flex;
}
.music_top_img_container > img {
    width: 35%;
    /* height: 35%; */
    margin-left: 5%;
    margin-top: 5%;
    margin-left: 5%;
}
.music_top_lowlevel_container {
    margin:5%;
    margin-bottom:0;
    flex-grow: 1;
    display:flex;
    flex-direction: column;
    justify-content: space-between;
}
.basic_container {
    height:6vmin;
    display: flex;
    justify-content: left;
    align-items: center;
}
.basic {
    border: 0.5vmin white solid;
    width:5.5vmin;
    height:5.5vmin;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: green;
    color:white;
    font-weight: bold;
}
.advanced_container {
    height:6vmin;
    display: flex;
    justify-content: left;
    align-items: center;
}
.advanced {
    border: 0.5vmin white solid;
    width:5.5vmin;
    height:5.5vmin;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: orange;
    color:white;
    font-weight: bold;
}
.music_highlevel_container{
    margin: 5%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    flex-grow: 1;
}
.expert {
    /* flex-grow: 1; */
    height:8vmin;
    background-color: white;
    display:flex;
}
.expert_container {
    background-color: red;
    margin:0.5vmin;
    height:7vmin;
    width:7vmin;
    color:white;
    display:flex;
    text-align: center;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    font-weight:bold;
}
.expert_detail {
    flex-grow: 1;
    margin:0.5vmin;
    display:flex;
    flex-direction:column;
    justify-content: space-around;
}
.master {
    /* flex-grow: 1; */
    height:8vmin;
    background-color: white;
    display:flex;
}
.master_container {
    background-color: purple;
    margin:0.5vmin;
    height:7vmin;
    width:7vmin;
    color:white;
    display:flex;
    text-align: center;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    font-weight:bold;
}
.master_detail {
    flex-grow: 1;
    margin:0.5vmin;
    display:flex;
    flex-direction:column;
    justify-content: space-around;
}
.music_high_level {
    font-size:90%;
    font-weight: lighter;
}
.music_high_level_val {
    font-size:120%;
}

.music_bottom {
    height:15vmin;
    display: flex;
    align-items: center;
    flex-direction: column;
}
.music_title {
    font-size: 1.5rem;
}
.divider {
    width: 80%;
    height:2px;
    background-color: darkgray;
}
.music_artist {
    overflow:scroll
}
.music_bottom_container {
    width: 100%;
    display: flex;
    justify-content: space-around;
}
</style>

<template>
    <div class="app">
        <div class="geners">
            <div class="gener_container">
                <div v-for="cat of categories" class="gener">
                    <button v-if="cat == category" @click="() => {category = cat}" class="gener_btn" style="background-color:red">{{cat}}</button>
                    <button v-else @click="() => {category = cat}" class="gener_btn" >{{cat}}</button>
                </div>
            </div>
        </div>
        <div class="musics">
            <div class="music_container">
                <div v-for="item of musics[category]" class="music">
                    <div class="music_top">
                        <div v-if="category == 'WORLD\'S END'">
                            {{item["data"]}}
                        </div>
                        <div v-else class="music_top_container">
                            <div class="music_top_img_container">
                                <img v-bind:src="'https://new.chunithm-net.com/chuni-mobile/html/mobile/img/'+item['image']" >
                                <div class="music_top_lowlevel_container">
                                    <div class="basic_container">
                                        <div class="basic">{{item["data"]["BAS"]["level"]}}</div>
                                        <div>最大コンボ数</div>
                                        <div>{{item["data"]["BAS"]["maxcombo"]}}</div>
                                    </div>
                                    <div class="advanced_container">
                                        <div class="advanced">{{item["data"]["ADV"]["level"]}}</div>
                                        <div>最大コンボ数</div>
                                        <div>{{item["data"]["ADV"]["maxcombo"]}}</div>
                                    </div>
                                </div>
                            </div>
                            <div class="music_highlevel_container">
                                <div class="expert">
                                    <div class="expert_container">
                                        <div class="music_high_level">
                                            LEVEL
                                        </div>
                                        <div class="music_high_level_val">
                                            {{item["data"]["EXP"]["level"]}}
                                        </div>
                                    </div>
                                    <div class="expert_detail">
                                        <div>コンボ {{item["data"]["EXP"]["maxcombo"]}}</div>
                                        <div>定数　 {{item["data"]["EXP"]["const"]}}</div>
                                    </div>
                                </div>
                                <div class="master">
                                    <div class="master_container">
                                        <div class="music_high_level">
                                            LEVEL
                                        </div>
                                        <div class="music_high_level_val">
                                            {{item["data"]["MAS"]["level"]}}
                                        </div>
                                    </div>
                                    <div class="master_detail">
                                        <div>コンボ {{item["data"]["MAS"]["maxcombo"]}}</div>
                                        <div>定数　 {{item["data"]["MAS"]["const"]}}</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="music_bottom">
                        <div class="music_title">{{item["meta"]["title"]}}</div>
                        <div style=""></div>
                        <div class="divider"></div>
                        <div class="music_artist">{{item["meta"]["artist"]}}</div>
                        <div class="music_bottom_container">
                            <div>RELEASE:{{item["meta"]["release"]}}</div>
                            <div>BPM:{{item["meta"]["bpm"]}}</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
