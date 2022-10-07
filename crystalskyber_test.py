from _libpqccrystals_kyber_cffi import ffi, lib


_CRYPTO_PUBLICKEYBYTES = 1568 # 1184*2
_CRYPTO_SECRETKEYBYTES = 3168 #2400*2
_KEX_AKE_SENDABYTES = 2272*2
_KEX_AKE_SENDBBYTES = 2176*2
_KEX_SSBYTES = 32

pka = ffi.new("uint8_t[]", _CRYPTO_PUBLICKEYBYTES)
ska = ffi.new("uint8_t[]", _CRYPTO_SECRETKEYBYTES)

pkb = ffi.new("uint8_t[]", _CRYPTO_PUBLICKEYBYTES)
skb = ffi.new("uint8_t[]", _CRYPTO_SECRETKEYBYTES)

eska = ffi.new("uint8_t[]", _CRYPTO_SECRETKEYBYTES)

ake_senda = ffi.new("uint8_t[]", _KEX_AKE_SENDABYTES)
ake_sendb = ffi.new("uint8_t[]", _KEX_AKE_SENDBBYTES)

tk = ffi.new("uint8_t[]", _KEX_SSBYTES)
ka = ffi.new("uint8_t[]", _KEX_SSBYTES)
kb = ffi.new("uint8_t[]", _KEX_SSBYTES)

zero = ffi.new("uint8_t[]", _KEX_SSBYTES)

ct = ffi.new("uint8_t[]", _CRYPTO_PUBLICKEYBYTES) 

lib.pqcrystals_kyber1024_ref_keypair(pka,ska)
lib.pqcrystals_kyber1024_ref_keypair(pkb,skb)



lib.pqcrystals_kyber1024_ref_enc(eska, ka, pkb)

print("eksa\t ka \t pkb \n")
for i in range(32):
    print("{0}\t {1}\t {2}\n ".format(eska[i], ka[i], pkb[i]))

lib.pqcrystals_kyber1024_ref_dec(kb, eska, skb)


print("kb\t eska \n")
for i in range(32):
    print("{0}\t {1}\n ".format(kb[i], eska[i]))