window.onload = function () {
    //helps making sure the js is linked
    console.log("loaded script_post.js");

    document
        .querySelector("#insertImage")
        .addEventListener("submit", async function (event) {
            //cancels the event if cancelable ?
            event.preventDefault();
            //making sure it's clicked
            console.log("post form clicked")

            //
            let form = document.querySelector("#insertImage");
            let data = new FormData(form);
            console.log(data);

            try {
                let res = await fetch("/conversionComplete", {
                    method: "POST",
                    body: data,
                });

                let resJSON = await res.json();
                //shows the image
                document.querySelector("#result-image").innerHTML = `<img src = ${resJSON.imagePath} />`

                //fix ascii display  in future
                document.querySelector("#result-container").innerHTML = `<pre> ${resJSON.asciiArt} </pre>`
                
                console.log(resJSON);
            } catch (err) {
                console.log(err);
            }


        })
};