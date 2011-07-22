CC = gcc
CFLAGS = -ggdb -Wall -O3 -static

test: test_main.c aes.o
	$(CC) $(CFLAGS) $^ -o $@

aes.o: aes_core.c aes_locl.h aes.h
	$(CC) $(CFLAGS) -c $< -o $@

.PHONY: clean
clean:
	rm -f aes.o test
