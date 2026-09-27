# SuperiorCCGen
SuperiorCCGen is a Luhn-safe credit card number generator with 15 different credit card companies which include subsidiary card types.

# Available Companies
SuperiorCCGen is a practical tool for generating credit card numbers from various companies while abiding by the criteria of the Luhn algorithm. Supported brands include: 

- Visa
- Mastercard
- American Express
- Diners Club
- JCB
- Solo
- Switch
- Maestro
- China UnionPay
- Dankort
- RuPay
- Hipercard
- Elo
- Mir
- Discover

# Module Usage
This has additionally been rewritten as a module. Here is an example use-case of the module:

```python
import ccgen


def main():

    card:str = ccgen.generate("visa")

    print(card)


if __name__ == "__main__":
    main()

 ```
