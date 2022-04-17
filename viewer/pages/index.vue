<script setup lang="ts">

const chunirec_region = "jp2"
const chunirec_token = "YOUR_CHUNIREC_TOKEN"
const chunirec_url = new URL("https://api.chunirec.net/2.0/music/showall.json")
chunirec_url.searchParams.append("region", chunirec_region)
chunirec_url.searchParams.append("token", chunirec_token)
const chunirec_data = await fetch(chunirec_url.href).then(chunirec => chunirec.json())

const sega_data = await JSON.parse((await useFetch("/api/all")).data.value)
const sega_parsed = {}
sega_data.forEach(item => {
    sega_parsed[item["title"]] = item["image"]
});

const musics = {}
chunirec_data.forEach(music => {
    let {genre} = music["meta"]
    // categories_set.add(gener)
    if(sega_parsed[music["meta"]["title"]]){
        music["image"] = sega_parsed[music["meta"]["title"]]
    }
    musics[genre] ||= []
    musics[genre].push(music)
})
const categories: Array<string> = Object.keys(musics)//Array.from(categories_set)

const category = ref(categories[0])

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
    background-color: purple;
}
.music_top_container {
    display:flex;
    flex-direction: column;
    justify-content: space-between;
}
.music_top_img_container {
    display:flex;
}
.music_top_img_container > img {
    width: 35%;
    height: 35%;
    margin-left: 5%;
    margin-top: 5%;
    margin-left: 5%;
}

.music_bottom {
    height:15vmin;
    display: flex;
    align-items: center;
    flex-direction: column;
}
.music_title {
    font-size: 1.2rem;
}
.divider {
    width: 80%;
    height:2px;
    background-color: darkgray;
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
                                    <div>basic:{{item["data"]["BAS"]["level"]}}</div>
                                    <div>advanced:{{item["data"]["ADV"]["level"]}}</div>
                                </div>
                            </div>
                            <div>expert:{{item["data"]["EXP"]["level"]}}</div>
                            <div>master:{{item["data"]["MAS"]["level"]}}</div>
                        </div>
                    </div>
                    <div class="music_bottom">
                        <div class="music_title">{{item["meta"]["title"]}}</div>
                        <div style="height:inherit;"></div>
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
