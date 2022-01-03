const fs = require('fs');

let leastFuel = 0
let leastFuelPartTwo = 0

// Part 1
function findLeastFuel(data) {
    let seen = false;

    for (let currAlignment = data.length - 1; currAlignment >= 0; currAlignment--) {
        let tempLeastFuel = 0

        for (fuelNum of data) {
            tempLeastFuel += Math.abs(fuelNum - currAlignment)
        }
        if (!seen) {
            seen = true;
            leastFuel = tempLeastFuel;
        } else if (tempLeastFuel < leastFuel) {
            leastFuel = tempLeastFuel;
        }

        tempLeastFuel = 0
    }
    return leastFuel;
}

// Part 2
function findLeastFuelPartTwo(data) {
    let seen = false;

    for (let currAlignment = data.length - 1; currAlignment >= 0; currAlignment--) {
        let tempLeastFuel = 0

        for (fuelNum of data) {
            const absFuel = Math.abs(fuelNum - currAlignment);
            // Utilizing binomial coefficient formula
            tempLeastFuel += (((Math.pow(absFuel,2)) + absFuel)/2)
        }
        if (!seen) {
            seen = true;
            leastFuelPartTwo = tempLeastFuel;
        } else if (tempLeastFuel < leastFuelPartTwo) {
            leastFuelPartTwo = tempLeastFuel;
        }

        tempLeastFuel = 0
    }
    return leastFuelPartTwo;
}

fs.readFile('../input/7ab.txt', 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    } else {
        sortedData = data.split(',').map(x => parseInt(x, 10)).sort((x, y) => x - y);
        const part1Answer = findLeastFuel(sortedData);
        console.log('Part One Answer: ' + part1Answer);

        const part2Answer = findLeastFuelPartTwo(sortedData);
        console.log('Part Two Answer: ' + part2Answer);
    }
}); 