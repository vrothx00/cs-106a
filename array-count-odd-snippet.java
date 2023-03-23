// Given an int[] named array that is previously declared and initialized,
// write a snippet of code (not a method),
// that prints a line with the count of the number of values in array that are odd.

int count = 0;
for (int i = 0; i < array.length; i++) {
	if (array[i] % 2 != 0) {
		count++;
	}
}

System.out.println(count);
