import jinja2
from bs4 import BeautifulSoup
import os
from tqdm import *

env = jinja2.Environment(loader=jinja2.FileSystemLoader("./"))

for template in tqdm(os.listdir("./")):
    if template.endswith(".html"):
        if template == "index.html":
            outfile = "../index.html"
        else:
            outfile = "../pages/" + template

        template = BeautifulSoup(env.get_template(template).render(), "html.parser").prettify()
        with open(outfile, "w") as output:
            output.write(template)