CC := gcc
CFLAGS := -ggdb -Wall -O3 -static
MAKE := make

target := attack

aes := lib/aes
dft := lib/dft
lsfr := lib/lsfr

#libraries := $(aes) $(dft) $(lsfr)
libraries := $(aes)

.PHONY: all
all: $(target)

$(target) $(libraries):
	$(MAKE) --directory=$@

$(target): $(libraries)

.PHONY: clean
clean: 
	for d in $(target) $(libraries); 	\
	do					\
		$(MAKE) --directory=$$d clean; 	\
	done

