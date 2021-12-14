## ecephys_project_template
A bare-bones template for Python packages, ready for use with setuptools (PyPI), pip, and py.test.

### Using this as a template
Let's assume that you want to create a small scientific Python project called `smallish`.

To use this repository as a template, click the green "use this template" button on the front page of the "ecephys_project_template" repository.

In "Repository name" enter the name of your project. For example, enter `smallish` here. After that, you can hit the "Create repository from template" button.

You should then be able to clone the new repo into your machine. You will want to change the names of the files. For example, you will want to move `ecephys_project_template/ecephys_project_template.py` to be called `smallish/smallish.py`
```
git mv ecephys_project_template smallish
git mv smallish/ecephys_project_template.py smallish/smallish.py
git mv smallish/tests/test_ecephys_project_template.py smallish/tests/test_smallish.py
```

Make a commit recording these changes. Something like:
```
git commit -a -m "Moved names from `ecephys_project_template` to `smallish`"
```

You will want to edit a few more places that still have `ecephys_project_template` in them. Type the following to see where all these files are:
```
git grep ecephys_project_template
```

You can replace `ecephys_project_template` for `smallish` quickly with:
```
git grep -l 'ecephys_project_template' | xargs sed -i 's/ecephys_project_template/smallish/g'
```

Edit `ecephys_project_template/__init__.py`, and `ecephys_project_template/version.py` with the information specific to your project.

This very file (`README.md`) should be edited to reflect what your project is about.

At this point, make another commit, and continue to develop your own code based on this template.


### Installation

This will also install [`ecephys`](https://github.com/CSC-UW/ecephys) and [`ecephys_project_manager`](https://github.com/CSC-UW/ecephys_project_manager as local, editable sibling directory.
Ignore the `git clone` commands if these were cloned already.

NB: The `ecephys` and `ecephys_project_manager` repositories need to be sibling directories. 

```
git clone https://github.com/CSC-UW/ecephys.git
git clone https://github.com/CSC-UW/ecephys_project_manager.git
git clone https://github.com/CSC-UW/ecephys_project_template.git

conda create -n myenv python=3
conda activate myenv

cd ecephys_project_template
pip install -r requirements.txt
```

### Contributing
If you wish to make any changes (e.g. add documentation, tests, continuous integration, etc.), please follow the [Shablona](https://github.com/uwescience/ecephys_project_template) template.