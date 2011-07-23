CC := gcc
CFLAGS := -ggdb -Wall -O3 -I include
MAKE := make

target := attack.run

aes := lib/aes
dft := lib/dft
lfsr := lib/lfsr

#libraries := $(aes) $(dft) $(lfsr)
libraries := $(aes) $(lfsr)

VPATH = src

$(target): attack.c $(libraries)
	$(CC) $(CFLAGS) $< $(aes)/aes.o -o $@

.PHONY: $(libraries)
$(libraries):
	$(MAKE) --directory=$@

.PHONY: clean
clean: 
	rm -f $(target)
	for d in $(libraries); 			\
		do $(MAKE) --directory=$$d clean; done

