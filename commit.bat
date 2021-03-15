py setup.py sdist bdist_wheel
py -m twine upload dist/*
py clean.py
pause