def main():
 class TemperatureConversion:
     def __init__(self, temp=1):
         self._temp = temp
 class CelsiusToFahrenheit(TemperatureConversion):
     def conversion(self):
         return (self._temp * 9) / 5 + 32

 class CelsiusToKelvin(TemperatureConversion):
     def conversion(self):
         return self._temp + 273.15

 class FahrenheitToCelsius(TemperatureConversion):
     def conversion(self):
         return (self._temp - 32)  * 5 / 9
 class KelvinToCelsius(TemperatureConversion):
    def conversion(self):
        return self._temp - 273.15

 tempInCelsius = float(input("Enter the temperature in Celsius: "))
 convert = CelsiusToKelvin(tempInCelsius)
 print("Celsius to Kelvin")
 convert = CelsiusToKelvin(tempInCelsius)
 print(str(convert.conversion()) + " Kelvin\n")

 print("Celsius to Fahrenheit")
 convert = CelsiusToFahrenheit(tempInCelsius)
 print(str(convert.conversion()) + " Fahrenheit\n")

 print("Fahrenheit to Celsius")
 tempInFahrenheit= float(input("Enter the temperature in Fahrenheit: "))
 convertF = FahrenheitToCelsius(tempInFahrenheit)
 print(str(convertF.conversion()) + " Celsius\n")

 print("Kelvin to Celsius")
 tempInKelvin = float(input("Enter the temperature in Kelvin: "))
 convertK = KelvinToCelsius(tempInKelvin)
 print(str(convertK.conversion()) + " Celsius\n")


main()