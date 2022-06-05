import functools
words=input().split()
def validate(word):
    letters=[]
    for i in word:
        if i.upper() not in letters:
            letters.append(i.upper())
    if len(letters)>3:
        return True
    return False
if __name__=='__main__':
    answer1=list(filter(validate, words))
    print(list(map(lambda a: a[0].swapcase()+a[1:], answer1)))
    answer2 = list(filter(lambda x: 'foo' in x, words))
    print(len(functools.reduce(lambda a,b: a+b, answer2)))