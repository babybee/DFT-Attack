CC := gcc
CFLAGS := -ggdb -Wall -O3 -static
MAKE := make

target := app/aes-correlation-attack

lib_aes := lib/aes
lib_dft := lib/dft
lib_lsfr := lib/lsfr

libraries := $(lib_aes) $(lib_dft) $(lib_lsfr)

.PHONY: all
all: $(target)

$(target) $(libraries):
	$(MAKE) --directory=$@

$(target): $(libraries)

.PHONY: clean
clean: 
	
