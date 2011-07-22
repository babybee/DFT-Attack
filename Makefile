CC = gcc
CFLAGS = -ggdb -Wall -O3 -static
OBJECT = aes_test.o

$(OBJECT): aes_test.c aes.o
	$(CC) $(CFLAGS) -o $@ $^

aes.o: aes_core.c aes_locl.h aes.h
	$(CC) $(CFLAGS) -c -o $@ $<

.PHONY: clean
clean:
	rm -f *.o
	
