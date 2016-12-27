import random
import math

from collections import namedtuple

###########################################################
##
## Simple class to generate RSA keys and then encrypt or
## decrypt an integer.
##
## 1. Find two random prime numbers p and q
## 2. Compute the modulus n as n = p * q
## 3. Compute phi(n), phi being Euler's totient function
##    which returns the number of coprimes of n in the
##    range of [1;n].
## 4. Find the first exponent e as a random coprime of
##    phi(n) in the range of [2;phi(n)].
## 5. Compute d as the multiplicative inverse of phi(n)
## 6. The public key consists of n and e.
## 7. The private key consists of n and d.
## 8. An integer m is encrypted as m^e mod n
## 9. An encrypted integer m is decrypted as m^d mod n
##
###########################################################


class RSA:

    def __init__(self):

        self.key = namedtuple("Key",["modulus","exponent"])

    ###########################################################
    ##
    ## @brief   Function to generate public and private keys.
    ##
    ## @return  The public and private keys.
    ##
    ###########################################################

    def generateKeys(self):

        # two distinct prime numbers p and q
        p = self.__findPrime()
        q = self.__findPrime()

        # the modulus value
        n = p * q

        # compute phi of n, phi being Euler's
        # totius function which returns all
        # integers k in the range of 1 <= k <= n
        # for which n and k are coprime, so gcd(n,k)
        # is equal to 1. This is the shortened form
        phi = (p - 1) * (q - 1)

        e = self.__findExponent(phi)

        d = self.__multiplicativeInverse(e,phi)

        publicKey = self.key(n,e)

        privateKey = self.key(n,d)

        return publicKey, privateKey

    ###########################################################
    ##
    ## @brief   Encrypts a message with a public key.
    ##
    ## @param   message The integer to encrypt.
    ##
    ## @param   key The public key.
    ##
    ## @return  The encrypted message.
    ##
    ###########################################################

    def encrypt(self,message,key):

        return self.__squareMultiply(message,key.exponent) % key.modulus

    ###########################################################
    ##
    ## @brief   Decrypts a message with a private key.
    ##
    ## @param   message The encrypted integer to decrypt.
    ##
    ## @param   key The private key.
    ##
    ## @return  The decrypted message.
    ##
    ###########################################################

    def decrypt(self,message,key):

        return self.__squareMultiply(message,key.exponent) % key.modulus

    ###########################################################
    ##
    ## @brief   Determines whether an integer is a prime.
    ##
    ## @param   n The integer to determine the primality for.
    ##
    ## @return  Boolean, True if n is prime else False
    ##
    ###########################################################

    def __isPrime(self,n):

        # 2 and 3 are prime, 0 and 1 not
        if n <= 3:
            return n >= 2

        # easy check for 2 and 3
        if n % 2 == 0 or n % 3 == 0:
            return False

        # other numbers
        for i in range(5, int(math.sqrt(n)) + 1, 6):

            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True

    ###########################################################
    ##
    ## @brief   Finds a random prime number.
    ##
    ## @return  A random prime number.
    ##
    ###########################################################

    def __findPrime(self):

        # look for the first 10-bit prime
        n = random.randrange(1024)

        while(self.__isPrime(n) == False):

            n = random.randrange(1024)

        return n

    ###########################################################
    ##
    ## @brief   Determines the GCD for two values.
    ##
    ## @details This function uses the Euclidean algorithm to
    ##          determine the greatest common divisor (GCD)
    ##          for two values a and b.
    ##
    ## @param   a The first integer.
    ##
    ## @param   b The second integer.
    ##
    ## @return  The greatest common divisor of a and b.
    ##
    ###########################################################

    def __gcd(self,a,b):

        temp = a

        # switch a for b so that
        # a is always greater b
        if b > a:
            a = b
            b = temp

        while(temp):

            temp = a % b

            a = b

            b = temp

        return a

    ###########################################################
    ##
    ## @brief   Finds the exponent of phi(n).
    ##
    ## @details Determines the exponent of the public key,
    ##          for the totient function value phi(n), n
    ##          being the modulus value. Part of the RSA
    ##          algorithm. e is a random coprime of phi(n)
    ##          in the range of [2;phi].
    ##
    ## @param   phi The totient function value of n.
    ##
    ## @return  The exponent e.
    ##
    ###########################################################

    def __findExponent(self,phi):

        e = random.randrange(2,phi)

        while(self.__gcd(phi,e) != 1):

            e = random.randrange(2,phi)

        return e

    ###########################################################
    ##
    ## @brief   Finds the multiplicative inverse of two values.
    ##
    ## @details Determines the modular multiplicative inverse
    ##          of two integers, one being a modulus value n
    ##          and the other the value a. The multiplicative
    ##          inverse is the value for which a^-1 mod n = 1,
    ##          so the modular multiplicative inverse d is the
    ##          value for which a * d = 1 (mod n). This value
    ##          is found using the extended euclidean algorithm.
    ##          This algorithm goes as follows:
    ##          1. Start with coef (d) being equal to 1 and a
    ##             delayed version of coef, coefDelayed equal
    ##             to 0. There is also a delay for value,
    ##             valueDelay, initally equal to the modulus.
    ##          2. While valueDelay is not 0, compute the
    ##             floored quotient of valueDelay and value;
    ##             then update value to valueDelay - quotient
    ##             * value, and set valueDelay to what value
    ##             was before. Do the same for coef and
    ##             coefDelay.
    ##          3. Before returning, check if coefDelay is
    ##             negative. If so, add the modulus value
    ##             to get a positive (but congruent) value.
    ##          4. Return the positive coefDelay.
    ##
    ##
    ## @param   value The value for the algorithm.
    ##
    ## @param   modulus The modulus for the algorithm.
    ##
    ## @return  The modular multiplicative inverse d.
    ##
    ###########################################################

    def __multiplicativeInverse(self,value,modulus):

        coef = 1

        coefDelay = 0

        valueDelay = modulus

        while(value):

            quotient = valueDelay//value

            valueDelay, value = value, valueDelay - quotient * value

            coefDelay, coef = coef, coefDelay - quotient * coef

        if coefDelay < 0:
            coefDelay += modulus

        return coefDelay

    ###########################################################
    ##
    ## @brief   Square-and-multiply algorithm.
    ##
    ## @details The square-and-multiply version is an efficient
    ##          way to compute high exponents of certain values.
    ##          x^n is broken down to (x^2)^(n/2) for even n.
    ##          For odd n, n is reduced by one and therefore
    ##          the value must be multiplied an addtional time
    ##          by x: x * (x^2)^((n-1)/2). Do this recursively.
    ##
    ## @param   base The base of exonentiation.
    ##
    ## @param   power The exponent.
    ##
    ## @return  The result of base^power.
    ##
    ###########################################################

    def __squareMultiply(self,base,power):

        if power < 0:
            raise ValueError("Negative powers not allowed")

        if power == 0:
            return 1

        if power == 1:
            return base

        # if power is odd, x_new = x * (x^2)^((n-1)/2)
        if power % 2:
            return base * self.__squareMultiply(base*base,(power-1)/2)

        # if power is even, x_new = (x^2)^(n/2)
        return self.__squareMultiply(base*base,power/2)

if __name__ == "__main__":

    rsa = RSA()

    pub,priv = rsa.generateKeys()

    print(pub,priv)

    m = ord("B")

    print(m)

    crypt = rsa.encrypt(m,pub)

    print(crypt)

    decrypt = rsa.decrypt(crypt,priv)

    print("Decrypted message: {} \t Original message: {}".format(int(decrypt),m))
