def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    f=open(data,'r')
    s=f.read()
    n=s.split(',')
    b=[]
    for i in n:
        b.append(int(i))
    return b
print(main('data01.txt'))
# Read data from file

# f=open('data01.txt','r')
# s=f.read()
# print(s.split(','))