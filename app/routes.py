from flask import request

from app import app

from app.pubchem_service import PubchemService


@app.route('/synonyms')
def get_synonyms():
    asset = request.args.get('asset')
    if asset is None:
        return "please provide an asset url param e.g., \"synonyms?asset=aspirin\""
    return PubchemService().get_synonym(asset)
