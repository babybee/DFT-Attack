#include <stdio.h>
#include "lfsr.h"

#define ONE 	1
#define ZERO 	0

#define LEN	2

int main()
{
	unsigned char state[LEN] = {ONE, ONE};

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
