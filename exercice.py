#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if (number < 0):
        return number * -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    noms = list()
    for i in range(0, len(prefixes), 1):
        nom = prefixes[i] + suffixe
        noms.append(nom)
    return noms


def prime_integer_summation() -> int:
    countPrimes = 0
    total = 0
    currentNumber = 2
    isNotPrime = True
    while(countPrimes < 100):
        isNotPrime = True
        if(currentNumber != 2 and currentNumber % 2 == 0): 
            isNotPrime = False
        else:
            for i in range(1, int(currentNumber/2), 1):
                if(i != 1 and currentNumber % i == 0):
                    isNotPrime = False
                    break
        if(isNotPrime):
            countPrimes += 1
            total += currentNumber
        currentNumber += 1
    return total


def factorial(number: int) -> int:
    total = 1
    for i in range(1, number + 1, 1):
        total = total * i
    return total


def use_continue() -> None:
    for i in range(1, 11, 1):
        if(i == 5):
            continue
        print(i)


def verify_ages(groups: List[List[int]]) -> List[bool]:
    verified = list()
    for i in range(0, len(groups), 1):
        if(len(groups[i]) < 3 or len(groups[i]) > 10):
            verified.append(False)
        else:
            has25yo = False
            hasUnder18yo = False
            has50yo = False
            hasOver70yo = False
            for i2 in range(0, len(groups[i]), 1):
                if(groups[i][i2] == 25):
                    has25yo = True
                elif(groups[i][i2] < 18):
                    hasUnder18yo = True
                elif(groups[i][i2] == 50):
                    has50yo = True
                elif(groups[i][i2] > 70):
                    hasOver70yo = True
            if(has25yo):
                verified.append(True)
            elif(hasUnder18yo):
                verified.append(False)
            elif(hasOver70yo and has50yo):
                verified.append(False)
            else:
                verified.append(True)
    return verified


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
