let star = '*'
for (let i=0; i<5; i++) {
    let space = ''
    for (let j=0; j<4-i; j++) {
        space += ' '
    }
    console.log(space + star + space)
    star += '**'
}

// 문자열 빼기는 안된다..
// 별은 두 개씩 늘고
// 공간은 앞 뒤 구분하면 한 개씩 줄어든다..
// 반복문을 통해 공간을 처음에 4개 붙여서 만들고
// 그다음은 3개.. 이런식으로 하면된다.