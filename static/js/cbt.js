
const questions = document.querySelectorAll("[question]")

questions[0].style.display = "flex"
const listOfInputClass = []
class InputClass{
    constructor(inputs, key, elem){
        this.inputs = inputs
        this.key = key + 1
        this.elem = elem
        this.b = null
        this.createBox()
        
    }
    createBox(){
        this.b = document.createElement('button')
        let qs = document.querySelector("[questions]")
        this.b.innerText = this.key
        this.b.style.width= "30px"
        this.b.style.height = "30px"
        this.b.style.border = "1px solid"
        qs.appendChild(this.b)
        this.b.addEventListener("click", ()=>this.select(this.elem))
    }
    select(elem){
        let elm = document.getElementById("q"+this.key)
        questions.forEach(el=>el.style.display="none")
        questions[this.key-1].style.display = "flex"
        this.position()
    }
    checked(){
        const isAtLeastOneChecked = this.inputs.some(input => input.checked);
        if (isAtLeastOneChecked) {
            this.b.style.backgroundColor = "lightblue"
        }else{
            this.b.style.backgroundColor = "#ff2b4ace"
        }
    }
    position(p, b=false){
        listOfInputClass.forEach(el=>el.b.style.borderColor="black")
       if(p){ 
       if (b) {
           listOfInputClass[this.key-2].b.style.borderColor = "orange"
       }else{
           listOfInputClass[this.key].b.style.borderColor = "orange"}
        }else listOfInputClass[this.key-1].b.style.borderColor = "orange"
    }
}



questions.forEach((elem,key)=>{
    const next = elem.querySelector("[next]")
    const prev = elem.querySelector("[prev]")
    const inputs = Array.from(elem.querySelectorAll("input"));

    const inputClass = new InputClass(inputs, key, elem)
    listOfInputClass.push(inputClass)
    next.addEventListener("click", ()=>{
        let nextElem = elem.nextElementSibling
        nextElem.style.display = "flex"
        elem.style.display="none"
        inputClass.checked()
        inputClass.position(true, false)
    })
    prev.addEventListener("click", ()=>{
        let prevElem = elem.previousElementSibling
        prevElem.style.display = "flex"
        elem.style.display="none"
        inputClass.checked()
        inputClass.position(true, b=true)
    })
})

