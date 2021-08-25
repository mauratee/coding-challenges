animals = [
    { name: 'Fluffykins', species: 'dog'},
    { name: 'Hamilton', species: 'dog'},
    { name: 'Ursula', species: 'fish'},
    { name: 'Baby', species: 'cat'}
]

var dogs = animals.filter(function(animal) {
    return animal.species === 'dog'
})

console.log(dogs);

var names = animals.map((animal) => animal.name)

console.log(names);