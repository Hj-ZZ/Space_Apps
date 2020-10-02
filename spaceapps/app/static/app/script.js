// color palette: https://coolors.co/d8f3dc-b7e4c7-95d5b2-74c69d-52b788-40916c-2d6a4f-1b4332-081c15?fbclid=IwAR2UJybevPTT7gSHFo_2lO60J3uU9Jvuuz2vz9UtF8B6IEv1Sy7K31tn6P4

const menu = document.querySelector('.menu-icon');
const m1 = document.querySelector('#m-1');
const m2 = document.querySelector('#m-2');
const navbar = document.querySelector('.navbar-nav');
const closef = document.querySelector('.fa-times-circle');
const join = document.querySelector('.join');
let mclosed = true;


//Page animations

TweenMax.from('.left-half', 3.5, {
    opacity: 0,
});

TweenMax.from(navbar, 3, {
    delay: 0.4,
    y : -100
});

TweenMax.from('.social-media', 3, {
    delay: 0.4,
    x : -250 
});

//Menu

menu.addEventListener('click', ()=>{
    if(mclosed == true){
        TweenMax.to(".navbar-nav", 1, {
            delay : 0,
            visibility : 'visible',
        })
        TweenMax.to(".navbar-nav", 0.3, {
            delay : 0.5,
            opacity : 1,
        })
        TweenMax.to(".link-text", 1, {
            delay : 2.5,
            opacity: 1,
        })
        TweenMax.to("#m-1", 0.5, {
            delay : 2.5,
            opacity: 1,
            transform : 'rotateZ(-45deg)',
            margin: '0',
            height: '2px'
        })
        TweenMax.to("#m-2", 0.5, {
            delay : 1,
            width: '30px',
        })
        TweenMax.to("#m-2", 0.5, {
            delay : 2.5,
            width: '30px',
            transform : 'rotateZ(45deg)',
            margin: '0',
            height: '2px'
        })
        mclosed = false;
    }else{
        TweenMax.to(".navbar-nav", 1, {
            delay : 1,
            visibility : 'hidden',
        })
        TweenMax.to(".navbar-nav", 1, {
            delay : 0.5,
            opacity: 0,
        })
        TweenMax.to(".link-text", 1, {
            delay : 0.5,
            opacity: 0,
        })
        TweenMax.to("#m-1", 0.5, {
            delay : 1,
            opacity: 1,
            margin: '6px 0 6px 0',
            height: '1px',
            transform : 'rotateZ(0deg)',
        })
        TweenMax.to("#m-2", 0.5, {
            delay : 1,
            margin: '6px 0 6px 0',
            height: '1px',
            transform : 'rotateZ(0deg)'
        })
        TweenMax.to("#m-2", 1, {
            delay : 2.2,
            width: '20px',
        })
        mclosed = true;
    }
});

//forms

document.addEventListener('DOMContentLoaded',function(){
    const signUpButton = document.getElementById('signUp');
    const signInButton = document.getElementById('signIn');
    const container = document.getElementById('container');

    signUpButton.addEventListener('click', () => {
        container.classList.add("right-panel-active");
    });

    signInButton.addEventListener('click', () => {
        container.classList.remove("right-panel-active");
    });
});

closef.addEventListener('click', ()=>{
    TweenMax.to('.forms', 0.5,{
        opacity: 0,
    })
    TweenMax.to('.forms', 0.01,{
        delay: 0.5,
        visibility: 'hidden'
    })
    TweenMax.to('.menu-icon', 0.01,{
        visibility: 'visible',
    })
});

join.addEventListener('click', ()=>{
    TweenMax.to('.forms', 0.01,{
        visibility: 'visible',
    })
    TweenMax.to('.forms', 0.5,{
        delay: 0.2,
        opacity: 1,
    })
    TweenMax.to('.menu-icon', 0.01,{
        visibility: 'hidden',
    })
})