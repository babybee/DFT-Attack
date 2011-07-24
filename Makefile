CFLAGS := -ggdb -Wall -O2 -I include

target := src

aes := lib/aes
dft := lib/dft
lfsr := lib/lfsr
bma := lib/bma

#libraries := $(aes) $(dft) $(lfsr) $(bma)
libraries := $(aes) $(lfsr)

.PHONY: $(target) $(libraries)
$(target) $(libraries):
	make --directory=$@

$(target): $(libraries)

$(dft): $(bma)

.PHONY: clean
clean: 
	for d in $(target) $(libraries); do make --directory=$$d clean; done

