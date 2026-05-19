from models import DataRepository, ToRepository

amazon = DataRepository.DataRepository('amzn')
netflix = DataRepository.DataRepository('netflix')
spotify = DataRepository.DataRepository('spotify')
apple = DataRepository.DataRepository('apple')

data_amazon = amazon.create_data_frame()
data_netflix = netflix.create_data_frame()
data_spotify = spotify.create_data_frame()
data_apple = apple.create_data_frame()

data_amazon.to_csv('data/languages_amazon.csv')
data_netflix.to_csv('data/languages_netflix.csv')
data_spotify.to_csv('data/languages_spotify.csv')
data_apple.to_csv('data/languages_apple.csv')

new_repo = ToRepository.ManipulateRepository('avelinoandre')
repo_name = 'Most-Used-Languages'
new_repo.create_repo(repo_name)

new_repo.put_repo(repo_name, './data/languages_amazon.csv', 'languages_amazon.csv')
new_repo.put_repo(repo_name, './data/languages_netflix.csv', 'languages_netflix.csv')
new_repo.put_repo(repo_name, './data/languages_spotify.csv', 'languages_spotify.csv')
new_repo.put_repo(repo_name,  './data/languages_apple.csv', 'languages_apple.csv')

