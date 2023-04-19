const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

function solve(array) {
    array.sort(function(a, b) {
        return a - b
    })
    for(let i =0;i<array.length;i++){
        if (i%2 === 0) {
            if (array[i] !== array[i+1]) {
                return array[i]
            }
        }
    }

    // for (let num in array) { 
    //     console.log(typeof Number(num))
    //     if (num % 2 === 0) {
    //         console.log(array[num])
    //         console.log(num)
    //         console.log(num + 1)
    //         if (array[num] !== array[num+1]) {
    //             return array[num]
    //         }
    //     }
    // }
}
// 3
// 100
// 62

for (array of participantNums) {
    console.log(solve(array))
    console.log(array)
}