CC := gcc
CFLAGS := -ggdb -Wall -O3 -static -I include
MAKE := make

target := attack.run

aes := lib/aes
dft := lib/dft
lsfr := lib/lsfr

#libraries := $(aes) $(dft) $(lsfr)
libraries := $(aes)

VPATH = src

$(target): attack.c $(libraries)
	$(CC) $(CFLAGS) $< $(aes)/aes.o -o $@

.PHONY: $(libraries)
$(libraries):
	$(MAKE) --directory=$@

.PHONY: clean
clean: 
	rm -f $(target)
	for d in $(target) $(libraries); 	\
	do					\
		$(MAKE) --directory=$$d clean; 	\
	done

