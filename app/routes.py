from flask import request

from app import app

from app.pubchem_service import PubchemService

service = PubchemService()


@app.route('/synonyms')
def get_synonyms():
    asset = request.args.get('asset')
    if asset is None:
        return "please provide an asset url param e.g., \"synonyms?asset=aspirin\""
    return service.get_synonym(asset)


@app.route('/compound-and-brands')
def get_compound_and_brands():
    asset = request.args.get('asset')
    if asset is None:
        return "please provide an asset url param e.g., \"compound-and-brands?asset=aspirin\""
    return service.get_compound_and_brands(asset)
