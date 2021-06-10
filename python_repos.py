import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response.
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)

# Store response
response_dict = r.json()
print("Total repositories:", response_dict["total_count"])

# Explore information about the repositories.
repo_dicts = response_dict["items"]
print("Repositories returned:", len(repo_dicts))

# Examine the first repository.
names, plt_dicts= [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plt_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'] or "",
        'xlink': repo_dict['html_url']
        }
    plt_dicts.append(plt_dict)

#Make Visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size =24
my_config.label_font_size = 14
my_config.majo_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred python Projects on Github'
chart.x_labels = names

chart.add('', plt_dicts)
chart.render_to_file('python_projects3.svg')

# print("\nSelected information about first repository:")
# print("Name: ", repo_dict['name'])
# print("Owner: ", repo_dict['owner']['login'])
# print("Stars: ", repo_dict['stargazers_count'])
# print("Description: ", repo_dict['description'])

