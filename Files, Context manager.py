#FILESFILESFILESFILESFILESFILESFILESFILESFILESFILESFILESFILESFILESFILESFILESFILESFILESFILESFILES
# 1.
txt = open("createtxt.txt","a")
insert_text = ("4eboor3k s pov1dl0m na privokzalno1 ploshad1")
txt.write(insert_text)

txt = open("createtxt.txt","r")
txt_read = txt.readline()
sum = 0
for x in txt_read:
    for y in x:
        if y.isdigit() == True:
            sum = sum + int(y)
print(sum)

# 2.
txt_path = "createtxt.txt"
txt_object = open(txt_path,"r")
txt_list = txt_object.read().split()
print(max(txt_list, key=len))

# 3.
txt.close()
txt_object.close()

with open("createtxt.txt", "r") as text_close:
    print(text_close.read().split())
print(text_close.closed)

# 4.
big_text = '''I added this text
because i want to have
very many lines in it!'''
another_big_text = '''several
another 
lines.'''
first_main_text = "main_text10.txt"
second_main_text = "main_text11.txt"

with open(first_main_text,"w") as main_text:
    main_text.write(big_text)
with open(first_main_text,"a") as main_text:
    main_text.write(another_big_text)


with open(first_main_text,"r") as main_text:
    with open(second_main_text,"w") as main_text_copy:
        lines = main_text.readlines()
        main_text_copy.writelines(lines[1:-1])

with open(second_main_text,"r") as main_text_copy:
    print(main_text_copy.read())


# 5.
big_text = '''I added this text
because i want to have
very many lines in it!'''
another_big_text = '''several
another 
lines.'''
main_source_text = "source_text.txt"
second_combined_text = "combined_text5.txt"

with open(main_source_text,"w") as source_text, open(second_combined_text,"w") as combined_text:
    source_text.write(big_text)
    combined_text.write(another_big_text)

with open(main_source_text,"r") as source_text, open(second_combined_text,"r") as combined_text:
    source_lines = source_text.readlines()
    combined_lines = combined_text.readlines()

with open(main_source_text, "r") as source_text, open(second_combined_text, "w") as combined_text:
    for x,y in zip(combined_lines, source_lines):
        combined_text.writelines(f"{x.strip()} {y.strip()}\n")

with open(second_combined_text,"r") as combined_text:
    print(combined_text.read())
