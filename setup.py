import re
import os
import os.path as osp
from setuptools import setup, find_packages

loc = os.path.dirname(os.path.abspath(__file__))

with open(osp.join(loc, 'src', 'artifice', '__init__.py'), 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

with open(osp.join(loc, 'requirements.txt')) as f:
    required = f.read().splitlines()

description_text = \
'''
-------- ARTIFICE --------
  "You Are What You See"

Artifice is a project which aims to unravel the
multi-faceted landscape of our modern media landscape.
Content is scraped from a wide variety of sources
and viewpoints and distilled into salient data,
which we use to train generative text models. The
output of these models is rendered in a realistic
mockup resembling a typical site one might encounter
on the web. In addition to the novelty of computer-
generated news stories, we also aim to decipher the
relationships between stories and the discussions
they spark. By tracking storylines from the first
mention to the point at which they influence the
national conversation around an issue, we can provide
insight into the mechanisms driving our understanding
of the modern news cycle.

[Web]
https://www.artifice-project.com/
[Source]
https://github.com/artifice-project/artifice-scraper.git
'''

setup(
    name="Artifice",
    version=version,
    license="MIT",
    author=["@minelminel", "@liberty3000"],
    author_email="theartificeproject@gmail.com",
    url="https://www.github.com/artifice-project/artifice-scraper",
    description="You Are What You See",
    long_description=description_text,
    install_requires=required,
    python_requires='>=3.5.*, <4',
    packages=find_packages("src", exclude=['contrib', 'docs', 'tests', 'lib', 'bin', 'include']),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "artifice=artifice.__main__:welcome",
            "artifice.scraper=artifice.scraper.core.manage:manager.run",
            # "name_of_executable = module.with:function_to_execute"
        ]
    }
)
