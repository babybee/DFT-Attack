INCLUDE := ../../include/bma
CFLAGS := -ggdb -Wall -O2 -I $(INCLUDE)

vpath %.h $(INCLUDE)

bma.o: bma.c bma.h
	gcc $(CFLAGS) -c $< -o $@

test: test_bma.c bma.o
	gcc $(CFLAGS) $^ -o $@

.PHONY: clean
clean:
	rm -f *.o test
