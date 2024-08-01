const form = document.querySelector(".form");
const siteData = document.querySelector(".wrapper")
const backButton = document.querySelector(".back")
async function postData(url = '', data){

    const respone = await fetch(url, {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
    });

    return respone.json()
}

async function getData(url = ''){

    const respone = await fetch(url, {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
        }
    });

    return respone.json()
}

form.addEventListener("submit", e => {

    answerArray = [];

    e.preventDefault();
    children = [...e.target.children]
    children.forEach(e => {

        if(e.children[1] !== undefined){

            answerArray.push(e.children[1].value); 
        }
    });

    postData("http://localhost:8000/calculated", answerArray).then(e => {
        
        console.log(e.message)
        const format = `
                <h2>The predicted price is:</h2>
                <div class="form" style="text-align: center; font-size: 50px">${parseInt(e.price)}€</div>
            `;
        backButton.classList.remove("back");
        backButton.classList.add("backAfter");
        siteData.innerHTML = format;
    });
});
