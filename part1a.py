import random
import time

random.seed(time.time())

def removeCharAtIndex(input: str, index: int) -> str:
    inputLen = len(input)
    splitNewInput = [input[i] for i in range(inputLen) if i != index]
    return ''.join(splitNewInput)

def deleteRandChars(input: str) -> str:
    charDeleteNum = random.randrange(2, len(input) + 1)
    newInput = input
    for i in range(charDeleteNum):
        charIndex = random.randrange(0, len(newInput))
        newInput = removeCharAtIndex(newInput, charIndex)
    return newInput

def reverseString(input: str) -> str:
    return input[::-1]

def main(input: str):
    slicedInput = deleteRandChars(input)
    return reverseString(slicedInput)
