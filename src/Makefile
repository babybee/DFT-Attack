CFLAGS := -ggdb -Wall -O2 -I ../include

target := ../attack.run
libaries := ../lib/aes/aes.o

$(target): attack.c
	gcc $(CFLAGS) $^ $(libaries) -o $@

.PHONY: clean
clean: 
	rm -f $(target)
