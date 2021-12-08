# Censys ASM API Example
Simple script to showcase pulling down Censys ASM data via the [Censys python wrapper API](https://github.com/censys/censys-python).

**Steps for getting started:**
- Install the libraries in requirements.txt
   - ```pip install --upgrade -r requirements.txt```
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
If want to use the **requests_pull_clouds.py** file, which showcases using the requests library instead of the Censys python wrapper, you need to rename the file '.env example' to '.env' and replace the placeholder api-key value with your censys-api-key.
