const fs = require('fs');

const character_lib = {
    '(': {
        'closing': ')',
        'points': 3
    },
    '[': {
        'closing': ']',
        'points': 57
    },
    '{': {
        'closing': '}',
        'points': 1197
    },
    '<': {
        'closing': '>',
        'points': 25137
    }
};

const illegalCharPoints = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
};

const incompleteCharPoints = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
};

let part2Scores = [];

function processPart1(data) {
    let condition = true;

    // While there are still closing characters in array.
    while (condition) {
        const finalCondition = data.find(item => !(item in character_lib));

        // If all characters in array are opening. This is the array of incompletes.
        if (!finalCondition) {
            let tempScore = 0;

            data.reverse().forEach(i =>
                tempScore = (tempScore *= 5) + incompleteCharPoints[character_lib[i].closing]
            )

            part2Scores.push(tempScore);
            condition = false;
        }

        // Check for opening and closing characters and remove until a mismatch is found.
        for (const [index, singleChar] of data.entries()) {
            if (!(singleChar in character_lib)) {
                if (singleChar !== (character_lib[data[index-1]] ? character_lib[data[index-1]].closing : singleChar)) {
                    return (illegalCharPoints[singleChar]);
                }
                else if (character_lib[data[index-1]] ? character_lib[data[index-1]].closing : '' == data[index-1]) {
                    data.splice(index, 1);
                    data.splice(index-1, 1);
                }
            }
        }
    }
}

fs.readFile('../input/10ab.txt', 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    } else {
        let charGroupList = [];
        let score1 = 0;
        const tempArr = data.split("\n");

        for (const line of tempArr) {
            charGroupList.push([...line]);
        }

        for (const group of charGroupList) {
            score1 +=  processPart1(group) ? processPart1(group) : 0;
        }

        console.log('Final Part 1: ' + score1);

        const k = part2Scores.sort((x, y) => x - y);
        const middle = k[parseInt((k.length-1)/2)];
        console.log('Final Part 2: ' + middle);
    }
});
