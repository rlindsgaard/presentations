import random


def generate_key():
    key = ''
    for i in range(5):
        key += str(random.randint(1,6))
    return key


def main():
    words = {}
    with open('eff_large_wordlist.txt') as f:
        for line in f:
            key, value = line.split()
            words[key] = value
    for _ in range(6):
        print(words[generate_key()])

if __name__ == '__main__':
    main()
