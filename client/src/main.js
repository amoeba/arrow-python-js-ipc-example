import { tableFromIPC } from "apache-arrow";

const URL = "http://localhost:3000/data"

async function main() {
    const table = await tableFromIPC(fetch(URL));
    document.querySelectorAll("div")[0].innerHTML = table.toString();
}

await main();
