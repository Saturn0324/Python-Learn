def main():
    #相对路径或绝对路径
    with open('python_demo/text.txt','r',encoding='utf-8') as file:
        print(file.read())
    print('-----------------')
    with open('python_demo/text.txt','r',encoding='utf-8') as file:
        for line in file:
            print(line,end=' ')
            #默认end='\n'
    print('-----------------')
    with open('python_demo/text.txt','r',encoding='utf-8') as file:
        lines=file.readlines()
        print(lines)
    print('-----------------')
    file.close()
    #w 覆盖之前的内容 a 插入最后 详见png
    file1=open('python_demo/text.txt','a',encoding='utf-8')
    file1.write("emmm")
    file1.close()
    # file=open('python_demo/text.txt','r',encoding='utf-8')
    # print(file.read())
    
if __name__ == '__main__':
    main()
    