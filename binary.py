"""
Name: Jorge Soto-Ventura
File: binary.py


Functions for decimal/binary conversions.
"""
import math
# Include your responses to 1-4 here after you've tested them.
#1a. 108
#1b. 108
#1c. 108
#2a. -51
#2b. -77
#2c. 205
#3a.00111000
#3b.11010101
#3c.11111111
#4a.38
#4b.1B6
#4c.D7
#
#
#

from re import X
from tokenize import Exponent


def invert(bitString):
   """Returns the bit string with the bits inverted."""
   invertedString = ''
   for bit in bitString:
      if bit == '1':
         invertedString += '0'
      else:
         invertedString += '1'
   return invertedString
## Return a decimal value from a unsigned Binary
def unsignedBinaryToDecimal(bitString):
   decimal = 0
   bitList = list(bitString)
   list.reverse(bitList)
   for char in range(len(bitList)):
      if bitList[char] == "1":
         decimal += 2**(char)
   return decimal
## This returns a binary from an unsigned decimal value
def unsignedDecimalToBinary(decimalValue):
   binaryString = ''
   if decimalValue == 0:
      binaryString += '0'
      return binaryString
   elif decimalValue == 1:
      binaryString += '1'
      return binaryString
   else:
      ## The while statement checks whether the remindar of the value is 1 or 0 until the decimal value == 0
      while decimalValue != 0:
         remainder = decimalValue % 2
         if remainder == 1:
            binaryString += '1'
            decimalValue = decimalValue // 2

         elif remainder == 0:
            binaryString += '0'
            decimalValue = decimalValue // 2
      return (binaryString [::-1])
## adds a one to the bitstring in order to complement two complement
def addOne(bitString):
   newValue = unsignedBinaryToDecimal(bitString)
   newValue += 1
   returnValue = unsignedDecimalToBinary(newValue)
   return returnValue
## returns the twosComp of a decimal
def twosCompToDecimal(bitString):
   bitList = list(bitString)
   if bitList[0] == '1':
      newValue = invert(bitString)
      plusOneValue = addOne(newValue)
      returnValue = unsignedBinaryToDecimal(plusOneValue)
      returnValue = returnValue - (returnValue * 2)
      return returnValue
   elif bitList[0] == '0':
      returnValue = unsignedBinaryToDecimal(bitString)
      return returnValue
      
