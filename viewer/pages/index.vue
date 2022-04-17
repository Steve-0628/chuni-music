<script setup lang="ts">
// // const token = localStorage.getItem('token') || ""
// const orig_data = await useFetch("/api/all")
// const wiki_data = await useFetch("/api/list")
// // console.log(data.data.value)

// const orig: Array<object> = JSON.parse(orig_data.data.value)
// const wiki: object = JSON.parse(wiki_data.data.value)

// const orig_parse = {}

// const categories: Array<string> = Object.keys(wiki)
// const category_reverse: object = {}

// categories.forEach(category => {
//   category_reverse[wiki[category]] = category
// })

// orig.forEach((item) => {
//     const categ = category_reverse[item["catname"]]
//     orig_parse[item["title"]] = item
// })

// Object.keys(wiki).forEach(key => {
//     wiki[key]["songs"].forEach(song => {
//         wiki[key]["songs"]["orig"] = orig_parse[song["title"]]
//     })
// })

// const category = ref(categories[0]);

const token = "YOUR_CHUNIREC_TOKEN"
const chunirec_url = "https://api.chunirec.net/2.0/music/showall.json"
const chunirec = await fetch(chunirec_url + "?region=jp2&token=" + token)
const chunirec_data: Array<object> = await chunirec.json()
const categories_set: Set<string> = new Set()
const musics = {}
chunirec_data.forEach(music => {
    let gener = music["meta"]["genre"]
    categories_set.add(gener)
    musics[gener] = musics[gener] || []
    musics[gener].push(music)
})
const categories: Array<string> = Array.from(categories_set)

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
                                <img v-bind:src="'https://db.chunirec.net/img/music/jkt/'+item['meta']['id']+'.jpg'" >
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
