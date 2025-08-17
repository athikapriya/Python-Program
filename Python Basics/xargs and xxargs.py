### xargs or Arbitary arguments
def student(*details):
    print(details[1])

student("Athika", 20, 3.56)
student("Rittika", 22, 3.00)

# addition
def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print(sum)

add(10, 20, 30)


### xxargs or Keyword arguments
def info(**detail_info):
    print(detail_info)
    print(detail_info["name"])

info(id = 22, name = 'Rittika')