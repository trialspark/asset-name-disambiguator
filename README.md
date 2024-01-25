# asset-name-disambiguator
### Setup
1. Check to see if you already have `chromedriver` installed by running  `chromedriver` in your terminal. If it does not start up, you can install it by doing `brew install chromedriver`.
2. Run `poetry install` to install dependencies
3. Run `poetry shell` to start up a venv
4. Run `flask run` to spin up the application at http://127.0.0.1:5000
5. If you are having issues with chromedriver being blocked, cd into `/usr/local/bin` and run `xattr -d com.apple.quarantine chromedriver`

### Endpoints
* `/synonyms` - takes an asset as a URL parameter and returns all known synonyms for the asset (derived from the [Pubchem database](https://pubchem.ncbi.nlm.nih.gov/))
* `/compound-and-brands` - takes an asset as a URL parameter, and returns the compound name (via Pubchem) and all FDA-approved brands with the compound as an active ingredient (derived from [Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm)) 