## returns a decimal from twos comp
def decimalToTwosComp(decimalValue):
   binaryString = ''
   newDecimalValue = decimalValue
   if decimalValue == 0:
      binaryString += '0'
      return binaryString
   else:
      while decimalValue != 0:
         remainder = decimalValue % 2
         if (decimalValue == (1.0 or -1.0)):
            binaryString += '1'
            break
         elif remainder == 1:
            binaryString += '1'
            if decimalValue < 0:
               decimalValue = (decimalValue // 2 + 1)
            elif decimalValue > 0:
               decimalValue = (decimalValue // 2)
         elif remainder == 0:
            binaryString += '0'
            decimalValue = decimalValue // 2
      if newDecimalValue > 0:
         binaryString += '0'
         return binaryString [::-1]
      elif newDecimalValue < 0:
         binaryString += '0'
         newBinaryString = binaryString [::-1]
         invertedString = invert(newBinaryString)
         invertedString = addOne(invertedString)

         return invertedString
## creates a sign for the bitstring
def signExtend(bitString, bits):
   bitList = list(bitString)
   newBitString = bitString [::-1]
   while len(bitList) < bits:
      if bitList[0] == '1':
         newBitString += '1'
      elif bitList[0] == '0':
         newBitString += '0'
      bitList.append(1)
   returnBitString = newBitString [::-1]
   return returnBitString
#Changes a fraction or floating point below 1 to a binary form
def unsignedFractionToBinary(unsignedFloat, maxBits):
   floatCounter = unsignedFloat
   floatString = ""
   ## While the float is greater than 0 it multiplies by two taking any whole number if there is one and then subtracting by 1 until the number is 0
   while floatCounter > 0:
      floatCounter = floatCounter * 2
      if floatCounter >= 1:
         floatString += "1"
         floatCounter -= 1
      elif floatCounter < 1:
         floatString += "0"
      if len(floatString) == maxBits:
         break
      else:
         continue
   return floatString
## This takes a float and changes it to binary using both unsignedFractionToBinary and unsignedDecimalToBinary
def unsignedFloatToBinary(unsignedFloat, maxBits):
   unsignedFloatString = str(unsignedFloat)
   unsignedFloatStringList = list(unsignedFloatString) 
   counter = 0  
   newUnsignedFloatList = []
   fractionFloatList = []
   while unsignedFloatStringList[counter] != "." :
      counter += 1
   for x in range(counter):
      newUnsignedFloatList.append(unsignedFloatStringList[x])
   for x in range(len(unsignedFloatStringList) - 1, -1, -1):
      if unsignedFloatStringList[x] == ".":
         break
      else:
         fractionFloatList.append(unsignedFloatStringList[x])
   wholeNumberStr = "".join(newUnsignedFloatList)
   wholeNumberFloat = float(wholeNumberStr)
   fractionFloatList.append(".")
   fractionFloatList.reverse()
   fractionNumber = "".join(fractionFloatList)
   fractionNumberFloat = float(fractionNumber)
   fractionNumberReturn = unsignedFractionToBinary(fractionNumberFloat, maxBits)
   newFractionList = list(fractionNumberReturn)
   decimalList = ["."]
   wholeNumberStrReturn = unsignedDecimalToBinary(wholeNumberFloat)
   newWholeNumberList = list(wholeNumberStrReturn)
   finalReturnList = newWholeNumberList + decimalList + newFractionList
   floatReturnValue = "".join(finalReturnList)
   finalStringValue = str(floatReturnValue)
   return finalStringValue

#This normalizes the bitString into a 0000E0 Format return a string of the normalized binary
def normalize(bitString):
   bitList = list(bitString)
   newBitList = []
   counter = 0
   if bitList[0] == '0':
      while bitList[counter] != '1':
         counter += 1
      for x in range(len(bitList) - 2):
         if  bitList[x + 2] == '.':
            continue
         elif x + 2 == counter:
            newBitList.append(bitList[x + 2])
            newBitList.append('.')
         elif x + 2 > counter:
            newBitList.append(bitList[x + 2])
      newBitString = "".join(newBitList)
      stringCounter = str(counter)
      newBitString += "E-" + stringCounter
      return newBitString
   if bitList[0] == '1': 
      while bitList[counter] != '.':
         counter += 1
      counter -= 1
      for x in range(len(bitList)):
         if bitList[x] == '.':
            continue
         else:
            newBitList.append(bitList[x])
            if x == 0:
               newBitList.append('.')
      newBitString = "".join(newBitList)
      stringCounter = str(counter)
      newBitString += "E" + stringCounter
      return newBitString
## This is the same as the function above but instead only returns the exponent part in order to be used for single Precision
def normalizeIEP(bitString):
   bitList = list(bitString)
   newBitList = []
   counter = 0
   if bitList[0] == '0':
      while bitList[counter] != '1':
         counter += 1
      for x in range(len(bitList) - 2):
         if  bitList[x + 2] == '.':
            continue
         elif x + 2 == counter:
            newBitList.append(bitList[x + 2])
            newBitList.append('.')
         elif x + 2 > counter:
            newBitList.append(bitList[x + 2])
      newBitString = "".join(newBitList)
      stringCounter = str(counter)
      newBitString += "E-" + stringCounter
      return newBitString
   if bitList[0] == '1': 
      while bitList[counter] != '.':
         counter += 1
      counter -= 1
      for x in range(len(bitList)):
         if bitList[x] == '.':
            continue
         else:
            newBitList.append(bitList[x])
            if x == 0:
               newBitList.append('.')
      newBitString = "".join(newBitList)
      return newBitString
## This function creates a single precision 32 bit binary number from a decimal
def decimalToSinglePrecision(signedFloat):
   ieeePrecision = ''
   maxBits = 0
   exponentValue = 0
   newSignedFloatListExponent = []
   exponentStr = "".join(newSignedFloatListExponent)
   exponentFloat = float(exponentStr)
   finalExponentStr = unsignedDecimalToBinary(exponentFloat)
   exponentList = list(finalExponentStr)
   ## Checks for the exponent value which will be used to grab exponent binary for the Single Precision
   for x in range(len(exponentList)):
      exponentValue+= 1
   exponentValue -= 1
   maxBits = (31 - exponentValue)
   ## This if statment is used to create the first binary number which will determine the sign of the Single Precision
   if signedFloat < 0:
      ieeePrecision += '1'
   elif signedFloat > 0:
      ieeePrecision += '0'
   absExponentValue = abs(exponentValue + 127)
   ## This gets the exponent part of the Single Precision
   exponentBinary = unsignedDecimalToBinary(absExponentValue)
   unsignedFloat = abs(signedFloat)
   ## This gets the float that will be used in order to get the normalized form of the fraction
   floatToBinaryNumberExpression = unsignedFloatToBinary(unsignedFloat, maxBits)
   normalizeIEPExpression = normalizeIEP(floatToBinaryNumberExpression)
   floatAndFractionStrList = list(normalizeIEPExpression)
   floatAndFractionStrList.remove('.')
   del floatAndFractionStrList[0]
   newFloatAndFractionStr = "".join(floatAndFractionStrList)
   ieeePrecisionReturn = ieeePrecision + exponentBinary + newFloatAndFractionStr
   ieeePrecisionReturnList = list(ieeePrecisionReturn)
   #This adds on the ending zeros that need to added to reach 32 bits
   for x in range(31):
      if x > len(ieeePrecisionReturnList):
         ieeePrecisionReturnList.append('0')
   ieeePrecisionReturn = "".join(ieeePrecisionReturnList)
   return ieeePrecisionReturn

def main():
   """Test bed for decimal/binary conversion functions."""
   print ("11001 ->", invert("00110"))
##   print ("0 ->", unsignedBinaryToDecimal("0"))
##
##   print ("6 ->", unsignedBinaryToDecimal("110"))
##
##   print ("0 ->", unsignedDecimalToBinary(0))
##
##   print ("110 ->", unsignedDecimalToBinary(6))
##
##   print ("110 ->", addOne("101"))
##
##   print ("5 ->", twosCompToDecimal("0101"))
##
##   print ("-5 ->", twosCompToDecimal("1011"))
##
##   print ("0101 ->", decimalToTwosComp(5))
##
##   print ("1011 ->", decimalToTwosComp(-5))
##
##   print ("00000101 ->", signExtend(decimalToTwosComp(5), 8))
##
##   print ("11111011 ->", signExtend(decimalToTwosComp(-5), 8))

if __name__ == "__main__":
   main()
