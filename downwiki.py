import requests 
from bs4 import BeautifulSoup
import os


def get_link(url):
     url ='https://en.wikipedia.org/wiki/Chess'
     respones = requests.get(url)

     if respones.status_code == 200:
        soup = BeautifulSoup(respones.content, 'html.parser')
        find_mages = soup.findAll('img')

        # Extract 'src' attribute of every image
        image_links = []
        for image in find_mages:
            image_links.append(image.attrs['src'])

        return image_links
           

def open_in_file(page_links, links):
    pagel =page_links
    requ = requests.get(pagel)
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(requ.text, 'html.parser')

    urls = []
    for link in soup.find_all('a'):
        print(link.get('href'))
   
    b = page_links
    dirName = b.split('/')[-1]
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    #download images to desired folder
    os.chdir(dirName)
    # Send GET request
    b = fix_link(links)
    for i in range(len(links)):
        response = requests.get(b[i])
        file_name = b[i].split('/')[-1]
        # Save the image
        if response.status_code == 200:
            with open(file_name, "wb") as f:
                    f.write(response.content)
                    f.close()
    os.chdir('..')
def fix_link(links):
    for i in range(0, len(links)):
        if links[i].startswith('//upload'):
            links[i] = 'https:' + links[i]
    return links
                    



#def crowl( page, file, depth, width):
def main():
    urll = get_link(f'https://en.wikipedia.org/wiki/Chess')
    print(urll)
    file = open_in_file(f'https://en.wikipedia.org/wiki/Chess', 'links')
    print(file)
    fix_link(links)

if __name__=="__main__":
    main()
    #get the image links from the url
#    image_links = get_link('https://en.wikipedia.org/wiki/Chess')
    #download and save the images in a defined folder
 #   downloaded_images = open_in_file('https://en.wikipedia.org/wiki/Chess',image_links)
    #add an 'http': prefix to the url
  #  fixed_link = fix_link(image_links)
    



#def main():


#def choos_new_ling():

    

































