import re

def replace(url):
    match = re.search('https\:\/\/(\S+?)\/(\S+)', url)
    site = match.group(1)
    article = match.group(2)
    proxy_site = site.replace('.', '-') + '.proxy2.library.illinois.edu/'
    new_url = proxy_site + article
    return new_url

def test():
    url = 'https://journals.aps.org/prb/abstract/10.1103/PhysRevB.102.155149'
    print(replace(url))

    url = 'https://www.nature.com/articles/nature26160'
    print(replace(url))

if __name__ == '__main__':
    # test()
    # print(replace('https://www.sciencedirect.com/science/article/abs/pii/S0368204804000350'))
    # print(replace('https://link.springer.com/chapter/10.1007/978-3-662-04011-9_4'))
    print(replace('https://link.springer.com/article/10.1007/BF01392016'))
