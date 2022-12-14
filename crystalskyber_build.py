from cffi import FFI
import os
ffibuilder = FFI()
libcint_dir = os.path.expanduser('/usr/local/libs/')
# cdef() expects a single string declaring the C types, functions and
# globals needed to use the shared object. It must be in valid C syntax.
ffibuilder.cdef("""
    // Choose the bytes according to the chosen algorithm that's being linked 
    // Currently initialised with 0 to make sure that it fails if not chosen
    
    #define KYBER_INDCPA_SECRETKEYBYTES 0
    #define KYBER_INDCPA_PUBLICKEYBYTES 0
    #define KYBER_SYMBYTES 0
    #define KYBER_INDCPA_BYTES 0
    #define KYBER_INDCPA_MSGBYTES 0
    int pqcrystals_kyber1024_ref_keypair(uint8_t *pk, uint8_t *sk);
    int pqcrystals_kyber1024_ref_enc(uint8_t *ct, uint8_t *ss, const uint8_t *pk);
    int pqcrystals_kyber1024_ref_dec(uint8_t *ss, const uint8_t *ct, const uint8_t *sk);
    
    void indcpa_keypair(uint8_t pk[KYBER_INDCPA_PUBLICKEYBYTES],uint8_t sk[KYBER_INDCPA_SECRETKEYBYTES]);
    void indcpa_enc(uint8_t c[KYBER_INDCPA_BYTES],const uint8_t m[KYBER_INDCPA_MSGBYTES],
                const uint8_t pk[KYBER_INDCPA_PUBLICKEYBYTES],
                const uint8_t coins[KYBER_SYMBYTES]);
    void indcpa_dec(uint8_t m[KYBER_INDCPA_MSGBYTES],
                const uint8_t c[KYBER_INDCPA_BYTES],
                const uint8_t sk[KYBER_INDCPA_SECRETKEYBYTES]);

    void kex_ake_initA(uint8_t *send, uint8_t *tk, uint8_t *sk, const uint8_t *pkb);
    void kex_ake_sharedB(uint8_t *send, uint8_t *k, const uint8_t* recv, const uint8_t *skb, const uint8_t *pka);
    void kex_ake_sharedA(uint8_t *k, const uint8_t *recv, const uint8_t *tk, const uint8_t *sk, const uint8_t *ska);


""")

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_libpqccrystals_kyber_cffi",
"""
   
""",
     libraries=['pqcrystals_kyber1024_ref','pqcrystals_fips202_ref', 'pqcrystals_aes256ctr_ref'], # without the lib prefix! libpqcrystals_sha2_ref.so
     library_dirs =  [libcint_dir], # [os.path.join(libcint_dir, 'build')],
     ),  # library name, for the linker
      

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
