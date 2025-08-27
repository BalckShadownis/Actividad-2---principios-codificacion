from dataclasses import dataclass


@dataclass
class Person:
  
    age: int
    name: str


class PersonValidator:
    
    @staticmethod
    def is_valid_age(age: str) -> bool:
        return age.isdigit() and 0 < int(age) < 150

    @staticmethod
    def is_valid_name(name: str) -> bool:
        return bool(name.strip())

    @classmethod
    def validate(cls, age: str, name: str) -> bool:
        return cls.is_valid_age(age) and cls.is_valid_name(name)


def main():
    raw_input = input("Ingrese datos (edad,nombre): ")
    parts = raw_input.split(",")

    if len(parts) != 2:
        print("❌ Error: el formato debe ser 'edad,nombre'")
        return

    age_str, name = parts[0].strip(), parts[1].strip()

    if PersonValidator.validate(age_str, name):
        person = Person(age=int(age_str), name=name)
        print(f"✅ OK: {person}")
    else:
        print("❌ Error: datos inválidos")


if __name__ == "__main__":
    main()
