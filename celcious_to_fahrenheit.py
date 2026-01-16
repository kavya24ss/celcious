def celsius_to_fahrenheit(celsius): 
    return (celsius * 9/5) + 32 
if __name__ == "__main__": 
    celsius = 25 
    print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F") 