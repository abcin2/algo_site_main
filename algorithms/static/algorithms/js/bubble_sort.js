// this works now!

// still considering using React as front end framework
// if I do that, I will need a REST API to connect to

let bar_data = document.getElementById('data-container')
let bar = document.getElementById('bar')

// console.log(bar_data.children)
for (let i = 0; i < bar_data.childElementCount; i++) {
    console.log(bar_data.children[i].innerHTML)
}
