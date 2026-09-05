#!/usr/bin/env python3

def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    name = input("Enter your name: ").strip() or "World"
    print(greet(name))


if __name__ == "__main__":
    main()
