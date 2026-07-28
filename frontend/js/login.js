const API = "http://127.0.0.1:8000";

document
.getElementById("loginBtn")
.addEventListener("click", login);

async function login() {

    const username =
        document.getElementById("username").value;

    const password =
        document.getElementById("password").value;

    if(!username || !password){

        alert("Enter Username & Password");

        return;

    }

    try{

        const response = await fetch(

            `${API}/login`,

            {

                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({

                    username,
                    password

                })

            }

        );

        const data = await response.json();

        if(data.status==="success"){

            localStorage.setItem(

                "token",

                data.access_token

            );

            window.location.href="/dashboard";

        }

        else{

            alert(data.message);

        }

    }

    catch(err){

        console.error(err);

        alert("Server Error");

    }

}