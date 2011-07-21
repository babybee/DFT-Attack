CC = gcc
CFLAGS = -g -Wall 
OBJECT = aes_test.o

$(OBJECT): aes_test.c aes.o
	$(CC) $(CFLAGS) -o $@ $^
	chmod u+x $(OBJECT)

aes.o: aes_core.c aes_locl.h aes.h
	$(CC) $(CFLAGS) -c -o $@ $<

.PHONY: clean
clean:
	rm -f *.o
	
