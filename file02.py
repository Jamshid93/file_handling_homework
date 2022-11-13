def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data,'r')
    s=f.read()
    n=0
    for i in s:
        if i.isalpha():
            n+=1
    return n
print(main("txt_file\\data02.txt"))
# Read data from file