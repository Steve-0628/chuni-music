import fs from "fs";

export default async function (req, res) {
    const data = await fetch("https://chunithm.sega.jp/storage/json/music.json")
    const text = await data.text()
    return text
}
