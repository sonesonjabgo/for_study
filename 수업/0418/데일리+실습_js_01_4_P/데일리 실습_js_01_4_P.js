const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
	// 작성해 주세요
	if (p1_choice === 'rock') {
		if (p2_choice === 'rock') {
			return '0'
		} else if (p2_choice === 'scissors') {
			return '1'
		} else if (p2_choice === 'paper') {
			return '2'
		}
	}
	else if (p1_choice === 'scissors') {
		if (p2_choice === 'rock') {
			return '2'
		} else if (p2_choice === 'scissors') {
			return '0'
		} else if (p2_choice === 'paper') {
			return '1'
		}
	}
	else if (p1_choice === 'paper') {
		if (p2_choice === 'rock') {
			return '1'
		} else if (p2_choice === 'scissors') {
			return '2'
		} else if (p2_choice === 'paper') {
			return '0'
		}
	}
}

for (let i=0; i<10; i++){
	console.log(playGame(p1[i], p2[i]))
}
// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2