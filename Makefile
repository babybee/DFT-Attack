CC := gcc
CFLAGS := -ggdb -Wall -O3 -static
MAKE := make

target := attack

lib_aes := lib/aes
lib_dft := lib/dft
lib_lsfr := lib/lsfr

#libraries := $(lib_aes) $(lib_dft) $(lib_lsfr)
libraries := $(lib_aes)

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

