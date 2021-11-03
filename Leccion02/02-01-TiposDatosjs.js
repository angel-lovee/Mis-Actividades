/* ejemplo de 
tipos de datos
*/


// Tipo de dato string
var nombre = "Angel";
console.log(typeof nombre);


nombre = 10.5;
console.log(typeof nombre);


// Tipo de datos numerico
var numero = 2000;
console.log(numero);

//Tipo de datos object
var objeto = {
    nombre : "Angel",
    apellido : "Pineda",
    telefono : "8984983"
}

console.log(typeof objeto);


//Tipo de dato boolean (true,false)
var bandera = true;
console.log(typeof bandera);

//tipo de dato funtion
function miFuncion(){}
console.log(typeof miFuncion);

//tipo de dato symbol
var simbolo = Symbol("mi simbolo");
console.log(typeof simbolo);

//Tipo de clases es una function
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

//tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);


//null = ausencia de valor
var y = null;
console.log(typeof y);


//arrays = /object
var autos = ['BMW', 'Audi', 'Volvo', ];
console.log( autos);
console.log(typeof autos);


var z = '';
console.log(z);
console.log(typeof z);