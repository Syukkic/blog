# Fisher_Yates_shuffle https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
from random import randint


def randomize(arr, n):
    for i in range(n - 1, 0, -1):
        j = randint(0, i + 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def gen_md_list(arr):
    for i in arr:
        name, link = i.split(": ")
        print(f"- [{name}]({link})")


friends_link = [
    "なままめ: https://robinzed.wordpress.com/",
    "萌狼: https://blog.horo.moe/",
    "太一: https://starlite.me/about/",
    "傑克工作了: https://jack-works.github.io/",
    "早川季子: https://137.ppfarm.boats/",
    "奈卜拉: https://astrologer.cc"
]
if __name__ == "__main__":
    n = len(friends_link)
    gen_md_list(randomize(friends_link, n))
