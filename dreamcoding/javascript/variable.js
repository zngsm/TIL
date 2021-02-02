// added ECMAScript 5
'use strict';

// 2. variable
// let (added in ES6)
let globalName = 'global name'
{
    let name = 'ellie';
    console.log(name);
    name = 'hello';
    console.log(name);
    console.log(globalName);
}
// global 선언은 계속 데이터로 남기 때문에, 함수에서 로컬내 선언하여 사용하는 것이 데이터 활용에 효율적이다
console.log(name);
console.log(globalName);

// var 이젠 쓰지마세요
console.log(age); // let 이었으면 선언도 전에 출력해서 error가 나와야하는 상황이지만 undefined가 나온다
age = 4;
console.log(age); // 역시 선언 전이지만 4가 출력된다
var age;

// why? 
// hoisting : 어디에 선언하든 제일 위로 선언을 끌어올려준다

// var는 block scopr를 무시할 수 있다

