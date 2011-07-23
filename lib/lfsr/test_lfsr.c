#include <stdio.h>
#include "lfsr.h"

#define LEN 4

int main()
{
	unsigned char state[LEN] = {1}; // or {0xFF}

	unsigned char feedback[LEN] = {1, 1};

	int i;
	
	for (i = 0; i < (2 << (LEN - 1)) - 1; i++) {
		printf("%2x ", state[0]);
		lfsr(state, state, feedback, LEN);
	}
	printf("\n");
	for (i = 0; i < (2 << (LEN - 1)) - 1; i++) {
		printf("%2x ", state[0]);
		lfsr(state, state, feedback, LEN);
	}
	printf("\n");
		
	return 0;
}
