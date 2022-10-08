### Python3 bindings for crystalskyber reference implementation using CFFI

**Note this python3 binding was built just for prototyping and playing around with the reference design for fast-paced development before building it properly in C**


This uses reference design from [kyber]([https://github.com/pq-crystals/kyber.git) and modified slightly to add randombytes to the sharedlibs


##### Getting kyber shared libraries

###### Building kyber
```sh
cd kyber/ref
make shared
```
###### Installing the libs 
```sh
# In the kyber/ref directory
sudo cp libpqcrystals_* /usr/local/lib
```
##### Getting to run the bindings

###### Installing cffi
```sh
pip3 install cffi
```

###### Adding local library path to variable for cffi to know where to look
```sh
export LD_LIBRARY_PATH=/usr/local/lib
```

###### Building python3 bindings
```sh
# In the parent directory kyber-pythonlib
make build
```

###### Test simple encapsulation and decapsulation test

```sh
make run
```

