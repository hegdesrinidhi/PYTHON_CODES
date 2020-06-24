import zipfile, re,os
os.chdir("C:\\Users\\srini\\Downloads")

f = zipfile.ZipFile("channel.zip")
print(f.read("readme.txt").decode("utf-8"))

num = '90052'

comments = []

while True:
    content = f.read(num + ".txt").decode("utf-8")
    #print(content)
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    #print(content)
    #print(comments)
    match = re.search("Next nothing is (\d+)", content)
    if match == None:
        break
    num = match.group(1)

print(comments.__len__())
print(type(comments))
print(comments[500])
print("".join(comments))