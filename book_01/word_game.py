japanese = ["りんご", "本", "猫", "犬", "卵", "女の子"]
english = ["apple", "book", "cat", "dog", "egg", "girl"]

n = len(japanese)
right = 0

for i in range(n):
    s = input(japanese[i] + "の英単語は: ")

    if s == english[i]:
        print("ok")
    else:
        print("no cat")
