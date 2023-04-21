console.clear();
function buscadordeapart(blocks, reqs) {
  const distancias = Array(blocks.length).fill(0, 0, blocks.length);

  // Para cada requerimiento, calcula la distancia de cada bloque a ese requerimiento
  for (const req of reqs) {
    for (let b = 0; b < blocks.length; b++) {
      let menordistancia = Infinity;
      for (let s = 0; s < blocks.length; s++) {
        if (blocks[s][req]) {
          const distancia = Math.abs(b - s);
          if (distancia < menordistancia) {
            menordistancia = distancia;
          }
        }
      }
      distancias[b] += menordistancia;
    }
  }

  // Encuentra el índice del apartamento que tenga la menor suma de distancias
  let mindistancia = Infinity;
  let result;
  for (let i = 0; i < distancias.length; i++) {
    if (distancias[i] < mindistancia) {
      mindistancia = distancias[i];
      result = i;
    }
  }

  return result;
}

const blocks = [
{},{"Mall":true},{},{"Barber Shop":true},{"Park":true},{"Gas Station":true},{"Kindergarten":false},{},{"Gas Station":true,"Hospital":false},{"Mall":true,"Beauty Salon":true},{"Mall":true,"Beauty Salon":true},{"Bar":true},{},{"Cofee shop":true},{"Grocery":true,"Kindergarten":true},{"Gas Station":false,"Mall":false},{},{"Beauty Salon":true},{"Clinic":true,"Mall":false},{},{"Gym":true,"Bakery":false},{},{},{"Mall":true,"Park":true},{"Clinic":true},{"Barber Shop":true},{"Clinic":true,"Barber Shop":true},{"Gym":false,"Gas Station":false},{"Gas Station":true,"Academy":false},{"Vet":false},{"Restaurant":true},{},{},{},{"Mall":true},{},{"Mall":false,"Vet":true},{"Academy":false,"Beauty Salon":false,"Cofee shop":true},{},{"Bar":true,"Academy":false},{"Restaurant":true,"Beauty Salon":true,"Kindergarten":true},{},{},{"Beauty Salon":true,"Vet":false,"Barber Shop":true},{"Academy":true},{},{"Clinic":true},{"Bar":true,"Hospital":true},{"Clinic":true},{"Pharmacy":false,"Bakery":true},{"Mall":true,"Vet":true},{},{"Bar":true},{"Hospital":false},{},{"Hospital":true},{"Academy":true,"Clinic":true,"Mall":true},{},{"Bakery":true,"Beauty Salon":false},{"Kindergarten":true,"Cofee shop":true},{},{"Gym":true},{"Barber Shop":true},{"Bakery":false},{},{},{"Vet":false,"Hospital":true},{"Vet":true},{"Bakery":true,"Kindergarten":true},{"Gas Station":true,"Mall":false,"Bakery":true},{"Mall":false,"Vet":true},{"Vet":true},{"Mall":false},{"Academy":false},{},{"Hospital":true},{"Mall":true,"Beauty Salon":true},{"Bakery":true,"Vet":true},{"Park":true},{"Grocery":true},{"Academy":true},{},{"Restaurant":true},{"Bakery":false},{"Gym":false,"Park":true},{},{},{"Restaurant":false,"Gym":false},{},{"Academy":true},{},{},{"Cofee shop":true},{"Academy":true},{},{},{"Vet":false,"Restaurant":true},{"Beauty Salon":true},{},{},{"Gas Station":true,"Hospital":true},{"Mall":true,"Clinic":true,"Vet":false},{"Bar":false,"Gym":true},{"Mall":true,"Vet":true},{"Vet":true,"Cofee shop":true},{},{"Vet":false,"Park":false,"Academy":false},{"Pharmacy":true},{"Barber Shop":false},{},{"Gym":false},{"Clinic":true},{"Clinic":true},{"Bakery":true},{"Hospital":true,"Gas Station":true},{"Cofee shop":true},{"Beauty Salon":false},{"Mall":false,"Bar":true,"Beauty Salon":true},{"Barber Shop":true,"Vet":true},{"Park":false},{"Academy":true},{"Park":false},{"Cofee shop":true},{},{},{},{"Bakery":true,"Grocery":false},{},{"Mall":true,"Hospital":false,"Cofee shop":true},{},{}];
const reqs = ["Vet","Kindergarten","Gas Station"];

console.log(buscadordeapart(blocks, reqs));