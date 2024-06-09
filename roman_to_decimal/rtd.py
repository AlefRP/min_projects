tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def main():
    roman = input("Enter a Roman numeral: ")
    print(len(roman))
    print("The decimal value is", roman_to_int(roman.upper()))

def roman_to_int(romanNumneral):
    sum = 0
    
    for i in range(len(romanNumneral) - 1):
        left = romanNumneral[i]
        right = romanNumneral[i + 1]

        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    
    sum += tallies[romanNumneral[-1]]
    return sum

if __name__ == "__main__":
    main()