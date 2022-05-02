from flask import request, render_template_string
from src.common.template import centeredHtml

def main():

  return {
        "status": "SUCCESS",
        "transaction_hash": "0x3edfd374c32265bf967376e57c26aa5dc9883ce796712cb735bddc884a6bbbce",
        "transaction_chain_scan_url": "https://mumbai.polygonscan.com/tx/0x3edfd374c32265bf967376e57c26aa5dc9883ce796712cb735bddc884a6bbbce"
    }