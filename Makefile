CC=python3
ciif_src= crystalskyber_build.py

src= crystalskyber_test.py

artifacts= _libpqccrystals_kyber_cffi*

build:
	$(CC) $(ciif_src)

run:
	$(CC) $(src)

clean:
	rm $(artifacts)


