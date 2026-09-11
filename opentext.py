try: 
    f = open('my_file.txt')
finally:
    print(f.read())
    f.close()

