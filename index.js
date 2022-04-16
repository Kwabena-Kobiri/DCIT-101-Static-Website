// console.log('Hello world')

// Variables in JavaScript
// let a = 45;
// let b = 67;
// const c = 100
// console.log(a + b);

// Functions in JavaScript
// function add(a, b){
//     console.log(a + b);
// } 
// add(45, 67);

// Arrow functions
// const add = a => console.log(a + 80);
// add(20);

// console.log(window);

// const head = document.getElementById('header');
// const nav = document.getElementsByTagName('ul');

// console.log(head);
// console.log(nav);

// const a = document.querySelector('p');
// console.log(a);

// Adding an event in our page with the submit button
MyForm = document.querySelector('#Form');

// console.log(MyForm);

MyForm.addEventListener('submit', onSubmit);

function onSubmit(event){
    event.preventDefault();
    alert("Form not configured. Reach me via yellocode.club@gmail.com");
}

// Changing the background of the LandingPage after a few seconds 
// as soon as someone comes unto the platform.

// setTimeout(function(){}, 2000);

setTimeout(() => {
    greet = document.querySelector('.Details');
    greet.children[0].innerText = 'Hello';
    document.querySelector('#LandingPage').style.background = 'linear-gradient(to right, #43e97b 0%, #38f9d7 100%)';
}, 3000);
