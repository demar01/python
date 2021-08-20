console.log("Hello World");
console.log(5); 
/* This is all commented
This is not going to run 
*/
console.log('Hello' + ' '+ 'World');
console.log('Hello'.length); 

const foo= 'Hello world'


// Use .toUpperCase() to log 'Codecademy' in all uppercase letters
console.log('Codecademy'.toUpperCase());
console.log('    Remove whitespace   '.trim());

console.log(Math.random()*100); //  create a random number with Math.random(), then multiply it by 100
console.log(Math.floor(Math.random() * 100)); // create a random number with Math.random(), then multiply it by 100 and to make the output a whole number.
console.log(Math.ceil(43.8)); //returns the smallest integer greater than or equal to a decimal number.
console.log(Number.isInteger(2017)); //method on the built-in Number object that checks if a number is an integer.

//how to use the var, let, and const keywords to create variables.

var favoriteFood = 'pizza';
console.log(favoriteFood);
// Output: favoriteFood

var numOfSlices = 8 ;
console.log(numOfSlices);
// Output: favoriteFood

//let can change whereas var cant
let meal = 'Enchiladas';
console.log(meal); // Output: Enchiladas
meal = 'Burrito';
console.log(meal); // Output: Burrito

let changeMe = true;
changeMe = false;
console.log(changeMe); 

//constant do not change
const entree = 'Enchiladas';
console.log(entree); // Output: Enchiladas

let levelUp = 10;
levelUp+=5
console.log('The value of levelUp:', levelUp); 

//Increment and decrement
let gainedDollar = 3;
let lostDollar = 50;

gainedDollar++;
console.log(gainedDollar); // Output: 4
lostDollar--;
console.log(lostDollar); // Output: 49

