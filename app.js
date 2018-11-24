const inputValue = document.querySelector("#search");
const searchButton = document.querySelector(".searchButton");
const nameContainer = document.querySelector(".main__profile-name");
const unContainer = document.querySelector(".main__profile-username");
const reposContainer = document.querySelector(".main__profile-repos");
const urlContainer = document.querySelector(".main__profile-url");
const client_id = "1a5afd0975169dac1e83";
const client_secret="a165dbd28f3c7dd3d4be06ef998a465319ff90c6";

const fetchUsers =async (user)=>{
  const api_call = await fetch(`https://api.github.com/users/${user}?client_id=${client_id}&client_secret=${client_secret}`);

  const data = await api_call.json();
  return {data}
};

const showData = ()=>{
  fetchUsers(inputValue.value).then((res)=>{
    let followers;
    let repos;
    repos = res.data.public_repos
    followers = res.data.followers;
    console.log(res)
    console.log(repos)
    return repos
  })
};

const  showData2 = async (username)=>{
  fetchUsers(username).then((res)=>{
    let followers;
    let repos;
    repos = await(res.data.public_repos)
    followers = res.data.followers;
    console.log(repos);
    return repos;
  })
};

searchButton.addEventListener("click", ()=>{
   showData();  });


//https://github.com/users/DumbMachine/contributions?to=2018-24-18
  //const usernames = ["DumbMachine","war-turtle","nkkumawat","MacBox7","avinashbharti97","phoenixking25"];
//let constributions = {};
//for(let i=0;i<usernames.length;i++){
  //constributions[usernames[i]] = showData(usernames[i]);
  //console.log(constributions);