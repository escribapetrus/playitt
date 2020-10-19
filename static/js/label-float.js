
document.addEventListener('DOMContentLoaded',
    () => {
        let labels = document.querySelectorAll("label");
        let inputs = document.querySelectorAll("input");

        // add floating labels to filled inputs
        inputs.forEach(el => {
            let elLabel = el.parentElement.querySelector("label")
            el.autofocus = false;
            if (el.value.length > 1 && el.parentElement.tagName == "FIELDSET"){
                elLabel.classList.add("label-tiny")
            }
        })
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
