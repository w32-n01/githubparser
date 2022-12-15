import atoma, requests, datetime, dateutil

feeds = [
    'https://github.com/revolution-populi/revpop-core/commits.atom',
    'https://github.com/revolution-populi/revpop-core/releases.atom',
    'https://github.com/revolution-populi/revpop-core/tags.atom'
]

print("Current date is: " + str(datetime.datetime.utcnow()))
now_date = datetime.datetime.utcnow()

def parse_a_feed(current_feed):
    for j in current_feed.entries:
        naivetime = j.updated.replace(tzinfo=None)
        publishedWithinThreshold = now_date - naivetime < datetime.timedelta(days=6)
        if publishedWithinThreshold:
            print(j.links)
        print(naivetime)

def parse_all(feeds):
    for i in feeds:
        response = requests.get(i)
        feed = atoma.parse_atom_bytes(response.content)
        print("Current feed is: " + str(feed.title))
        parse_a_feed(feed)

parse_all(feeds)
