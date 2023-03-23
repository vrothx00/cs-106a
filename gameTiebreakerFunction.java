/*
 *Two players have completed a game.
 Write a method (or function) named whoWon to determine the winner!
 */

 int whoWon(int first, int second, boolean firstStarted) {
	int winner =1;
	if (first > second) {
		winner = 1;
	} else if (second > first) {
		winner = 2;
	} else if (!firstStarted) {
		winner = 1;
	} else {
		winner = 2;
	}
	return winner;
 }
