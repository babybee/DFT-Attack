CC := gcc
INCLUDE := ../../include/aes
CFLAGS := -ggdb -Wall -O3 -I $(INCLUDE)

vpath %.h $(INCLUDE)

aes.o: aes_core.c aes_locl.h aes.h
	$(CC) $(CFLAGS) -c $< -o $@

test: test_main.c aes.o
	$(CC) $(CFLAGS) $^ -o $@

.PHONY: clean
clean:
	rm -f aes.o test
