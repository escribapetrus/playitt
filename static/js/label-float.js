document.addEventListener('DOMContentLoaded',
    () => {
        let labels = document.querySelectorAll("label");
        let inputs = document.querySelectorAll("input")

        //remove colons from labels
        labels.forEach(el => {
            el.innerText = el.innerText.replace(/:/,"")
        })

        //make labels float
        inputs.forEach(el => {
            el.addEventListener('focus', () => {
                let elLabel = el.parentElement.querySelector("label")
                elLabel.classList.add("label-tiny")                
                elLabel.classList.add("focused")  
            })
            el.addEventListener('blur', () => {
                let elLabel = el.parentElement.querySelector("label")
                if (el.value == ""){
                    elLabel.classList.remove("label-tiny")                
                    elLabel.classList.remove("focused")                
                }
                else {
                    elLabel.classList.remove("focused")                
                }
            })
        })
    }
)
