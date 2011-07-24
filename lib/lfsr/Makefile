CC := gcc
INCLUDE := ../../include/lfsr
CFLAGS := -ggdb -Wall -O2 -I $(INCLUDE)

vpath %.h $(INCLUDE)

lfsr.o: lfsr.c lfsr.h
	$(CC) $(CFLAGS) -c $< -o $@

test: test_lfsr.c lfsr.o
	$(CC) $(CFLAGS) $^ -o $@

.PHONY: clean
clean:
	rm -f *.o test
