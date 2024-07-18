function clickTest() {
    console.log('test')
    var inputText = document.getElementById('my-input').value
    var inputColor = document.getElementById('my-input-2').value
    document.getElementById('hello-h1').textContent = inputText
    document.getElementById('hello-h1').style.color = inputColor
}

function plusOne() {
    var current = document.getElementById('hello-calc').textContent
    current = Number(current) + 1
    document.getElementById('hello-calc').textContent = current
    if (current % 7 == 1){
        document.getElementById('hello-calc').style.color = 'red'
    } else if (current % 7 == 2){
        document.getElementById('hello-calc').style.color = 'orange'
    } else if (current % 7 == 3){
        document.getElementById('hello-calc').style.color = 'yellow'
    }else if (current % 7 == 4){
        document.getElementById('hello-calc').style.color = 'green'
    } else if (current % 7 == 5){
        document.getElementById('hello-calc').style.color = 'blue'
    }else if (current % 7 == 6){
        document.getElementById('hello-calc').style.color = 'purple'
    } else if (current % 7 == 0){
        document.getElementById('hello-calc').style.color = 'pink'
    }
}

function plusTwo() {
    // todo: for lucas   
    var current = document.getElementById('hello-calc').textContent
    current = Number(current)+2
    document.getElementById('hello-calc').textContent = current
}

function plusThree() {
    // todo: for lucas   
    var current = document.getElementById('hello-calc').textContent
    current = Number(current)+3
    document.getElementById('hello-calc').textContent = current
}

function Minusone() {
    // todo: for lucas   
    var current = document.getElementById('hello-calc').textContent
    current = Number(current)-1
    document.getElementById('hello-calc').textContent = current
    if (current % 7 == 1){
        document.getElementById('hello-calc').style.color = 'red'
    } else if (current % 7 == 2){
        document.getElementById('hello-calc').style.color = 'orange'
    } else if (current % 7 == 3){
        document.getElementById('hello-calc').style.color = 'yellow'
    }else if (current % 7 == 4){
        document.getElementById('hello-calc').style.color = 'green'
    } else if (current % 7 == 5){
        document.getElementById('hello-calc').style.color = 'blue'
    }else if (current % 7 == 6){
        document.getElementById('hello-calc').style.color = 'purple'
    } else if (current % 7 == 0){
        document.getElementById('hello-calc').style.color = 'pink'
    }
}

function TimesTwo() {
    // todo: for lucas   
    var current = document.getElementById('hello-calc').textContent
    current = Number(current)*2
    document.getElementById('hello-calc').textContent = current
}

function RED() {
    document.getElementById('hello-calc').style.color = 'red'
}

function BLUE() {
    document.getElementById('hello-calc').style.color = 'blue'
}

function CHANGE_COLOR() {
    var current_value = Number(document.getElementById('hello-calc').textContent)
    console.log(current_value)
    if (current_value % 9 === 0) {
        document.getElementById('hello-calc').style.color = 'red'  
    }else if (current_value % 2 === 0) {
        document.getElementById('hello-calc').style.color = 'green'  
    }
     else {
        document.getElementById('hello-calc').style.color = 'blue'
    }

}