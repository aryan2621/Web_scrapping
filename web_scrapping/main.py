import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# Tag
# Navigable string
# Beautiful Soup
# Comment

# title =soup.title
# print(type(title))
# print(type(title.string))
# print(type(soup))


# Get any tag of html
# print(soup.findAll('p'))
# print(soup.findAll('a'))

# for the first p and it class
# print(soup.find('p'))
# print(soup.find('p')['class'])

#  find all the element with class lead
# print(soup.find_all("p",class_="lead"))

# get the text from the tag
# print(soup.find('p').get_text())

# get all the links of the page
anchors = soup.find_all('a')
all_links = set()
for links in anchors:
    if links.get("href") != "#":
        link ="https://codewithharry.com"+links.get("href")
        all_links.add(link)
        # print(link)

# markup ="<p><!--This is the comment--></p>"
# soup2 =BeautifulSoup(markup,'features:"lxml"')
# print(type(soup2.p.string))

navbarSupportedContent =soup.find(id="navbarSupportedContent")
# for inde in navbarSupportedContent.contents:
    # print(inde)
# .content -> a tags children available as a list
# .children -> a tags children available as a generator

# for inde in navbarSupportedContent.strings:
#     print(inde)
# print(navbarSupportedContent.parents)
# print(navbarSupportedContent.parent)

# for i in navbarSupportedContent.parents:
    # print(i)
    # print(i.name)
    
# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

# print(soup.select("#loginModal"))
print(soup.select(".btn-success"))

