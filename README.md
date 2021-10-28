# Censys ASM API Example
Simple script to showcase pulling down Censys ASM data via the [Censys python wrapper API](https://github.com/censys/censys-python).

**Steps for getting started:**
- Install the libraries in requirements.txt
   - ```python -m pip install -r requirements.txt```
- If for whatever reason your environment installs an old version of the censys module, you can upgrade it.
   - ```pip install --upgrade censys```
- Set your Censys ASM API key
   - ```censys asm config```
   - (find your ASM API key here: https://app.censys.io/integrations)

If want to do anything else with the API, you can [read the documentation here](https://censys-python.readthedocs.io/en/stable/usage-asm.html).
\
\
Now just run the script:
``` 
py -3 pull_clouds.py
```
