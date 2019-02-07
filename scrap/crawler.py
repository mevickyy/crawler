import urllib
import re
import json
class Crawler:
    """
    level
        1 - fetch links from the url
        2 - follow page and fetch images
        3 - follow page 2 and fetch images
    """

    def __init__(self, url, level=1):
        self.url = url
        self.level = level
        self.response = []


    def scrape(self):
        self.parse(links=[self.url], level=self.level)
        # import ipdb;ipdb.set_trace()
        # return json.dumps(self.response)
        return self.response

    def fetch_page_urls(self, content):
        absolute_pattern = r"(href=[\'\"]?({domain}/(\w+/)+))".format(domain=self.url)
        relative_pattern = r"(href=['\"]([/.]+\w+/?)['\"])"
        #Relative Pattern

        links_relative = re.findall(relative_pattern, content)
        links_relative = [self.url + link[1] for link in links_relative]
        #Absolute Pattern
        links_absolute = re.findall(absolute_pattern, content)
        links_absolute = [link[1] for link in links_absolute]

        links = list(set(links_relative + links_absolute))
        # import pdb;pdb.set_trace()
        return links

    @staticmethod
    def fetch_image_links(content):
        image_pattern = r"src=['\"]((.*?)(png|jpg|jpeg|svg))['\"]"
        image_pattern = re.findall(image_pattern, content)
        # import pdb;pdb.set_trace()
        images = [link[0] for link in image_pattern]
        return images

    def parse(self, links, level):
        if 0 < level:
            res = {"links": [],
                    "images": []
                  }
            for url in links:
                print(url)
                content = urllib.urlopen(url).read()
                if level >= 1:
                    res['links'] = self.fetch_page_urls(content)
                    res["images"] = self.fetch_image_links(content)
                    # print(res['links'])
                    # import pdb;pdb.set_trace()
                    self.parse(links=res['links'], level=level-1)
                self.response.append(res)