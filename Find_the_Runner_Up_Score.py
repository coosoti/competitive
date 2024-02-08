if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # remove duplicate score and sort the list
    sorted_unique_scores = sorted(set(arr), reverse=True)
    
    #print runners up score
    print(sorted_unique_scores[1])