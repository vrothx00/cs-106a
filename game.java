// Two players have completed a game. The score of Player 1 is saved in a int variable first, and the score of Player 2 in an int variable second.
// If either player scored more points than the other, they are the winner!
// However, if both players tie, then the player that played second is the winner.
//You also have access to a boolean variable firstStarted that is set to true if Player 1 played first and false otherwise.
// Record the result of the game in an existing int variable winner, which you should set to 1
//if Player 1 won and 2 if Player 2 won. (Do not declare winner, simply set its value appropriately.)

if (first > second) {
	winner = 1;
} else if (first == second && !firstStarted) {
	winner = 1;
} else {
	winner = 2;
}
