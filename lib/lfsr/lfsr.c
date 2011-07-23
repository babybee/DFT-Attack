#include "lfsr.h"

void lfsr(const unsigned char *in, unsigned char *out, const unsigned char *coeffs, const int length)
{
	int i;
	unsigned char temp = 0;

	if (length > 0) {
		if (0 != coeffs[0])
			temp = in[0];
	}

	for (i = 1; i < length; i++) {
		if (0 != coeffs[i])
			temp ^= in[i];
		out[i - 1] = in[i];
	}

	out[length - 1] = temp;
}

