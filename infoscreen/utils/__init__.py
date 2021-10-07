test1 = "https://youtu.be/16GVZ6s5XEw"
test2 = "https://www.youtube.com/watch?v=16GVZ6s5XEw&ab_channel=BigLozOfficial"
test3 = "https://youtu.be/16GVZ6s5XEw/?id=1"

def parse_url(url):
    if("https://youtu.be/" in url):
        new = url.replace("https://youtu.be/", '')
        new = new.split("/", 1)
        return new[0]
    elif("https://www.youtube.com/" in url):
        new = url.split("=", 1)
        new = new[1].split("&", 1)
        return new[0]
    else:
        return "oopsie woopsie, you made a fucky wucky"
