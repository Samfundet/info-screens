TEST1 = 'https://youtu.be/16GVZ6s5XEw'
TEST2 = 'https://www.youtube.com/watch?v=16GVZ6s5XEw&ab_channel=BigLozOfficial'
TEST3 = 'https://youtu.be/16GVZ6s5XEw/?id=1'


def parse_url(url):
    if 'https://youtu.be/' in url:
        new = url.replace('https://youtu.be/', '')
        new = new.split('/', 1)
        return new[0]
    if 'https://www.youtube.com/' in url:
        new = url.split('=', 1)
        new = new[1].split('&', 1)
        return new[0]
    return 'oopsie woopsie, you made a fucky wucky'
