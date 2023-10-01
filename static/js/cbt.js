
const questions = document.querySelectorAll("[question]")

questions[0].style.display = "flex"

questions.forEach(elem=>{
    const next = elem.querySelector("[next]")
    const prev = elem.querySelector("[prev]")
    
    next.addEventListener("click", ()=>{
        let nextElem = elem.nextElementSibling
        nextElem.style.display = "flex"
        elem.style.display="none"
        
    })
    prev.addEventListener("click", ()=>{
        let prevElem = elem.previousElementSibling
        prevElem.style.display = "flex"
        elem.style.display="none"
        
    })
})