function addTask(){
    let input=document.getElementById("taskInput");
    let task=input.value;
    
    if(task==""){
        alert("Enter a task");
        return;

    }
    let li=document.createElement("li");
    li.textcontent=task;
    //delete button
    let btn=
    document.createElement("button");
    btn.textContent="X";
    btn.onclick=function(){
        li.remove();
    };
    li.appendChild(btn);
    document.getElementById("tasklist").appendChild(li);
    input.value="";
    }
