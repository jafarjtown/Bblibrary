const get_m = document.querySelector("[get-m]");
const list_dom = document.querySelector("[list]");

get_m.addEventListener('click', () => {
    let input = document.querySelector("[input]");
    

    const s = input.value
    const q = "search="+s

    list_dom.innerHTML = "<p>Loading ... Please wait</p>";
    loadMaterials(q);
});

async function loadMaterials(queries = null) {
    const url = `/api/rest/materials/${queries ? `?${queries}` : ''}`;
    const response = await fetch(url);
    const data = await response.json();
    populate_dom(data.results);
}

function createMaterialElement(obj) {
    const material = document.createElement("div");
    material.className = "material";
    const material_card = document.createElement("div");
    material_card.className = "material-card";
    const material_info = document.createElement("div");
    material_info.className = "material-info";
    const btns = document.createElement("div");
    btns.className = "btns";
    material_card.append(material_info, btns);
    material.appendChild(material_card);

    const img = document.createElement('img');
    img.src = "/static/imgs/files.png";
    img.loading = "lazy";

    const info = document.createElement('div');
    info.className = "info";
    info.innerHTML = `
        <span>${obj.code}</span>
        <span>${obj.title}</span>
        <span>${obj.department_name}</span>
    `;
    material_info.append(img, info);

    const createButton = (text, iconSrc, url) => {
        const button = document.createElement("a");
        button.href = url;
        button.style.textAlign = 'center';
        button.innerHTML = `
            <img src="${iconSrc}" alt="${text}"><br>
            <small>${text}</small>
        `;
        return button;
    };

    const download = createButton("Download", '/static/imgs/download.png', obj.file);
    const view = createButton("View", '/static/imgs/view.png', obj.file);
    const report = createButton("Report", '/static/imgs/issue.png', obj.flag_url);

    btns.append(download, view, report);
    return material;
}

function populate_dom(arr) {
    list_dom.innerHTML = "";

    if (arr.length === 0) {
        list_dom.innerHTML = "<p>Ops, nothing is returned, try again</p>";
    }

    for (let obj of arr) {
        const materialElement = createMaterialElement(obj);
        list_dom.appendChild(materialElement);
    }
}

loadMaterials();
