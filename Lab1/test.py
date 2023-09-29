import FindMax
import timeit
import numpy as np

def main():
    tests()

def tests():
    print("Linear tests:")
    a = np.random.randint(100, size=14)
    print("Randomly-generated array: ", a)
    print("Highest value (linear scan): ", FindMax.FindMaxLinear(a))
    print("Highest value with count (linear scan:)", FindMax.FindMaxLinearWithCount(a))
    print("Second highest value (linear scan): ", FindMax.FindSecondLinear(a))
    print("-----------------------")
    print("Divide-and-conquer tests:")
    a = np.random.randint(100, size=14)
   # a = [54, 22, 22, 22, 22, 32, 4, 99, 43, 99, 23, 89]
    print("Randomly-generated array: ", a)
    print("Highest value (DNC): ", FindMax.FindMaxDNC(a, 0, len(a)-1))
    print("Highest value with count (DNC): ", FindMax.FindMaxDNCWithCount(a, 0, len(a)-1))
    print("Second highest value (DNC): ", FindMax.FindSecondDNC(a))
    print("Second highest value with count (DNC): ", FindMax.FindSecondDNCWithCount(a, 0, len(a)-1))


if __name__ == "__main__":
    main()
