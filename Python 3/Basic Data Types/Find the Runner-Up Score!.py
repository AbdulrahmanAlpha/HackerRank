if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    score = list(arr)
    sorte = sorted(set(score))
    print(sorte[-2])
