import json
from urllib.request import urlopen
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


def get_repositoris(pages):
    with urlopen(f'https://api.github.com/search/repositories?q=tetris+language:python&sort=stars&order=desc&per_page=100&page={pages}') as repo:
        json_opj = json.load(repo)
        data_repo = json_opj['items']
    return data_repo


def arrays_from_repo():
    array_repo = []
    for i in range(2):
        repo_page = get_repositoris(i)
        for rep in repo_page:
            array_repo.append(rep)
        print(array_repo)
    return array_repo


def split_data(data_repo):
    forks = []
    stars = []
    for repo in data_repo:
        fork = repo.pop(f'forks_count')
        star = repo.pop('stargazers_count')
        forks.append(fork)
        stars.append(star)
        print(len(forks))
        print(len(stars))

    return forks, stars

def anilasing_into(forks, stars):
    
    forks_train = forks[:700]
    stars_train = stars[:700]
    forks_test = forks[700:]
    stars_test = stars[700:]
    #print(forks,stars)
    model = LinearRegression()#.fit(forks_train, stars_train)
   # score = model.score(forks_test, stars_test )
    x = np.array(forks).reshape((-1, 1))
    y = np.array(stars)
    line_model = model.predict(forks_train)
    plt.scatter(x,y)
    plt.scatter(y,x)
    plt.plot(forks_train ,forks_test, forks_test, stars_test)
    plt.show()
    return forks,stars, forks_train, stars_train, forks_test, stars_test,  line_model

  

def main():
    repositories = arrays_from_repo()
    forks_train, stars_train = split_data(repositories)
    anilasing_into( forks_train, stars_train)





#    test01 = (arrays_from_repo())
#    print (test01)
#    print(test[3])
#    test2 = split_data(test)
#    print(test2)
#    test3 = anilasing_into(test2, 'forks')
#    #plt.plot(forks, stars)
#    print(test3)

    
    



if __name__=="__main__":
    main()


































































































































