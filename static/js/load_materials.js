

const get_m = document.querySelector("[get-m]");
const list_dom = document.querySelector("[list]");

const URL_STR = '/api/rest/materials/'
const PAGING_MAX = 20

get_m.addEventListener('click', () => {
    let department = document.querySelector("[department]");
    let course = document.querySelector("[course]");
    let level = document.querySelector("[level]");

    const d = department.value;
    const c = course.value;
    const l = level.value;
    const q = [];

    if (c !== 'null') {
        q.push(`course__code=${c}`);
    }
    if (l !== 'null') {
        q.push(`course__level=${l}`);
    }
    if (d !== 'null') {
        q.push(`course__department__id=${d}`);
    }

    list_dom.innerHTML = "<p>Loading ... Please wait</p>";
    loadMaterials(queries=q.join("&"));
});

async function loadMaterials(queries = null, u=null) {
    let url;
    if (u && u !== "null") {
        url = u
    }else{
        url = URL_STR + "?"
    }
    url += queries ? queries : '';
    const response = await fetch(url);
    const data = await response.json();
    populate_dom(data.results);
    pagination(data)
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
    let dialog = document.createElement('dialog')
    let dialog_actions = document.createElement("div")
    dialog_actions.style.borderTop = "1px solid"
    dialog_actions.style.padding = "5px"
    let dialog_close = document.createElement("button")
    dialog_close.innerText = "close"
    dialog_close.style.padding="4px"
    dialog_actions.appendChild(dialog_close)
    dialog.append(obj.comment, dialog_actions)
    dialog.style.position = "fixed"
    dialog.style.top = "40px"
    dialog.style.padding = "10px"
    dialog.style.margin = "40px auto"
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

    btns.append(download, view, report, dialog);
    
    // event listeners
    
    img.addEventListener("click", ()=>dialog.showModal())
    dialog_close.addEventListener("click", ()=>dialog.close())
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


function pagination(data) {
    const next = data.next;
    const previous = data.previous;
    const count = Number.parseInt(data.count);
    let current_page = 1
    if (next !== null) {
        const url_r = new URL(next);
        const params = new URLSearchParams(url_r.search);
        current_page = Number.parseInt(params.get("page"))-1
    }else if (previous !== null) {
        const url_r = new URL(previous);
        const params = new URLSearchParams(url_r.search);
        current_page = Number.parseInt(params.get("page"))+1 | 2
    }

    const createBtn = (text, url) => {
        const btn = document.createElement('button');
        btn.innerText = text;
        //btn.className = "submit-btn";
        btn.addEventListener("click", () => loadMaterials(null, url));
        return btn;
    }
    
    const createPagination=()=>{
        const next_btn = createBtn("ᕗ", next);
        const prev_btn = createBtn("ᕙ", previous);
        if (current_page == 1) {
            prev_btn.disabled = true
        }
        if(current_page == Math.ceil(count / PAGING_MAX)){
        next_btn.disabled = true
        }
        
        const createArr = () => {
            let arr = [];
            let l = Math.ceil(count / PAGING_MAX)+1
            for (let i = 1; i < l; i++) {
                let a = document.createElement('button');
                a.innerText = i;
                a.id = i
                if (current_page === i) {
                    a.disabled = true;
                    
                }
                a.addEventListener("click", () => loadMaterials(`page=${i}`));
                arr.push(a);
            }
            let p,s,e;
            e = 7
            if (current_page>4) {
                s = cp-4
                e = cp+3
            }
            if (current_page>l-7) {
                s = l-8
                e = arr.length
            }
            p = arr.slice(s,e)
            return arr;
        }
        const pageButtons = createArr();
        return [prev_btn, ...pageButtons, next_btn]
    }
    document.querySelectorAll("[pagination]").forEach(pg=>{
    pg.innerHTML = "";
    pg.append( ...createPagination());
    })
  
}
loadMaterials();
